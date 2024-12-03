

class Questions:
    def add_questions(self):
        while True:
            print("\n\nChoose what type of questions you would like to add!")
            print("1. Quizz questions!")
            print("2. Free-form text questions!")
            print("3. Go back to main menu.")
            try:
                optionQ = int(input("Choose type of the question or go back to main menu: "))
                if optionQ == 1:
                    print("Quizzzzz")
                elif optionQ == 2:
                    print("Free-form")
                elif optionQ == 3:
                    break
                else:
                    print("You must enter a number between 1 and 3") 
            except ValueError:
                print("Invalid input")
                

    
    # def __init__(self):
    #     self.quiz = input()
    #     self.free = 
