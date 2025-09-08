basic=int(input("enter the salary:"))
total=0
for  i  in  range(basic):
    if basic>20000:
        total+= basic+0.10*basic
        total+=basic+0.12*basic
        total+=basic+0.15*basic
else:
    total+=basic+0.15*basic
    total+=basic+0.18*basic
    total+=basic+0.20*basic
total_salary=0    
print("Total salary:",basic) 

