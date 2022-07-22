# Project DB to UI

This is a demo project to create an end to end functionality using Vue.js (v2 + Vuetify).

It's just a CRUD app where you can see a list of Projects, you can create more, filter and delete them.

# Architecture

In this project there are 3 main components, with the respective folders:

- **/scripts** containing Python scripts to create random data in the db
- **/api** containing the Node.js Back End
- **/ui** containing the Vue.js (v2 + Vuetify) Front End

# Setup

## Requirements

- **PostgreSQL / MySQL database** I used one in elephantsql.com but you can run your own.
- **Node.js** installed in your own machine (or emulated thrugh Docker) to run frontend and backend.

## Env Vars

You should add a `.env` file in `api` folder:

```bash
export POSTGRES_HOST=...
export POSTGRES_USER=...
export POSTGRES_PWD=...
export POSTGRES_PORT=...
export POSTGRES_DB_NAME=...
```

and another `.env` file in the `scripts` folder, with full link:

```bash
export POSTGRES_URI=postgres://...
```

Also, make sure to activate the Python environment and install dependencies:

```bash
source scripts/.venv/bin/activate
source scripts/.env
pip install -r scripts/requirements.txt
```

## Database

You can check you can reach the PostgreSQL database by running the "check version" script

```bash
python scripts/00_check_version.py
```

Then you can create tables by running:

```bash
python scripts/01_create_tables.py
```

and generate data with the following command:

```bash
python scripts/02_insert_batch_data.py
```

To verify, you can run the query `SELECT * FROM PROJECTS` into your db.

> If you will need to drop table for some reason, just run the script `scripts/03_drop_tables.py`

## API

Once the database is setup, it's time to setup the Node.js API.

```bash
cd api
source .env # Read env variables
npm install
node index.js
```

## UI

If the API is running, just open a new terminal and start the Vue.js UI:

```bash
cd ui
npm install
npm run serve
```

Navigate to [localhost:8080](http://localhost:8080/) to access the running application
