# Note To Self

<div align="center">
  <img src="xx">
</div>

<br>

<strong>Domain Modeling :: To-Do Lists</strong><br>
To-Do Tasks app with Python, Flask and SQL frameworks.<br>

<p><a href="xx">YouTube Demo</a></p>
<p><a href="xx">DEV Blog</a></p>

## About

<p>This is my final project of CS50 (<a href="https://pll.harvard.edu/course/cs50-introduction-computer-science?delta=0">CS50x through edX</a>), Harvard University's introduction to the intellectual enterprises of computer science and the art of programming. </p>
<p>Note to Self app is To-Do Tasks application.</p>

## Features

<div align="center">
  <img src="images/wireframe.png">
</div>

<br>

<div align="center">
  <img src="images/erd_present.png">
</div>

<br>

<div align="center">
  <img src="images/components.png">
</div>

<br>

**Models** <br>
User, Event, Category, Image<br>

> user `has_many` :events

> event `belongs_to` :user<br>
> event `belongs_to` :category<br>
> event `has_many` :images

> category `has_many` :events

> image `belongs_to` :event

**Controller** <br>
ApplicationController<br>
Api::V1::AuthController<br>
Api::V1::CategoriesController<br>
Api::V1::EventsController<br>
Api::V1::ImagesController<br>
Api::V1::UsersController<br>

**User Account and Validation** <br>
JWT Authentication: Sign Up, Log In and Log Out.<br>

## API Database

- [x] <a href="https://console.cloud.google.com/apis/dashboard">Google Developer API</a>
- [x] <a href="https://cloudinary.com/">Cloudinary API</a>

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

<strong>Instructions</strong>

<p>Open Chrome browser, and redirect to a new local host to start the app.</p>

**Alternatively, it is fully deployed on Netlify!**
<br>
<a href="xx">Note To Self</a>

## Build Status and Future Improvement

<p>Storybook was completed in a 2-week timeframe from implementing Rails back-end, ReactJS front-end, Cloudinary API, Google Maps API and Material-UI library. Future cycle of product development as follows:</p>

- [x] Search Bar. Over the time, the user will have many events, and it gets troublesome when the user needs to immediately access a specific event entry. A search bar to quickly type event title and access the journal entry would be useful.
- [x] \_\_

<div align="center">
  <img src="xx">
</div>

- [x] \_\_

## Stack

- [x] Flask
- [x] SQL

## Resources

- [x] <a href="https://getbootstrap.com/">Bootstrap</a>
- [x] <a href="https://giphy.com/">Giphy</a>
