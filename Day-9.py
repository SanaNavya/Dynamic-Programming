##To write a python program which prints the sum of the numbers in an array and if the sum of the array is equal to the target it rturns the index
def check_sum_target(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False
target=1
arr=[1,2,3,4,5,6]
print(check_sum_target(arr,target))


###sliding window

def findAllIndices(nums, k, target):
    n = len(nums)
    currTotal = sum(nums[:k])
    result = []
    if currTotal == target:
        result.append(0)
 
    left, right = 0, k 
    while right < n:
        currTotal -= nums[left]
        currTotal += nums[right]
        if currTotal == target:
            result.append(left + 1)
        left += 1 
        right += 1 
    return result
 
nums = [10, 2, 3, 43, 2, 10, 35, 3]
k = 3 
target = 48
result = findAllIndices(nums, k, target)
print(result)


###


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        result = []
        store = []
        
        #[300, 20, 80, 90, 150]
        # k = 4
        # [0, 1, 2, ]
        
        for i in range(k):
            # step-2 (eliminate all smaller elements indices)
            while store and nums[store[-1]] <= nums[i]:
                store.pop()
    
            # step-3 (insert current index)
            store.append(i)
        
        result.append(nums[store[0]])
        
        
        left, right = 0, k
        while right < n:
            # step-1 (eliminate unwanted indices)
            if store and store[0] == left:
                store.pop(0)

            # step-2 (eliminate all smaller elements indices)
            while store and nums[store[-1]] <= nums[right]:
                store.pop()

            # step-3 (insert current index)
            store.append(right)
            result.append(nums[store[0]])
            left += 1 
            right += 1 
            
        return result
