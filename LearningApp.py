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
        self.subjects = subjects

    def grade_level(self):
        """ Uses regular expressions to match the grade level given by the user
        with the specificed spelling given by this program for kindergarten,
        first, and second grade.
        
        Returns:
            str: returns the matched grade level given by the user
            
        Side Effects:
            Sets the grade attribute to the match found by the regular 
            expression
        """
        
        regex = r"([K]|K\w+|[1]|1\w+|F\w+|[2]|2\w+|S\w+)$"
        match = re.search(regex, self.grade)
        
        if match:
            grade_given = match.group(0)
        
            if grade_given in ["K", "Kindergarten"]:
                self.grade = "K"
            elif grade_given in ["1", "1st", "First"]:
                self.grade = "1"
            elif grade_given in ["2", "2nd", "Second"]:
                self.grade = "2"
            
        return f"""You will be doing questions for {self.grade}! You have 
    choosen to do practice in {self.subjects}."""
            
    

user1 = User("Sarah","Kindergarten",["Math"])
print(user1.name)
print(user1.grade_level())

    

# Harshitha's Math Class
# Math class

# Tatyana's Vocab Class
# Vocab Class

# Nivitha's Summary Class
# Summary Class

# Jess's Grammar Class
# Grammar Class