from flask import Flask, render_template, request, redirect, flash, session
import os
from dotenv import load_dotenv
from db import Database

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("KEY")
db = Database()

@app.route('/')
def _root():
    return render_template('index.html')

@app.route('/about')
def _about():
    return render_template('about.html')

@app.route('/projects')
def _projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def _contact():
    if request.method == 'POST':
        db.add_message(
            name=request.form['name'],
            email=request.form['email'],
            subject=request.form.get('subject', '—'),
            message=request.form['message']
        )
        flash('message sent!')
    return render_template('contact.html')


@app.route('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == os.getenv('user') and request.form['password'] == os.getenv('pass'):
            session['logged_in'] = True
            return redirect('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin')
        flash('invalid credentials')
    return render_template('login.html')

@app.route('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin')
def _admin():
    if not session.get('logged_in'):
        return redirect('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin/login')
    
    messages = db.get_all_messages()
    return render_template('messages.html', messages=messages)

@app.route('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin/logout')
def admin_logout():
    session.clear()
    return redirect('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin/login')

@app.route('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin/messages/delete', methods=['POST'])
def delete_message():
    if not session.get('logged_in'):
        return redirect('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin/login')
    message_id = int(request.form['message_id'])
    db.delete_message(message_id)
    flash('message deleted')
    return redirect('/9699f64f7f06427b1d4d1679b195a5b898eda467/admin')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
