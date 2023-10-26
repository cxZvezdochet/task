num=input()
print(int((num.replace('<span>','').replace('&nbsp;','').replace('P</span>','')))+1)