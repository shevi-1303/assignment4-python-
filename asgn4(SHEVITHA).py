class Database:
    def __init__(self, s_name,s_dept,s_year,s_cgpa):
        self.s_name=s_name
        self.s_dept=s_dept
        self.s_year =s_year
        self.s_cgpa=s_cgpa

    def student1_profile(self):                         
        print("Name:",self.s_name)
        print("Dept:",self.s_dept)
        print("Year:",self.s_year)

""" OUTPUT:
   Name: SHEVITHA
   Dept: CSE
   Year: THIRD
""" 
    s_cgpa=float(input("enter cgpa : "))
    match s_cgpa :
        case s_cgpa if s_cgpa < 8.0 : 
            print("{self.s_name}is not scholarship student") 
        case _ : 
            print("{self.s_name} is scholarship student")

"""  OUTPUT:          
    enter cgpa : 8.0
    SHEVITHA is scholarship student
"""

    def exception(self,s_name):
        return s_cgpa+.0
    try:
        cgpa=str
    except Exception:
        print("cgpa cannot be string")

s=Database("SHEVITHA","CSE","THIRD",8)
s.student1_profile()

#MATH INBUILD FUNCTION
import math
print(math.floor(8.7))
print(math.factorial(20))
print(math.cos(25))
print(math.sin(0))
print(math.tan(20))
print(math.gcd(10,1))
print(math.log(2))

"""OUTPUT:
8
2432902008176640000
0.9912028118634736
0.0
2.237160944224742
1
0.6931471805599453 
"""
#DAYTIME INBUILD FUNCTION
from datetime import date
today=date.today()
print("today date :",today)

""" OUTPUT:
today date : 2024-03-17
"""

