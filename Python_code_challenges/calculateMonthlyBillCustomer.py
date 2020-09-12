""" calculateMonthlyBillCustomer

You are employed on a company that provides online services for customers. Your task is to calculate 
the monthly bill (rounded to 2 decimal places) for each customer based on the number of active users 
per day and the subscription rate. 

Each active user should be charged a prorated amount for the day active until deactivated (both inclusive). 
Your input is raw customer data provided in JSON. The data includes 3 parameters:

1) Month: 
Always present, provided in YYYY-MM format.
Ex: "2018-01"

2) Subscription:
May be present or not. If present, shows the current subscription for the customer
Ex: 
{
  'id': 1,
  'monthly_price_per_user': 4 
}

3) Users:
May be empty or not. If not empty, has this structure:
[
  {
    'id': 1,
    'name': 'Employee #1',
    'customer_id': 1,
    'activated_on': datetime.date(2018, 11, 4),
    'deactivated_on': datetime.date(2019, 1, 10)
  },
  {
    'id': 2,
    'name': 'Employee #2',
    'customer_id': 1,
    'activated_on': datetime.date(2018, 12, 4),
    'deactivated_on': None
  }
]

Calculation example:
If a customer had 2 users activated for 2 days each in a 30-day month at a $30 subscription rate, then the 
total bill would be:

2 x 2 x (30/30) = 4.0

"""

import datetime
import calendar

def bill(month, subscription, users):
    if not subscription or not users:
        return 0.0
    f_day_mon = datetime.date(int(month[:4]), int(month[-2:]), 1)
    l_day_mon = (f_day_mon + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
    n_days_mon = l_day_mon.day
    cost_day = subscription['monthly_price_per_user'] / n_days_mon
    res = 0.0
    for u in users:
        u_n_days = n_days_mon
        if u['activated_on']:
            diff_act = (f_day_mon - u['activated_on']).days
            u_n_days = (u_n_days + diff_act) if diff_act < 0 else u_n_days
            if u['deactivated_on']:
                diff_dia = (u['deactivated_on'] - l_day_mon).days
                u_n_days = (u_n_days + diff_dia) if diff_dia < 0 else u_n_days
        else:
            u_n_days = 0
        res += u_n_days * cost_day
    return round(res, 2)


customer_1 = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 10, 7),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 9),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },  
]

customer_2 = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 9, 8),
        'deactivated_on': None,
        'customer_id': 2,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 2,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 2,
    },
    {
        'id': 4,
        'name': 'Employee #4',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': datetime.date(2019, 1, 10),
        'customer_id': 2,
    },    
]


customer_3 = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 10, 18),
        'deactivated_on': None,
        'customer_id': 3,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 11, 5),
        'deactivated_on': None,
        'customer_id': 3,
    },
]

customer_4 = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': None,
        'deactivated_on': None,
        'customer_id': 4,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 5),
        'deactivated_on': None,
        'customer_id': 4,
    },
]

customer_5 = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': None,
        'deactivated_on': None,
        'customer_id': 5,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': datetime.date(2019, 1, 10),
        'customer_id': 5,
    },
]


subscription = {
    'id': 1,
    'monthly_price_per_user': 4
}

print(bill('2019-01', subscription, [])) #0.0
print(bill('2019-01', {}, customer_4)) #0.0
print(bill('2019-01', subscription, customer_1)) #10.84
print(bill('2019-01', subscription, customer_2)) #12.13
print(bill('2019-01', subscription, customer_3)) #8.0
print(bill('2019-01', subscription, customer_4)) #4.0
print(bill('2019-01', subscription, customer_5)) #0.13
