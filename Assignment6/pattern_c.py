for i in range(1, 5):         
    print(" " * (5- i), end="")  
    val = 1
    for j in range(1, i + 1):  
        print(val, end=" ")
        val = val * (i - j) // j  
    print()


    
