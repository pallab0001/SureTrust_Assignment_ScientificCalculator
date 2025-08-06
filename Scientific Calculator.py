"""
Menu Driven Scientific Calculator (No math module)
This calculator performs basic and advanced mathematical operations.
All calculations are implemented manually without external libraries.
"""

PI = 3.1415926535
E = 2.7182818284


class MathError(Exception):
    pass

# ARITHMETIC OPERATIONS 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise MathError("Division by zero is not allowed")
    return a / b

def modulus(a, b):
    if b == 0:
        raise MathError("Modulus by zero is not allowed")
    return a % b

#  NUMBER THEORY 
def find_gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while (a % b) != 0:
        (a, b) = (b, a % b)
    return abs(b)

def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    elif a < b:
        (a, b) = (b, a)
    return abs(a * b) // find_gcd(a, b)

# ADVANCED MATH 
def power(base, exponent):
    int_exponent = int(exponent)
    result = 1
    for _ in range(abs(int_exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result

def square_root(number):
    if number < 0:
        raise MathError("Square root of negative numbers is not real")
    
    guess = number / 2
    tolerance = 1e-10
    while True:
        better_guess = (guess + number/guess) / 2
        if abs(better_guess - guess) < tolerance:
            return better_guess
        guess = better_guess

def factorial(n):
    if n < 0:
        raise MathError("Factorial not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# TRIGONOMETRY
def degrees_to_radians(degrees):
    return degrees * (PI / 180)

def radians_to_degrees(radians):
    return radians * (180 / PI)

def sine(angle, use_degrees=False, terms=15):
    x = degrees_to_radians(angle) if use_degrees else angle
    
    result = 0.0
    sign = 1
    
    for n in range(terms):
        exponent = 2 * n + 1
        term = sign * (x ** exponent) / factorial(exponent)
        result += term
        sign *= -1
    return result

def cosine(angle, use_degrees=False, terms=15):
    x = degrees_to_radians(angle) if use_degrees else angle 
    result = 1.0
    sign = -1
    
    for n in range(1, terms):
        exponent = 2 * n
        term = sign * (x ** exponent) / factorial(exponent)
        result += term
        sign *= -1
    return result

def tangent(angle, use_degrees=False, terms=15):
    cos_val = cosine(angle, use_degrees, terms)
    if abs(cos_val) < 1e-10:
        raise MathError("Tangent undefined (cosine is zero)")
    return sine(angle, use_degrees, terms) / cos_val

# BASE CONVERSION
""" 
Converts numbers between binary, octal, decimal and hexadecimal Base options: 
1 = Binary, 2 = Octal, 3 = Decimal, 4 = Hexadecimal
"""
def convert_base(number_str, from_base, to_base):
    base_map = {
        1: 2,  # Binary
        2: 8,  # Octal
        3: 10, # Decimal
        4: 16  # Hexadecimal
    }

    try:
       
        decimal_value = int(number_str, base_map[from_base])
    except ValueError:
        raise MathError("Invalid number for selected base")
    
    if to_base == 1:
        return bin(decimal_value)
    elif to_base == 2:
        return oct(decimal_value)
    elif to_base == 3:
        return str(decimal_value)
    elif to_base == 4:
        return hex(decimal_value)
    else:
        raise MathError("Invalid base selection")

# USER INTERFACE
def display_menu():
    print("\n" + "=" * 40)
    print("SCIENTIFIC CALCULATOR")
    print("=" * 40)
    print("Basic Operations:")
    print("  1. Add\t  2. Subtract\t  3. Multiply\t  4. Divide")
    print("  5. Modulus\t  6. Power\t  7. Square Root  8. Factorial")
    
    print("\nAdvanced Functions:")
    print("  9. Sine\t 10. Cosine\t 11. Tangent")
    print(" 12. Degrees→Radians\t 13. Radians→Degrees")
    
    print("\nNumber Systems:")
    print(" 14. Base Conversion")
    
    print("\nNumber Theory:")
    print(" 15. GCD\t 16. LCM")
    
    print("\n 0. Exit")
    print("=" * 40)

def get_float_input(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_int_input(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")

def main():
    
    while True:
        display_menu()
        try:
            choice = get_int_input("Enter your choice (0-16): ")
            
            if choice == 0:
                print("\nThank you for using the calculator. Goodbye!")
                break
                 
            elif 1 <= choice <= 6:
                num1 = get_float_input("Enter first number: ")
                num2 = get_float_input("Enter second number: ")
                
                if choice == 1:
                    result = add(num1, num2)
                elif choice == 2:
                    result = subtract(num1, num2)
                elif choice == 3:
                    result = multiply(num1, num2)
                elif choice == 4:
                    result = divide(num1, num2)
                elif choice == 5:
                    result = modulus(num1, num2)
                elif choice == 6:
                    result = power(num1, num2)
                    
                print(f"Result: {result}")
                
            elif choice == 7: 
                num = get_float_input("Enter number: ")
                print(f"Square root: {square_root(num)}")
                
            elif choice == 8:  
                num = get_int_input("Enter non-negative integer: ")
                print(f"Factorial: {factorial(num)}")
                
            elif 9 <= choice <= 11:
                angle = get_float_input("Enter angle: ")
                unit = input("Use degrees? (y/n): ").lower() == 'y'
                
                if choice == 9:
                    result = sine(angle, unit)
                    func_name = "Sine"
                elif choice == 10:
                    result = cosine(angle, unit)
                    func_name = "Cosine"
                elif choice == 11:
                    result = tangent(angle, unit)
                    func_name = "Tangent"
                    
                print(f"{func_name}: {result:.6f}")
            
            elif choice == 12:  
                deg = get_float_input("Enter degrees: ")
                print(f"Radians: {degrees_to_radians(deg):.6f}")
            elif choice == 13:
                rad = get_float_input("Enter radians: ")
                print(f"Degrees: {radians_to_degrees(rad):.6f}")
                
            elif choice == 14:
                print("\nNumber Base Options:")
                print("1. Binary  2. Octal  3. Decimal  4. Hexadecimal")
                from_base = get_int_input("Convert FROM base (1-4): ")
                to_base = get_int_input("Convert TO base (1-4): ")
                number_str = input("Enter number: ").strip()
                print(f"Converted: {convert_base(number_str, from_base, to_base)}")
                
            elif choice == 15: 
                num1 = get_int_input("Enter first integer: ")
                num2 = get_int_input("Enter second integer: ")
                print(f"GCD: {find_gcd(num1, num2)}")
            elif choice == 16: 
                num1 = get_int_input("Enter first integer: ")
                num2 = get_int_input("Enter second integer: ")
                print(f"LCM: {find_lcm(num1, num2)}")
                
            else:
                print("Invalid choice! Please select 0-16.")
                
        except MathError as me:
            print(f"Math Error: {me}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()