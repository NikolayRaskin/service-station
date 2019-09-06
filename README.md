Service station

Python v. 3.7.1;
Django v. 2.2;
Data Base: MySQL;

Start app:
Download Python 3.7+, django 2+
go to serviceStation folder and find manage.py file
about db:
    I used local MySQL server you should to configure it. Change my mysql's settings at setting.py file (
        'NAME': 'nameOfDB',
        'USER': 'userName',
        'PASSWORD': 'Pass',
        )
    When you configure your db, run:
        python manage.py makemigrations
        python manage.py migrate
        python manage.py loaddata datadump.json
For run server run this:
    run python manage.py runserver
    and go to: http://localhost:8000/   (or another port what you set)
For Sing In use: 
    login: admin
    pass: admin

Short info:
At the Main Page you can find:
  -- lists of Customers, Cars, Orders
  -- search(searching by table's colums(id,name,email and other))
  -- buttons to add customer, car, order
  -- using the list and search, you can determine whether this user has already been registered before. If so, using the edit button, put a flag in the isReturning field.
  -- buttons(with icons) to view customer profile, 
  -- edit and remove customer
  -- edit and remove car
  -- edit and remove order
At the Customer Profile(client card) you can find: personal data, lists of customer's cars and orders.
You can't remover Customer while he(she) has a car with order. 

Ty for for watching :)
I will be very glad to see your feedback (nikolay.raskin98@gmail.com).