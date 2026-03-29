from flask import Flask, render_template, request
import os

app = Flask(__name__)


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
        print("Received contact form submission:")
        print("Name:", request.form.get('name'))
        print("Email:", request.form.get('email'))
        print("Subject:", request.form.get('subject'))
        print("Message:", request.form.get('message'))
        pass
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
