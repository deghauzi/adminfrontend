release: python manage.py collectstatic --dry-run --noinput
release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn core.wsgi --log-file -