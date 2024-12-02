import re
from Math import MathQ
from learning_app_vocab import Vocab

def math_choosen(self):
    """ If the user chooses to work on math, this method is called and uses
    the Math class to instantiate a user, and generate math questions.
    
    Returns:
        list: list of the correct answers and the user's answers
    
    Side effects:
        prints each math question for the grade choosen, prints thh final score,
        and stores user's answers as input
    """
    count = input("How many questions would you like to get?: ")
    count = int(count)
    mathUser = MathQ(self.grade,count)
    mathUser.get_questions()
    print(mathUser.questions)
    
    attempts = 0
    
    for attempt in range(3):
        question = mathUser.math_questions()
        attempts = attempts_taken(attempt)
        if question != mathUser.answers and attempt < 2:
            print("Try Again")
        else:
            break

    if mathUser.score() < 100.0:
        print(f"You scored: {mathUser.score()}% in {attempts} attempts." + 
              f"The correct answers were {mathUser.answers}")
    else:
         print(f"You scored: {mathUser.score()}% in {attempts} attempts.")

def vocab_choosen(self):
    """ If the user chooses to work on vocab, this method is called and uses
    the Vocab class to instantiate a user, and generate vocab questions.
    
    Returns:
        list: list of the correct answers and the user's answers
        
    Side effects:
        prints each vocab question for the grade choosen, and stores user's
        answers as input
    """
    userGrade = ""
    if self.grade == "K":
        userGrade = "kindergarten"
    elif self.grade == "1":
        userGrade = "first_grade"
    elif self.grade == "2":
        userGrade = "second_grade"    

    vocabUser = Vocab(userGrade)
    user_answers = []

    vocabGenerate = vocabUser.vocab_generator()
    #vocabQs = vocabGenerate.split("&")[0]
    correct_answers = vocabGenerate.split("&")[1]
    #print(vocabQs)
    #print(vocabGenerate)
    userAnswer = input("\nWhat is the answer?: ")
    user_answers.append(userAnswer)
    return [correct_answers, user_answers]

def checkAnswer(answers, userAnswers):
    """ Checks answers given by the user with the correct answers. Counts how
    many answers were correct, and returns count
    
    Args:
        answers (str): the correct answers pertaining to the questions given to 
        the user
        userAnswers (list): the answers given by the user
    
    Returns:
        str: provides the user information on their results; 
        how many questions are correct from the three rounds.
    
    """
    userCorrectAs = 0
    for word in userAnswers:
        if word in answers:
            userCorrectAs += 1
        return f"You got {userCorrectAs}/3 correct!"

def attempts_taken(attempt):
    attempts = 1
    attempts += attempt
    return attempts

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
    def __init__(self):
        """ Creates an instance of the user class.
        
        Args:
            name (str): name of the student using the app
            grade (str): grade level the student is in (either K, 1st, or 2nd)
            subjects (list): list of subjects the student wants to improve in
                can be 1 to all subjects
        """
        self.name = input("What is your name? ")
        self.grade = input(f"Hi {self.name}, what grade are you learning in?" + 
                           " Options are Kindergarten through 2nd grade.: ")
        self.subjects = input(f"Hi {self.name}, you are doing questions in " +
                    f"{self.grade}. What subjects do you want to improve in?" +
                        " Options are Math, Vocab, Grammar: ")
        self.subjects = self.subjects.lower()

    def grade_level(self):
        """ Uses regular expressions to match the grade level given by the user
        with the specificed spelling given by this program for kindergarten,
        first, and second grade.
        
        Returns:
            str: returns the matched grade level given by the user
            
        Side effects:
            Sets the grade attribute to the match found by the regular 
            expression
        """
        
        regex = r"([Kk]|K\w+|[1]|1\w+|F\w+|[2]|2\w+|S\w+)$"
        match = re.search(regex, self.grade)
        
        if match:
            grade_given = match.group(0)
        
            if grade_given in ["K", "Kindergarten"]:
                self.grade = "K"
            elif grade_given in ["1", "1st", "First"]:
                self.grade = "1"
            elif grade_given in ["2", "2nd", "Second"]:
                self.grade = "2"
            
        return (f"You will be doing questions for {self.grade}!" +
    f" You have choosen to do practice in {self.subjects}.")
   
    def subjects_choosen(self):
        """ Calls on the classes for each subject and creates instances, and
        calls methods to provide the user questions
        
        Returns:
            str: the result of the checkAnswer() method; the information on how
            the user did on the questions
        """
        if self.subjects == "math":
            result = math_choosen(self)
        elif self.subjects == "vocab":
            for round in range(3):
                result = vocab_choosen(self)
                correct = checkAnswer(result[0], result[1])
            return correct
       # elif self.subjects == "Grammar":
            # print_gquestions(self)

            
def main():
    user1 = User()
    print(user1.grade_level())
    user1.subjects_choosen()
    
if __name__ == "__main__":
    main()