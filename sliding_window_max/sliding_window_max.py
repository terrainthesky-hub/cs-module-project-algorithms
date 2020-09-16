'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#what if k is larger than the list of nums
# does the returned array need to be sorted
#window shouldn't exceed array length, so moving only so many
# moves one index over each time with total window size not to exceed array length
# finds the max of each window
# append the max to a list
# shift window

def sliding_window_max(nums, k, products=[], counter=0):
    # Your code here
    window = k
    if counter < (len(nums) - k + 1):
        list1 = nums[counter:window]
        products.append(max(list1))
        counter += 1
        return sliding_window_max(nums, k, products, counter, window + 1)
    return products


    
l = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
sliding_window_max(l, k)
'''
    Solution that utilizes a Queue
    We'll maintain the invariant that the front element of the Queue will be the max value of the window at all times
    O(n) time, O(k) space
    '''
    from collections import deque
    maxs = []
    q = deque()
    for i, n in enumerate(nums):
        # remove elements from the Queue so long as the current number is greater that the element
        while len(q) > 0 and n > q[-1]:
            q.pop()
        # add the number once all smaller numbers have been evicted from the Queue
        q.append(n)
        # calculate the window range 
        window = i - k + 1
        # so long as the window's range == k, we'll add elements to the Queue
        if window >= 0:
            # add the max element, in this case the first element in the Queue, to the output List 
            maxs.append(q[0])
            # check if the number on the left side of the window is going to be evicted in the next iteration
            # if it is, and if that value is at the front of the Queue, we need to evict it from the Queue
            if nums[window] == q[0]:
                q.popleft()
    return maxs
    # counter = 0
    # n = k    
    # if counter <= (len(nums) - n):
    #     list1 = nums[counter:k]
    #     max(list1)
    #     counter += 1
    #     sliding_window_max(nums, k+1)



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
