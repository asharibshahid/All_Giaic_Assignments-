class logger:
    def __init__(self):
        print("Logger Is Created")
    def __del__(self):
        print("Logger Is Destroyed")

result = logger()            
print(result)