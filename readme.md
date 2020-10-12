# Web Form Project

---

## About

The goal of this project was to create an ultra-simplistic example of
how webforms work with flask. This is primarily to get practice working
with flask and to get practice working with HTML forms.

I also am intentionally leaving out plugins like SQLAlchemy. I hope to
learn how to do these things without the extra framework and, later,
build up to comfortability with plugins.

---

## Process

1. Create directory
1. Setup Git repo  
	- Set the working directory
		> `set-location C:\Users\thoma\Desktop\Development\webdev\webform`
	- Initialize git repo
		> `git init`
	- Create .gitignore
		> `new-item -path . -name ".gitignore" -itemtype "file"`
1. Create .md and begin writing procedures
	>`new-item -path . -name "readme.md" -itemtype "file"`
1. Create application file
	>`new-item -path . -name "app.py" -itemtype "file"`
1. Create virtual environment and install packages
	- Create virtual python environment
		>`py -m venv venv`
	- Activate virtual environment
		>`venv\Scripts\activate`
	- Install flask
		>`pip install flask`
1. app.py
	> `from flask import Flask`  
	> `app = Flask(__name__)`
	> `app.config['DEBUG'] = True`  
	> `@app.route('/')`  
	> `def index(): return '<h1>Welcome!</h1>'`  
	> `if __name__ == '__main__': app.run()`  
1. Check to see that you get a working app
	> `py app.py`
1. Create static and templates folders
	- Create static folder
		> `new-item -path . -name "static" -itemtype "directory"`
	- Create templates folder
		> `new-item -path . -name "templates" -itemtype "directory"`
	- Create HTML files in templates folder
		> `new-item -path ".\templates\" -name "home.html" -itemtype "file"`  
		> `new-item -path ".\templates\" -name "form.html" -itemtype "file"`
	- Create CSS file in static folder
		> `new-item -path ".\static\" -name "styles.css" -itemtype "file"`
1. Add HTML to HTML files
1. Add CSS to CSS files
1. app.py
	- Replace
		> `@app.route('/')`  
		> `@app.route('/home')`  
		> `def home(): render_template('home.html')`
	- Add
		> `@app.route('/submit')`  
		> `def submit(): render_template('form.html')`
1. Check to see that you get a working app
	- Your HTML and CSS files should be set up with {{ url_for }} and you should be able to navigate.
		> `py app.py`
1. Create tables.sql file
	> `new-item -path . -name "tables.sql" -itemtype "file"`
1. Write the SQL script in tables.sql
1. Create the database and table in sqlite3
	> `sqlite 3 app.db -init tables.sql`
1. Check to see that the table was created
	> `.tables`
1. Quit sqlite3
	> `.exit`
1. app.py
	- Add
		> `from flask import session, g`  
		> `import sqlite3`  
		> `def connect_db(): `  
		>> `sql = sqlite3.connect('app.db')`  
		>> `sql.row_factory = sqlite3.Row`  
		>> `return sql`
		
		>`def get_db():`  
		>> `if not hasattr(g,'sqlite3'):`  
		>>> `g.sqlite_db = connect_db()`  
		
		>> `return g.sqlite_db`
		
		> `@app.teardown_appcontext`  
		> `def close_db(error):`
		>> `if hasattr(g, 'sqlite_db'):`
		>>> `g.sqlite_db.close()`
1. Check to see that you get a working app
	> `py app.py`
1. app.py
	- Add so that it looks like current commit.
1. Modify HTML and CSS so that it looks like current commit.
			
		
		
		
		
		
		
		
		