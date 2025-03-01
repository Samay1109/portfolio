from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        # Table for portfolio projects
        cursor.execute('''CREATE TABLE IF NOT EXISTS projects (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            description TEXT,
                            link TEXT)''')
        # Table for contact messages
        cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            email TEXT,
                            message TEXT)''')
    print("Database initialized!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT title, description, link FROM projects')
        projects = cursor.fetchall()
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)',
                           (name, email, message))
            conn.commit()
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route('/api/projects', methods=['GET'])
def api_projects():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT title, description, link FROM projects')
        projects = cursor.fetchall()
    return jsonify({"projects": projects})

@app.route('/about')
def about():
    # Replace these details with your actual information
    details = {
        "name": "Samay Ashish Mistry",
        "role": "MCA Student & Aspiring Developer",
        "bio": "I am currently pursuing an MCA at TIMSCDR and have completed my BCA. I specialize in building websites using Python, SQL, HTML, CSS, and React. I have experience working on projects like a Hall Ticket Generator and Doodle Board.",
        "skills": ["Python", "SQL", "HTML", "CSS", "JavaScript", "React", "Flask", "MongoDB", "Git"],
        "hobbies": ["Coding", "Learning new technologies", "Playing chess", "Gaming"]
    }
    return render_template('about.html', details=details)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
