from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# 1️⃣ Create Flask app
app = Flask(__name__)

# 2️⃣ Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3️⃣ Initialize SQLAlchemy
db = SQLAlchemy(app)

# 4️⃣ Define the Contact model BEFORE using it
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

# 5️⃣ Create database tables
with app.app_context():
    db.create_all()

# 6️⃣ Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Print raw form data for debugging
        print("Raw form data:", request.form)

        # Safely get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Debug print individual fields
        print(f"Received form data - name: {name}, email: {email}, message: {message}")

        # Validate fields explicitly with clear errors
        if not name:
            return "Error: Name is required.", 400
        if not email:
            return "Error: Email is required.", 400
        if not message:
            return "Error: Message is required.", 400

        # Create new contact instance and commit
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()

        return f"Thanks {name}, we received your message!"

    # For GET request, render the contact form
    return render_template('contact.html')

@app.route('/view-contacts')
def view_contacts():
    contacts = Contact.query.all()
    return render_template("view_contacts.html", contacts=contacts)

# 7️⃣ Run app
if __name__ == '__main__':
    app.run(debug=True)
