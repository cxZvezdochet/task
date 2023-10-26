def count_ones(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def binary_sort(arr):
    counts = [count_ones(num) for num in arr]

    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if counts[j] < counts[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        counts[i], counts[min_idx] = counts[min_idx], counts[i]

    return arr

# Пример использования:
nums = [7, 12, 6, 10, 15, 8]
sorted_nums = binary_sort(nums)
print(sorted_nums)
