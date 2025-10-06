# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.

divisible = [x for x in range(1, 1001) 
             if True in [x % y == 0 
                         for y in range(2, 10)]]
print(divisible)

