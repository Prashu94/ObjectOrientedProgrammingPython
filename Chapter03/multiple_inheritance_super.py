class BaseClass:
    # class variable
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls+=1

class LeftSubClass(BaseClass):
    """LeftSubClass extends the BaseClass."""
    # class variable
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls+=1

class RightSubClass(BaseClass):
    """RightSubClass extends the BaseClass. """
    # class variable
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls+=1

class Subclass(RightSubClass, LeftSubClass):
    """Multiple Inhertiance on LeftSubClass & RightSubClass."""
    # class variable
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls+=1

if __name__=='__main__':
    s = Subclass()

    print(s.call_me())
    print(s.num_base_calls, s.num_left_calls, s.num_right_calls,
          s.num_sub_calls)

""" In this example the BaseClass is called only once.
1. The BaseClass first printed through the call of RightSubClass.
2. If we invert the order of inheritance in the Subclass the 
BaseClass is called through LeftSubClass."""