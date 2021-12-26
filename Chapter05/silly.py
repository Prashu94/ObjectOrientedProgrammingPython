class Silly:

    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Woah, you killed silly")
        del self._silly

    """
    Parameter definition:
    1. _get_silly - method for the property getter
    2. _set_silly - method for the property setter
    3. _del_silly - method for deleting the property
    4. docstring - pass the docstring for the property.
    """
    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")


"""
Decorators: Another way to create properties
1. Prefix the function name with @ symbol and placing the result just before
the definition of the function that is being decorated.
"""
class SillyDecorated:

    @property
    def silly(self):
        """This is a silly property"""
        print("Your are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Woah, you killed silly!")
        del self._silly

if __name__=='__main__':
    s = Silly()

    s.silly = "funny"
    print(s.silly)
    del s.silly

"""
1. First we decorate the silly method as getter.
2. Second we decorate a new method with exactly the same name with the setter attribute of 
the original decorated silly method, as the property function returns an object; this object is 
automatically set up to have a setter attribute, and this attribute can be applied as 
a decorator to other functions.
"""