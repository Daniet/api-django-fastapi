# API Django + FastAPI

This a API REST. The idea is to demonstrate a simple way to integrate FastAPI with Django. The elegance of FastAPI y the robustness of Django together is a truly wonderfull combination.

## Quickstart

First of all, clone this repo.

```
git clone https://github.com/DD21S/api-django-fastapi.git
```

Then, in the project directory, install the requirements.

```
pip install -r requirements.txt
```

Now, make the migrations.

```
python manage.py migrate
``` 

And finally, run the project.

```
uvicorn django_fastapi.asgi:app --reload
```

Ready, now your API is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create and activate one with these commands:

```
python3 -m venv venv
source venv/bin/activate
```

## Routes

| **METHOD**  | **ROUTE**                  | **FUNCTIONALITY**              |
| ----------- | -------------------------- | ------------------------------ |
| **GET**     | /                          | Django root page               |
| **GET**     | /admin                     | Django administration page     |
| **GET**     | /docs                      | Documentation                  |
| **GET**     | /characters                | Get all characters             |
| **POST**    | /characters                | Create a new character         |
| **PUT**     | /characters/{character_id} | Update a character             |
| **DELETE**  | /characters/{character_id} | Delete a character             |
