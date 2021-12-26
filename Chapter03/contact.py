# Inheritance using the built-ins
class ContactList(list):
    def search(self, name):
        """ Return all contacts that contain the search value
        in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

# Basic Inheritance
class Contact:
    # Class variable i.e instance variable
    """
    the class variable when called using Contact.all_contacts will be different
    than self.all_contacts which is referred to the any one object.
    """
    # all_contacts = []
    # The above all_contacts was a list initialized using the actual list()

    # The below will use the bult-ins extended in the ContactList class
    all_contacts = ContactList()



    # Constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Supplier(Contact):
    """The Supplier class is extending the Contact class."""
    def order(self, order):
        print(
            "If this were a real system we would send "
            "'{}' order to '{}'".format(order, self.name)
        )

class Friend(Contact):
    """Inherits the Contact class"""
    # Overriding the constructor example
    def __int__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone



if __name__=='__main__':
    
    c1 = Contact("Prashant Bhat", "prashantbhat94@gmail.com")
    c2 = Contact("Lewis Hamilton", "lewishamilton@gmail.com")
    print([ c.name for c in Contact.all_contacts.search('Lewis')])
    # On inheriting the Contact class the attributes and the methods
    # all are inherited by the supplier class, alongwith the constructor.
    s = Supplier('Mercedes', "mercedeslogistics@gmail.com")
    print(c1.name, s.name, c1.email, s.email)
    print(s.order(c1))



