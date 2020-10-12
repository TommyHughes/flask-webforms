from flask import Flask, render_template, session, g, request, redirect, url_for
import sqlite3

app = Flask(__name__,instance_relative_config=False)
app.config['DEBUG'] = True

def connect_db():
    sql = sqlite3.connect('app.db')
    sql.row_factory = sqlite3.Row
    return sql
    
def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite3'):
        g.sqlite_db.close()

@app.route('/')
@app.route('/home')
def home():
    db = get_db()
    cur = db.execute("SELECT * FROM posts ORDER BY submit_date DESC")
    posts = cur.fetchall()
    return render_template('home.html',posts=posts)
    
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        db = get_db()
        author = request.form['author']
        post = request.form['post']
        
        db.execute("INSERT INTO posts (author, post, submit_date) values (?,?,strftime('%Y-%m-%d %H:%M:%S','now'))", [author, post])
        db.commit()
        
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()