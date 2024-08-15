# define a function that retunrs the maximum of two numbers
def max_of_two(x,y):
    # check if x is greater than y
    if x > y:
        # if x is greater, return x
        return x
    # if y is greater than x, return y
    return y

# define a function that retunrs the maximum of three numbers
def max_of_three(x,y,z):
    # call max_of_two function to find the maximum of y and z,
    # then compare it with x to find the overall maximum
    return max_of_two(x, max_of_two(y, z))
# print the result of calling max_of_three function with arguments 3, 6, and -5
print(max_of_three(3, 6, -5))