#Luluh Almogbil
'''
## Bonus

### Sum of Even Numbers

Write a Python program that prompts the user for a positive integer `n`, and then calculates the sum of all even numbers between 1 and `n`, inclusive.

Your program should use a loop (either a `for` loop or a `while` loop) to iterate over the numbers between 1 and `n`, and only add the even numbers to the sum.

For example:

```
Enter a positive integer: 10
The sum of even numbers between 1 and 10 is 30.
```

In this example, the even numbers between 1 and 10 are 2, 4, 6, 8, and 10, and their sum is 30.
'''


while True:
    n = int(input("Please enter a number and make sure it is positive : "))
    if n > 0:
        break
    else:
        print("Please enter a POSITIVE number")

total=0
for number in range (1,n + 1):
    if number % 2 == 0:
        total+=number

print("The sum of even numbers between 1 and",n,"is",total)







