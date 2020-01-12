# Tweet's Project

A simple data fetching from twitter.

### Prerequisites

Before you continue, ensure you meet the following requirements:  

* Installed Python (you can download it via https://www.python.org/downloads/). Note: This project using python 3.7
* Installed Django
* Installed djangorestframework
* Installed tweepy (for using Twitter's API)

Note: I've provided all of these requirements in requirements.txt so you can install it by type command

```
pip install -r requirements.txt
```

### Migrations

After installed. Next thing that you've to do is migrate project for detecting changed following:

```
python manage.py migrate

python manage.py makemigrations
```
### Runserver

Now you can run project via:

```
python manage.py runserver
```

## Running the tests

Running test for checking whether if the endpoint return corrected data or not. Or if there are any changed in code you can check it via run this test.
```
python manage.py test
```

