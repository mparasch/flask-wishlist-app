# Wishlist App

This project is an unfinished web application built with Flask that allows users to create and manage wishlists that can be shared for any occassion. It features user authentication and CRUD operations for wishlist items. The app connects to a MySQL database for data persistence.

## Project Structure

wishlist-app/  
├── SQL/                  # SQL scripts for creating and managing database tables  
├── static/styles         # CSS styles and image assets for the webpages  
├── templates/            # HTML templates
├── venv/                 # Virtual environment for the Python dependencies  
└── main.py               # Flask application script  


---

## Features

- **User Authentication**:
  - **Register**: Create a new user account.
  - **Login**: Log in with existing credentials.
- **Wishlist Management**:
  - Add new items to the wishlist with priority, notes, and links.
  - View all items in the wishlist.
- **Account Management**:
  - Edit account settings.
  - Delete account.
  - Switch between accounts.

---

## Prerequisites

- Python 3.x
- MySQL
- Virtual environment setup (optional)

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd wishlist-app
   ```
2. **Set up virtual environment** (optionatl but recommended):
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. **Install dependencies:**
  ```bash
  pip install flask flask-mysqldb
  ```
4. **Configure the database:**
* Set up a MySQL database and execute the SQL scripts in the `SQL/` folder to create the required tables.
* Update the database credentials in `main.py`:
```python
app.config['MYSQL_HOST'] = '<your_database_host>'
app.config['MYSQL_USER'] = '<your_database_user>'
app.config['MYSQL_PASSWORD'] = '<your_database_password>'
app.config['MYSQL_DB'] = '<your_database_name>'
```
5. **Run the app:**
   ```bash
   python main.py
   ```
6. **Access the app:** Open your browser and navigate to http://127.0.01:5000.

---

### Folder Details

- **`SQL/`**:
  - Contains SQL scripts for creating the database schema and tables.
  - Example: `site_users` table stores user information.
  - Example: `user_items` table stores wishlist items.

- **`static/styles/`**:
  - Stores CSS files for styling the app.

- **`templates/`**:
  - Contains HTML templates and assets (e.g., background images) for rendering the app's UI.

- **`venv/`**:
  - Contains the virtual environment for managing Python dependencies.

- **`main.py`**:
  - The core application script with Flask routes, database integration, and logic.

---

### Application Workflow

1. **Login/Register**:
   - Navigate to the homepage to log in or register.
   - Registration checks for unique usernames and prevents spaces in usernames.

2. **View Wishlist**:
   - Once logged in, users can view their wishlist items, including item name, priority, notes, and links.

3. **Add Wishlist Items**:
   - Use the "Add Item" feature to include new items in the wishlist.

4. **Account Settings**:
   - Edit account details or delete the account.
   - Switch between user accounts.

---

### Future Enhancements

- **Enhanced Validation**:
  - Implement better form validation for user input.
  
- **Responsive Design**:
  - Improve styling for better user experience across devices.
  
- **Enhanced Features**:
  - Add the ability to edit or delete wishlist items.
  - Add categories or tags for wishlist items.
  
- **Security**:
  - Use password hashing for secure storage of user passwords.

### LICENSE
You can modify this documentation as needed to reflect any changes to your project or repository. Let me know if you need further assistance!

