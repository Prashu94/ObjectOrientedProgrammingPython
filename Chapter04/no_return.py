def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never be executed")
    return "I won't be returned"

def call_exceptor():
    print("call exceptor starts here....")
    no_return()
    print("an exception was raised")
    print("... so these lines don't run")

try:
    no_return()
except:
    print("I caught an exception")

print("executed after exception")