import random
import sys
import time


class CollegeProcess():
    
    
    def __init__(self):
        
        """Initialize the Khosla Kollege system.
        
        Parameters
        ----------
        No parameters but takes inputs and tuition money from the user.
        
        Returns
        -------
        Returns the college experience.
        """
        
        self.college_list = ["Killmonger", "Hulk", "Okoye", "Spiderman", "LilAntman", "Antman"]
        
        self.new_college = None 
        
        #Associates a housing area for each college
        self.housing_dict = {"Killmonger" : "Harlem", 
                             "Hulk" : "Hulk Hotels",
                             "Okoye" : "Wakanda", 
                             "Spiderman" : "New York City", 
                             "LilAntman" : "Smurf City",
                             "Antman" : "S'Ant Francisco"}
        
        self.housing_choice = None
        
        self.dining_plans = {"Starving Starks" : "$10,000",
                             "Thicc Thanos" : "$8,500",
                             "Hungry Hulks" : "$7,000",
                             "Dank Drax" : "$4,200", 
                             "Slim Spiders" : "$3,000 "}
        
        self.dining_choice = None
        
        self.majors = ["Khoslanomics", "Khoslogics", "Khosology", "Undeclared", "Coleslaw", "Raccoons"]
        
        self.final_major = None
        
        #Keeps track of the user"s choices for colleges
        self.college_choices = []
        
        #Gives the user higher chances of getting their priorty college choices
        #https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
        self.weights = [0.5, 0.25, 0.10, 0.05, 0.05, 0.05]
        
        
    def text_effect(self, string):
        
        """Creates a typing effect with code from 
        https://stackoverflow.com/questions/20302331/typing-effect-in-python
        
        Parameters
        ----------
        string: string
        String used for typing effect
        
        Returns
        -------
        None, but prints out the string with text effect
        """
        
        for char in string:
            time.sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()
            
        print("\n")
        
        
    def check_college_input(self, college):
        
        """Checks for correct input. If incorrect, quits with error message.
        
        Parameters
        ----------
        college : String
        User inputted college they want added to their ranked list of colleges.
                 
        Returns
        -------
        Doesn't return anything but updates a list, tracking inputted colleges.
        """
        
        if college not in self.college_list:
            raise ValueError("That's not a college you dropout! Restart cuz no refunds!")
            
        elif college in self.college_list:
            
            if college not in self.college_choices:
                self.college_choices.append(college)
                
            else:
                self.college_choices = []
                raise ValueError("You can only rank a college once! Restart")
       
    
    def college_ranking(self):
        
        """Takes user input and checks it using check_college_input.
        
        Parameters
        ----------
        None but takes user input as a string.
            
        Returns
        -------
        None but the check_college_input method appends the user"s inputs into a list.
        """
        
        self.text_effect("Welcome to KHOSLA Kollege and congrats on your admission!")
        self.text_effect("We'll now begin the KHOSLA Kollege Process")
        self.text_effect("Here are the six colleges of KHOSLA Kollege:")
        self.text_effect("Killmonger, Hulk, Okoye, Spiderman, LilAntman, Antman")
        self.text_effect("Please rank each college")
        
        self.college_choice1 = input("Choice #1: ")
        self.check_college_input(self.college_choice1)
    
        self.college_choice2 = input("Choice #2: ")
        self.check_college_input(self.college_choice2)
        
        self.college_choice3 = input("Choice #3: ")
        self.check_college_input(self.college_choice3)
        
        self.college_choice4 = input("Choice #4: ")
        self.check_college_input(self.college_choice4)
        
        self.college_choice5 = input("Choice #5: ")
        self.check_college_input(self.college_choice5)
        
        self.college_choice6 = input("Choice #6: ")
        self.check_college_input(self.college_choice6)
    
    
    def lottery(self):
        
        """Creates a lottery out of the user's ranked colleges.
        Uses code from https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
        and https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Prints out a randomly selected college, depending on the rank of the college.
        """
        
        time.sleep(1)
        
        self.text_effect("Did you know? The 'L' also stands for Lottery!")
        self.text_effect("That means we'll use a number generator to choose your college.")
        self.text_effect("But don't worry, your chances are probably better than 1 in 14,000,605.")
        
        #Randomly selects a college with weighted probabilities
        #https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
        self.new_college = random.choices(self.college_choices, weights = self.weights, k = 1)
        
        #Since random.choices() returns the selection as a list, "".join() converts it to a string
        #https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
        self.new_college = "".join(self.new_college)
        
        #Creates suspense in waiting for college result
        for seconds in range (3):
            time.sleep(seconds)
            self.text_effect("Loading...")
            
        self.text_effect("Congratulations! Your new college is:")
        self.text_effect(self.new_college)
       

    def housing(self):
        
        """User chooses to live on or off campus.
            
        Parameters
        ----------
        None but takes input from the user.
            
        Returns
        -------
        Doesn't return anything. It just prints out where the user will live.       
        """
        
        time.sleep(1)
        
        self.housing_choice = input("Would you like to live on or off campus? Type On or Off: ")
        self.housing_choice = self.housing_choice.capitalize()
        
        if self.housing_choice == "On":
            self.housing = self.housing_dict[self.new_college]
            self.text_effect("Okay! Based on your college, your on campus living space is: ")
            self.text_effect(self.housing)
            
        elif self.housing_choice == "Off":
            self.housing = "The Wild"
            self.text_effect("Cheapo. Good luck finding housing out there.")
            
        else:
            raise ValueError("Follow directions hobo.")

            
    def dining(self):
        
        """User chooses their dining plan
            
        Parameters
        ----------
        None but takes user input
            
        Returns
        -------
        Doesn't return anything but saves the user's choice of dining plan
        """
        
        time.sleep(1)
        
        self.text_effect("Here at KHOSLA Kollege we have dining plans more flexible than Black Widow!")
        self.text_effect("Our dining plans are:" )
        self.text_effect("Starving Starks, Thicc Thanos, Hungry Hulks, Dank Drax, and Slim Spiders")
        
        self.dining_choice = input("Which plan would you like?: ")
        
        #Checks to make sure user types in name of Dining Plan correctly.
        if self.dining_choice not in self.dining_plans:
            raise ValueError("Woops looks like you gonna starve homie.")
            
        else: 
            self.text_effect("Good choice! Your dining plan costs: ")
            self.text_effect(self.dining_plans[self.dining_choice])
        
        
    def major(self):
        
        """User chooses their Major and alternate major and is randomly given one of the two.
        
        Parameters
        ----------
        None but takes user input
            
        Returns
        -------
        None.     
        """
         
        time.sleep(1)
        
        self.text_effect("Every college makes you choose your life's career at 18.")
        self.text_effect("Here at KHOSLA Kollege, we do too!")
        self.text_effect("You're smart you can guess what the majors focus on.")
        self.text_effect("Here are our majors:")
        self.text_effect("Khoslanomics, Khoslogics, Khosology, Undeclared, Coleslaw, and Raccoons")
        
        self.major_choice1 = input("Your choice: ")
        self.major_choice2 = input("Alternate major (you know in case it doesn't work out: ")
              
        if self.major_choice1 not in self.majors or self.major_choice2 not in self.majors:
            raise ValueError("Learn to spell your own career correctly bruh")
        
        elif self.major_choice1 == self.major_choice2:
            raise ValueError("Your alternate choice has to be different.")
            
        else:
            self.final_major = random.choice([self.major_choice1, self.major_choice2])
            self.text_effect("Your major is " + self.final_major + ". Good luck.")
            
            
    def result(self):
        
        """Prints the result of the Kollege Process
        
        Parameters
        ----------
        None
            
        Returns
        -------
        Nothing
        """
        
        time.sleep(1)
        
        self.text_effect("Congrats! You finished the KHOSLA Kollege Process!")
        self.text_effect("Enjoy the " + self.new_college + " college experience!") 
        self.text_effect("We hope you feel at home in " + self.housing + ".")
        self.text_effect("Make good use of your " + self.dining_choice + " dining plan.")
        self.text_effect("Study hard in " + self.final_major + ", too many tryhards nowadays.")
        self.text_effect("Note we require a thicc $10,000 fee for anyone declining admission.")
        self.text_effect("Thank you for your money! I mean... yeah money :)")