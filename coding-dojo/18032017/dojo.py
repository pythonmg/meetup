def FizzBuzz(numero):
    initial = ""
    
    if numero % 3 == 0:
        initial += "Fizz"

    if numero % 5 == 0:
        initial += "Buzz"

    return initial or str(numero)

def FizzBuzzList(n):
    return [FizzBuzz(i) for i in range(1, n + 1)]
