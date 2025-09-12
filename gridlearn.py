""" Grid is actually 2D containing rows and coloumns basically can be made by list """

grid = [
    [" "," "," "],
    [" ","O"," "],
    [" "," "," "]
]

print(grid)  #This will print with brackets and in a single line
# To print in a string formatwe have to use loop
print("-"*50)
for x in grid:
    print("".join(x))    # this is used for string 