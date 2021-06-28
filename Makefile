shell-django:
    docker-compose exec web python manage.py shell

ssh:
    docker-compose exec $c bash

.PHONY: shell-django, ssh
