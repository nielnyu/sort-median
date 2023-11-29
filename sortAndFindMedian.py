#pseudocode
def sortAndFindMedian(numbers):
    numbers = mergeSort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return ((numbers[int(n/2) - 1] + numbers[int(n/2)]) / 2)
    else:
        return numbers[n//2]
    

# mergesort function
def mergeSort(numbers):
    n = len(numbers)
    #base case of 1
    if n <= 1:
        return numbers
    
    # get mid of the list
    mid = n//2
    left_array = mergeSort(numbers[:mid]) #partition list into 0 to mid-1 
    right_array= mergeSort(numbers[mid:]) #partition list into mid to n

    return merge(left_array, right_array) #call merge function on partition

#merge function to sort numbers
def merge(left, right):
    #return result
    result = []
    # while left and right is not none
    while len(left) != 0 and len(right) != 0:
        #if left is smaller append to result
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        #if right is smaller append to result
        else:
            result.append(right[0])
            right.pop(0)

    #this is if right was smaller than left. right is empty, so we need to append left into result
    while len(left) != 0:
        result.append(left[0])
        left.pop(0)

    #if left was smaller than right. left is empty, so we need to append right into result
    while len(right) != 0:
        result.append(right[0])
        right.pop(0)

    return result


print("Test Cases:")
print("Test Case 1: [5, 2, 8, 1, 7, 3, 9, 4, 6, 10]: ",sortAndFindMedian([5, 2, 8, 1, 7, 3, 9, 4, 6, 10]))
print("Test Case 2: [56, 12, 98, 34, 72]: ",sortAndFindMedian([56, 12, 98, 34, 72]))
print("Test Case 3: [-27, 5, 41, -12, 0, 37, 19, 20]: ",sortAndFindMedian([-27, 5, 41, -12, 0, 37, 19, 20]))


user_input = input("Please input a list: (Ex input: 1,12,3 ) DO NOT enter with [] (Ex: [1,12,3]): ")
user_clean = user_input.split(',')
user_list = []
#user_input is a string, User_clean is a list of strings, we need to convert into list of numbers
for i in user_clean:
    user_list.append(int(i))
print("Your list", user_list, ": ", sortAndFindMedian(user_list))