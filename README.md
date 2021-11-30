# Django
Django makes it easier to build better web apps more quickly and with less code.

### Activate environment
```
python3 -m venv .env  
source venv/bin/activate
```
### Deactivate environment
```
deactivate
```
### Install tools
```
pip install django -U
pip freeze
```

### Creating a project

If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a **Django project – a collection** of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

From the command line, **cd** into a directory where you’d like to store your code, then run the following command:

```
# Interfaz
django-admin
```
```
# New project
django-admin startproject photobucket

# New project with existing files
django-admin startproject photobucket .

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
These files are:

* The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
* **manage.py:** A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in [django-admin and manage.py](https://docs.djangoproject.com/en/3.2/ref/django-admin/).
* The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
* **mysite/__init__.py:** An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
* **mysite/settings.py:** Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/3.2/topics/settings/) will tell you all about how settings work.
* **mysite/urls.py:** The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/3.2/topics/http/urls/).
* **mysite/asgi.py:** An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/) for more details.
* **mysite/wsgi.py:** An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/) for more details.

### Launch application
```
# Available subcommands:
python manage.py

# Commands:
python manage.py runserver
```

### Testing
```
# Debug endpoint
def debugger(request):
    import pdb; pdb.set_trace()
    return HttpResponse('Oh, hi!')

# Exit: Enter letter 'c' and Intro

```

# Django Specification

[Django](https://www.djangoproject.com/)

[Source code](https://github.com/django/django)

[Documentation](https://docs.djangoproject.com/en/3.2/)

[URL dispatcher](https://docs.djangoproject.com/en/3.2/topics/http/urls/)

[Request and response objects](https://docs.djangoproject.com/en/3.2/ref/request-response/)

#### General description

Django is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.

#### Technician description 

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

* **Ridiculously fast.** Django was designed to help developers take applications from concept to completion as quickly as possible.

* **Reassuringly secure.** Django takes security seriously and helps developers avoid many common security mistakes.

* **Exceedingly scalable.** Some of the busiest sites on the web leverage Django’s ability to quickly and flexibly scale.

# Tools

### []()

[Source code]()



### [TailwindCSS](https://tailwindcss.com/)

[Integrating TailwindCSS into Flask Apps](https://www.section.io/engineering-education/integrate-tailwindcss-into-flask/)

TailwindCSS is a utility-first CSS framework used to build frontend applications. TailwindCSS differs from other kinds of CSS frameworks as it gives the user total control over their design.

Rather than adding obscure CSS classes to your code, with TailwindCSS you use utility classes to create your components, with as much control over every single styling as you want. All without having to ever write a single line of CSS.




