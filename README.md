# Flask Template

A template for a Flask project with built in database and authentication support. Bootstrap 5.3.2 is also included.

## Setting up Your Dev Environment

This template uses [Poetry](https://python-poetry.org/) for package management, but you don't need to if you don't want to. Simply install any required dependencies and you're good to go! Note: You should be using Python version 3.10 or higher.

### Install Dependencies Using Poetry (Recommended)

```
poetry install
```

### Install Dependencies Using Pip

```
python3 -m pip install -r requirements.txt
```

## Running the Application

You can run the application with the command 

```sh
python3 run.py
```

By default, this will run the application on port 5000.

### Initializing the Database

If this is your first time running the application, you need to initialize the database first. This is easy to do - simply use the command

```sh
python3 run.py init_db
```

### Running in Debug Mode

Running your application in debug mode will help you during development because it'll allow you to see helpful messages when errors occur in your code. However, it's not safe to run a production app (open to the public) in debug mode, which is why it's disabled by default. To run the application in debug mode, simply use the command

```sh
python3 run.py debug
```

## Environment Variables

There are several configuration environment variables you should set (and probably rename) when using this template:

- `SECRET_KEY`:
    - The secret key used to secure request information in your application
    - You can use the following command to generate a secure secret key:
        - `python3 -c "import secrets; print(secrets.token_hex())"`
    - By default, the application will generate one for you, but it will be changed for every run, so you should set it manually
- `DATABASE_URI`:
    - SQL Database URI used to connect to your database.
    - Defaults to `sqlite:///app.db`, creating a `app.db` sqlite database in the project root
- `FLASK_PORT`:
    - Specifies the port the application will run on.
    - Defaults to `5000`

You can find all of this in `config.py`

### Renaming Environment Variables

You'll probably want to rename your environment variables to something more memorable and specific to your application. This is because if you're running multiple applications on one system, there may be a naming conflict where two apps use the same name for their environment variables.

For example, in config.py, you can change `os.environ.get('SECRET_KEY')` to `os.environ.get('FLASK_TODO_APP_SECRET_KEY')` if you're making a todo list application.

### .env File

You can specify the values of the environment variables in a `.env` file. Something like:

```
SECRET_KEY=mysupersecretkey
DATABASE_URI=sqlite:///app.db
FLASK_PORT=5001
```

## Overview of Files and Folders

- **LICENSE**: License file for the template.
- **README.md**: Readme file providing information about the template.
- **app.db**: SQLite database file.
- **run.py**: Main script to run the Flask application.
- **config.py**: Configuration file for the Flask application.
- **poetry.lock**: Poetry lock file (dependency version locking).
- **pyproject.toml**: Poetry project configuration file.
- **requirements.txt**: Requirements file listing dependencies for the project.

### app/
Main application directory containing:
- **__init__.py**: Initialization script for the app package.
- **extensions.py**: Script for initializing Flask extensions.
  
#### auth/
Directory for authentication-related functionalities containing:
- **__init__.py**: Initialization script for the auth package.
- **helpers.py**: Module containing helper functions for authentication.
- **routes.py**: Module containing routes for authentication.

#### main/
Directory for main functionalities/routes containing:
- **__init__.py**: Initialization script for the main package.
- **routes.py**: Module containing routes for main functionalities.

#### models/
Directory for database models containing:
- **__init__.py**: Initialization script for the models package.
- **user.py**: Module defining the user model.

#### static/
Directory for static files (e.g., CSS, JS) containing:
- **bootstrap.5.3.2.bundle.min.js**: Minified Bootstrap JS bundle.
- **bootstrap.5.3.2.min.css**: Minified Bootstrap CSS.
- **favicon.ico**: Favicon icon.
- **icon.png**: Icon image.
- **style.css**: Custom CSS stylesheet.

#### templates/
Directory for HTML templates containing:
- **about.html**: About page HTML template.
- **base.html**: Base HTML template (common structure for other templates).
- **index.html**: Index/home page HTML template.
- **login.html**: Login page HTML template.
- **register.html**: Register page HTML template.
- **temp.html**: Temporary HTML template (for reference or testing).

## Credits

This template was inspired by [this DigitalOcean article](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy).

Several parts of the template have been modified and updated.
