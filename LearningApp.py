import re

class User:
    """ LearningApp created for students in kindergarten to second grade, to 
    improve in subjects of math, grammar, and vocabulary.
    User Class is utilized to get information specific to each user such as
    name, grade, and reason they are using our app.
    
    Attributes:
        name (str): name of the student using the app
        grade (str): grade level the student is in (either K, 1st, or 2nd)
        subjects (list): list of subjects the student wants to imporve in
            can be 1 to all subjects 
    """
    def __init__(self, name, grade, subjects):
        """ Creates an instance of the user class.
        
        Args:
            name (str): name of the student using the app
        grade (str): grade level the student is in (either K, 1st, or 2nd)
        subjects (list): list of subjects the student wants to imporve in
            can be 1 to all subjects
        """
        self.name = name
        self.grade = grade
        self.subjects = []

    def grade_level(self, grade):
        """ Uses regular expressions to match the grade level given by the user
        with the specificed spelling given by this program for kindergarten,
        first, and second grade.
        
        Args:
            grade (str): grade given in the user's information
        
        Returns:
            str: returns the matched grade level given by the user
            
        Side Effects:
            Sets the grade attribute to the match found by the regular 
            expression
        """
        
        regex = r"""
            (?x)
            ^
            ([K]|K\w+|[1]|1\w+|F\w+|[2]|2\w+|S\w+)$
            """
        if re.search(regex, grade):
            match = re.search(regex, grade)
            self.grade = match.group(0)
        
        return self.grade
    

user1 = User("Sarah","Kindergarten","Math")
print(user1.name)
print(user1.grade_level(user1.grade))
print(user1.subjects)

    

# Harshitha's Math Class
# import MathQ

# Tatyana's Vocab Class
# import Vocab

# Nivitha's Summary Class
# import Summary

# Jess's Grammer Class
# import Grammar