class Human :

    human_num = 0
    human_ex = 2000

    def __init__(self, hair, muscle, eye_color, year):
        self.hair = hair
        self.muscle = muscle
        self.eye_color = eye_color
        self.year = year
        Human.human_num += 1
    
    def describe(self):
        print(f"human has {self.hair} hair")
    
    def born(self):
        print(f"Human was bor in {self.year}")
    
    @classmethod
    def get_info(cls):
        print(f"Human numbers are; {cls.human_num}")
    
    @staticmethod
    def call_me():
        return "staticmethod is working"

    def __str__(self):
        return "exist"
class Child(Human) :
    def __init__(self, hair, muscle, eye_color,year):
        super().__init__(hair, muscle, eye_color, year)
    
    def moving():
        print("Human is moving")


h1 = Child("red", True, "blue", 2003)

print(f"human exist from the time {Human.human_ex} and there are {Human.human_num}")
print(h1)
