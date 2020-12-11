import json
import os
import random


class EmployeeList:
    
    def check_input(self, emp_dic):
        
        if not emp_dic or not isinstance(emp_dic,dict):
            return False 
        
        for key, value in emp_dic.items():
            if not key or not value:
                return False

        return True


    def error_print(self, err, err_mes=''):
        
        if err == 1:
            print('Operation failed! A dictionary with non-empty Employee ID and Full Name entries must be provided for successfull operation.')
        elif err == 2:
            print('Request failed! Exception raised: ' + str(err_mes))
        elif err == 3:
            print('Request failed! An non-empty employee id must be provided.')
        elif err == 4:
            print('Employee list was already empty!')
        elif err == 5:
            print('Employee list is empty! Cannot generate groups!')
        elif err == 6:
            print('Employee list does not have enough employees to generate a group!')
        elif err == 7:
            print('Employee list is empty!')


        
    def employee_list_save(self, emp_dic):
        
        if not self.check_input(emp_dic):
            self.error_print(1)
            return
        
        with open('employee_list.json', 'w') as el:
            json.dump(emp_dic, el, sort_keys=True, indent=4)


    def employee_list_retrieve(self):

        if os.path.exists('employee_list.json'):
            try:
                with open('employee_list.json', 'r') as el:
                    emp_dic = json.load(el)
                    print(json.dumps(emp_dic, sort_keys=True, indent=4))
            except Exception as e: 
                self.error_print(2, str(e))
                return

        else:
            self.error_print(7)
            return

            
    def add_update_employee(self, new_emp_dic):
        
        if not self.check_input(new_emp_dic):
            self.error_print(1)
            return
        
        if os.path.exists('employee_list.json'):
            try:
                with open('employee_list.json', 'r') as el:
                    emp_dic = json.load(el)
                for key, value in new_emp_dic.items():
                    emp_dic[key] = value
                with open('employee_list.json', 'w') as el:
                    json.dump(emp_dic, el, sort_keys=True, indent=4)
            except Exception as e: 
                self.error_print(2, str(e))
                return
            
        else:
            with open('employee_list.json', 'w') as el:
                json.dump(new_emp_dic, el, sort_keys=True, indent=4)



    def delete_employee(self, emp_id):
        
        emp_id = str(emp_id)
        if not emp_id:
            self.error_print(3)
            return
        
        if os.path.exists('employee_list.json'):
            try:
                with open('employee_list.json', 'r') as el:
                    emp_dic = json.load(el)
                emp_dic.pop(emp_id, None)
                with open('employee_list.json', 'w') as el:
                    json.dump(emp_dic, el, sort_keys=True, indent=4)
            except Exception as e: 
                self.error_print(2, str(e))
                return
            
        else:
            self.error_print(4)
            return


    def employee_groups(self):
        
        if os.path.exists('employee_list.json'):
            try:
                with open('employee_list.json', 'r') as el:
                    emp_dic = json.load(el)
                if len(emp_dic) <= 2:
                    self.error_print(6)
                    return
                elif 2 < len(emp_dic) <= 5 :
                    print(json.dumps(emp_dic, sort_keys=True, indent=4))
                else:
                    res = []
                    for i in range(len(emp_dic)//3):
                        temp = {}
                        for j in range(3):
                            a = random.choice(list(emp_dic.keys()))
                            temp.update({a:emp_dic[a]})
                            emp_dic.pop(a)
                        res.append(temp)
                    if emp_dic:
                        a = random.choice(res)
                        a.update(emp_dic)
                    print(json.dumps(res, sort_keys=True, indent=4))

            except Exception as e: 
                self.error_print(2, str(e))
                return
            
        else:
            self.error_print(5)
            return
