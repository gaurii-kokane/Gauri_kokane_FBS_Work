#Python Program to Detect if Two Strings are Anagrams 

str1='abbcc'
str2='abcbc'

if(len(str1)==len(str2)):
    di={}
    for i,j in zip(str1,str2):
        if i in di:
            di[i]=di[i]+1
        else:
            di[i]=1

        if j in di:
            di[j]=di[j]-1
        else:
            di[j]=-1
    print(di)
    for val in  di.values():
        if(val!=0):
            print('Strings are not anagrams')
    else:
        print('Strings  are anagrams')    



