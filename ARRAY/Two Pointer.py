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
     