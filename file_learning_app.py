import matplotlib.pyplot as plt
import pandas as pd

"""
"""
class Summary(User):
    """ Once the user is done with the game, this class will calculate statistics about their round, like the percentage of questions 
    answered correctly/incorrectly. These values will be printed to file.
            
    """
             
    def bar_visual_math(self): 
        stats = self.math_choosen()  
        
        correct_ans = stats[0]
        user_ans = stats[1]
        num_attempts = stats[2]
        num_questions = len(correct_ans)
        
        attempt_number = []
        perc_correct = []
        num_correct = 0
        attempt_labels = ["One Attempt", "Two Attempts", "Three Attempts"]
            
        for attempt in range(len(user_ans)):
            attempt_number.append(attempt_labels[attempt])
            
            num_correct = 0
                
            for answer in range(num_questions):
                if correct_ans[answer] == user_ans[attempt][answer]:
                    num_correct += 1
                    
                perc_correct.append((num_correct/len(correct_ans)) * 100)
                        
        
        plot_data = {"Attempt Number": attempt_number,
                "Percentage of Correctly Answered Questions": perc_correct
                } 
        
        df = pd.DataFrame(plot_data)  
        
        barplot = df.plot.bar(x = "Attempt Number", y = "Percentage of Correctly Answered Questions", color = ["red", "blue", "green"])
        barplot.get_legend().set_visible(False)
        
        barplot.set_xlabel("Attempt Number") 
        barplot.set_ylabel("Percentage of Correctly Answered Questions") 
        barplot.set_title(f"{self.grade} Level: {self.name}'s Performance Over {num_attempts} Attempt(s) in Math") 
        barplot.set_ylim(0, 110)
        
        return barplot
    
    def bar_visual_vocab(self): 
        stats = self.vocab_choosen() 
        
        correct_ans = stats[0]
        user_ans = stats[1]
        score = stats[3]
        
        perc_correct = []
        perc_incorrect = []
        num_correct = 0
        num_incorrect = 0
        attempt_labels = ["One Question", "Two Questions", "Three Questions"]
         
        for answer in range(3):
            
            if correct_ans[answer] == user_ans[answer]:
                num_correct += 1
                perc_correct.append((num_correct/(answer+1))/100)
                perc_incorrect.append(num_incorrect(answer+1)/100)
                
            else:
                num_incorrect += 1
                perc_correct.append((num_correct/(answer+1))/100)
                perc_incorrect.append(num_incorrect(answer+1)/100)
            
         
        plot_data = {"Percentage of Correctly Answered Questions": perc_correct,
                "Percentage of Incorrectly Answered Questions": perc_incorrect
                }
        
        df = pd.DataFrame(plot_data, index = attempt_labels)
        
        stacked_bar = df.plot(kind = "bar", stacked = True)
        
        stacked_bar.set_ylabel("Scores")
        stacked_bar.set_xlabel("Students")
        stacked_bar.set_title(f"{self.grade} Level: {self.name}'s Vocabulary Performance") 
        stacked_bar.set_ylim(0, 110)
        
       
    def bar_visual_grammar(self): 
        stats = self.grammar_choosen()
        
    def stats(self):     
        return(f"{self.name} practiced {self.subjects} at the {self.grade} level.\n"
               f"Questions Answered: {self.num_questions}\n"
               f"Number of Attempts: \n"
               f"Final Score: \n"
        )
    
            
         
                
                
            
            
            
                
                
                
        