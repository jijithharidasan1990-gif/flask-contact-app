📇 Flask Contact Manager

A simple web-based Contact Management Application built using Flask and SQLite.
It allows users to add, view, and manage contacts through an easy-to-use web interface.

🚀 Features

📝 Add new contacts (Name, Email, Phone)

📋 View all saved contacts

🗑️ Delete contacts (optional, if implemented)

🔐 User authentication (if you added login)

🧱 Built using Flask and SQLAlchemy ORM

🛠️ Technologies Used

Python 3

Flask (Web framework)

SQLite (Database)

SQLAlchemy (ORM)

HTML / Bootstrap (Frontend styling)

⚙️ Installation & Setup

Clone this repository

git clone https://github.com/jijithharidasan/flask-contact-app.git
cd flask-contact-app


Create a virtual environment

python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS/Linux


Install dependencies

pip install -r requirements.txt


Run the app

flask run


Open in your browser

http://127.0.0.1:5000/

📁 Project Structure
flask-contact-app/
│
├── app.py               # Main Flask application
├── models.py            # Database models (Contact class)
├── templates/           # HTML templates
│   ├── base.html
│   ├── add_contact.html
│   └── contacts.html
├── static/              # (Optional) CSS or JS files
├── requirements.txt
└── README.md

💡 Example

Add Contact Page:
Enter the contact’s name, email, and phone number — then click Add Contact.
Your data will be stored in a local SQLite database and shown on the main contact list page.

🧠 Learning Goals

This project helps you understand:

Flask routes (@app.route)

HTML forms and POST requests

SQLAlchemy models and database integration

Rendering templates using Jinja2

CRUD (Create, Read, Update, Delete) basics

🤝 Contributing

Pull requests and suggestions are welcome!
Feel free to fork the repo and make improvements.

🧑‍💻 Author

👤 Jijith Haridasan
📅 Created as part of Flask learning projects
🌐 GitHub Profile
