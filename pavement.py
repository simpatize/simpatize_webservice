from paver.easy import task
from paver.shell import sh

@task
def runserver():
    sh('python manage.py runserver 0.0.0.0:8000')