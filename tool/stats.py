import csv

class Stats:
    def __init__(self):
        pass

    def view_statistics(self):
        print("\nStatistics for the quiz questions:")
        self.show_statistics("qquestion.csv")
        print("\nStatistics for the free-form questions:")
        self.show_statistics("ffqquestions.csv")
        print("\nStatistics from tests!")
        self.show_test_stats("result.txt")

    def show_statistics(self, file_name):
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                answered = int(row[-2])
                incorrect = int(row[-1])
                correct_answers = answered - incorrect
                if correct_answers > 0:
                    precentage = (correct_answers / answered) * 100
                else: 
                    precentage = 0 
                print(f"In practice, ID: {row[0]}, Active: {row[1]}, Question: {row[3]}, Answer: {row[2]}, Times asked: {row[-3]}, Correctly answered rate: {precentage}%")

    def show_test_stats(self, file_name):
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(f"{row}")