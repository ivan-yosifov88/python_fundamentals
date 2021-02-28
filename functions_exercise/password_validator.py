def pass_validator(password):
    is_password_valid = True
    counter_digits = 0
    for digits in password:
        if digits.isnumeric():
            counter_digits += 1
    if not 6 <= len(password) <= 10:
        is_password_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        is_password_valid = False
        print("Password must consist only of letters and digits")
    if counter_digits < 2:
        is_password_valid = False
        print("Password must have at least 2 digits")
    if is_password_valid:
        print("Password is valid")


password_for_validation = input()

pass_validator(password_for_validation)


