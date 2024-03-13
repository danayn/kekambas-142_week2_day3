nums = [1, 3, 5, 7, 8]

def ret_negative(nums): # Defining the function
    output = []
    for i in nums:
        if i > 0:
            i = i * -1
            output.append(i)
    
    print(output)