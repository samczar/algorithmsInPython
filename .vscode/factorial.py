def factorial(index):
    if(index < 1):
        return 0
    else:
        return index + factorial(index - 1)


print(factorial(4))
