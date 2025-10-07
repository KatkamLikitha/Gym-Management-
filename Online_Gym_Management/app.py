from flask import Flask, render_template, request, redirect, url_for
from utils.database import init_db, add_member, get_members

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/members')
def members():
    member_list = get_members()
    return render_template('members.html', members=member_list)

@app.route('/add_member', methods=['GET', 'POST'])
def add_member_route():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        membership = request.form['membership']
        add_member(name, age, membership)
        return redirect(url_for('members'))
    return render_template('add_member.html')

if __name__ == '__main__':
    app.run(debug=True)