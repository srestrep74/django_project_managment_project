<div align="center">
  <h3 align="center">Django Project-Tasks Management Project</h3>
</div>

<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li><a href="#about-the-project">About the project</a></li>
    <li><a href="#development-tools">Development Tools</a></li>
    <li><a href="#instalation">Instalation</a></li>
  </ol>
</details>

## About the project

This project is a web application developed in Django that allows basic management of projects and tasks, enabling CRUD operations on these entities and providing advanced functionalities such as filtering for better organization and tracking.

### Key Features : 

- **Project and Task Management:** The application facilitates creating, reading, updating, and deleting projects and tasks efficiently.

- **Filters and Search:** It includes filtering capabilities to find specific projects and tasks based on various criteria, enhancing data organization and accessibility.

### Project Purpose

This project was developed with the aim of deepening the understanding of the Django framework and exploring various tools and functionalities it offers:

- **Deep Dive into Django:** Focused on enhancing knowledge of Django framework, including its ORM (Object-Relational Mapping), templates, views, models, and other essential features.

- **Exploration of New Tools:** Explored and applied new tools and techniques available in Django to optimize application development and management.

- **Skill Development:** The project served as a platform to improve skills in developing Django-based web applications, providing practical experience in implementing CRUD functionalities and managing complex data.

## Development tools

<p align="center">
  <a href="https://skillicons.dev">
    <img src = "https://raw.githubusercontent.com/tandpfun/skill-icons/65dea6c4eaca7da319e552c09f4cf5a9a8dab2c8/icons/Django.svg" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "django"/>
     <img src = "https://raw.githubusercontent.com/tandpfun/skill-icons/65dea6c4eaca7da319e552c09f4cf5a9a8dab2c8/icons/Python-Dark.svg" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "python"/>
     <img src = "https://raw.githubusercontent.com/tandpfun/skill-icons/65dea6c4eaca7da319e552c09f4cf5a9a8dab2c8/icons/Bootstrap.svg" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "bootstrap"/>
     <img src = "https://github.com/tandpfun/skill-icons/raw/main/icons/HTML.svg" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "html"/>
       <img src = "https://raw.githubusercontent.com/tandpfun/skill-icons/65dea6c4eaca7da319e552c09f4cf5a9a8dab2c8/icons/Git.svg" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "git"/>
  </a>
</p>

## Instalation

1. Clone Django Project : 
```bash
  git clone https://github.com/srestrep74/django_project_managment_project.git
  cd django_project_managment_project/
```

2. Install virtualenv for the management of virtuals envs : 
```bash
  pip install virtualenv
```

3. Create a virtual env and activate it : 
```bash
  virtualenv env
  source env/bin/activate
```

4. Install project requirements (dependencies) : 
```bash
  pip install -r requirements.txt
```

5. Rename the .env.example to .env : 
```bash
  mv .env.example .env
```

6. In the .env , configure your MySQL database parameters : 
```bash
  DB_NAME=
  DB_USER=
  DB_PASSWORD=
  DB_HOST=
  DB_PORT=
```
7. Make the migrations : 
```bash
  python manage.py migrate
```

8. Run the project: 
```bash
  python manage.py runserver
```