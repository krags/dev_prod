local
krags
password

# ???
Type this in the console (and within the venv)
cmd.exe /c chcp 1252
before typing this in the console
heroku pg:psql



To commit changes
git add .
git commit -m "desctription of changes"
git push heroku main
heroku open

To add a file to requirement.txt
pip freeze > requirements.txt
This adds all the installation files to the requirements.txt file.

heroku ps -> lists running apps
heroku ps:stop "process name" -> stops a process


How to get Heroku ready to run our project
https://www.youtube.com/watch?v=kBwhtEIXGII
requirements.txt
Procfile contains Python version
    web: gunicorn crm1.wsgi --log-file -
ALLOWED_HOSTS = [heroku url, '127.0.0.1']
DEBUG = false
Add build pack python

Summary:  Heroku setup requirments
Freeze deps:
pip freeze > requirement.txt
Procfile:
web: gunicorn gettingstarted.wsgi
whitenoise installed and added to middle ware settings

To open the live application
Type in a venv terminal:
heroku open

py manage.py check --deploy

git rm -r --cached .

https://stackoverflow.com/questions/40975751/copy-changes-from-one-branch-to-another

print("Hey programmer ===> ")
print("set DJANGO_ENV='mysite.settings.dev' for dev work.")
print("set DJANGO_ENV='mysite.settings.prod' for production work.")
print("once at the beginning of your session.")
WARNING => There cannot be spaces around the '='

Add the following code to asgi.py, wsgi.py, and manage.py.
Setting the environment variable sets working in development or production mode.
django_env=os.environ['DJANGO_ENV']
os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_env)

Two scoops of django
And how to setup the settings files.
https://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django

# Running django for local development
$ ./manage.py runserver 0:8000 --settings=project.settings.local

# Running django shell on the production site
$ ./manage.py shell --settings=project.settings.production