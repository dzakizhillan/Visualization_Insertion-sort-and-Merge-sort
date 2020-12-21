from time import sleep
import numpy as np


test = False

class Array:

    full_array = None

    def stack_it(self):
        to_stack  = np.array(self.values)
        if not np.array_equal(to_stack, self.pile[-1]):
            self.pile = np.vstack((self.pile, np.array(self.values)))
        
    def set_all(self, values):
        for i in range(len(self.values)):
            self.values[i] = values[i]
            self.stack_it()
        for i in range(len(self.values)):
            Array.full_array[self.lower_index + i] = values[i]
            self.stack_it()
            

    def __init__(self, values, lower_index=0):
        self.lower_index = lower_index
        self.values = list(values)
        
        self.pile = np.array(self.values)
        if Array.full_array == None:
            Array.full_array = list(values)

    def swap(self, index1, index2):
        self.values[index2], self.values[index1] = self.values[index1], self.values[index2]
        Array.full_array[self.lower_index + index2], Array.full_array[self.lower_index +
                                                                      index1] = Array.full_array[self.lower_index + index1], Array.full_array[self.lower_index + index2]
        self.stack_it()

    def set(self, index, num):
        self.values[index] = num
        Array.full_array[self.lower_index + index] = num
        self.stack_it()

    def get_len(self):
        return len(self.values)


def insertion_sort(nums):  # n^2
    # Start on the second element as we assume the first element is sorted
    for i in range(1, nums.get_len()):
        item_to_insert = nums.values[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums.values[j] > item_to_insert:
            nums.set(j + 1, nums.values[j])
            j -= 1
        # Insert the item
        nums.set(j + 1, item_to_insert)


def merge_sort(nums, lower_index=0):  # n * logn
    def merge(left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        # We use the list lengths often, so it's handy to make variables
        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                # We check which value from the start of each list is smaller
                # If the item at the beginning of the left list is smaller, add it
                # to the sorted list
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                # If the item at the beginning of the right list is smaller, add it
                # to the sorted list
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            # If we've reached the end of the of the left list, add the elements
            # from the right list
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            # If we've reached the end of the of the right list, add the elements
            # from the left list
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list

    # If the list is a single element, return it
    if nums.get_len() <= 1:
        return nums.values

    # Use floor division to get midpoint, indices must be integers
    mid = nums.get_len() // 2

    # Sort and merge each half
    left_list = merge_sort(Array(nums.values[:mid], lower_index))
    right_list = merge_sort(Array(nums.values[mid:], mid), mid)

    nums.set_all(left_list + right_list)

    # Merge the sorted lists into a new one
    sorted_list = merge(left_list, right_list)

    nums.set_all(sorted_list)
    return sorted_list


