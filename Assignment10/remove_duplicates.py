def remDup(li):
    output=[]
    for ele in li:
        if ele not in output:
            # output.append(ele)
            output=output+[ele]
    return output    
li=[10,14,18,14,10,18]
res=remDup(li)
print(res)    