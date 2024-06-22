##Longest Common Subsequence

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, str1, str2):
        
        def recursiveApproach(index1, index2):
            if index1 == n or index2 == m:
                return 0 
            elif str1[index1] == str2[index2]:
                return 1 + recursiveApproach(index1 + 1, index2 + 1)
            
            choice1 = recursiveApproach(index1 + 1, index2)
            choice2 = recursiveApproach(index1, index2 + 1)
            return max(choice1, choice2)
            
        cache = [[-1] * m for i in range(n)]
        
        def memoizationApproach(index1, index2):
            if index1 == n or index2 == m:
                return 0 
            elif cache[index1][index2] != -1:
                return cache[index1][index2]
            elif str1[index1] == str2[index2]:
                cache[index1][index2] = 1 + memoizationApproach(index1 + 1, index2 + 1)
                return cache[index1][index2]
            
            choice1 = memoizationApproach(index1 + 1, index2)
            choice2 = memoizationApproach(index1, index2 + 1)
            cache[index1][index2] = max(choice1, choice2)
            return cache[index1][index2]
            
            
        def tabulationApproach():
            cache = [[0] * (m + 1) for i in range(n + 1)]
            for index1 in range(n - 1, -1, -1):
                for index2 in range(m - 1, -1, -1):
                    if str1[index1] == str2[index2]:
                        cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1]
                    else:
                        choice1 = cache[index1 + 1][index2]
                        choice2 = cache[index1][index2 + 1]
                        cache[index1][index2] = max(choice1, choice2)
                    
            return cache[0][0]
            
        return tabulationApproach()
    
##Longest increasing subsequence


class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)

        def recursiveApproach(index, prevIndex):
            if index == n:
                return 0 

            include = 0
            if prevIndex == -1 or nums[prevIndex] < nums[index]:
                include = 1 + recursiveApproach(index + 1, index) 
            exclude = recursiveApproach(index + 1, prevIndex)
            return max(include, exclude)

        # index can range from 0 till n - 1 
        # prevIndex can range from -1 till n - 1 
        cache = [[-1] * (n) for i in range(n + 1)]

        def memoizationApproach(index, prevIndex):
            if index == n:
                return 0 
            elif cache[prevIndex + 1][index] != -1:
                return cache[prevIndex + 1][index]

            include = 0
            if prevIndex == -1 or nums[prevIndex] < nums[index]:
                include = 1 + memoizationApproach(index + 1, index) 
            exclude = memoizationApproach(index + 1, prevIndex)
            cache[prevIndex + 1][index] = max(include, exclude)
            return cache[prevIndex + 1][index]

        def tabulationApproach():
            result = [1] * n 
            finalLis = 1
            for index in range(1, n): 
                for prevIndex in range(index):
                    if nums[index] > nums[prevIndex]:
                        result[index] = max(result[index], result[prevIndex] + 1)
                finalLis = max(finalLis, result[index])
            return finalLis

        return tabulationApproach()
       
##Buy and sell stocks-1

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        minValue = prices[0]
        result = 0
        for index in range(n):
            minValue = min(minValue, prices[index])
            result = max(result, prices[index] - minValue)
        return result       
    
##Buy and sell stocks-2

class Solution(object):
    def maxProfit(self, prices):
        result = 0 
        n = len(prices)
        for index in range(1, n):
            if prices[index] > prices[index - 1]:
                result += (prices[index] - prices[index - 1])
        return result

##Buy and sell stocks -4


