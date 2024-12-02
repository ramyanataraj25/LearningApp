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
        ops (list of str): the operators used in math questions
        questions (list of str): each question that would be provided to the user
        answers (list of int): the answers to each respective question
        user_ans (list of str): the answers the user provides for each question
    """
    def __init__(self, grade, max_questions = 10):
        """
        Initializes an instance of the user learning in the Math mode
        
        Arguments:
            grade (str): the grade of the user
            max_questions (int): the maximum questions a user wants to have, the 
            default number is 10
        
        Side effects:
            Initializes the attributes related to a set of Math questions
        """
        self.grade = grade
        self.max_questions = max_questions
        if grade == "K" or grade == "1" or grade == "2":
            self.ops = ["+", "-"]
        self.questions = set()
        self.answers = []
        self.user_ans = []
        
    def get_questions(self):
        """
        Generates questions and the corresponding answers
        
        Side effects:
            Generates questions for the user and the corresponding answers
        """
        countq = 1
        if self.grade == "K":
            
            while countq <= self.max_questions:
                val1 = random.randint(0, 9)
                val2 = random.randint(0, 9)
                this_ops = random.randint(0, 1)
                if val1 > val2:
                    countq = countq + 1
                    self.questions.add(f"{val1} {self.ops[this_ops]} {val2}")
                    self.answers.append(eval(f"{int(val1)} {self.ops[this_ops]}\
                    {int(val2)}"))
                    
            
        elif self.grade == "1":
            while countq <= self.max_questions:
                val1 = random.randint(0, 99)
                val2 = random.randint(0, 99)
                this_ops = random.randint(0, 1)
                if val1 > val2:
                    countq = countq + 1
                    self.questions.add(f"{val1} {self.ops[this_ops]} {val2}")
                    self.answers.append(eval(f"{int(val1)} {self.ops[this_ops]}\
                    {int(val2)}"))
            
        elif self.grade == "2":
            
            while countq <= self.max_questions:
                val1 = random.randint(0, 999)
                val2 = random.randint(0, 999)
                this_ops = random.randint(0, 1)
                if val1 > val2:
                    countq = countq + 1
                    self.questions.add(f"{val1} {self.ops[this_ops]} {val2}")
                    self.answers.append(eval(f"{int(val1)} {self.ops[this_ops]}\
                    {int(val2)}"))
                    
    def math_questions (self):
        """
        Gets user's answers to generated questions
        
        Side effects:
            Prints each question and stores input in the attribute user_ans
        """
        self.user_ans = [input(f"{q} = ") for q in self.questions]
    
    def score (self):
        """
        Computes score in percentage that the user gets for their play
        
        Returns:
            The percentage of correct answers
        """
        num_correct = 0
        for a in self.user_ans:
            for correct_a in self.answers:
                if str(a) == str(correct_a):
                    num_correct = num_correct + 1
        percent_correct = num_correct / len(self.questions)
        return percent_correct * 100
        

"""
def main():
    q = MathQ("K",3)
    q.get_questions()
    print(q.questions)
    print(q.answers)
    q.math_questions()
    print(q.score())
    
if __name__ == "__main__":
    main()
"""       
                
            
        
    
    
        