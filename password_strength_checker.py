import re

def password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~""]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    error_count = sum(errors)

    if error_count == 0:
        return "Strong"
    elif error_count == 1:
        return "Moderate"
    else:
        return "Weak"

# Example usage:
password = input("Enter your password: ")
strength = password_strength(password)
print("Password strength:", strength)