
from heapq import *

def minOperations(self,arr,n,k):
    ans = 0
    heapify(arr)

    while len(arr) > 1 and arr[0] <k:
