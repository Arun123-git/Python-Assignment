#list1=[12,13,15,16,19,20,30,50,60,61,62]
#for item in  list1 :
#    if item % 2 ==0 : 
 #       print(f"{item} is even number")
     #  else :
#     print(f"{item} is odd number")


#for i in range(1,11):
#    if i==5:
#        continue
#    print(i)

#for i in range (1,11):
#    if i==6:
#        break
#    print(i)

#n= int(input("enter the number"))
#for i in range(1,11):
#    print(f"{n} X {i}={n*i}" )

#print 1 to 100
#for i in range (1,101):
#    print(i)   


#print only even number between 1 to 10
#for i in range (1,11):
#    if i%2 == 0:
#        print(i)

'''
Question 2: Write a Python program to find the sum of all numbers from 1 to 100 using a for
loop.

total = 0
for i in range (1,101):
    total = total + i
    print(total)
'''

''' 
Question 3: Write a Python program to print the multiplication table of a given number using a
for loop.

n = int(input("Enter the no. = "))
for i in range (1,11) :
    print(f"{n} X {i} = {n*i}")

'''

'''
Question 4: Write a Python program to count the number of even and odd numbers from a
series of numbers using a for loop.
Hint: Find even and odd from this list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = 0 
odd = 0
for i in table:
    if i % 2==0:
        even = even + 1    
    else:
        odd = odd +1
        
print(even)
print(odd)
'''

'''
Question 5: Write a Python program to find the factorial of a number using a for loop.

n= int(input("Enter the no. = "))
fact = 1
for i in range (1,n):
    fact = fact * i
    print(fact)
'''

'''
Question 7: Write a Python program to check if a given number is prime or not using a for loop.

n= int(input("Enter the no. = "))
for i in range (2,n-1):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
    else:
        print(f"{n} is prime number")
        '''

'''
Question 8: Write a Python program to find the largest element in a list using a for loop.


num= [88,2,56,103,4,49,100]
largest= num[0]
for i in num:
    if i> largest:
     largest= i
    print(largest) 
    '''
'''
Question 9: Write a Python program to reverse a given string using a for loop.

text = "PythoN"
reversed_text = ""

for i in text:
    reversed_text = i + reversed_text
    print(reversed_text)
       '''


'''
Question 10: Write a Python program to find the common elements between two lists using a
for loop.
List1 = [1,2,3]
List2 = [4,5,1]
'''

list1 = [1,2,3]
list2 = [4,5,1]
common = []
for i in list1:
    for j in list2:
        if i == j :
            common.append(i)
            print(common)