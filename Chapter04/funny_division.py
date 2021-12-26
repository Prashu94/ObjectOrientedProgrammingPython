def funny_division(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        return "Zero is not a good idea"

# This will raise an exception but will be caught in ZeroDivisionError
# and return statment will be printed
print(funny_division(0))
# This will print the correct value
print(funny_division(50.0))
# This is a TypeError which is not caught and thrown to the console to stop execution.
print(funny_division("hello"))

def funny_divison2(divider):
    try:
        if divider == 13:
            # will exit the method with ValueError exception raised
            raise ValueError("13 is not a good number")
        return 100/divider
    # ZeroDivisionError and TypeError is handled in the exception
    except(ZeroDivisionError, TypeError):
        return "Enter a number other than zero"

for val in (0, "hello", 50.0, 13):
    print("Testing {}: ".format(val), end="")
    print(funny_divison2(val))

def funny_division3(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise

for val in (0, "hello", 50.0, 13):
    print("Testing {}: ".format(val), end="")
    print(funny_division3(val))