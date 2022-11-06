## Create new revision and upgrade DB

1. alembic revision -m "some message" --autogenerate
2. alembic upgrade head

## Upgrading and downgrading

alembic upgrade +1
alembic downgrade -1
