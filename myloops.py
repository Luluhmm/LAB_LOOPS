#Luluh Amogbil
'''
# LAB_LOOPS


## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. 
Skip the number 100 and break the loop at 205

## 2) Using a while loop and input , do the following :
- Ask the the user : "what is the product of 7 * 24 ?"
- check if the answer is right then exit the loop and print "You answered this Question correctly"
- if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.
'''

#1
numbers = range(45,210)
for num in numbers:# num is the values of numbers(set) in each iteration
    if num == 100:
        continue
    elif num == 206:
        break
    print(num)



print("-"*50)


#2
result = "what is the product of 7 * 24 ?"

while int(input(result)) != 168:
    print("Your Answer is wrong try again..")

else:
    print("You answered this Question correctly")

