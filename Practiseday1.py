

def maximum(word,n,index,result):
    if index==n:
        print("vowel count is:",result)
        return
    vowels="aeiouAEIOU"
    if word[index] in vowels:
        result+=1
    maximum(word,n,index+1,result)
word=input()
maximum(word,len(word),0,0)    



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



###practise problem
#write a python program to accept a list of integers and print the sum of all 5 divisible numbers using recursion


def Sum(n,number,index,result):
    if index==n:
        print("The sum is:",result)
        return
    if number[index]%5==0:
        result+=number[index]
    Sum(n,number,index+1,result)
    return    
number=list(map(int,input("Enter the list:").replace(','," ").split()))
n=len(number)
Sum(n,number,0,0)


#write a python program to print all even indexed numbers in the given list left and right using recursion function.

def Even(n,number,index,result):
    if index==n:
        print("The result is:",result)
        return
    if index%2==0:
        result+=number[index]
    Even(n,number,index+1,result)
    return
number=list(map(int,input().replace(','," ").split()))
n=len(number)
Even(n,number,0,0)        
'''

 
# Child function to parent function
def findSum(index, nums, n):
	if index == n:
		return 0 
	nextEleSum = findSum(index + 1, nums, n)
	if nums[index] % 5 == 0:
		nextEleSum += nums[index] 
	return nextEleSum
 
# parent function to child function 
def findSum2(index, nums, n, result):
	if index == n:
		print("Sum is:", result)
		return 
	if nums[index] % 5 == 0:
		result += nums[index]
	findSum2(index + 1, nums, n, result)
 
 
 
	[10, 11, 12, 13, 14, 15]
	 0.  1.  2.   3.  4.  5 
	even indices: 0, 2, 4 
	odd indices: 1, 3, 5 
 
def printLeftToRight(index, nums, n):
	if index == n:
		return 
 
	if index % 2 == 0:
		print(nums[index])
	printLeftToRight(index + 1, nums, n)
 
def printLeftToRightBetterOne(index, nums, n):
	if index >= n:
		return 
 
	print(nums[index])
	printLeftToRightBetterOne(index + 2, nums, n)
 
def printRightToLeftBetterOne(index, nums, n):
	if index >= n:
		return 
 
	printLeftToRightBetterOne(index + 2, nums, n)
	print(nums[index])
printLeftToRight(0, nums, len(nums))
 
 
 
def printRightToLeftInReverseManner(index, nums, n):
	if index < 0:
		return 
	print(nums[index])
	printRightToLeftInReverseManner(index - 2, nums, n)
 
 
 
n = len(nums)
if n % 2 == 0:
	printRightToLeftInReverseManner(n - 2, nums, n)
else:
	printRightToLeftInReverseManner(n - 1, nums, n)
 


'''