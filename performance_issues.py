# performance_issues.py
# This file contains various performance issues that need optimization

import time
import re
import requests
from typing import List, Dict

class PerformanceIssues:
    def __init__(self):
        self.data = []
        self.cache = {}
    
    # Inefficient loops and data structures
    def find_duplicates_slow(self, numbers: List[int]) -> List[int]:
        """Inefficient O(n²) approach to find duplicates"""
        duplicates = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
        return duplicates
    
    # String concatenation in loop (inefficient)
    def build_large_string_slow(self, items: List[str]) -> str:
        """Inefficient string concatenation"""
        result = ""
        for item in items:
            result += item + ", "  # Creates new string object each time
        return result[:-2]
    
    # Inefficient list operations
    def process_large_list_slow(self, data: List[int]) -> List[int]:
        """Multiple passes through large list"""
        # Multiple separate loops instead of single pass
        evens = []
        for item in data:
            if item % 2 == 0:
                evens.append(item)
        
        squared = []
        for item in evens:
            squared.append(item ** 2)
        
        filtered = []
        for item in squared:
            if item > 100:
                filtered.append(item)
        
        return filtered
    
    # Regex compilation in loop
    def validate_emails_slow(self, emails: List[str]) -> List[bool]:
        """Compiling regex pattern repeatedly"""
        results = []
        for email in emails:
            # BAD: Compiling regex in every iteration
            pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            results.append(bool(pattern.match(email)))
        return results
    
    # Inefficient dictionary lookups
    def count_frequencies_slow(self, words: List[str]) -> Dict[str, int]:
        """Inefficient frequency counting"""
        frequencies = {}
        for word in words:
            # BAD: Multiple dictionary lookups
            if word in frequencies:
                frequencies[word] = frequencies[word] + 1
            else:
                frequencies[word] = 1
        return frequencies
    
    # No caching for expensive operations
    def fibonacci_recursive_slow(self, n: int) -> int:
        """Inefficient recursive fibonacci without memoization"""
        if n <= 1:
            return n
        return self.fibonacci_recursive_slow(n-1) + self.fibonacci_recursive_slow(n-2)
    
    # Inefficient file I/O
    def read_large_file_slow(self, filename: str) -> List[str]:
        """Reading entire large file into memory"""
        with open(filename, 'r') as f:
            # BAD: Loading entire file into memory at once
            all_lines = f.readlines()
        
        processed = []
        for line in all_lines:
            if len(line.strip()) > 0:
                processed.append(line.strip().upper())
        return processed
    
    # Inefficient database-like operations
    def filter_users_slow(self, users: List[Dict], criteria: Dict) -> List[Dict]:
        """Inefficient filtering without indexing"""
        results = []
        for user in users:
            matches = True
            for key, value in criteria.items():
                if user.get(key) != value:
                    matches = False
                    break
            if matches:
                results.append(user)
        return results
    
    # Memory-inefficient operations
    def process_numbers_memory_heavy(self, numbers: List[int]) -> List[int]:
        """Creating unnecessary intermediate lists"""
        # BAD: Creating multiple large intermediate lists
        doubled = [x * 2 for x in numbers]
        squared = [x ** 2 for x in doubled]
        filtered = [x for x in squared if x > 1000]
        sorted_result = sorted(filtered, reverse=True)
        return sorted_result
    
    # Inefficient sorting
    def sort_custom_slow(self, items: List[Dict]) -> List[Dict]:
        """Inefficient custom sorting"""
        # BAD: Bubble sort implementation O(n²)
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j]['score'] < items[j + 1]['score']:
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items
    
    # Network calls without connection pooling
    def fetch_multiple_urls_slow(self, urls: List[str]) -> List[str]:
        """Making individual requests without connection pooling"""
        results = []
        for url in urls:
            # BAD: New connection for each request
            response = requests.get(url)
            results.append(response.text)
        return results
    
    # Inefficient data structure choice
    def frequent_insertions_slow(self, items: List[int]) -> List[int]:
        """Using list for frequent insertions at beginning"""
        result = []
        for item in items:
            # BAD: Inserting at beginning of list is O(n)
            result.insert(0, item)
        return result
    
    # Inefficient exception handling
    def convert_strings_slow(self, strings: List[str]) -> List[int]:
        """Using exceptions for control flow"""
        results = []
        for s in strings:
            try:
                # BAD: Using exceptions for expected cases
                results.append(int(s))
            except ValueError:
                results.append(0)
        return results
    
    # Inefficient global variable access
    global_counter = 0
    
    def increment_global_slow(self, times: int):
        """Inefficient global variable access"""
        global global_counter
        for i in range(times):
            # BAD: Global access in tight loop
            global_counter += 1
    
    # Inefficient class attribute access
    def calculate_totals_slow(self, amounts: List[float]) -> float:
        """Inefficient repeated attribute access"""
        total = 0
        for amount in amounts:
            # BAD: Accessing self.data repeatedly in loop
            if len(self.data) > 100:
                total += amount * 1.1
            else:
                total += amount
        return total
    
    # No lazy evaluation
    def find_first_match_slow(self, items: List[str], pattern: str) -> str:
        """Processing all items instead of stopping at first match"""
        matches = []
        # BAD: Processing entire list even after finding matches
        for item in items:
            if pattern in item:
                matches.append(item)
        
        return matches[0] if matches else None

# Example usage demonstrating performance issues
def demonstrate_performance_issues():
    """Function to test all performance issues"""
    perf = PerformanceIssues()
    
    # Large dataset for testing
    large_numbers = list(range(10000))
    emails = ['user@example.com'] * 1000
    
    # Test inefficient operations
    start_time = time.time()
    
    # This will be slow
    duplicates = perf.find_duplicates_slow(large_numbers[:100])
    
    # This will be memory inefficient  
    large_string = perf.build_large_string_slow(['item'] * 10000)
    
    # This will make multiple passes
    processed = perf.process_large_list_slow(large_numbers)
    
    # This will compile regex repeatedly
    email_results = perf.validate_emails_slow(emails)
    
    # This will be extremely slow for large n
    fib_result = perf.fibonacci_recursive_slow(30)
    
    end_time = time.time()
    print(f"All operations took: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    demonstrate_performance_issues()