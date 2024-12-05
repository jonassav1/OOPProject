import random
import csv

class IDS:
    
    def __init__(self):
        self.ids = []

    def read_id_from_file(self, *file_names):
        for file_name in file_names:
            try:
                with open(file_name, "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row:
                            self.ids.append(row[0])
            except FileNotFoundError:
                print(f"File named {file_name} is not found")

    def generate_id(self):
        while True:
            new_id = random.randint(1,100)
            if new_id not in self.ids:
                self.ids.append(new_id)
                return new_id
