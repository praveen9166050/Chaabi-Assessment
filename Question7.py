# Q7. Calculate the factorial of a number using lambda function.

fact = lambda n: 1 if n <= 1 else n * fact(n - 1)

print(fact(6))