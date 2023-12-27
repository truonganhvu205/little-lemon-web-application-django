# Clone project
```bash
git init
git clone https://github.com/truonganhvu205/little-lemon-web-application.git
cd little-lemon-web-application
```

## Install pipenv
```bash
pip3 install pipenv
```

## Activate virtual environment
```bash
pipenv --python 3.10
pipenv shell
```

## Install Django & Frameworks
```bash
pipenv install django
pipenv install mysqlclient
pipenv install djangorestframework
pipenv install djoser
```

## Connect to MySQL
```bash
mysql -u root -p
create database littlelemon;
exit
```

# Run server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

# API endpoints
```bash
/auth/
/restaurant/api-token-auth/
```

```bash
/restaurant/
/restaurant/booking/tables
/restaurant/api/menu-items/
/restaurant/api/menu-items/<int:pk>
```
