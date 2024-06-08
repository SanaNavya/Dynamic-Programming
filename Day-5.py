'''
##Normal fibonacci
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
n=int(input())
print(fib(n))

# ## fibonacci using recursion

def fib(n):
    if n==1 or n==2:
        return 1
    res1=fib(n-1)
    res2=fib(n-2)
    return res1+res2
n=int(input())
fib(n)


# Using Recursion
def findNthTerm(n):
    if n == 1 or n == 2:
        return 1 
    result1 = findNthTerm(n - 1)
    result2 = findNthTerm(n - 2)
    return result1 + result2 
 
# Using Memoization 
def findNthTermUsingCache(n, cache):
    if n == 1 or n == 2:
        return 1 
    elif cache[n] != -1:
        return cache[n]
 
 
    result1 = findNthTermUsingCache(n - 1, cache)
    result2 = findNthTermUsingCache(n - 2, cache)
    cache[n] = result1 + result2
    return result1 + result2 
# n=int(input())
# cache = [-1] * (n + 1)
# findNthTermUsingCache(n, cache)

# Tabulation approach (Ultimate Dynamic programming solution)
def findNthTermUsingTabulation(n):
    cache = [-1] * (n + 1)
    # Whatever base condition we wrote 
    # recursive solutin, we need to 
    # initialize them 
 
    cache[1] = 1 
    cache[2] = 1 
    # 1 - wherever 'n' is present, replace it with index 
    # 2 - wherever 'functionCall' is there replace it with cache 
    for index in range(3, n + 1):
        result1 = cache[index - 1]
        result2 = cache[index - 2]
        cache[index] = result1 + result2
    return cache[n]
n = int(input())
# cache = [-1] * (n + 1)
# print(findNthTermUsingCache(n, cache))
print(findNthTermUsingTabulation(n))
'''

##steps program using recursion

def stairs(i,n):
    if n==i: 
        return i 
    for i in range(0,n+1):
        res1=stairs(i+1,n)
        res2=stairs(i+n,n)
    return res1+res2
n=int(input())
i=0
print(stairs(i,n))