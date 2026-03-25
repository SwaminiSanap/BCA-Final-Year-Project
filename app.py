from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create DB connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Contact Form Save
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']

    conn = get_db_connection()
    conn.execute('INSERT INTO contacts (name, phone, message) VALUES (?, ?, ?)',
                 (name, phone, message))
    conn.commit()
    conn.close()

    return redirect('/')

# Run app
if __name__ == "__main__":
    app.run(debug=True)
