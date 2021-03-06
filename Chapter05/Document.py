class Document:

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character):
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, "w") as f:
            f.write("".join(self.characters))

    @property
    def string(self):
        return "".join(str(c) for c in self.characters)


class Cursor:

    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Go to the beginning of the file before newline
                break

    def end(self):
        while (
                self.position < len(self.document.characters)
                and self.document.characters[self.position].character != '\n'
        ):
            self.position += 1


class Character:

    def __init__(self, character, bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character


if __name__=='__main__':
    d = Document()
    d.insert('h')
    d.insert('e')
    d.insert(Character('l', bold=True))
    d.insert(Character('l', bold=True))
    d.insert('o')
    d.insert('\n')
    d.insert(Character('w', italic=True))
    d.insert(Character('o', italic=True))
    d.insert(Character('r', underline=True))
    d.insert('l')
    d.insert('d')
    print(d.string)
    d.cursor.home()# Go to W letter
    d.delete()
    d.insert('W')
    print(d.string)
    d.characters[0].underline = True
    print(d.string)