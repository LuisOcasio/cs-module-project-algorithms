'''
Input: a List of integers
Returns: a List of integers
'''
# move each non-zero integer to the left side of the array

# return altered array


def moving_zeroes(arr):

    #     # Your code here
    #     for i in arr:
    #         print('inidividual', i)
    #         if i > 0:
    #             arr.slice()
    #             print('sliced', i)
    insert_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_index] = arr[i]
            insert_index += 1
    for i in range(insert_index, len(arr)):
        arr[i] = 0

    return arr


moving_zeroes([0, 3, 1, 0, -2])

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
