# Clone project
```bash
mkdir little-lemon-web-application

cd little-lemon-web-application

git init

git clone https://github.com/truonganhvu205/little-lemon-web-application.git
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

## Install Django
```bash
pipenv install django
```

## Install Framework
```bash
pipenv install djangorestframework
pipenv install djoser
```

## Connect to MySQL
```bash
sudo mysql -u root -p OR mysql -u root -p
CREATE DATABASE littlelemon;
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
auth/
restaurant/api-token-auth/
```

```bash
restaurant/
restaurant/booking/tables
restaurant/api/menu-items/
restaurant/api/menu-items/<int:pk>
```
