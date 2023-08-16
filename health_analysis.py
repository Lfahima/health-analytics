import pandas as pd
import numpy as np

a = 5
print("a is : ", a)
b = "this is difficult"
print("b is : ", b)
c = ["red", "yellow", "blue"]
print("c is : ", c)
d = {   
    "name": "Fahima",
    "fav_num": [25, 26, 27],
    "fave_food": {"one": "pizza", "two": "icecream"} 
}
print("d is : ", d)

def my_function(y,z):
    if y > z:
        return("y wins!")
    else:
        return("z wins!")


print("this is a project")

my_first_function = my_function(100, 101)
print("winner is : ", my_first_function) 

