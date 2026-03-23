#Function to find the pair of numbers in a sorted array that sum target value

#This code uses the two-pointer technique to find two numbers in a sorted array that sum to a target.
It starts with one pointer at the beginning and one at the end of the array.
Based on the sum, it moves the left pointer forward or the right pointer backward.
The algorithm is efficient with O(n) time and O(1) space complexity.


def two_pointer(arr,target):
    left = 0
    right = len(arr)-1
    while left < right:
        sum = arr[left]+arr[right]
        if sum == target:
            return arr[left],arr[right]
        elif sum<target:
            left+=1
        else:
            right-=1
    return None    
arr=[1,2,3,5,7,10,11,15]
target = 15
print(two_pointer(arr,target))
     