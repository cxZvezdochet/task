#Задача 4
import heapq

def klargest(arr,n,k):
    # arr = [-i for i in arr] если нужно найти максимальное
    heapq.heapify(arr)
    for _ in range(k):
        print(heapq.heappop(arr))
klargest([1,23,12,9,30,2, 50], 7,3)