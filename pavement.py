from paver.easy import task, needs
from paver.shell import sh

@task
def runserver():
    sh('python manage.py runserver 0.0.0.0:8000')


@task
def migratedb():
    sh('python manage.py migrate')


@task
@needs('migratedb')
def test():
    sh('python manage.py test')

