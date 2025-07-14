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

