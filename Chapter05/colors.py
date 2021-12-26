class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        # Private variable
        self._name = name

    # Create private setter method for name variable
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    # Create private getter method for name variable
    def _get_name(self):
        return self._name

    # The property method acts like a constructor which will
    # allow access of the _set_name and _get_name methods outside the class
    name = property(_get_name, _set_name)
if __name__ == '__main__':
    c = Color("#0000ff", "bright red")
    # All the method and variables marked with _ cannot be access outside the class.
    print(c.name)
    c.name = "red"
    print(c.name)
    c.name = "" # This will throw error as it is trying to set empty property value.