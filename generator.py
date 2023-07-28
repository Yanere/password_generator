import random
import string
import sys

letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation
all_characters = letters + numbers + special_characters


class PasswordGenerationError(Exception):
    pass


def password_generator(length):
    """
    Generate a random password that contains at least 1 number and 1 special character.

    :param length: The length of the password to be generated.
    :type length: int

    :return: The generated password.
    :rtype: str
    """
    max_attempts = 1000  # Maximum number of attempts to generate a password meeting constraints
    attempts = 0

    while attempts < max_attempts:
        generated_pw = "".join(random.SystemRandom().choice(all_characters) for _ in range(length))

        if (any(char in special_characters for char in generated_pw) and
                any(char in numbers for char in generated_pw)):
            return generated_pw

        attempts += 1

    raise PasswordGenerationError("Could not generate a password meeting constraints after maximum attempts.")


if __name__ == "__main__":
    try:
        password_length = int(sys.argv[1])
        generated_password = password_generator(password_length)
        print(generated_password)

    except (ValueError, IndexError):
        print("Length missing - type the command like this: <python generator.py 16>")

    except PasswordGenerationError as e:
        print(e)