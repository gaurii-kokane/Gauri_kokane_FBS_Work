#convert time into seconds
h=int(input("enter Hours:"))
min=int(input("enter Minutes:"))
sec=int(input("enter Seconds:"))
Hour_sec=h*3600
min_sec=min*60
Total_hours=Hour_sec+min_sec+sec
print("Total Hours is :",Total_hours)