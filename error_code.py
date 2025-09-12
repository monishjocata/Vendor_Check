# error_code.py
# Comprehensive collection of all Python errors and exceptions for testing

import sys
import os
import math
import json
import socket
import threading
import subprocess
from typing import List, Dict

class PythonErrorDemonstrator:
    """Class to demonstrate all types of Python errors and exceptions."""
    
    def __init__(self):
        self.data = []
        self.file_handle = None
    
    # ==================== SYNTAX ERRORS ====================
    # These would prevent the script from running at all
    
    def demonstrate_syntax_errors(self):
        """Examples of syntax errors (commented out as they prevent execution)"""
        # SyntaxError examples:
        # if True  # Missing colon
        # print("Hello"  # Missing closing parenthesis
        # def function(  # Incomplete function definition
        # x = 1 = 2  # Invalid assignment
        # return  # Return outside function
        # break   # Break outside loop
        # continue  # Continue outside loop
        pass
    
    # ==================== RUNTIME EXCEPTIONS ====================
    
    def demonstrate_arithmetic_errors(self):
        """ArithmeticError and its subclasses"""
        errors = []
        
        try:
            # ZeroDivisionError
            result = 10 / 0
        except ZeroDivisionError as e:
            errors.append(f"ZeroDivisionError: {e}")
        
        try:
            # OverflowError
            result = math.exp(1000)  # Too large for float
        except OverflowError as e:
            errors.append(f"OverflowError: {e}")
        
        try:
            # FloatingPointError (rare, usually disabled)
            import numpy as np
            np.seterr(all='raise')
            result = np.float64(1) / np.float64(0)
        except:
            errors.append("FloatingPointError: Division by zero in numpy")
        
        return errors
    
    def demonstrate_lookup_errors(self):
        """LookupError and its subclasses"""
        errors = []
        
        try:
            # IndexError
            my_list = [1, 2, 3]
            value = my_list[10]
        except IndexError as e:
            errors.append(f"IndexError: {e}")
        
        try:
            # KeyError
            my_dict = {"a": 1, "b": 2}
            value = my_dict["z"]
        except KeyError as e:
            errors.append(f"KeyError: {e}")
        
        return errors
    
    def demonstrate_name_errors(self):
        """NameError and UnboundLocalError"""
        errors = []
        
        try:
            # NameError
            print(undefined_variable)
        except NameError as e:
            errors.append(f"NameError: {e}")
        
        try:
            # UnboundLocalError
            def problematic_function():
                print(local_var)  # Referenced before assignment
                local_var = "value"
            problematic_function()
        except UnboundLocalError as e:
            errors.append(f"UnboundLocalError: {e}")
        
        return errors
    
    def demonstrate_type_errors(self):
        """TypeError examples"""
        errors = []
        
        try:
            # TypeError - wrong number of arguments
            len()  # len() takes exactly 1 argument
        except TypeError as e:
            errors.append(f"TypeError (arguments): {e}")
        
        try:
            # TypeError - unsupported operand types
            result = "string" + 5
        except TypeError as e:
            errors.append(f"TypeError (operands): {e}")
        
        try:
            # TypeError - object not callable
            my_int = 5
            result = my_int()
        except TypeError as e:
            errors.append(f"TypeError (not callable): {e}")
        
        try:
            # TypeError - unhashable type
            my_dict = {[1, 2]: "value"}  # List is not hashable
        except TypeError as e:
            errors.append(f"TypeError (unhashable): {e}")
        
        return errors
    
    def demonstrate_value_errors(self):
        """ValueError examples"""
        errors = []
        
        try:
            # ValueError - invalid literal for int()
            number = int("not_a_number")
        except ValueError as e:
            errors.append(f"ValueError (int conversion): {e}")
        
        try:
            # ValueError - math domain error
            result = math.sqrt(-1)
        except ValueError as e:
            errors.append(f"ValueError (math domain): {e}")
        
        try:
            # ValueError - invalid base for int()
            number = int("123", base=37)  # Base must be 2-36
        except ValueError as e:
            errors.append(f"ValueError (invalid base): {e}")
        
        try:
            # ValueError - list.index() not found
            my_list = [1, 2, 3]
            index = my_list.index(5)
        except ValueError as e:
            errors.append(f"ValueError (not in list): {e}")
        
        return errors
    
    def demonstrate_attribute_errors(self):
        """AttributeError examples"""
        errors = []
        
        try:
            # AttributeError - object has no attribute
            my_string = "hello"
            my_string.non_existent_method()
        except AttributeError as e:
            errors.append(f"AttributeError: {e}")
        
        try:
            # AttributeError - module has no attribute
            import math
            result = math.non_existent_function()
        except AttributeError as e:
            errors.append(f"AttributeError (module): {e}")
        
        return errors
    
    def demonstrate_import_errors(self):
        """ImportError and ModuleNotFoundError"""
        errors = []
        
        try:
            # ModuleNotFoundError
            import non_existent_module
        except ModuleNotFoundError as e:
            errors.append(f"ModuleNotFoundError: {e}")
        
        try:
            # ImportError - cannot import name
            from math import non_existent_function
        except ImportError as e:
            errors.append(f"ImportError: {e}")
        
        return errors
    
    def demonstrate_os_errors(self):
        """OSError and its subclasses"""
        errors = []
        
        try:
            # FileNotFoundError
            with open("non_existent_file.txt", "r") as f:
                content = f.read()
        except FileNotFoundError as e:
            errors.append(f"FileNotFoundError: {e}")
        
        try:
            # PermissionError
            with open("/root/protected_file.txt", "w") as f:
                f.write("test")
        except PermissionError as e:
            errors.append(f"PermissionError: {e}")
        
        try:
            # IsADirectoryError
            with open("/", "r") as f:
                content = f.read()
        except IsADirectoryError as e:
            errors.append(f"IsADirectoryError: {e}")
        
        try:
            # NotADirectoryError
            os.listdir("non_existent_file.txt")
        except (NotADirectoryError, FileNotFoundError) as e:
            errors.append(f"NotADirectoryError/FileNotFoundError: {e}")
        
        try:
            # FileExistsError
            os.mkdir("/")  # Directory already exists
        except FileExistsError as e:
            errors.append(f"FileExistsError: {e}")
        
        return errors
    
    def demonstrate_runtime_errors(self):
        """RuntimeError and RecursionError"""
        errors = []
        
        try:
            # RecursionError
            def infinite_recursion():
                return infinite_recursion()
            infinite_recursion()
        except RecursionError as e:
            errors.append(f"RecursionError: {e}")
        
        try:
            # RuntimeError - general runtime error
            raise RuntimeError("Custom runtime error")
        except RuntimeError as e:
            errors.append(f"RuntimeError: {e}")
        
        return errors
    
    def demonstrate_system_errors(self):
        """SystemError and SystemExit"""
        errors = []
        
        try:
            # SystemExit
            sys.exit(1)
        except SystemExit as e:
            errors.append(f"SystemExit: {e}")
        
        # SystemError is rare and usually indicates internal Python error
        # Cannot easily demonstrate without corrupting Python state
        
        return errors
    
    def demonstrate_memory_errors(self):
        """MemoryError"""
        errors = []
        
        try:
            # MemoryError - trying to allocate too much memory
            huge_list = [0] * (10**10)  # May cause MemoryError
        except MemoryError as e:
            errors.append(f"MemoryError: {e}")
        
        return errors
    
    def demonstrate_unicode_errors(self):
        """UnicodeError and its subclasses"""
        errors = []
        
        try:
            # UnicodeDecodeError
            byte_string = b'\xff\xfe'
            decoded = byte_string.decode('utf-8')
        except UnicodeDecodeError as e:
            errors.append(f"UnicodeDecodeError: {e}")
        
        try:
            # UnicodeEncodeError
            text = "café"
            encoded = text.encode('ascii')
        except UnicodeEncodeError as e:
            errors.append(f"UnicodeEncodeError: {e}")
        
        return errors
    
    def demonstrate_assertion_errors(self):
        """AssertionError"""
        errors = []
        
        try:
            # AssertionError
            assert 1 == 2, "One does not equal two"
        except AssertionError as e:
            errors.append(f"AssertionError: {e}")
        
        return errors
    
    def demonstrate_stop_iteration(self):
        """StopIteration and StopAsyncIteration"""
        errors = []
        
        try:
            # StopIteration
            iterator = iter([1, 2, 3])
            next(iterator)  # 1
            next(iterator)  # 2
            next(iterator)  # 3
            next(iterator)  # StopIteration
        except StopIteration as e:
            errors.append(f"StopIteration: {e}")
        
        return errors
    
    def demonstrate_generator_errors(self):
        """GeneratorExit"""
        errors = []
        
        def my_generator():
            try:
                yield 1
                yield 2
            except GeneratorExit:
                errors.append("GeneratorExit: Generator was closed")
                raise
        
        gen = my_generator()
        next(gen)
        gen.close()  # Triggers GeneratorExit
        
        return errors
    
    def demonstrate_keyboard_interrupt(self):
        """KeyboardInterrupt (Ctrl+C)"""
        errors = []
        
        try:
            # Simulate KeyboardInterrupt
            raise KeyboardInterrupt("Simulated Ctrl+C")
        except KeyboardInterrupt as e:
            errors.append(f"KeyboardInterrupt: {e}")
        
        return errors
    
    def demonstrate_connection_errors(self):
        """Network-related errors"""
        errors = []
        
        try:
            # ConnectionError
            import requests
            response = requests.get("http://nonexistent-domain-12345.com", timeout=1)
        except Exception as e:
            errors.append(f"ConnectionError: {e}")
        
        try:
            # socket errors
            sock = socket.socket()
            sock.connect(("192.0.2.0", 1))  # Non-routable address
        except socket.error as e:
            errors.append(f"Socket Error: {e}")
        
        return errors
    
    def demonstrate_json_errors(self):
        """JSON-related errors"""
        errors = []
        
        try:
            # JSONDecodeError
            invalid_json = '{"key": value}'  # Missing quotes around value
            data = json.loads(invalid_json)
        except json.JSONDecodeError as e:
            errors.append(f"JSONDecodeError: {e}")
        
        return errors
    
    def demonstrate_subprocess_errors(self):
        """Subprocess-related errors"""
        errors = []
        
        try:
            # CalledProcessError
            result = subprocess.run(["false"], check=True)
        except subprocess.CalledProcessError as e:
            errors.append(f"CalledProcessError: {e}")
        
        try:
            # TimeoutExpired
            result = subprocess.run(["sleep", "10"], timeout=1)
        except subprocess.TimeoutExpired as e:
            errors.append(f"TimeoutExpired: {e}")
        except FileNotFoundError as e:
            errors.append(f"FileNotFoundError (subprocess): {e}")
        
        return errors
    
    def demonstrate_threading_errors(self):
        """Threading-related errors"""
        errors = []
        
        try:
            # RuntimeError in threading
            lock = threading.Lock()
            lock.release()  # Release without acquiring
        except RuntimeError as e:
            errors.append(f"Threading RuntimeError: {e}")
        
        return errors
    
    def demonstrate_custom_exceptions(self):
        """Custom exception examples"""
        errors = []
        
        class CustomError(Exception):
            """Custom exception class"""
            pass
        
        try:
            raise CustomError("This is a custom exception")
        except CustomError as e:
            errors.append(f"CustomError: {e}")
        
        return errors
    
    def demonstrate_context_manager_errors(self):
        """Context manager related errors"""
        errors = []
        
        class BadContextManager:
            def __enter__(self):
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                raise RuntimeError("Error in context manager exit")
        
        try:
            with BadContextManager():
                pass
        except RuntimeError as e:
            errors.append(f"Context Manager Error: {e}")
        
        return errors
    
    def demonstrate_buffer_errors(self):
        """Buffer-related errors"""
        errors = []
        
        try:
            # BufferError
            data = bytearray(b'hello')
            mem_view = memoryview(data)
            data.clear()  # This might cause BufferError in some contexts
        except BufferError as e:
            errors.append(f"BufferError: {e}")
        except Exception as e:
            errors.append(f"Buffer-related error: {e}")
        
        return errors
    
    def demonstrate_indentation_errors(self):
        """IndentationError examples (would prevent script execution)"""
        # These would cause IndentationError:
        # def bad_function():
        # print("No indentation")
        #
        #   print("Wrong indentation")
        #     print("Inconsistent indentation")
        pass
    
    def demonstrate_tab_errors(self):
        """TabError examples (would prevent script execution)"""
        # These would cause TabError:
        # def mixed_function():
        #     print("Using spaces")
        # 	print("Using tab")  # Mixed tabs and spaces
        pass
    
    def run_all_demonstrations(self):
        """Run all error demonstrations and return results"""
        all_errors = []
        
        demonstrations = [
            ("Arithmetic Errors", self.demonstrate_arithmetic_errors),
            ("Lookup Errors", self.demonstrate_lookup_errors),
            ("Name Errors", self.demonstrate_name_errors),
            ("Type Errors", self.demonstrate_type_errors),
            ("Value Errors", self.demonstrate_value_errors),
            ("Attribute Errors", self.demonstrate_attribute_errors),
            ("Import Errors", self.demonstrate_import_errors),
            ("OS Errors", self.demonstrate_os_errors),
            ("Runtime Errors", self.demonstrate_runtime_errors),
            ("System Errors", self.demonstrate_system_errors),
            ("Memory Errors", self.demonstrate_memory_errors),
            ("Unicode Errors", self.demonstrate_unicode_errors),
            ("Assertion Errors", self.demonstrate_assertion_errors),
            ("Stop Iteration", self.demonstrate_stop_iteration),
            ("Generator Errors", self.demonstrate_generator_errors),
            ("Keyboard Interrupt", self.demonstrate_keyboard_interrupt),
            ("Connection Errors", self.demonstrate_connection_errors),
            ("JSON Errors", self.demonstrate_json_errors),
            ("Subprocess Errors", self.demonstrate_subprocess_errors),
            ("Threading Errors", self.demonstrate_threading_errors),
            ("Custom Exceptions", self.demonstrate_custom_exceptions),
            ("Context Manager Errors", self.demonstrate_context_manager_errors),
            ("Buffer Errors", self.demonstrate_buffer_errors),
        ]
        
        for category, demo_func in demonstrations:
            try:
                errors = demo_func()
                all_errors.extend([(category, error) for error in errors])
            except Exception as e:
                all_errors.append((category, f"Unexpected error: {e}"))
        
        return all_errors

# Example usage
if __name__ == "__main__":
    demonstrator = PythonErrorDemonstrator()
    all_errors = demonstrator.run_all_demonstrations()
    
    print("Python Error Demonstrations:")
    print("=" * 50)
    
    for category, error in all_errors:
        print(f"\n[{category}]")
        print(f"  {error}")
    
    print(f"\nTotal errors demonstrated: {len(all_errors)}")

