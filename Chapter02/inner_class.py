def format_string(string, formatter=None):
    """Format string using the formatter object, which
    is expected to have a format() method that accepts a string"""

    class DefaultFormatter:
        """Format a string in title case."""

        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()
    return formatter.format(string)

hello_string = "Hello world, how are you today?"
print(" Input: "+hello_string)
print(" Output: "+format_string(hello_string))