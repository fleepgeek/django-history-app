# django-history-app

A history management app powered by Django. This app uses Djnago's contenttypes framework to manage different types of pages a user views in your application.

The idea behind this application is to show you a how to achieve better polymorphic relationship between objects of different types using GenericForeignKey.

## Use Cases
* History -  managing different page objects (eg product and blog post object)
* Shopping Cart - managing different types of products (ebook, electronics and furniture objects)

Managing these types of relationship using a ForeignKey could be more difficult and there would be need for you to manage your inheritance and migrations when new types of objects are added.

## Link to the tutorial
Learn and understand how to build this app.
[Watch on YouTube](https://www.youtube.com/watch?v=bEEFo75IkYU) 

## Installation

Create a folder on your computer then clone this repo with this command:

```bash
git clone https://github.com/fleepgeek/django-history-app.git
#Next
cd django-history-app
```
I used pipenv to create a virtual environment, so you install pipenv globally on your computer:
```bash
pip install pipenv
```

Create a new virtual environment:
```bash
pipenv shell
```

Next, install required packages stored in the ``Pipfile.lock`` file using the ``sync`` command.
```bash
pipenv sync
```

Then you enter the app directory
```bash
cd django_project
```

After that, you run your migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Finally, run the app
```bash
python manage.py runserver
```
You're good to go :sparkles:


