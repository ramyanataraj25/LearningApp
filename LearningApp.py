class Math:
    def __init__(self, name, grade, score):
        self.name = name
        self.grade = grade
        self.score = score

class User:
    def __init__(self, name, grade, reason):
        self.name = name
        self.grade = grade
        self.reason = reason
        
class Vocab:
    def __init__(self, grade, name):
        self.grade = grade
        self.name = name

class Summary:
    def __init__(self, math, vocab, grammar):
            self.math = math
            self.vocab = vocab
            self.grammar = grammar 

class Grammar:
    def __init__(self, name, grade, feedback):
        self.name = name
        self.grade = grade
        self.feedback = feedback