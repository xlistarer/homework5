'''Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers'''
import random
if __name__ == '__main__':
    a=[]
    for i in range(10):
        a.append(random.randint(1, 100))
    print("Max=",max(a))
'''Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers'''
first=[]
second=[]
while(len(first)<10):
    first.append(random.randint(1, 10))
    second.append(random.randint(1, 10))
third=set(first+second)
print(first,"+",second,"=",third)
'''Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration'''
rang=list(range(1,100,1))
res=[]
counter=0
while(counter<len(rang)):
    if rang[counter]%7==0 and rang[counter]%5!=0:
        res.append(rang[counter])
    counter+=1
print("Elements that divisible by 7 but not a multiple of 5:",res)