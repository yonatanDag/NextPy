import string

# Exception for username containing illegal characters


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        char, index = self.get_illegal_char()
        return f'The username contains an illegal character "{char}" at index {index}'

    # function that ind and return the illegal character and its position
    def get_illegal_char(self):
        username_length = len(self._username)
        for i in range(username_length):
            current_char = self._username[i]
            if not (current_char.isalpha() or current_char.isdigit() or current_char == "_"):
                return current_char, i
        return "", -1


# Exception for username that is too short


class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "The username is too short"


# Exception for username that is too long


class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "The username is too long"


# Exception for password missing a required character


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password is missing a character"


# Exception for password missing an uppercase letter


class MissingUpperCase(PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def __str__(self):
        return super().__str__() + " (Uppercase)"


# Exception for password missing a lowercase letter


class MissingLowerCase(PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def __str__(self):
        return super().__str__() + " (Lowercase)"


# Exception for password missing a digit


class MissingDigit(PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def __str__(self):
        return super().__str__() + " (Digit)"


# Exception for password missing a special character


class MissingSpecial(PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def __str__(self):
        return super().__str__() + " (Special)"


# Exception for password that is too short


class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password is too short"


# Exception for password that is too long


class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    try:
        # check if the username contains illegal characters
        if any(not ((char.isalpha()) or (char.isdigit()) or (char == '_')) for char in username):
            raise UsernameContainsIllegalCharacter(username)

        # check if the username is too short
        if len(username) < 3:
            raise UsernameTooShort(username)

        # check if the username is too long
        if len(username) > 16:
            raise UsernameTooLong(username)

        # check if the password is too short
        if len(password) < 8:
            raise PasswordTooShort(password)

        # check if the password is too long
        if len(password) > 40:
            raise PasswordTooLong(password)

        # check if the password is missing a lowercase letter
        if not any(char.islower() for char in password):
            raise MissingLowerCase(password)

        # check if the password is missing an uppercase letter
        if not any(char.isupper() for char in password):
            raise MissingUpperCase(password)

        # check if the password is missing a digit
        if not any(char.isdigit() for char in password):
            raise MissingDigit(password)

        # check if the password is missing a special character
        if not any(char in string.punctuation for char in password):
            raise MissingSpecial(password)

        # in case that all checks pass
        else:
            print("OK")
            return True

    except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong, MissingLowerCase,
            MissingUpperCase, MissingDigit, MissingSpecial, PasswordTooShort,PasswordTooLong) as e:
        # print the error message in case of an exception
        print(e)
        return False


def main():
    # get username and password from the user and check them until they are valid
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    while not check_input(username, password):
        username = input("Please enter again your username: ")
        password = input("Please enter again your password: ")


if __name__ == "__main__":
    main()
