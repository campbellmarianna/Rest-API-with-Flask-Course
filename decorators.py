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

my_function()
