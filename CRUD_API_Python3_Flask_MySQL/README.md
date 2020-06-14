# Flask-Python3-MySQL CRUD API:

### This API allows four basic actions:
* **Create a User:** must provide a (non-empty) first name (max.: 100 Characters), last name (max.: 100 Characters), and unique email (max.: 100 Characters, must not be in use by another user)
* **Update a User:** must provide an id and at least one field to update
* **Retrieve a List of All Current Users:** self-explanatory
* **Delete a User:** must provide an id

### Packages required, tech info and how to run:
* This API was created and tested on a Linux Debian 10 machine
* Main software packages used/installed for this API:
    MySQL (8.0.2), Python (3.7.3 -- including: python3.7-venv), Flask 1.1.2, PyMySQL 0.9.3
* To run (locally): on a terminal emulator, change working directory to the API folder (ex: cd ~/CRUD_API_Python3_Flask_MySQL) and start the virtual environment and the application by running:  **source venv/bin/activate && python3 main.py**, 
* After the step above, open a browser on http://127.0.0.1:5000, and you should see the message: **API is ready!**
* To quit, press CTRL+C and then run command **deactivate** on the terminal

### Database creation:
Please see all details on the file **database.sql**
    
### Using the API (with curl command):
**Get all users**

```curl --location --request GET 'http://localhost:5000/users'```    

**Add a new user**

```curl --location --request POST 'http://localhost:5000/users/create' --form 'first_name=Johnny' --form 'last_name=Doe' --form 'email=jodoewonder4411@google.com'```    

```curl --location --request POST 'http://localhost:5000/users/create' --form 'first_name=Jeff' --form 'last_name=Smith' --form 'email=jeffyrs8123@google.com'```    

**Update User**

```curl --location --request POST 'http://localhost:5000/users/update/3' --form 'first_name=Riley'```

```curl --location --request POST 'http://localhost:5000/users/update/2' --form 'last_name=Moe'```

**Delete User**

```curl --location --request DELETE 'http://localhost:5000/users/delete/1'```

```curl --location --request DELETE 'http://localhost:5000/users/delete/2'```


### Flask-Python3-MySQL CRUD API Author:
Jamil Said Jr. -- Copyright (C) Jamil Said Jr
