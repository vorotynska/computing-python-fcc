# This is a sorting algorithm that uses the divide-and-conquer 
# principle to sort collections of data. That is, it 'divides' 
# a collection into smaller sub-parts, and 'conquers' the sub-parts 
# by sorting them independently, then merges the sorted sub-parts.

def merge_sort(array):
    # create a base case that stops the function execution when 
    # the length of array is less than or equal to 1
    if len(array) <= 1:
        return

    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    # These variables will help you keep track of each index during 
    # the sorting process.
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0
    while left_array_index < len(left_part) and right_array_index < len(right_part):

        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1

            sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Now, you are going to replicate the same while loop logic for right_part.
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array:')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))