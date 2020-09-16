'''
Input: a List of integers
Returns: a List of integers

'''

# at every index we multiply all the other numbers
# except the number at the index
# touch every number in the list
# return a list of products

# when iterating over the input array, the expected value at the current
# iteration index needs to be the product of every number except at the
# current iteration index

# while loop where the base case is when counter == len(arr)
# while lop keeps iterating through for loop
# for loop through the array multiplying all the numbers except for
# the one at index counter. Append those to a list
# everytime you loop through the numbers you incremement counter by 1
# setting if x is == to the last element x[-1] in the array you incremeent counter
# may need to append the product as a variable to a list
# return the list of products
#

def product_of_all_other_numbers(arr):
    # Your code here
    counter = 0
    products = []
    result = 1
    while counter != len(arr)-1:
        for i, x in enumerate(arr):
            if arr[i] == arr[counter]:
                continue
            if i == len(arr)-1:
                result *= x
                products.append(result)
                result = 1
                counter += 1
            else:
                result *= x
    for i, x in enumerate(arr):
        if arr[i] == arr[counter]:
            products.append(result)
            continue
        if i == len(arr)-1:
            result *= x
            products.append(result)
            result = 1
            counter += 1
        else:
            result *= x
    
    return products

    # counter = 0
    # products = []
    # result = 1
    # while counter <= len(arr):
    #     for i, x in enumerate(arr):
    #         if arr[i] == arr[counter]:
    #             continue
    #         if arr[i] == len(arr):
    #             result *= x
    #             products.append(result)
    #             result = 1
    #             counter += 1
    #         else:
    #             result *= x



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    # for x in arr:
    #     for y in arr:
    #         if arr[x] == arr[y]:
                
    #         x * y

    #     if x == 0:
    #         arr[x:] * arr[x:]
    #     elif x == len(arr):
    #         arr[:x]

    #     return arr