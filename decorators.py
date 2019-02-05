# decorators - a function that gets called before another function
import functools # decorators is going to use this library so that allows us to use these methods

def my_decorator(func): # the decorator should always call the function
    @functools.wraps(func)
    def function_that_runs_func():
        print("I'm the decorator!")
        func() # pass in as a parameter
        print("After the decorator!")
    return function_that_runs_func # extends the func() with some stuff before it and some stuff after

@my_decorator # apply the decorator to my_function
def my_function(): # changes the function
    print("I'm the function!")

# my_function()

##
# This is something we can do in python - develop functions inside functions, 3 levels of defining functions it doesn't go any deeper
def decorator_with_arguments(number):
    def my_decorator(func): # this is the decorator that creates the wrap function - that tells us that the function below is going to replace the my_function_too function
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs): # your decorators should alaways have parameters
            print("In the decorator!")
            if number == 56: # example if the function is the admin page, if the user doesn't have the appropiate permission we don't show the admin page
                print("Not running the function!")
            else:
                func()
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator

# a more complex decorator can except arguments itself
@decorator_with_arguments(56) # example: insert elements into an database
def my_function_too(x, y):
    print(x + y )

my_function_too(57, 67)
