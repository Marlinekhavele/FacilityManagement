## Inventory Management System for Gas Storage Facilities
A web-based inventory management system for gas storage facilities.

### Features

- Managing a hierarchical inventory structure.
- Providing real-time, dynamic interactions without full page reloads.
- Ensuring seamless user experience with infinite scrolling, filtering, and sorting.
- Allowing quick component creation through modals.

### Requirements

- Python 3.11
- Django 3.2+
- PostgreSQL

### Installation

- Clone the repository:
`git clone https://github.com/Marlinekhavele/FacilityManagement`

- cd `facility`

Set up PostgreSQL database:
```shell
  # Ubuntu
   - sudo apt-get update
   - sudo apt-get install postgresql postgresql-contrib
   # macOS
   - brew install postgresql

  # Switch to the PostgreSQL user
  - sudo -i -u postgres
  # linux
  - psql

  # Open PostgreSQL shell Mac
  -  brew services start postgres
  -  psql postgres

  # Create a new user 
  - CREATE USER postgres WITH PASSWORD 'password';

  # Create the database
  - CREATE DATABASE atmio;

  # Grant privileges to the user
  - GRANT ALL PRIVILEGES ON DATABASE atmio TO postgres;

  # Exit the PostgreSQL shell
   - \q
```
Create and activate a virtual environment: [install pyenv](https://ericsysmin.com/2024/02/05/how-to-install-pyenv-on-macos/)
```shell
pyenv virtualenv venv
pyenv activate venv
```

Install dependencies:
```shell
pip install -r requirements.txt
```

Initialize the database:
```shell
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:
```shell
python manage.py createsuperuser
```

Access the admin interface with the above command:
```shell
http://127.0.0.1:8000/admin/
```
Start the development server:
```shell
python manage.py runserver 
```

#### Usage
The application provides the following:
```shell
inventory/: Lists all Inventory
inventory_create/: Ability to create an inventory
component_lis/: List all components on the database
components_create/: Creates a new component
```
#### Testing
Run the test suite with:
```bash
python manage.py test
```

#### Lint
Run Lint:
```bash
make lint
```

#### Running the Service Locally:
```bash
make serve
```
Stopping the Service:
```bash
make stop
```
Restarting the Service:
```bash
make start
```
