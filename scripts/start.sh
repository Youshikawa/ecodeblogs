#! /bin/bash
echo yes | python3 ../manage.py collectstatic
uwsgi --ini ../scripts/uwsgi.ini