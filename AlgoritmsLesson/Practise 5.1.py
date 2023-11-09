#Задача 3

from collections import deque

A = [[0, 1, 0, 1, 1],
     [1, 1, 1, 1, 2],
     [0, 1, 0, 2, 2],
     [3, 3, 1, 2, 2],
     [0, 1, 1, 0, 0]]
x0 = 1
y0 = 0
c = 5
init_c = A[y0][x0]

queue = deque([(x0, y0)])

while queue:
    x, y = queue.popleft()
    A[y][x] = c

    sosedi = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    for sx, sy in sosedi:
        if 0 <= sx < len(A[0]) and \
           0 <= sy < len(A) and \
           A[sy][sx] == init_c:
            queue.append((sx, sy))

print(*A, sep='\n')