# buggy_code.py
# This file contains various types of bugs and logic errors

import json
import datetime
from typing import List, Dict, Optional

class BuggyCalculator:
    def __init__(self):
        self.history = []
        self.memory = 0
    
    # Division by zero bug
    def divide(self, a: float, b: float) -> float:
        """BUG: No division by zero check"""
        return a / b  # Will crash if b is 0
    
    # Index out of bounds bug
    def get_last_n_results(self, n: int) -> List[float]:
        """BUG: No bounds checking"""
        results = []
        for i in range(n):
            # Will crash if n > len(self.history)
            results.append(self.history[-1-i])
        return results
    
    # Type error bug
    def add_to_memory(self, value) -> None:
        """BUG: No type checking"""
        # Will crash if value is not numeric
        self.memory += value
    
    # Logic error in conditional
    def calculate_discount(self, price: float, customer_type: str) -> float:
        """BUG: Logic error in conditions"""
        if customer_type == "premium":
            discount = 0.2
        elif customer_type == "regular":
            discount = 0.1
        elif customer_type == "vip":
            discount = 0.3
        # BUG: No else clause - discount undefined for other types
        
        return price * (1 - discount)  # NameError if customer_type is unexpected

class BuggyDataProcessor:
    def __init__(self):
        self.data = []
    
    # Mutable default argument bug
    def add_items(self, items: List = []) -> None:
        """BUG: Mutable default argument"""
        items.append("default_item")  # Modifies shared default list
        self.data.extend(items)
    
    # Off-by-one error
    def get_middle_elements(self, lst: List) -> List:
        """BUG: Off-by-one error"""
        if len(lst) <= 2:
            return lst
        
        start = len(lst) // 2 - 1
        end = len(lst) // 2 + 1
        # BUG: end index might be out of bounds
        return lst[start:end+1]
    
    # Infinite loop bug
    def countdown(self, start: int) -> List[int]:
        """BUG: Potential infinite loop"""
        result = []
        current = start
        while current >= 0:
            result.append(current)
            # BUG: Forgot to decrement current - infinite loop!
        return result
    
    # Variable shadowing bug
    def process_numbers(self, numbers: List[int]) -> int:
        """BUG: Variable shadowing"""
        total = 0
        for total in numbers:  # BUG: shadows the total variable
            total += 1  # This doesn't accumulate correctly
        return total  # Returns last number + 1, not sum
    
    # Resource leak bug
    def read_config_file(self, filename: str) -> Dict:
        """BUG: Resource leak - file not properly closed"""
        f = open(filename, 'r')  # BUG: No try/except or with statement
        data = json.load(f)
        # BUG: File never closed if exception occurs
        f.close()
        return data

class BuggyStringProcessor:
    # Encoding/Unicode bug
    def save_text(self, text: str, filename: str) -> None:
        """BUG: Encoding issues"""
        with open(filename, 'w') as f:
            # BUG: No encoding specified, may fail with Unicode
            f.write(text)
    
    # String comparison bug
    def validate_password(self, password: str) -> bool:
        """BUG: Case-sensitive comparison"""
        forbidden = ["password", "admin", "123456"]
        # BUG: Case-sensitive check misses "Password", "ADMIN", etc.
        return password not in forbidden
    
    # Regular expression bug
    def extract_phone_numbers(self, text: str) -> List[str]:
        """BUG: Incorrect regex pattern"""
        import re
        # BUG: Regex doesn't handle various phone formats correctly
        pattern = r'\d{3}-\d{3}-\d{4}'  # Too restrictive
        return re.findall(pattern, text)
    
    # String formatting bug
    def format_currency(self, amount: float) -> str:
        """BUG: Incorrect string formatting"""
        # BUG: No handling of None or negative values
        return f"${amount:.2f}"  # Will crash if amount is None

class BuggyDateTimeHandler:
    # Timezone bug
    def get_current_timestamp(self) -> str:
        """BUG: No timezone handling"""
        # BUG: Uses local timezone, inconsistent across systems
        return datetime.datetime.now().isoformat()
    
    # Date calculation bug
    def add_business_days(self, start_date: datetime.date, days: int) -> datetime.date:
        """BUG: Incorrect business day calculation"""
        current = start_date
        added = 0
        while added < days:
            current += datetime.timedelta(days=1)
            # BUG: weekday() returns 0-6, not 1-7
            if current.weekday() < 5:  # Should be <= 4 for Mon-Fri
                added += 1
        return current
    
    # Leap year bug
    def is_leap_year(self, year: int) -> bool:
        """BUG: Incorrect leap year logic"""
        # BUG: Incomplete leap year calculation
        return year % 4 == 0  # Missing century year rules

class BuggyCollections:
    # Dictionary key error
    def get_user_info(self, users: Dict, user_id: int) -> str:
        """BUG: No key existence check"""
        # BUG: Will crash if user_id doesn't exist
        user = users[user_id]
        return f"{user['name']} - {user['email']}"
    
    # List modification during iteration
    def remove_even_numbers(self, numbers: List[int]) -> List[int]:
        """BUG: Modifying list during iteration"""
        for num in numbers:
            if num % 2 == 0:
                # BUG: Modifying list while iterating over it
                numbers.remove(num)
        return numbers
    
    # Set/List confusion
    def find_unique_items(self, items: List) -> List:
        """BUG: Incorrect data structure usage"""
        unique = []
        for item in items:
            # BUG: Inefficient O(n) lookup instead of using set
            if item not in unique:
                unique.append(item)
        return unique

class BuggyNetworkHandler:
    # Exception handling bug
    def fetch_data(self, url: str) -> Optional[Dict]:
        """BUG: Poor exception handling"""
        import requests
        try:
            response = requests.get(url)
            # BUG: No status code check
            return response.json()  # May fail if not JSON
        except:  # BUG: Bare except catches everything
            return None  # BUG: Loses error information
    
    # Timeout bug
    def download_file(self, url: str, filename: str) -> bool:
        """BUG: No timeout handling"""
        import requests
        # BUG: No timeout - may hang indefinitely
        response = requests.get(url)
        
        with open(filename, 'wb') as f:
            # BUG: Loading entire file into memory
            f.write(response.content)
        return True

# Global state bug
counter = 0

def increment_counter() -> int:
    """BUG: Global state modification"""
    global counter
    counter += 1
    # BUG: Not thread-safe
    return counter

# Memory leak simulation
class MemoryLeakExample:
    def __init__(self):
        self.callbacks = []
        self.data = []
    
    def add_callback(self, callback):
        """BUG: Circular reference potential"""
        self.callbacks.append(callback)
        # BUG: If callback references self, creates circular reference
    
    def process_large_data(self, data):
        """BUG: Accumulating data without cleanup"""
        # BUG: Never clears old data, memory usage grows
        self.data.append(data)
        return len(self.data)

# Example usage that will demonstrate bugs
def demonstrate_bugs():
    """Function to trigger various bugs for testing"""
    calc = BuggyCalculator()
    processor = BuggyDataProcessor()
    
    # These will cause various errors:
    try:
        result = calc.divide(10, 0)  # Division by zero
    except ZeroDivisionError:
        print("Caught division by zero")
    
    try:
        last_results = calc.get_last_n_results(5)  # Index error
    except IndexError:
        print("Caught index error")
    
    try:
        calc.add_to_memory("not a number")  # Type error
    except TypeError:
        print("Caught type error")
    
    try:
        countdown = processor.countdown(5)  # Infinite loop (commented out)
        # print(countdown)  # Don't actually run this!
    except KeyboardInterrupt:
        print("Stopped infinite loop")

if __name__ == "__main__":
    demonstrate_bugs()