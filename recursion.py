
# To find sum of numbers in the list by Passing data from parent function to child function
def printSum(index, n, nums, result):
    if index == n:
        print("Sum is:", result)
        return 
    result += nums[index]
    printSum(index + 1, n, nums, result)

# To find sum of numbers in the list by Passing data from child function to Parent function
def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]

nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("Sum is:", result)

#To find Maximum number in the list by both child to parent and vice versa

def findMaxInWay1(index, nums, n, result):
    if index == n:
        print("Max ele is:", result)
        return 
    if nums[index] > result:
        result = nums[index]
    findMaxInWay1(index + 1, nums, n, result)
 
nums = [12, 32, 11, 10]
result = findMaxInWay1(0, nums, len(nums), 0)
 
 
def findMaxInWay2(index, nums, n):
    if index == n - 1:
        return nums[index]
    nextGreater = findMaxInWay2(index + 1, nums, n)
    if nextGreater < nums[index]:
        return nums[index]
    return nextGreater 
 
nums = [12, 32, 11, 10]
result = findMaxInWay2(0, nums, len(nums))
print("Max ele:", result)

##To find Minimum number in the list by both child to parent and vice versa

def findMinInWay1(index, nums, n, result):
    if index == n:
        print("Min ele is:", result)
        return 
    if nums[index] < result:
        result = nums[index]
    findMaxInWay1(index + 1, nums, n, result)
 
nums = [12, 32, 11, 10]
result = findMaxInWay1(0, nums, len(nums), 0)
 
 
def findMinInWay2(index, nums, n):
    if index == n - 1:
        return nums[index]
    nextGreater = findMinInWay2(index + 1, nums, n)
    if nextGreater > nums[index]:
        return nums[index]
    return nextGreater 
 
nums = [12, 32, 11, 10]
result = findMinInWay2(0, nums, len(nums))
print("Max ele:", result)


##vowels in given string 

def countVowelsWay1(word, index, n, result):
    if index == n:
        print("Vowels count is:", result)
        return 
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        result += 1 
    countVowelsWay1(word, index + 1, n, result)
word = "navsvasjay"
countVowelsWay1(word, 0, len(word), 0)
def countVowelsWay2(word, index, n):
    if index == n:
        return 0 
    nextVowelsCount = countVowelsWay2(word, index + 1, n)
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        nextVowelsCount += 1 
    return nextVowelsCount
word = "abcdeefuigh"
result = countVowelsWay2(word, 0, len(word))
print("Vowels count is:", result)


##binary string

def printbin(size,result,n):
    if size==n:
        print(result)
        return
    printbin(size+1,result+ '1',n)
    printbin(size+1,result+ '0',n)
n=int(input())
printbin(0,'',n)

###practise problem
#write a python program to accept a list oof integers and print the sum of all 5 divisible numbers using recursion
#write a python program to print all even indexed numbers in the given list using recursion function.

