<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://img2.freepng.es/20180711/rtc/kisspng-django-web-development-web-framework-python-softwa-django-5b45d913f29027.4888902515313042119936.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Kilimo Challenge</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

<p align="center"> Kilimo Challenge.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Testing API](#testing)
- [Built Using](#built_using)
- [TODOs](#todo)
- [Author](#author)


## 🧐 About <a name = "about"></a>

Challenge Kilimo:
1. Implements business model.
2. Configurate admin site to manage business models
3. With DRF:
  a. List grounds with avg of rains y las N days (0 <= N <= 7).
  b. List of Rains by ground.
  c. List of grounds where rain sum > N (N >= 0)
  d. Add rain to a ground.


Database configuration: In kilimo/settings.py file is the database cofiguration

We use sqlite for this small project


If you need to change this, please configure access and run the following line to create data structure:

Windows:
```
reset_db.bat
```

Linux:
```
TODO
```


### Prerequisites <a name = "prerequisites"></a>

To run the project you need some prerequisites:

- I recommend that you have installed virtualenv to manage different development  environments.

1. You have installed python 3.6 
2. run pip install -r requirements.txt to install all dependencies


## 🎈 Usage <a name="usage"></a>

Go to kilimo directory (there is manage.py file) 

Run API Rest.

run: python manage.py runserver

Server runs at http://localhost:8000


## 🚀 Testing the API <a name = "testing"></a>

To test Rest API, you can use the Rest Client you want.

For example you can use postman.

Another ways are:
1) Run simple reponse test without check content:

    ```
    python manage.py test
    ```

2) You could go to http://127.0.0.1:8000/ and navigate exposed api.

3) You could go to http://127.0.0.1:8000/admin and navigate admin site.


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Language
- [Django](https://www.djangoproject.com/) - Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Rest Framework
- [Postman](https://www.postman.com/) - Rest Client
- [Postgres](https://www.postgresql.org/) - Database


of course, Google and some others...

## ✍️ TODOs (not requested in the challenge) <a name = "todo"></a>

  - Split classes into single files.
  - Improve project files structure.
  - Improve the rigor of the test.
  - Provide authentication to api.
  - Run over HTTPs.
  

## ✍️ Authors <a name = "author"></a>

- [@diegorichi](http://www.diegorichi.com.ar/)

