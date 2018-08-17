"""Zac Bramham"""
MIN_LENGTH = 2
MAX_LENGTH = 10
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain: ")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    for i, char in enumerate(password):
        #Really sloppy coding, trying to find the correct way to make it work.
        print(end=' ')
    print("Your {}-character password is valid: {}".format(len(password), i * '*' + '*'))


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in SPECIAL_CHARS:
            count_special += 1
    if count_upper == 0 or count_lower == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False

    return True


main()
