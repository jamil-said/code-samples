# Python3-JSON CRUD Employee List Random Groups:

### Description:
This program allows users to create, read, update and delete a list of "company employees", as well as generate a list of randomly selected employee groups (min: 3, max: 5 employees per group). The employee list is "persistent", saved in a JSON file created/located in the same folder where the main program is located.

### This program allows five basic actions:
* **Bulk Create/Overwrite an Employee List:** must provide a non-empty dictionary with employee id as the key and the employee full name as the value. If an employee list exists, it will be overwritten by the new one
* **Retrieve the Existing Employee List:** this operation will display all employees on the employee list. If the employee list doesn't exist, this operation will fail
* **Create or Update Employees on the Employee List:** must provide a non-empty dictionary with employee id as the key and the employee full name as the value. If the employee list exists, it will be updated, if the employee list doesn't exist, it will be created
* **Delete a User:** must provide an employee id for the user to be deleted
* **Generate Random Group of Employees:** all employees on the employee list will be combined randomly in groups (min: 3, max: 5 employees per group), and the list of groups will be displayed

### Packages required, and tech info:
* This program was created and tested on a Linux Debian 10 machine
* Main software packages used/installed:
    Python (3.7.3)

### Using the program:
**Running the Program**

On a terminal emulator, change the working directory to the folder where the program is located (ex: ```cd /home/user/scripts```), then type the command ```python3``` to create a Python 3 session and then run ```exec(open("employee_list.py").read())```. After that, run one of the following commands to interact with the program.

**Bulk Create/Overwrite an Employee List**

```EmployeeList().employee_list_save({'1001':'John Smith', '1002':'John Smith', '1005':'Mary Doe', '1007': 'Joanne Sullivan', '1008':'Robert Smith', '1009': 'Lilly Schmidt', '1012':'Josh Garland', '1015':'Louise Blue', '1023':'Nina Simone', '1024':'Albert Moe', '1027':'Lisa Monroe', '1028':'Joe Sullivan', '1029':'Carl Benson', '1031':'Joe Gabriel', '1033':'Laura Blacksmith', '1034':'Ming Li', '1035':'Amilcar Doze', '1037':'Liza Windsor', '1039':'Roger Willy', '1042':'Andy Ma', '1044':'Marie Willy', '1045':'Adriana P. Almeida'})```    

**Retrieve the Existing Employee List**

```EmployeeList().employee_list_retrieve()```

**Create or Update Employees on an Existing Employee List**

```EmployeeList().add_update_employee({'1045':'Adriana P. Soza', '1047':'Jose N. Rodriguez'})```

**Delete User**

```EmployeeList().delete_employee(1047)```

**Generate Random Group of Employees**

```EmployeeList().employee_groups()```

### Python3-JSON CRUD Employee List Random Groups Author:
Jamil Said Jr. -- Copyright (C) Jamil Said Jr
