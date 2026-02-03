from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Database Model
class BuddyGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100), nullable=False)
    mentor_name = db.Column(db.String(100), nullable=False)
    member_count = db.Column(db.Integer, default=0)

# Initialize Database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    groups = BuddyGroup.query.all()
    return render_template('index.html', groups=groups)

@app.route('/add', methods=['POST'])
def add_group():
    new_group = BuddyGroup(
        group_name=request.form['group_name'],
        mentor_name=request.form['mentor_name'],
        member_count=request.form['member_count']
    )
    db.session.add(new_group)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_group(id):
    group = BuddyGroup.query.get(id)
    group.mentor_name = request.form['new_mentor']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_group(id):
    group = BuddyGroup.query.get(id)
    db.session.delete(group)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)