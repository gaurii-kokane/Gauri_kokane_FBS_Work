#Write a program of having n number of elements in the list and find out even 
# and odd elements in that list and then create two separate lists which will have  
# even elements and other will have odd elements. 

numbers = [1, 2, 3, 4, 5, 6]
even = [] 
odd = [] 
for n in    numbers: 
    if n % 2 == 0: 
        even.append(n) 
    else:
        odd.append(n) 
print("Even:", even)
print("Odd:", odd)