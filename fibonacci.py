def fibonacci(index):
    if(index < 3):
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


print(fibonacci(7))
