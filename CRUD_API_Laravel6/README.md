# Laravel 6 CRUD API:

### This API allows four basic actions:
* **Create a User:** must provide a (non-empty) first name (max.: 100 Characters), last name (max.: 100 Characters), and unique email (max.: 100 Characters, must not be in use by another user)
* **Update a User:** must provide an id and at least one field to update
* **Retrieve a List of All Current Users:** self-explanatory
* **Delete a User:** must provide an id

### Packages required, tech info and how to run:
* This API was created and tested on a Linux Debian 10 machine
* Main software packages used/installed for this API:
    apache2 (2.4.38), MySQL (8.0.19), composer (1.8.4), Laravel (6.15.1), PHP (7.3 -- including: php7.3-common php7.3-cli php7.3-gd php7.3-mysql php7.3-curl php7.3-intl php7.3-mbstring php7.3-bcmath php7.3-imap php7.3-xml php7.3-zip)
* To run (locally): on a terminal emulator, change working directory to the API folder (ex: cd ~/CRUD_API_Laravel6/CRUD_API_Laravel6) and  start the Laravel service by running:  **php artisan serve**
* After the step above, open browser on http://127.0.0.1:8000 to see if Laravel is running

### Database creation:
Please see all details on the file **database.sql**
    
### Using the API (with curl command):
**Get all users**
```curl --location --request GET 'http://localhost:8000/api/users'```    

**Add a new user**
```curl --location --request POST 'http://localhost:8000/api/users/create' --form 'first_name=Johnny' --form 'last_name=Doe' --form 'email=jodoewonder4411@google.com'```    

```curl --location --request POST 'http://localhost:8000/api/users/create' --form 'first_name=Jeff' --form 'last_name=Smith' --form 'email=jeffyrs8123@google.com'```    

**Update User**
```curl --location --request POST 'http://localhost:8000/api/users/update/3' --form 'first_name=Riley'```

```curl --location --request POST 'http://localhost:8000/api/users/update/2' --form 'last_name=Moe'```

**Delete User**
```curl --location --request DELETE 'http://localhost:8000/api/users/delete/1'```

```curl --location --request DELETE 'http://localhost:8000/api/users/delete/2'```


### Laravel 6 CRUD API Author:
Jamil Said Jr. -- Copyright (C) Jamil Said Jr
