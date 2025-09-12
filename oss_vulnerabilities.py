# oss_vulnerabilities.py
# This file contains code using vulnerable OSS dependencies

# Outdated and vulnerable dependencies
import requests  # Using old version with known CVEs
import flask     # Using old version with security issues
import pyyaml    # Using version vulnerable to code execution
import jinja2    # Using version with XSS vulnerabilities
import urllib3   # Using version with SSL verification issues

# Deprecated and insecure libraries
import cgi       # Deprecated module
import imp       # Deprecated and unsafe import mechanism
import pickle    # Potentially unsafe for untrusted data

class VulnerableOSSUsage:
    def __init__(self):
        self.app = flask.Flask(__name__)
        
    # Using vulnerable YAML loading
    def load_config(self, config_file):
        """Using unsafe YAML loading - CVE-2017-18342"""
        with open(config_file, 'r') as f:
            # VULNERABLE: yaml.load() without safe loading
            config = pyyaml.load(f)  # Should use yaml.safe_load()
        return config
    
    # Using requests without SSL verification
    def fetch_data(self, url):
        """Disabling SSL verification - security risk"""
        # VULNERABLE: SSL verification disabled
        response = requests.get(url, verify=False)
        return response.json()
    
    # Using Flask with debug mode in production
    def run_app(self):
        """Running Flask in debug mode - security risk"""
        # VULNERABLE: Debug mode exposes sensitive information
        self.app.run(debug=True, host='0.0.0.0')
    
    # Using deprecated cgi module
    def parse_form_data(self, form_data):
        """Using deprecated cgi module"""
        # VULNERABLE: cgi module is deprecated and has security issues
        form = cgi.FieldStorage()
        return form
    
    # Using unsafe pickle loading
    def deserialize_data(self, data):
        """Using pickle with untrusted data"""
        # VULNERABLE: pickle.loads() with untrusted data
        return pickle.loads(data)
    
    # Using urllib3 without proper SSL context
    def make_request(self, url):
        """Using urllib3 with insecure settings"""
        import urllib3
        # VULNERABLE: Disabling SSL warnings and verification
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        http = urllib3.PoolManager(cert_reqs='CERT_NONE')
        response = http.request('GET', url)
        return response.data
    
    # Using Jinja2 with autoescape disabled
    def render_template(self, template_string, data):
        """Using Jinja2 without auto-escaping"""
        from jinja2 import Template
        # VULNERABLE: Auto-escape disabled, prone to XSS
        template = Template(template_string, autoescape=False)
        return template.render(data)
    
    # Using vulnerable XML parsing
    def parse_xml_unsafe(self, xml_string):
        """Using vulnerable XML parsing"""
        import xml.etree.ElementTree as ET
        # VULNERABLE: No protection against XML bombs/XXE
        return ET.fromstring(xml_string)
    
    # Using subprocess without proper sanitization
    def execute_command(self, command):
        """Using subprocess unsafely"""
        import subprocess
        # VULNERABLE: Shell injection possible
        return subprocess.run(command, shell=True, capture_output=True)
    
    # Using eval() with user input
    def calculate_expression(self, expression):
        """Using eval() with user input"""
        # VULNERABLE: Code injection through eval()
        return eval(expression)
    
    # Using exec() with user input  
    def execute_code(self, code):
        """Using exec() with user input"""
        # VULNERABLE: Arbitrary code execution
        exec(code)
    
    # Using assert for security checks
    def validate_user(self, user_role):
        """Using assert for security validation"""
        # VULNERABLE: assert statements can be disabled
        assert user_role == 'admin', "Access denied"
        return True
    
    # Using weak random for security purposes
    def generate_token(self):
        """Using weak random number generation"""
        import random
        # VULNERABLE: Not cryptographically secure
        return str(random.randint(100000, 999999))
    
# Example requirements.txt content that would have vulnerabilities:
VULNERABLE_REQUIREMENTS = """
# These versions have known security vulnerabilities
requests==2.20.0         # CVE-2018-18074
flask==0.12.2            # CVE-2018-1000656  
PyYAML==3.12             # CVE-2017-18342
Jinja2==2.8.1            # CVE-2016-10745
urllib3==1.24.1          # CVE-2019-11324
django==2.0.1            # CVE-2018-6188
pillow==5.0.0            # CVE-2018-16509
lxml==4.2.0              # CVE-2018-19787
cryptography==2.1.4     # CVE-2018-10903
paramiko==2.0.0          # CVE-2018-7750
"""

# Example of using vulnerable dependency patterns
def vulnerable_dependency_usage():
    """Examples of vulnerable OSS usage patterns"""
    
    # Using old requests version with SSL issues
    import requests
    response = requests.get("https://api.example.com", verify=False)
    
    # Using old PyYAML with unsafe loading
    import yaml
    with open("config.yaml") as f:
        config = yaml.load(f)  # Should use yaml.safe_load()
    
    # Using deprecated imp module
    import imp
    module = imp.load_source('mymodule', '/path/to/module.py')
    
    return "Vulnerable patterns demonstrated"

if __name__ == "__main__":
    app = VulnerableOSSUsage()
    
    # Test vulnerable functionality
    config = app.load_config("config.yaml")
    data = app.fetch_data("https://api.example.com/data")
    result = app.calculate_expression("__import__('os').system('ls')")