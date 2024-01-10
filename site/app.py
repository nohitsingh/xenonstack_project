from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy database (replace with a proper database in a real-world scenario)
users_db = []

# Routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic (replace with actual authentication)
        username = request.form.get('username')
        password = request.form.get('password')
        # Dummy check (replace with proper authentication logic)
        if username == 'demo' and password == 'demo':
            return f'Welcome, {username}!'
        else:
            return 'Invalid credentials. Please try again.'

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup logic (replace with actual user registration)
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        # Dummy check (replace with proper validation and database storage)
        if password == confirm_password:
            users_db.append({'username': username, 'email': email, 'password': password})
            return redirect(url_for('login'))
        else:
            return 'Password and Confirm Password do not match. Please try again.'

    return render_template('signup.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission logic (replace with actual storage)
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Dummy storage (replace with proper database storage)
        # For now, print the received data to the console
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        return 'Thank you for your message!'

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
