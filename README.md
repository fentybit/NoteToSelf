# Note to Self

<div align="center">
  <img src="xx">
</div>

<br>

<strong>Domain Modeling :: To-Do Lists</strong><br>
To-Do Tasks app with Python, Flask and SQL frameworks.<br>

<p><a href="xx">YouTube Demo</a></p>
<!-- <p><a href="xx">DEV Blog</a></p> -->

## About

<p>This is my final project of CS50 (<a href="https://pll.harvard.edu/course/cs50-introduction-computer-science?delta=0">CS50x through edX</a>), Harvard University's introduction to the intellectual enterprises of computer science and the art of programming. </p>
<p>Note to Self app is a To-Do Tasks application. First time user is required to register, and returning user needs to log in. The Minimum Viable Product (MVP) of Note to Self is for users to be able to log chores along with correspoding level of priorities.</p>

## Project Files

```
.
├── static
│   ├── apology.gif
│   ├── favicon.ico
│   ├── giphy.gif
│   └── styles.css
├── templates
│   ├── apology.html
│   ├── index.html
│   ├── layout.html
│   ├── login.html
│   ├── new.html
│   ├── register.html
│   └── todos.html
├── app.py
│       user flow, business logic
├── helpers.py
│       apology, login_required
├── notetoself.db
│       users, todos tables
├── notetoself.sql
│       schema
└── README.md
```

## Installation

<strong>How to set up on local IDE</strong>

```
$ git clone 👾
$ python3 (to confirm Python fully installed)
$ node -v (to confirm Node.js fully installed)
$ npm i -g http-server
$ which sqlite3 (to confirm SQLite fully installed)
$ pip3 install flask
$ pip3 install cs50
$ pip3 install lib50
(restart terminal if this is first time of installation)
$ flask run
```

<p>Open Chrome browser, and redirect to a new local host to start the app.</p>

<!-- **Alternatively, it is fully deployed!**
<br>
<a href="xx">Note to Self</a> -->

## Build Status and Future Improvement

<p>Note to Self was completed in a week timeframe from implementing JavaScript, Python, SQL and Bootstrap library. Future cycle of product development as follows:</p>

- [x] Edit. User can only create, read and delete. Ideally, we would like edit functionality.
- [x] Quick Find tab. Over the time, the user will have many tasks, and it gets troublesome when the user needs to immediately access a specific task entry. A search bar to quickly type event title and access the journal entry would be useful.
- [x] Current task entry allows priority, title and description attributes. Each entry should have more functionality for the user, such as weather, scheduling, sharing capability, image upload and so on. 
- [x] Create a toggle track for dark mode. 😎

## Stack

- [x] Flask
- [x] Jinja
- [x] SQL

## Resources

- [x] <a href="https://getbootstrap.com/">Bootstrap</a>
- [x] <a href="https://giphy.com/">Giphy</a>
- [x] <a href="https://jinja.palletsprojects.com/en/3.1.x/">Jinja</a>
