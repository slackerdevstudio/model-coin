# model-coin

[![Build Status](https://travis-ci.org/slackerdevstudio/model-coin.svg?branch=master)](https://travis-ci.org/slackerdevstudio/model-coin)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Its all about an earning score > 1. Check out the project's [documentation](http://slackerdevstudio.github.io/model-coin/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```
