def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False #The "swapped = False" statement is used to set a flag that indicates whether any swaps were made during the latest pass through the list.If no swaps were made, it means that the list is already sorted and there is no need to continue iterating through it. 
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i] # Thi sline swaps the elements in the given indexes
                # Set the flag to True so we'll loop again
                swapped = True 
# Verify it works
random_list_of_nums = [5, 2, 9, 1, 5, 6]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)