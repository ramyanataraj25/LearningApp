import random

class MathQ:
    """
    This class represents the mode of the Learning App that specializes in 
    providing Math questions to the user.
    
    Attributes:
        grade (str): the grade of the user
        num_correct (int): the number of questions the user wants to get correct
        before advancing in level
        max_questions (int): the maximum number of questions the user wants to 
        answer
        ops (set of int): the operators used in math questions
        questions (set of str): each question that would be provided to the user
        answers (set of int): the answers to each respective question
    """
    def __init__(self, grade, max_questions):
        """
        Initializes an instance of the user learning in the Math mode
        
        Arguments:
            grade (str): the grade of the user
            max_questions (int): the maximum questions a user wants to have
        
        Side effects:
            Initializes the attributes related to a set of Math questions
        """
        self.grade = grade
        self.max_questions = max_questions
        self.ops = []
        self.questions = []
        self.answers = []
        
    def get_questions(self):
        """
        Generates questions and the corresponding answers
        
        Side effects:
            Generates questions for the user and the corresponding answers
        """
        countq = 1
        if self.grade == "K":
            self.ops = ["+", "-"]
            
            while countq <= self.max_questions:
                val1 = random.randint(0, 9)
                val2 = random.randint(0, 9)
                this_ops = random.randint(0, 1)
                if val1 > val2:
                    countq = countq + 1
                    self.questions.append(f"{val1} {self.ops[this_ops]} {val2}")
                    self.answers.append(eval(f"{int(val1)} {self.ops[this_ops]} \
                    {int(val2)}"))
                    
            
        elif self.grade == "1":
            self.ops = ["+", "-"]
            for num in range(self.max_questions):
                val1 = random.randint(0, 99)
                val2 = random.randint(0, 99)
                this_ops = random.randint(0, 1)
                if val1 > val2:
                    self.questions.append(f"{val1} {self.ops[this_ops]} {val2}")
                    self.answers.append(eval(f"{int(val1)} {self.ops[this_ops]} \
                    {int(val2)}"))
            
        elif self.grade == "2":
            self.ops = ["+", "-"]
            for num in range(self.max_questions):
                val1 = random.randint(0, 999)
                val2 = random.randint(0, 999)
                this_ops = random.randint(0, 1)
                if val1 > val2:
                    self.questions.append(f"{val1} {self.ops[this_ops]} {val2}")
                    self.answers.append(eval(f"{int(val1)} {self.ops[this_ops]} \
                    {int(val2)}"))

"""               
def main():
    q = MathQ("K", 10)
    print(q.get_questions())
    
if __name__ == "__main__":
    main()
"""
        
    
                
            
        
    
    
        