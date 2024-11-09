class Summary:
    """ Once the user is done with the game, this class calculates statistics about their round, like the percentage of questions 
    answered correctly/incorrectly. These values will be printed to file.
    
    Attributes: 
            self.topics (dict): Keys are the question names/number(to identify the question). The values will be the number
            of tries it took to get the question right.
            
    """
    def __init__(self, topic):
        """Initializes the input recieved a topic within the math, grammar, or vocab functions, and creates a dictionary 
        containing the information. For example, a topic within the math function could be addition. 
        
        Args: 
            topic (dict): Keys are the question names/number(to identify the question). The values will be the number
            of tries it took to get the question right. Used to initialize self.topic. 
            
        Side effects:
            Initializes the topic dictionary.
        """
        self.topic = topic 
         
    
    def topic_counter(self):
        """Creates and updates a dictionary called topic_values in which keys the number of tries it took to answer a question correctly.
        Values are counters in order to count the number of questions within the topic that took either 1, 2, 3 tries, or were incorrect.
        This dictionary will be used to calculate the percentage of questions that took either 1, 2, 3 tries, or were incorrect.
        
        Returns:
            A tuple with percentages for the number questions for each try number. 
        """
        
        topic_values = {1: 0, 2: 0, 3: 0, "wrong": 0}
                        
        
        for question, tries in self.topic.items():
            if tries == 1:
                    topic_values[1] += 1
                    
            elif tries == 2:
                    topic_values[2] += 1
                    
            elif tries == 3:
                    topic_values[3] += 1  
                    
            elif tries == "wrong":
                    topic_values["wrong"] += 1
                    
            
        perc1 = (topic_values[1]/len(self.topic)) * 100
        perc2 = (topic_values[2]/len(self.topic)) * 100
        perc3 = (topic_values[3]/len(self.topic)) * 100
        perc4 = (topic_values["wrong"]/len(self.topic)) * 100
                
        return (perc1, perc2, perc3, perc4)
    
    
topic = {
    "Q1": 1,   
    "Q2": 2,    
    "Q3": "wrong",  
    "Q4": 3,    
    "Q5": 1    
}

sum_instance = Summary(topic)
percentage = sum_instance.topic_counter()

print(percentage) 