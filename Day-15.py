##minimimum heap example
#basically python has default minimum heap

from heapq import heapify,heappush,heappop
minheap=[100,-121]
heapify(minheap)
heappush(minheap,90)
heappush(minheap,8)
heappush(minheap,76)
heappush(minheap,89)
while minheap:
    curele=heappop(minheap)
    print(curele)
print("End of minimum heap")


##maximum eap example in python


from heapq import heapify,heappush,heappop
minheap=[]
heapify(minheap)
nums=[10,20,1,200,99]
for ele in nums:
    heappush(minheap,-1*ele)
while minheap:
    curele=heappop(minheap)
    print(curele*-1)
print("End of the maximum heap")