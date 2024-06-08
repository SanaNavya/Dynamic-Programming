##write a python program to accept an integer as input and print the valid balanced parenthesis of size N>
def printThis(n, result, openOnes, closedOnes):
    if closedOnes > openOnes:
        return
    if openOnes > (n // 2) or closedOnes > (n // 2):
        return
    if len(result) == n:
        print(result)
        return 
 
    printThis(n, result + "(", openOnes + 1, closedOnes)
    printThis(n, result + ")", openOnes, closedOnes + 1)
n = int(input())
printThis(n, "", 0, 0)

##Write a python program to print all possible subsets of a given list. nums = [10, 11, 12, 13, 14]

def findSubsets(i,l,res):
    if i==len(l):
        print(res)
        return
    res.append(l[i])
    findSubsets(i+1,l,res)
    res.pop()
    findSubsets(i+1,l,res)
l=[1,2,3,4,5]
res = []
findSubsets(0,l,res)


###Phone number pattern where 1 will be nothing and 2-abc and wise versa using recursion and backtracking(Leetcoode problem)

store = {}
store["1"] = ""
store["2"] = "abc"
store["3"] = "def"
store["4"] = "ghi"
store["5"] = "jkl"
store["6"] = "mno"
store["7"] = "pqrs"
store["8"] = "tuv"
store["9"] = "wxyz"
class Solution(object):
    def printLetter(self, word, index, result, bigResult):
        if index == len(word):
            bigResult.append("".join(result))
            return 
        ch = word[index]
        for val in store[ch]:
            result.append(val)
            self.printLetter(word, index + 1, result, bigResult)
            result.pop()
    def letterCombinations(self, digits):
        bigResult = []
        if len(digits) == 0:
            return bigResult
        result = []
        self.printLetter(digits, 0, result, bigResult)
        return bigResult
            

            
    