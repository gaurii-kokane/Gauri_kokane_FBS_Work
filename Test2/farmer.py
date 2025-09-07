import math
radius = 20
rect_length = 50
rect_breadth = 40
cost_per_m = 35
wire_layers = 5
# calculate half-circle + rectangle perimeter
half_circle = math.pi * radius
perimeter = half_circle + rect_length + 2 * rect_breadth

total_length = perimeter * wire_layers
total_cost = total_length * cost_per_m

if total_cost > 0:
    print("Total fencing cost = Rs.", round(total_cost, 2))
else:
    print("Calculation error")
