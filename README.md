## REQUIREMENTS:

- Docker Engine: https://docs.docker.com/engine/install/
- Docker Compose: https://docs.docker.com/compose/install/

## tap-postgres's pip_url:

| type              | tap/target   | pip_url                                                        |
| ----------------- | ------------ | -------------------------------------------------------------- |
| local-environment | tap-postgres | -e /pipelinewise-tap-postgres                                  |
| original-code     | tap-postgres | pipelinewise-tap-postgres                                      |
| modified-code     | tap-postgres | git+https://github.com/franciscoprin/pipelinewise-tap-postgres |

## GETTING STARTED:

If you haven't don't already, check the REQUIREMENTS section.
After that, run these commands:

- modified the pip_url of the tap-postgres in the meltano-pipeline/meltano.yml, following the available options in the `tap-postgres's pip_url` section.
- (terminal #1): docker-compose up
- (Note): waiting until all the containers are lift.
- (terminal #2, repeated this command if the meltano.yml is manually changed): ./meltano.sh install
- (terminal #2): cd meltano-pipeline
- (terminal #2, log schemas): ./meltano.sh invoke tap-postgres --discover
- (terminal #2, check selected/excluded fields): ./meltano.sh select tap-postgres --list --all

## REFERENCE:

- Tenant and Postgres' schema: https://hackernoon.com/your-guide-to-schema-based-multi-tenant-systems-and-postgresql-implementation-gm433589
- Dockerizing Django: https://docs.docker.com/samples/django/
- Waiting for Postgres script: https://docs.docker.com/compose/startup-order/
- docker-compose multiline commands: https://stackoverflow.com/questions/30063907/using-docker-compose-how-to-execute-multiple-commands
- Install psql (so the waiting-for-postgres.sh works): https://phoenixnap.com/kb/how-to-install-postgresql-on-ubuntu
- .gitignore: https://github.com/github/gitignore/blob/master/Python.gitignore
- Multistage dockerfile build, to have different resources in each environments: https://docs.docker.com/develop/develop-images/multistage-build/
- Multi-tenant transport industry example: https://sophilabs.com/blog/django-tenant-schemas-multi-tenant-application
- Installing django_tenants: https://django-tenants.readthedocs.io/en/latest/install.html
- Makefile tutorial: https://makefiletutorial.com/
- django-commands (helpful to create the populate_db Django command): https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/
- django-commands optional/default arguments: https://stackoverflow.com/questions/35635128/how-to-make-a-django-custom-management-command-argument-not-required
- sing django-tenants (helpful to create the populate_db Django command): https://django-tenants.readthedocs.io/en/latest/use.html
- meltano getting started (useful to create the meltano-pipeline folder): https://meltano.com/docs/getting-started.html#local-installation
- meltano postgres extractor: https://hub.meltano.com/extractors/postgres
- meltano json loader: https://hub.meltano.com/loaders/jsonl
- meltano configure tap-postgres' creds: https://meltano.com/docs/getting-started.html#configure-the-extractor
- fork tap-postgres: https://github.com/franciscoprin/pipelinewise-tap-postgres
- creating tables in github README.md: https://docs.github.com/es/github/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables
