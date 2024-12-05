import re
from Math import MathQ
from learning_app_vocab import Vocab
from learning_app_grammar import Grammar

def math_choosen(self):
    """ If the user chooses to work on math, this method is called and uses
    the Math class to instantiate a user, and generate math questions. The user
    will get 3 attempts on each question.
    
    Returns:
        list: list of the correct answers and the user's answers
    
    Side effects:
        prints each math question for the grade choosen, prints the final score,
        and stores user's answers as input
    """
    count = input("How many questions would you like to get?: ")
    count = int(count)
    mathUser = MathQ(self.grade,count)
    mathUser.get_questions()
    print(mathUser.questions)
    
    attempts = 0
    correct_answers = mathUser.answers
    user_answers = []
    
    for attempt in range(3):
        mathUser.math_questions()
        user_answers.append(mathUser.user_ans)
        
        if mathUser.score() == 100.0:
            attempts = attempts_taken(attempt)
            print("All Correct!")
            break
        else:
            attempts = attempts_taken(attempt)
            print("Try Again")

    if mathUser.score() < 100.0:
        print(f"You scored: {mathUser.score()}% in {attempts} attempt(s)." + 
              f"You answered {user_answers} and the " + 
              f"correct answers were {mathUser.answers}.")
    else:
        print(f"You scored: {mathUser.score()}% in {attempts} attempt(s).")
    
    return [correct_answers, user_answers, attempts]

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
    correct_answers = []
    attempts = 0
    
    
    for round in range(3):
        vocabGenerate = vocabUser.vocab_generator()
        vocabQs = vocabGenerate.split("&")[0]
        correct_answer = vocabGenerate.split("&")[1]
        print(vocabQs)
        userAnswer = input("\nWhat is the answer?: ")
        attempts = attempts_taken(round)
        user_answers.append(userAnswer)
        correct_answers.append(correct_answer)
    
    return [correct_answers, user_answers, attempts]

def grammar_choosen(self):
    grammar_user = Grammar(self.name, self.grade)
    for _ in range(3):
        user_sentence = input("\nEnter a sentence here:")
        error_count = grammar_user.error_count(user_sentence)

        if error_count ==0:
            print("\nGreat job! No errors found.")
        else:
            print("\nIssues found in the sentence:") 
        for error in grammar_user.errors:
            print(f"{error}")
    print("\nKeep Practicing!")
    return [grammar_user.errors, error_count]
    

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
    """ Calculates the number of attempts out of 3 the user takes to get the 
    questions correct or incorrect.
    
    Args:
        attempt (int): one attempt that is added to the total each time a 
        question is tried again
        
    Returns:
        int: total count of attempts taken
    """
    total_attempts = 1
    total_attempts += attempt
    
    return total_attempts

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
                        "\nOptions are Math, Vocab, Grammar: ")
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
        
        regex = r"([kK]|K\w+|[1]|1\w+|F\w+|[2]|2\w+|S\w+)$"
        match = re.search(regex, self.grade)
        
        if match:
            grade_given = match.group(0)
        
            if grade_given in ["K", "k", "Kindergarten"]:
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
            str: the result of the checkAnswer(); the information on how the 
            user did on the questions
            
            list: result of math_choosen() method, a list of 
            the answers given, the correct answers, and the last attempt
        """
        if self.subjects == "math":
            result = math_choosen(self)
            return result
        elif self.subjects == "vocab":
            result = vocab_choosen(self)
            correct = checkAnswer(result[0], result[1][2])
            return correct
        elif self.subjects == "Grammar":
            result = grammar_choosen(self)
            return result

            
def main():
    user1 = User()
    print(user1.grade_level())
    result = user1.subjects_choosen()
    print(result)
    
if __name__ == "__main__":
    main()