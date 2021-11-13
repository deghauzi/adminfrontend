release: python manage.py collectstatic --dry-run --noinput python manage.py makemigrations python manage.py migrate
web: gunicorn core.wsgi --log-file - --log-level debug