def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def is_valid_password(password):
    parts = password.split(':')

    if len(parts) != 3:
        return False

    a, b, c = parts

    if a != a[::-1]:
        return False

    if not is_prime(int(b)):
        return False

    if int(c) % 2 != 0:
        return False

    return True

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
