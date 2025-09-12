# code_quality_issues.py
# This file contains various code quality and style issues

import os,sys,json # Bad: Multiple imports on one line
from typing import *  # Bad: Wildcard import

# Bad: No docstring for module

# Bad: Global variables
global_var = "bad practice"
ANOTHER_GLOBAL = 123

class badClassName:  # Bad: Class name not CamelCase
    """Bad example class with quality issues."""
    
    def __init__(self,name,age,email):  # Bad: No spaces after commas
        self.name=name  # Bad: No spaces around assignment
        self.age =age   # Bad: Inconsistent spacing
        self.email= email
        self._private_var = "should be documented"
        
        # Bad: Magic number without explanation
        if age > 65:
            self.discount = 0.15
    
    # Bad: Method name not snake_case
    def getName(self):
        return self.name
    
    # Bad: Too many parameters, no type hints
    def updateUserInfo(self, name, age, email, phone, address, city, state, zip_code, country):
        self.name = name
        self.age = age
        self.email = email
        # ... and so on
    
    # Bad: No docstring, unclear method purpose
    def calc(self, x, y, z=None):
        if z:
            return x * y + z
        else:
            return x * y
    
    # Bad: Complex nested conditions
    def checkEligibility(self, user_type, age, income, credit_score):
        if user_type == "premium":
            if age >= 18:
                if income > 50000:
                    if credit_score > 700:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    # Bad: Long method doing multiple things
    def processUserData(self, user_data):
        # Validate data
        if not user_data:
            raise ValueError("No data")
        if 'email' not in user_data:
            raise ValueError("No email")
        if '@' not in user_data['email']:
            raise ValueError("Invalid email")
        
        # Clean data
        user_data['name'] = user_data['name'].strip().title()
        user_data['email'] = user_data['email'].lower()
        
        # Save to database
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)", 
                      (user_data['name'], user_data['email'], user_data['age']))
        db_conn.commit()
        
        # Send welcome email
        self.send_email(user_data['email'], "Welcome!")
        
        # Update statistics
        self.user_count += 1
        self.last_signup = datetime.now()
        
        # Log activity
        print(f"User {user_data['name']} registered")
        
        return True

# Bad: Function name not descriptive
def func1(data):
    """Bad function with quality issues."""
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

# Bad: Too many local variables, unclear logic
def process_order(order_id, customer_id, items, shipping_address, billing_address, payment_method, discount_code, special_instructions):
    order_total = 0
    tax_amount = 0
    shipping_cost = 0
    discount_amount = 0
    final_total = 0
    processed_items = []
    
    # Bad: Deeply nested logic
    for item in items:
        if item['available']:
            if item['price'] > 0:
                if item['quantity'] > 0:
                    if item['category'] == 'electronics':
                        if item['warranty']:
                            item['price'] += 50
                            if item['extended_warranty']:
                                item['price'] += 100
                    processed_items.append(item)
                    order_total += item['price'] * item['quantity']
    
    # More complex logic continues...
    return final_total

# Bad: Unused imports and variables
import random
import datetime
from collections import defaultdict

unused_variable = "This is never used"

def calculate_something():
    another_unused = 42
    x = 10
    y = 20
    # z is calculated but never used
    z = x + y
    return x * y

# Bad: Inconsistent naming conventions
class user_manager:  # Should be UserManager
    def __init__(self):
        self.UserList = []     # Should be user_list
        self.MAX_users = 100   # Should be MAX_USERS
        self.current_User = None  # Should be current_user
    
    def AddUser(self, NewUser):  # Should be add_user, new_user
        self.UserList.append(NewUser)
    
    def getUser(self, UserID):   # Should be get_user, user_id
        for User in self.UserList:  # Should be user
            if User.id == UserID:
                return User
        return None

