'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    count = 0
    pop_arr = []
    for i, x in enumerate(arr):
        if x == 0:
            pop_arr.append(i)
            count += 1
    for i in reversed(pop_arr):
        arr.pop(i)
    arr.extend([0] * count)

    return arr
    # Your code here
    # for x in len(arr)-1:
    #     if arr[x] == 0:
    #         moving_zeroes(arr[x+1], arr[x] = arr[x+1], arr[x])
        



    # for x in arr:
    #     while arr[x] is not arr[-1]:
    #         while arr[x+1] < 0 or arr[x+1] > 0:
    #             arr[x+1], arr[x] = arr[x], arr[x+1]
    #             if arr[x+1] == 0:
    #                 arr[x], arr[x+2] = arr[x+2], arr[x]
            
        # else:
        #     return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]
    print(arr[:3])

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")