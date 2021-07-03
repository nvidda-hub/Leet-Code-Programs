# class Student:
#     no_of_leaves = 10
#
#     def __init__(self, sname, srole, sage):
#         self.name = sname
#         self.age = sage
#         self.role = srole
#
#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split('-'))
#
#     def print_details(self):
#         return f"{self.name}, {self.age} and {self.role}"
#
#
# class Player(Student):
#     no_of_leaves = 15
#
#     def __init__(self, sname, srole, sage, sgame):
#         super(Player, self).__init__(sname, srole, sage)
#         self.game = sgame
#
#     def print_details(self):
#         return f"{self.name}, {self.age} and {self.role}. He playes {self.game}"
#
# s1 = Student.from_dash("Narendra-25-student")
# p1 = Player.from_dash("Yadav-25-student-Cricket")
# print(p1.print_details())
import json

import requests
response = requests.get('https://api.postalpincode.in/pincode/110001')

x = response.json()[0]['PostOffice']

pincode_ls = []
for ele in x:
    pincode_ls.append(ele['Pincode'])

print(pincode_ls)