import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, path):
        words = open(path, 'r')
        self.word_list = [word.strip() for word in words]
        print(f'{len(self.word_list)} words read')
        
    
    def random(self):
        return random.choice(self.word_list)
        

class SpecialWordFinder(WordFinder):
    def parse(self, words):
        return [word.strip() for word in words
                if word.strip() and not word.startswith('#')]

swf = SpecialWordFinder("/Users/jgbeavers/words.txt")
