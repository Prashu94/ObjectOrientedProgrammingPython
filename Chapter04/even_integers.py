class EvenOnly(list):
    def append(self, integer):
        # raise TypeError if the integer is not type of int
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        # raise the ValueError exception if integers are not even
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        # call the append method of list
        super().append(integer)


if __name__=='__main__':
    e = EvenOnly()
    e.append(0)