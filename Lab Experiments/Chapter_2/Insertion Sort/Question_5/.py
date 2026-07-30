import random

def insertion_sort_count_shifts(arr):
    """
    Sorts an array using insertion sort and counts the number of shifts.
    """
    # Create a copy so we don't modify the original list in-place during tests
    sorted_arr = arr.copy() 
    shifts = 0
    
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        
        # Move elements of sorted_arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            shifts += 1
            j -= 1
            
        sorted_arr[j + 1] = key
        
    return sorted_arr, shifts

# --- Test Cases from the Image ---

# 1. Nearly Sorted Data
log = [18.2, 18.5, 18.9, 17.9, 19.1, 19.4, 19.0]
sorted_log, shifts_nearly = insertion_sort_count_shifts(log)

# Verify the sort was successful
assert sorted_log == sorted(log)

# 2. Randomly Shuffled Data
shuffled_log = log.copy()
random.seed(42) # Seed added for consistent output in this example
random.shuffle(shuffled_log)
_, shifts_random = insertion_sort_count_shifts(shuffled_log)

# Output Results
print("Input Log (Nearly Sorted):", log)
print("Corrected Sorted Log:     ", sorted_log)
print("Input Log (Shuffled):     ", shuffled_log)
print("-" * 50)
print('Nearly-sorted shifts:', shifts_nearly, '| Random shifts:', shifts_random)
print('All test cases passed!')
