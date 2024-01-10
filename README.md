# Airflow SQLite Docker Compose
This repo contains resources for deploying a development Airflow instance with an SQLite metadata backend using Docker Compose. The `./airflow/docker-compose.yaml` is a modified version of the official Airflow [docker-compose.yml](https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml) and is based on instructions from the official Airflow docs for [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/2.8.0/howto/docker-compose/index.html).

Note: This resources are based on Airflow version `2.8.0`. However, I imagine the instructions can apply to all versions `2.x.x` with minor modifications.

## Warnings
- The resources in this repo are purely for testing/development purposes and should not be used for production.
- You can only use `SequentialExecutor` with SQLite. If require a different executor you should reference the official Airflow docs for [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/2.7.0/howto/docker-compose/index.html).

## Usage
### Initial Setup
1. Create Airflow supporting folders: ```mkdir -p ./{config,dags,db,logs,plugins}```
2. Create `.env` file: ```echo -e "AIRFLOW_UID=$(id -u)" > .env```

### (Option 1) Deploy Airflow without Custom Image
- Start docker containers: `docker compose up -d`

### (Option 2) Deploy airflow with Custom Image
- Update the `docker-compose.yml`. Comment the line `image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.8.0}` and uncomment the line below `build: .`. [reference](https://airflow.apache.org/docs/apache-airflow/2.7.0/howto/docker-compose/index.html#special-case-adding-dependencies-via-requirements-txt-file)
- (Optional) Update the `Dockerfile` as necessary. The common changes you can make is to modify the Airflow version.
- (Optional) Add custom Python packages to the `requirements.txt` file. Airflow plugins hosted on Pypi can also be added here.
- Build custom docker image: `docker compose build`
- Start docker containers: `docker compose up -d`. Alternative, you can build and start the container automatically using the command: `docker compose up --build -d`

### Login to Airflow UI
- Go to `http://localhost:8080`
- Login with the username and password. The default username and password is `airflow` and `airflow` respectively
### (Optional) Configure Connection on Airflow UI
- Go to the menu directory: Admin > Connections
- Click on the `+` icon to add a new record
- For `Connection Type`, choose the type of connection from the drop-down
- Input a `Connection Id` value. This will be the name of the connection. Exammple: clickhouse_conn
- Fill in the rest of the fields as necessary

### (Optional) Create DAG
New DAGs should be created in the `./dags` folder. Simply create a `.py` Python file and write the logic for the DAG. The result will be visible on the Airflow UI homepage when the file is saved.

### Tear down deployment
- Destroy Docker container: `docker compose down --volumes --remove-orphans`
- Delete the `./db/airflow.db` file

## Commands
- Build Custom Airflow Image: `docker compose build`
- Start Docker Containers: `docker compose up -d`
- Destroy Docker Containers: `docker compose down --volumes --remove-orphans`

## References
- [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/2.7.0/howto/docker-compose/index.html)