class Solution(object):
    def maxProfit(self, K, prices):
        n = len(prices)
        def recursiveApproach(day, k, brought):
            if day == n or k == 0:
                return 0 

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + recursiveApproach(day + 1, k, 1)
                dontBuyNow = recursiveApproach(day + 1, k, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + recursiveApproach(day + 1, k - 1, 0)
                dontSellNow = recursiveApproach(day + 1, k, 1)
                maxProfit = max(sellNow, dontSellNow)

            return maxProfit

        cache = []
        for i in range(n + 1):
            row = []
            for j in range(K + 1):
                col = []
                for r in range(2):
                    col.append(0)
                row.append(col)
            cache.append(row)

        def memoizationApproach(day, k, brought):
            if day == n or k == 0:
                return 0 
            elif cache[day][k][brought] != -1:
                return cache[day][k][brought]

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + memoizationApproach(day + 1, k, 1)
                dontBuyNow = memoizationApproach(day + 1, k, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + memoizationApproach(day + 1, k - 1, 0)
                dontSellNow = memoizationApproach(day + 1, k, 1)
                maxProfit = max(sellNow, dontSellNow)
                
            cache[day][k][brought] = maxProfit 
            return maxProfit

        def tabulationApproach():
            for day in range(n - 1, -1, -1):
                for k in range(1, K + 1):
                    for brought in range(2):
                        maxProfit = 0
                        if brought == 0:
                            buyNow =  -prices[day] + cache[day + 1][k][1]
                            dontBuyNow = cache[day + 1][k][0]
                            maxProfit = max(buyNow, dontBuyNow)
                        else:
                            sellNow = prices[day] + cache[day + 1][k - 1][0]
                            dontSellNow = cache[day + 1][k][1]
                            maxProfit = max(sellNow, dontSellNow)
                        cache[day][k][brought] = maxProfit 
            return cache[0][k][0]

        return tabulationApproach()

##Buy and sell stocks in cool down

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        def recursiveApproach(day, brought):
            if day >= n:
                return 0 

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + recursiveApproach(day + 1, 1)
                dontBuyNow = recursiveApproach(day + 1, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + recursiveApproach(day + 2, 0)
                dontSellNow = recursiveApproach(day + 1, 1)
                maxProfit = max(sellNow, dontSellNow)

            return maxProfit

        cache = []
        for i in range(n + 3):
            row = []
            for j in range(2):
                row.append(0)
            cache.append(row)

        def memoizationApproach(day, brought):
            if day >= n:
                return 0 
            elif cache[day][brought] != -1:
                return cache[day][brought]

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + memoizationApproach(day + 1, 1)
                dontBuyNow = memoizationApproach(day + 1, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + memoizationApproach(day + 2, 0) 
                dontSellNow = memoizationApproach(day + 1, 1)
                maxProfit = max(sellNow, dontSellNow)
                
            cache[day][brought] = maxProfit 
            return maxProfit

        def tabulationApproach():
            for day in range(n - 1, -1, -1):
                for brought in range(2):
                    maxProfit = 0
                    if brought == 0:
                        buyNow =  -prices[day] + cache[day + 1][1]
                        dontBuyNow = cache[day + 1][0]
                        maxProfit = max(buyNow, dontBuyNow)
                    else:
                        sellNow = prices[day] + cache[day + 2][0] 
                        dontSellNow = cache[day + 1][1]
                        maxProfit = max(sellNow, dontSellNow)
                    cache[day][brought] = maxProfit 
            return cache[0][0]

        return tabulationApproach()
    
## Buy and sell stocks  without transaction fee

class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        def recursiveApproach(day, brought):
            if day == n:
                return 0 

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + recursiveApproach(day + 1, 1)
                dontBuyNow = recursiveApproach(day + 1, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + recursiveApproach(day + 1, 0) - fee
                dontSellNow = recursiveApproach(day + 1, 1)
                maxProfit = max(sellNow, dontSellNow)

            return maxProfit

        cache = []
        for i in range(n + 1):
            row = []
            for j in range(2):
                row.append(0)
            cache.append(row)

        def memoizationApproach(day, brought):
            if day == n:
                return 0 
            elif cache[day][brought] != -1:
                return cache[day][brought]

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + memoizationApproach(day + 1, 1)
                dontBuyNow = memoizationApproach(day + 1, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + memoizationApproach(day + 1, 0) - fee
                dontSellNow = memoizationApproach(day + 1, 1)
                maxProfit = max(sellNow, dontSellNow)
                
            cache[day][brought] = maxProfit 
            return maxProfit

        def tabulationApproach():
            for day in range(n - 1, -1, -1):
                for brought in range(2):
                    maxProfit = 0
                    if brought == 0:
                        buyNow =  -prices[day] + cache[day + 1][1]
                        dontBuyNow = cache[day + 1][0]
                        maxProfit = max(buyNow, dontBuyNow)
                    else:
                        sellNow = prices[day] + cache[day + 1][0] - fee
                        dontSellNow = cache[day + 1][1]
                        maxProfit = max(sellNow, dontSellNow)
                    cache[day][brought] = maxProfit 
            return cache[0][0]

        return tabulationApproach()
        
##Chocolates pickup

class Solution:
    def solve(self, n, m, grid):
        def recursiveApproach(row, col1, col2):
            if row == n or min(col1, col2) < 0 or max(col1, col2) >= m:
                return 0 
                
            currResult = grid[row][col1]
            if col1 != col2:
                currResult += grid[row][col2]
                
            old1 = grid[row][col1]
            old2 = grid[row][col2]
                
            grid[row][col1] = 0
            grid[row][col2] = 0
            
            nextResult = 0
            directions = [-1, 0, 1]
            for index1 in range(3):
                for index2 in range(3):
                    newCol1 = col1 + directions[index1]
                    newCol2 = col2 + directions[index2]
                    nextResult = max(nextResult, recursiveApproach(row + 1, newCol1, newCol2))
                
            
            grid[row][col1] = old1 
            grid[row][col2] = old2
            
            
            return currResult + nextResult
        
        
        cache = []
        for i in range(n):
            row = []
            for j in range(m):
                col = []
                for k in range(m):
                    col.append(0)
                row.append(col)
            cache.append(row)
                    
    
        
        def memoizationApproach(row, col1, col2):
            if row == n or min(col1, col2) < 0 or max(col1, col2) >= m:
                return 0 
            elif cache[row][col1][col2] != -1:
                return cache[row][col1][col2]
                
            currResult = grid[row][col1]
            if col1 != col2:
                currResult += grid[row][col2]
                
            old1 = grid[row][col1]
            old2 = grid[row][col2]
                
            grid[row][col1] = 0
            grid[row][col2] = 0
            
            nextResult = 0
            directions = [-1, 0, 1]
            for index1 in range(3):
                for index2 in range(3):
                    newCol1 = col1 + directions[index1]
                    newCol2 = col2 + directions[index2]
                    nextResult = max(nextResult, memoizationApproach(row + 1, newCol1, newCol2))
                
            
            grid[row][col1] = old1 
            grid[row][col2] = old2
            
            
            cache[row][col1][col2] = currResult + nextResult 
            return cache[row][col1][col2]
        
        def tabulationApproach():
            for col1 in range(m):
                for col2 in range(m):
                    cache[n - 1][col1][col2] = grid[n - 1][col1]
                    if col1 != col2:
                        cache[n - 1][col1][col2] += grid[n - 1][col2]
                        
                        
            for row in range(n - 2, -1, -1):
                for col1 in range(m):
                    for col2 in range(m - 1, -1, -1):
                        currResult = grid[row][col1]
                        if col1 != col2:
                            currResult += grid[row][col2]
                            
                        
                        nextResult = 0
                        directions = [-1, 0, 1]
                        for index1 in range(3):
                            for index2 in range(3):
                                newCol1 = col1 + directions[index1]
                                newCol2 = col2 + directions[index2]
                                if min(newCol1, newCol2) < 0 or max(newCol1, newCol2) >= m:
                                    continue
                                
                                nextResult = max(nextResult, cache[row + 1][newCol1][newCol2])
                            
                        
                        
                        cache[row][col1][col2] = currResult + nextResult 
            return cache[0][0][m - 1]
        
        return tabulationApproach()
    