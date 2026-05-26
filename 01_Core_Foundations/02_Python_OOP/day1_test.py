class SummerFoundation:
    def __init__(self, language):
        self.language = language

    def display_status(self):
        print(f"Success! Python OOP structures are executing for {self.language}.")

# Instantiating a new object
session = SummerFoundation("Day 1 Core Drills")
session.display_status()