area_wall=float(input("enter the area of wall:"))
cost_Interior=float(input("Enter the cost of interior wall:"))
cost_Exterior=float(input("enter the cost of exterior wall:"))

Total_interior_area=4*area_wall
Total_exterior_area=4*area_wall

Total_cost_int=Total_interior_area*cost_Interior
Total_cost_ext=Total_exterior_area*cost_Exterior
Total_cost=Total_cost_int+Total_cost_ext

print("Total interior area:",Total_interior_area)
print("Total Exterior area:",Total_exterior_area)
print("cost of interior:",Total_cost_int)
print("cost of exterior:",Total_cost_ext)
print("Total cost of both is:",Total_cost)