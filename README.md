1. Create a folder called marketplace
2. cd into marketplace and create a venv using the command python3 -m venv env
3. Activate the env, using source env/bin/activate
4. Install django, using pip install django
5. create a django project, using django-admin startproject marketplace
6. You can now bring up your app, using python3 manage.py runserver
7. create an app using command, django-admin startapp core
8. To start an app you can also use "python3 manage.py startapp item"
9. If you have models in your app, and you want to create migrations, then do "python3 manage.py makemigrations"
10. Check the migrations folder in the app folder, and make sure migrations file has what you want.
11. Once you are good with migration file, use "python3 manage.py migrate"
12. Create a superuser to interact with the admin interface django provides
"python3 manage.py createsuperuser"
