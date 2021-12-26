class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street = "", city="", state ="", code = "", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    """Class that demonstrates multiple-inheritance using diamond problem."""
    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


"""
1. **kwargs- collects any keyword argument passed to the method 
that were not explicitly listed in the parameter list.
2. These arguments are stored in the dictionary named kwargs.
"""

