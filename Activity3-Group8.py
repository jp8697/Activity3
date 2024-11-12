"""
Activity 3 - Creating a Search and Sort Pipeline - Group 8
by Yahya Kaddoura, Julian Pascher and Georgii Terzi
This code aims to fullfill all the necessary rubrics present in Activity 3 including the required Refelection.
"""
import random
import time
"""
Phase 1: Data Generation and Sorting
In this phase we will create  the generate_sorted_data function with the parameter size that generates an array
of random integers which is then sorted with the insertion sort method
"""
#Generate List with Random Data 
def generate_sorted_data(size):
    list_1 = []
    #Fill empty list with random numbers
    for i in range (0, size):
        list_1.append(random.randint(1,100))
    print("Unsorted list", list_1)
    insertion_sort(list_1)
    return list_1

#FUnction for Insertion Sort
def insertion_sort(list):
    for i in range (len(list)):
        j = i
        while list[j-1] > list[j] and j > 0:
            list[j-1], list[j] = list[j], list[j-1]
            j -= 1
    print("Sorted List using Insertion Sort", list)
    return list
"""
Phase 2: Implement Binary Search on Sorted Data
In this phase we will find the index of one target element in the list generated in Phase 1
with the help of Binary Search
"""
#Function with Binary Search that is also called in Phase 4
def binary_Search(list, start, end, target):
    if start > end:
        return None
    mid = (start+end)//2
    if list[mid] == target:
        return mid
    elif list[mid] < target:
        return binary_Search(list, mid + 1, end, target)
    else:
        return binary_Search(list, start, mid - 1, target)
    
"""
Phase 3: Recursive Merge Sort for Large Data
The generate_sorted_data function is reused except instead of calling the insertion sort function we are now 
calling the merge sort function to accomodate the increased size of the list
"""
def generate_sorted_data_large(size_1):
    list_2 = []
    #Fill empty list with random numbers
    for i in range (0, size_1):
        list_2.append(random.randint(1,100))
    print("Unsorted large list", list_2)
    merge_sort(list_2)
    print("Large List sorted using Merge Sort", list_2)
    return list_2

#Function for merge sort
def merge_sort(list):
    if len(list) > 1:
        left_list = list[:len(list)//2]
        right_list = list[len(list)//2:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = 0 
        j = 0 
        k = 0 

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i +=1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1
        
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1
"""
Phase 4: Performance Comparison
In Phase 4 we will compare the time linear search and binary search need to find the same target element in a large datastructure
The linear search function also needs to be written as it was not yet used 
"""
def Performance(target_1, list_2):
    #Time linear Search
    time_begin = time.perf_counter()
    linear_search(target_1, list_2)
    time_end = time.perf_counter()
    print(f"Linear Search needs {time_end-time_begin}")
    
    #Time binary search
    time_begin_1 = time.perf_counter()
    mid = binary_Search(list_2,0 , len(list_2), target_1)
    if mid == None:
        print("Target not found")
    else:
        print(f"Using Binary Search: Target {target_1} first found at index {mid}")
    time_end_1 = time.perf_counter()
    print(f"Binary Search needs {time_end_1 - time_begin_1}")

#Function for linear search 
def linear_search(target_1, list):
    for i in range (len(list)):
        if list[i] == target_1:
            print(f"Using Linear Search: Target {target_1} fist found at index {i}")
            break
    else:
        print("Target not found")
       
"""
Organization of Phases:
Phase 2 can not be used without Phase 1
Phase 4 can not be used without Phase 3
"""
def organization():
    def Phase_1_and_2():
        #Phase 1
        size = int(input("Enter the size of the list (small: < 100): "))
        list_1 = generate_sorted_data(size)
        #Phase 2
        target = int(input("Enter the value you want to find: "))
        mid = binary_Search(list_1, 0, len(list_1), target)
        if mid == None:
            print(f"{None}, as it is not in the list")
        else:
            print(f"Result found on index {mid} using Binary Search")
    def Phase_3_and_4():
        #Phase 3
        size_1 = int(input("Enter the size of the list (large: > 500): "))
        list_2 = generate_sorted_data_large(size_1)
        #Phase 4
        target_1 = int(input("Enter the target value: "))
        Performance(target_1, list_2)

    
    return Phase_1_and_2, Phase_3_and_4
def main():
    Phase_1_and_2, Phase_3_and_4 = organization()
    # Uncomment to call 
    # Phase_1_and_2()
    # Phase_3_and_4()
    

if __name__ == "__main__":
    main()


