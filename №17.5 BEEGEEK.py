def is_password_good(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_number = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_number = True

    return has_upper and has_lower and has_number

def is_valid_password(password):
    parts = password.split(':')

    if len(parts) != 3:
        return False

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
asd
