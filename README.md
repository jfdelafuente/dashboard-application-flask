# Instrucciones

Ejemplo de aplicación `Flask` que se conecta a una base de datos `postgresql`.

👉 Set Up for Windows

Install modules via VENV (windows)

```bash
python<version> -m venv <virtualenv-name>
.\venv\Scripts\activate
pip3 install -r requirements.txt
```

Set Up Flask Environment

```bash
# CMD
set FLASK_APP=run.py
set FLASK_ENV=development

# Powershell
$env:FLASK_APP = ".\run.py"
$env:FLASK_ENV = "Development"
$env:FLASK_DEBUG = "true"
```

Start the app

```bash
$ flask run

o

$ flask --app run --debug run
```

python -m pip uninstall flask-sqlalchemy
Flask-SQLAlchemy >= 2.5.1
