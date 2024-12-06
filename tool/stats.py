import csv

class Stats:
    def __init__(self) -> None:
        pass

    def view_statistics(self):
        print("\nStatistics for the quiz questions:")
        self.show_statistics("qquestion.csv")
        print("\nStatistics for the free-form questions:")
        self.show_statistics("ffqquestions.csv")

    def show_statistics(self, file_name):
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                print(f"ID: {row[0]}, Active: {row[1]}, Question: {row[3]}, Answer: {row[2]}")
                # ir kai turesiu practice moda tada pridesiu per ji du naujus data tipus i gala situ failu vienas bus counteris kiek kartu pasirode klausimas kitas kiek kartu i ji atsake procentaliai
