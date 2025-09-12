# security_vulnerabilities.py
# This file contains various security vulnerabilities for testing

import os
import sqlite3
import subprocess
import pickle
import hashlib

class VulnerableWebApp:
    def __init__(self):
        self.db_connection = None
        
    # SQL Injection Vulnerability
    def get_user_by_id(self, user_id):
        """Vulnerable to SQL injection attacks"""
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        # VULNERABLE: Direct string interpolation
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor.execute(query)
        return cursor.fetchone()
    
    # Command Injection Vulnerability  
    def ping_host(self, hostname):
        """Vulnerable to command injection"""
        # VULNERABLE: Direct execution without sanitization
        result = subprocess.run(f"ping -c 1 {hostname}", shell=True, capture_output=True)
        return result.stdout.decode()
    
    # Path Traversal Vulnerability
    def read_file(self, filename):
        """Vulnerable to path traversal attacks"""
        # VULNERABLE: No path validation
        file_path = f"/var/www/uploads/{filename}"
        with open(file_path, 'r') as f:
            return f.read()
    
    # Insecure Deserialization
    def load_user_data(self, serialized_data):
        """Vulnerable to pickle deserialization attacks"""
        # VULNERABLE: Unpickling untrusted data
        return pickle.loads(serialized_data)
    
    # Weak Cryptography
    def hash_password(self, password):
        """Using weak hashing algorithm"""
        # VULNERABLE: MD5 is cryptographically broken
        return hashlib.md5(password.encode()).hexdigest()
    
    # Hard-coded Credentials
    def connect_to_database(self):
        """Contains hard-coded credentials"""
        # VULNERABLE: Hard-coded secrets
        DB_HOST = "localhost"
        DB_USER = "admin" 
        DB_PASSWORD = "admin123"  # Hard-coded password
        API_KEY = "sk-1234567890abcdef"  # Hard-coded API key
        
        connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/mydb"
        return connection_string
    
    # Insecure Random Number Generation
    def generate_session_token(self):
        """Using predictable random number generation"""
        import random
        # VULNERABLE: Using predictable random for security-critical operations
        token = ""
        for i in range(32):
            token += str(random.randint(0, 9))
        return token
    
    # Information Disclosure
    def handle_error(self, e):
        """Exposes sensitive information in error messages"""
        # VULNERABLE: Exposing stack traces and sensitive info
        error_msg = f"Database error: {str(e)}\nConnection string: postgresql://admin:admin123@localhost/mydb"
        print(error_msg)
        return error_msg
    
    # Insecure File Upload
    def upload_file(self, file_content, filename):
        """Allows dangerous file uploads"""
        # VULNERABLE: No file type validation
        upload_path = f"/var/www/uploads/{filename}"
        with open(upload_path, 'wb') as f:
            f.write(file_content)
        return upload_path
    
    # XML External Entity (XXE) Vulnerability
    def parse_xml(self, xml_data):
        """Vulnerable to XXE attacks"""
        import xml.etree.ElementTree as ET
        # VULNERABLE: XML parser allows external entities
        root = ET.fromstring(xml_data)
        return root
    
    # Insecure Direct Object Reference
    def get_user_profile(self, user_id, requesting_user_id):
        """Missing access control checks"""
        # VULNERABLE: No authorization check
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT profile FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()
    
# Example usage with vulnerabilities
if __name__ == "__main__":
    app = VulnerableWebApp()
    
    # These calls demonstrate the vulnerabilities
    user_data = app.get_user_by_id("1 OR 1=1")  # SQL injection
    ping_result = app.ping_host("google.com; rm -rf /")  # Command injection
    file_content = app.read_file("../../etc/passwd")  # Path traversal