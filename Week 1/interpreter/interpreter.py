expression = input("Expression: ")
#convert this into variables
x,y,z = expression.split(" ")
#changing the type of variable to float
new_x = float(x)
new_z = float(z)

#calculating the result
if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z
print(round(result,1))

