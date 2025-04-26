
class InvalidAgeError(Exception):
    def __init__(self, message="You  Are Under 18 Sorry....Not Eligible"):
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise InvalidAgeError("You are not eligible to vote.")
    else:
        return "You are eligible to vote."


try:
    user_input = int(input("Enter your age: "))
    result = check_age(user_input)
    print(result)

except InvalidAgeError as e:
    print("Custom Exception Caught:", e)

except ValueError as ve:
    print("Value Error:", ve)
