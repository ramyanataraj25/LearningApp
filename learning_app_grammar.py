class Grammar:
    """Class that identifies mistakes from user input from each student while
    tallying errors.
    Attributes:
        name (str): Name of the student
        grade (str): The grade of the user
        errors (list): A list that stores amount of errors made 
    """
    def __init__(self, name, grade):
        """Sets the attributes of the Grammar class."""
        self.name = name
        self.grade = grade
        self.errors = []

    def punctuation(self, user_input):
        """Checks if the sentence ends with the correct punctuation."""
        if not user_input.endswith(('.', '!', '?')):
            self.errors.append('This sentence must end with a period (.), exclamation mark (!), or question mark (?).')
            return 1
        return 0

    def capitalization(self, user_input):
        """Checks if the sentence starts with an appropriate capital letter."""
        if not user_input[0].isupper():
            self.errors.append('This sentence must start with a capital letter!')
            return 1
        return 0

    def word_count(self, user_input):
        """Checks if the sentence has at least three words within it."""
        word_count = len(user_input.split())
        if word_count < 3:
            self.errors.append(f"A complete sentence should have at least 3 words! This sentence is ({word_count}) words.")
            return 1
        return 0

    def pronoun_capitalization(self, user_input):
        """Checks if the pronoun 'I' is capitalized.""" 
        if ' i ' in user_input or user_input.startswith('i '):
            self.errors.append("'I' is a pronoun that must always be capitalized.")
            return 1
        return 0

    def error_count(self, user_input):
        """Counts errors in the user input."""
        self.errors.clear()
        count_errors = (
            self.punctuation(user_input)
            + self.capitalization(user_input)
            + self.word_count(user_input)
            + self.pronoun_capitalization(user_input)
        )
        for error in self.errors:
            print(error)
        if count_errors > 0:
            print(f"Total errors found: {count_errors}.")
        else:
            print("No errors found! Great job!")

        return count_errors
    
student = Grammar("Jess", "K")
sentence = input("Enter a sentence: ")
error_number = student.error_count(sentence)
#print(f"Total errors: {error_number}")   