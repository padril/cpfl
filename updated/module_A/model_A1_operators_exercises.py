from model_problem import ModelProblem
import re

def threshold(score: float):
    if score >= 0.999:
        return "Congradulations! You got everything right!"
    else:
        return f"You got {score * 100:.0f}% of the questions correct, keep trying!"

# model notebook needs:
# solution functions
# prep functions (which create lists of arguments for the solution + student functions)
# model functions (which instantiate the ModelProblem class and run the tests)

## SOLUTIONS ##
# same format as student functions, but return the correct answer
give_me_the_password = True
q1 = 9 % 2
q2 = 9 // 2
q3 = 9.0 % 2
q4 = 9 // -2
q5 = 5 + 017
q6 = 60 * (24.95 * 0.6) + 3 + 0.07 * 59
q7 = 4 * 60
q8 = 10 * 10.0
q9 = (10 * 3) % 5
q10 = 4.0 % 2
# ## Question 10
# 
# What is the output of these calculations?
# 
# ```python
# 4.0%2
# ```
# 
# Store your answer in a variable called `q10`

# ## Question 11
# 
# What is the data type of the following value: `"Linguistics is cool"`  
# Please assign your answer as a String variable to `q11`.
# E.g. `q11 = "int"`
# 
# The possible answers are "str", "int", "bool", "float", and "NoneType".

# ## Question 12
# 
# What is the data type of the following value: `False`  
# Please assign your answer as a String variable to `q12`.
# 
# E.g. `q12 = "int"`
# 
# The possible answers are "str", "int", "bool", "float", and "NoneType".

# ## Question 13
# 
# Consider a variable that represents the total cost of a shopping trip in dollars and cents.
# 
# What type should its value be?
# 
# NOTE: Please assign your answer as a String variable to `q13`. 
# E.g. `q13 = "int"`
# 
# The possible answers are "str", "int", "bool", "float", and "NoneType".

# ## Question 14
# 
# Combine the integer `7`and the string `'years'` into a string `'7years'` stored in a variable called `q14`.

# ## Question 15
# 
# Convert the value in `number` into an integer and store it in a variable `integer`, then convert the value in `integer` into an integer and store it in a variable `q15`.
# 
# ```Python
# number = -4.3
# ```


## PREP ##
# return format is list of tuples with the first element being the list of args (can be partial)
# and the second element being the visibility of the tests connected to that list of args
# (if the list of args in the prep fuunction is only partial, the remaining arguments need to be specified
# in extra_sfunc_args and extra_model_args when initializing the ModelProblem class)

def model_give_me_the_password_prep():
    return [([], True)]

## Tests ##
def model_give_me_the_password(student_func):
    model = ModelProblem(model_give_me_the_password_prep, give_me_the_password, student_func, is_var=True)

    return model.run_basic_tests(err_num=False)

#!/usr/bin/env python
# coding: utf-8

