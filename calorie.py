class Calorie:
    """calcutaes the amount of calories with this formular:
    10*weight + 6.25* height - 5*age +5 + 5 (for men) or 
    10*weight + 6.25* height - 5*age +5 -161 (for women)"""

    def __init__(self, sex, weight, height, age):
        self.sex = sex
        self.weight = weight
        self.height = height
        self.age = age
        

    def calculate(self):
        try:
            if self.sex == "male":
                last_bit = 5
            elif self.sex == "female":
                last_bit = -161
            result = 10*self.weight + 6.35*self.height - 5*self.age +5  + last_bit
            return f"You need {result} calories today."
        except: return "Please enter your sex as 'male' or 'female'"

calorie = Calorie("female",70,183,28,14)

print(calorie.calculate())
