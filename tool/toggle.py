import csv
import time

class Toggle:
    def __init__(self):
        pass

    def select_file(self):
        while True:
            print("\nWhich type of questions would you like to enable/disable?")
            print("1. Quiz questions.")
            print("2. Free-Form questions.")
            print("3. Go back to main menu.")
            try:
                option=int(input("\nEnter number of file to select it: \n"))
                if option == 1:
                    self.show_file("qquestion.csv")
                    time.sleep(0.3)
                    self.select_toggle("qquestion.csv")
                elif option == 2:
                    self.show_file("ffqquestions.csv")
                    time.sleep(0.3)
                    self.select_toggle("ffqquestions.csv")
                elif option == 3:
                    break
                else: 
                    print("You must choose between one ")
                    return self.select_file() 
            except ValueError:
                print("Invalid input")
    
    def show_file(self, file_name):
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(f"ID: {row[0]}, Enabled: {row[1]}, Question: {row[3]}, Answer: {row[2]}, ")

    def select_toggle(self, file_name):
        entered_id = int(input("\nEnter ID of the question you would like to enable/disable: "))
        optiont = input("\n would you like to enable (e) or disable (d)? ").lower().strip()
        if optiont == "e":
            self.enable(file_name, entered_id)
        elif optiont == "d":
            self.disable(file_name, entered_id)
        else:
            print("Enter 'e' to enable or 'd' to disable.")

    def enable(self, file_name, id):
        self.change_file(file_name, id, True)

    def disable(self, file_name, id):
        self.change_file(file_name, id, False)

    def change_file(self, file_name, id, status):
        with open(file_name, "r", newline="") as f:
            reader = csv.reader(f)
            data = list(reader)
        question_found_by_id = False
        for row in data:
            if int(row[0]) == id:
                row[1] = "True" if status else "False"
                question_found_by_id = True
                break
        if not question_found_by_id:
            print("\nThere are no questions with this ID.")
            return
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)