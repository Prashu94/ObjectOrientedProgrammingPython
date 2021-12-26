"""Example that shows bad way of multiple inheritance."""
class BaseClass:
    # class variable
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls+=1

class LeftSubClass(BaseClass):
    """The LeftSubClass extends the BaseClass."""
    # class variable
    num_left_calls=0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_calls+=1

class RightSubClass(BaseClass):
    """The RightSubClass extends the BaseClass"""
    # class variable
    num_right_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls+=1

class Subclass(LeftSubClass, RightSubClass):
    """The Subclass extends both LeftSubClass
    and RightSubClass forming multiple inheritance
    alongwith the diamond shape."""
    # class variable
    num_sub_calls = 0
    def call_me(self):
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print("Calling method on SubClass")
        self.num_sub_calls+=1

if __name__=='__main__':
    s = Subclass()

    print(s.call_me())
    print(s.num_base_calls, s.num_left_calls, s.num_right_calls,
          s.num_sub_calls)


"""The above example shows the num_base_calls is done twice 
as the LeftSubClass and RightSubClass both calls the BaseClass methods once.
This is not good way."""