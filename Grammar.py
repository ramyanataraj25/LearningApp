class Grammar: 
    """Class that identifies mistakes from user input from each student while
    tallying errors.
    Attributes:
        name (str): Name of the student
        grade (str): The grade of the user
        errors (list): A list that stores amount of errors made  
    """
    def __init__(self, name, grade):
        """Sets the attributes of the grammar class."""
        self.name = name
        self.grade = grade
        self.errors = []
   
    def error_count(self, user_input):
        """Counts errors of the user input while keeping score and appending to
        original errors list.
        Args:
            user_input(str): Takes the input of the user.
        Returns:
            count_errors(int): The amount of errors the user made. """
        count_errors = 0
      
        if not user_input.endswith(('.', '!', '?')):
            count_errors += 1
            self.errors.append('punctuation')

        if not user_input[0].isupper():
            count_errors += 1
            self.errors.append('capitalization')
            

        return count_errors
student = Grammar("Jess", "K")
sentence = input("Enter a sentence: ")
error_number = student.error_count(sentence)
print(f"Total errors: {error_number}")   
    