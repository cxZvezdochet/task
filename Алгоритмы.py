# a = {2025: 2025, 2026: 2026}
#
# for i in range(2024, 0, -1):
#     a[i] = a[i+1] - a[i+2] + 7
# print(a[15]-a[24])


n = 5
d ={ 1:0}
for i in range(2,n+1):
    op =[d[i-1]]
    if i%2==0:
        op.append(d[i//2])
    if i%3==0:
        op.append(d[i//3])
    d[i] = min(op) +1
print(d[n])