# Bad: Code duplication
class DatabaseManager:
    def save_user(self, user):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)", 
                      (user.name, user.email, user.age))
        conn.commit()
        conn.close()
    
    def save_product(self, product):
        conn = sqlite3.connect('database.db')  # Duplicated code
        cursor = conn.cursor()                  # Duplicated code
        cursor.execute("INSERT INTO products VALUES (?, ?, ?)", 
                      (product.name, product.price, product.category))
        conn.commit()                           # Duplicated code
        conn.close()                            # Duplicated code
    
    def save_order(self, order):
        conn = sqlite3.connect('database.db')  # Duplicated code
        cursor = conn.cursor()                  # Duplicated code
        cursor.execute("INSERT INTO orders VALUES (?, ?, ?)", 
                      (order.id, order.customer_id, order.total))
        conn.commit()                           # Duplicated code
        conn.close()                            # Duplicated code

# Bad: Magic numbers and strings throughout
def calculate_pricing(base_price, customer_type):
    if customer_type == "premium":  # Magic string
        discount = base_price * 0.15  # Magic number
    elif customer_type == "gold":   # Magic string
        discount = base_price * 0.25  # Magic number
    elif customer_type == "silver": # Magic string
        discount = base_price * 0.10  # Magic number
    else:
        discount = 0
    
    tax = (base_price - discount) * 0.08  # Magic number
    shipping = 15.99 if base_price < 50 else 0  # Magic numbers
    
    return base_price - discount + tax + shipping

# Bad: Overly complex one-liner
def process_data(data):
    return {k: [item for sublist in [[x*2 if x > 0 else x/2 for x in v if isinstance(x, (int, float))] for v in data[k] if isinstance(v, list)] for item in sublist] for k in data if k.startswith('num')}

# Bad: No error handling
def divide_numbers(a, b):
    return a / b  # No check for division by zero

def read_file(filename):
    with open(filename) as f:  # No check if file exists
        return f.read()

def access_dict(data, key):
    return data[key]  # No check if key exists

# Bad: Mixing tabs and spaces (simulated with comments)
def mixed_indentation():
    if True:
        print("Using 4 spaces")  # 4 spaces
        if True:
            print("Using tab")       # Tab (simulated)
            if True:
                print("Using 2 spaces")  # 2 spaces

# Bad: Too many return statements
def get_user_status(user):
    if not user:
        return "invalid"
    if not user.active:
        return "inactive" 
    if user.banned:
        return "banned"
    if user.suspended:
        return "suspended"
    if user.premium:
        return "premium"
    if user.verified:
        return "verified"
    return "regular"

# Bad: Commented out code left in
def old_function():
    # Old implementation
    # result = []
    # for item in data:
    #     if item.valid:
    #         result.append(item.process())
    # return result
    
    # New implementation
    return [item.process() for item in data if item.valid]

# Bad: Hardcoded file paths and URLs
def load_config():
    with open('/home/user/config.ini') as f:  # Hardcoded path
        return f.read()

def fetch_api_data():
    import requests
    # Hardcoded URL
    response = requests.get('http://api.mycompany.com/data')
    return response.json()

# Bad: Poor variable names
def calculate(x, y, z):
    a = x + y
    b = a * z
    c = b / 2
    d = c ** 0.5
    return d

# Bad: Functions that are too long (continuation of earlier pattern)
def mega_function(param1, param2, param3, param4, param5):
    """This function does way too many things."""
    # Step 1: Input validation (should be separate function)
    if not param1 or not param2:
        raise ValueError("Invalid input")
    
    # Step 2: Data preprocessing (should be separate function)
    cleaned_param1 = param1.strip().lower()
    processed_param2 = [x for x in param2 if x > 0]
    
    # Step 3: Complex calculations (should be separate function)
    intermediate_result = sum(processed_param2) * len(cleaned_param1)
    
    # Step 4: More processing (should be separate function)
    final_result = []
    for i in range(len(processed_param2)):
        temp = processed_param2[i] * param3
        if temp > param4:
            final_result.append(temp)
        else:
            final_result.append(temp * param5)
    
    # Step 5: Output formatting (should be separate function)
    formatted_output = {
        'result': final_result,
        'summary': f"Processed {len(final_result)} items",
        'total': sum(final_result)
    }
    
    return formatted_output

if __name__ == "__main__":
    # Bad: No proper main function
    user = badClassName("John", 30, "john@example.com")
    print(user.getName())
    
    # More bad practices in main execution
    data = func1([1, -2, 3, -4, 5])
    print(data)