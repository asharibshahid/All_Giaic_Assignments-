def Log_Function(func):
    def wrapper():
        print("Function is called")
        return func()
    return wrapper

@Log_Function 
def my_function():
    print("Hello, World!")


my_function()    