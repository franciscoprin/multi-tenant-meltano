#!/bin/sh
# wait-for-postgres.sh

set -e

shift

# DON'T RUN SCRIPT IF VARIABLES WEREN'T SET.
: "${DB_PASSWORD:?Variable not set or empty}"
: "${DB_HOST:?Variable not set or empty}"
: "${DB_PORT:?Variable not set or empty}"
: "${DB_USER:?Variable not set or empty}"

# SLEEP UNTIL DB IS AVAILABLE.
until PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up"
exec "$@"
