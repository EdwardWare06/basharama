class Character:
    def __init__(self, char):
        self.char = char

    def get_char(self):
        return self.char

class Word:
    def __init__(self, *chars):
        self.chars = [Character(char) for char in chars]

    def get_word(self):
        return ''.join([char.get_char() for char in self.chars])

class Sentence:
    def __init__(self, *words):
        self.words = [Word(*word) for word in words]

    def get_sentence(self):
        return ' '.join([word.get_word() for word in self.words])


goodbye_word = Sentence(
    ['g', 'o', 'o', 'd', 'b', 'y', 'e'] 
)


print(goodbye_word.get_sentence())
