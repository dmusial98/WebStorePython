# WebStorePython

Simple web application with [Django Rest Framework](https://www.django-rest-framework.org/) and [Angular](https://angular.io/) using [JSON Web Tocken](https://jwt.io/) for auhorization. Project made for university studies.

## Prerequisites for starting app

### Frontend

#### nodejs
First of all install [node.js](https://nodejs.org/en/download/?utm_source=blog). Next test instalation in terminal via 
```
$ node -v
```
You shold get message with number of version nmp like 
```
$ v16.2.0
```
Then test npm
```
$ npm -v
```
#### angular cli

Install angular cli using npm
```
$ npm install -g @angular/cli
```

To test the @angular/cli run 
```
$ ng version
```

#### Run frontend app

For installing all requsted libraries go to frontend directory and type in terminal
```
$ npm install
```
after that, run app via 
```
$ ng serve
```
app works on http://localhost:4200

### Backend

First install [python](https://www.python.org/downloads/), next in root directory create locally environment. Type in terminal
```
$ python3 -m venv env
$ env\scripts\activate # Windows 
$ . env/bin/activate # MAC or Linux 
```

Then, we can install Django and the Django REST Framework, within that environment:
```
$ pip install django
$ pip install djangorestframework
```

go to webstore directory and run backend app with
```
$ python3 manage.py runserver
```

Should get message like:
```
System check identified no issues (0 silenced).
February 19, 2022 - 08:56:46
Django version 4.0.2, using settings 'webstore.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Endpoints

Available endpoints in backend app:
* ```admin/``` - allows for managing entities in database
* ```products/``` - getting all products from database
* ```products/create/``` - creating one product with POST HTTP method
* ```products/{id}/``` - getting (with GET) or editing (with PUT) product
* ```users/``` - getting all users from database
* ```users/create/``` - creating new user with POST HTTP method
* ```users/byName/{name}/``` - getting user with specified username
* ```carts/``` - getting carts of all clients
* ```carts/add/``` - added new cart for user
* ```api/token/``` - login to server, in JSON response can get access token and refresh token from JWT (POST method)
* ```api/token/refresh/``` - getting refresh token from JWT

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
