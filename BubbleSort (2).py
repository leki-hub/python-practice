def bubble_sort(nums):
    # We set swapped to True keeps running infinitely
    swapped = True
    while swapped:
        swapped = False #This is a flag, that stop the loop from running infinitely if all options are used.
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True #Is set True to keep looping to the last option.

# Verify it works
random_list_of_nums = [5, 2, 9, 1, 5, 6]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
