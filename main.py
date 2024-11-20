from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = <db_host>
app.config['MYSQL_USER'] = <db_user>
app.config['MYSQL_PASSWORD'] = <db_user_pword>
app.config['MYSQL_DB'] = <db_schema>

mysql = MySQL(app)

global uname

@app.route('/')
def login():
    return render_template('loginHome.html')


@app.route('/login/newUser', methods=['GET', 'POST'])
def newUser():
    global uname
    if request.method == "POST":
        details = request.form
        u_id = details['uname']
        u_pass = details['pass']
        u_email = details['email']
        user_cur = mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cur.execute("SELECT DISTINCT u_id FROM site_users;")
        data = cur.fetchall()
        user_ids = []
        for i in data:
            user_ids.append(i[0])
        if u_id in user_ids:
            return "Username already exists."
        elif ' ' in u_id:
            return "Username cannot contain spaces"
        cur.execute("INSERT INTO site_users(u_id, u_pass, u_email) VALUES (%s, %s, %s)", (u_id, u_pass, u_email))
        mysql.connection.commit()
        cur.close()
        return render_template('LoginHome.html')
    return render_template('newUser.html')


@app.route('/login/existingUser', methods=['GET','POST'])
def existingUser():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT DISTINCT u_id FROM site_users ORDER By u_id;")
        data = cur.fetchall()
        user_ids = []
        for i in data:
            user_ids.append(i[0])
        cur.close()
        return render_template('existingUser.html', user_list = user_ids)
    elif request.method == 'POST':
        details = request.form
        u_id = details['uname']
        global uname
        uname = u_id
        u_pass = details['pass']
        cur = mysql.connection.cursor()
        cur.execute("SELECT u_pass FROM site_users WHERE u_id=%s",[u_id])
        data = cur.fetchmany(size = 1)
        print(data[0][0])
        true_pass = data[0][0]
        print(true_pass)
        cur.close()
        if u_pass == true_pass:
            cur = mysql.connection.cursor()
            cur.execute("SELECT i_name, i_priority, i_notes, i_link FROM user_items WHERE u_id=%s", [uname])
            data = cur.fetchall()
            print(data)
            cur.close()
            return render_template("home.html", name = uname, data = data)
        else:
            return 'Invalid Login.'


@app.route('/home')
def home():
    if request.method == "GET":
        global uname
        cur = mysql.connection.cursor()
        cur.execute("SELECT i_name, i_priority, i_notes, i_link FROM user_items WHERE u_id=%s", [uname])
        data = cur.fetchall()
        print(data)
        cur.close()
        return render_template('home.html', name = uname, data = data)
    return render_template('home.html', name = uname)


@app.route('/newItem', methods=('GET', 'POST'))
def newItem():
    global uname
    if request.method == "POST":
        details = request.form
        for key, value in details.items():
            print("key: {0}, value: {1}".format(key, value))
        _name = details['itemName']
        _priority = details['priority']
        _notes = details['notes']
        _link = details['link']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_items(u_id, i_name, i_priority, i_notes, i_link) VALUES (%s,%s, %s, %s, %s)", (uname, _name, _priority, _notes, _link))
        mysql.connection.commit()
        cur.close()
        return redirect('home')
    return render_template('newItem.html', name = uname)


@app.route('/accountSettings', methods=['GET', 'POST'])
def accountSettings():
    global uname
    if request.method == 'POST':
        if request.form['submit-button'] == 'delete':
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM site_users WHERE u_id=%s",[uname])
            mysql.connection.commit()
            cur.close()
            return render_template("loginHome.html")
        if request.form['submit-button'] == 'back':
            return render_template("home.html", name = uname)
        if request.form['submit-button'] == 'edit':
            return render_template("accountSettings.html", name = uname)
        if request.form['submit-button'] == 'switchUser':
            uname = ''
            return render_template("loginHome.html")
    return render_template("accountSettings.html", name = uname)


if __name__=='__main__':
    app.run(debug=True)
