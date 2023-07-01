# Zakerfit Project

A Gym(Sport-Crossfit) Project Built with Django, In Persian language.

### Setup Project:

1. Clone Repo:

```commandline
git clone https://github.com/Amirmahdikahdouii/zakerfit.git 
```

2. Open terminal in project root directory and make venv:

```commandline
python3 -m venv .venv
```

3. Active your venv:

```commandline
source .venv/bin/activate
```

4. Install Requirements:

```commandline
pip install -r requirements.txt
```

5. make .env file:

```commandline
vim A/.env
```

6. Put your own SECRET_KEY in .env:

```text
SECRET_KEY=Your SECRET_KEY here 
```
**For More Information about using django-environ read this [page](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)**

7. Runserver:

```commandline
python manage.py runserver
```
