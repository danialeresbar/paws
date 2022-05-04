# PAWS

## Documentation

### Directory tree

```
├── apps
│   ├── main
│   │   ├── fixtures
│   │   │   └── development.json
│   │   ├── migrations
│   │   ├── models
│   │   │   └── __init__.py
│   │   │   └── base_model.py
│   │   ├── tests
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── views.py
│   └── __init__.py
├── htmlcov
├── paws
│   ├── settings
│   │   ├── partials
│   │   │   └── utils.py
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── test.py
│   ├── static
│   ├── __init__.py
│   ├── asgi.py
│   ├── storage_backends.py
│   ├── urls.py
│   └── wsgi.py
├── scripts
│   ├── dev-entrypoint.sh
│   ├── prod-entrypoint.sh
│   └── wait-for-it.sh
├── .coveragerc
├── .editorconfig
├── .envrc
├── .gitignore
├── Dockerfile
├── Makefile
├── README.md
├── docker-compose.override.yml
├── docker-compose.yml
├── heroku.yml
├── manage.py
├── requirements.txt
└── test-requirements.txt
```

### How to run the project ###

The project use docker, so just run:

```
docker-compose up
```

*Your app will run in url `localhost`*

To recreate the docker images after dependencies changes run:

```
docker-compose up --build
```

To remove the docker containers including the database (Useful sometimes when dealing with migrations):

```
docker-compose down
```

> If you want to delete the information saved on docker volumes you can use `docker-compose down -v`

### Accessing Administration

The django admin site of the project can be accessed at `localhost/admin`

By default, the development configuration creates a superuser with the following credentials:

```
Username: admin
Password: admin
```

## Heroku

The project is Heroku ready with
**[Build Manifest](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)**
deploy approach. You should follow those steps to deploy it as heroku app.
> Keep in mind Docker-based deployments are limited to the same constraints that Git-based
> deployments are. For example, persistent volumes are not supported since the file system
> is ephemeral and web processes only support HTTP(S) requests.

### Prerequisites 📋 ###

The production environment requires certain configuration before deploying the docker image,
such as the database, and the AWS settings.

### Environment variables 🛠️ ###

The system is configured using environment variables. The following is the list of
environment variables that are required or optional before deploying the system:

| Variable                  | Description                                                                                                                                  | Required | Default       |
|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|:--------:|:--------------|
| `ALLOWED_HOSTS`           | Project environment settings                                                                                                                 | **yes**  | *             |
| `CORS_ALLOWED_ORIGINS`    | Project environment settings                                                                                                                 | **yes**  | *             |
| `DEBUG`                   | Project environment settings                                                                                                                 | **yes**  | *False*       |
| `DEBUG_TOOLBAR`           | Project environment settings                                                                                                                 |  **no**  | *False*       |
| `SECRET_KEY`              | Key used by Django for tokens like CSRF and cookies, it can be any secret key but it's recommended to generate it using https://djecrety.ir/ | **yes**  | *None*        |
| `ENVIRONMENT`             | Project environment settings                                                                                                                 |  **no**  | *development* |

### Backing services ⚙️ ###

As expected in a Twelve Factors App the following services needs to be configured
using environment variables as well:

| Service           | Environment variable | Value                                               | Example                                                                                                                                                    |
|:------------------|:--------------------:|:----------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Postgres Database |    `DATABASE_URL`    | `postgresql://<user>:<pass>@<host>:<port>/<dbname>` | `postgres://dlfgyvooqebjiq:7f5a5bfbedf60019262c16dbfa78ea1558e48f7977cb8bc91de670ff0aeeeb02@ec2-18-233-83-165.compute-1.amazonaws.com:5432/d88kfm43j69i0s` |

### Deployment ☁ ###

When having all the prerequisites, and you have logged in with your Heroku client, 
clone the repository in the server, then deploy the containers with the commands:

```
heroku update beta
heroku plugins:install @heroku-cli/plugin-manifest
```

Then create your app using the --manifest flag. The stack of the app will
automatically be set to container:

```
heroku create app-name --manifest
```

> Do not forget change app-name for your app name

Commit your [heroku.yml](heroku.yml) to git:

```
git add heroku.yml
git commit -m "Add heroku build manifest"
```

Push the code:

```
git push heroku master
```

> Please check the [Known issues and limitations](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml#known-issues-and-limitations)
> for this approach

Finally, your application can be accessed from the Heroku [dashboard](https://dashboard.heroku.com/apps)! 🚀

## Authors ✒️

- [Daniel Alejandro Restrepo Barbosa](https://github.com/danialeresbar)
- [Siervo Francisco Rodríguez Castellanos](https://github.com/fraroca97)
- [Ángel Alfonso Cruz Roa]()
- [Héctor Ivan Reyes Moncayo]()
