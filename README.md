# Flask Template

A template for a Flask project with built in database and authentication support. Bootstrap 5.3.2 is also included.

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

## Credits

This template was inspired by [this DigitalOcean article](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy).

Several parts of the template have been modified and updated.
