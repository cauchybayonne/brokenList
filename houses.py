a = input()
b = input()

a = a.split(' ')
money = int(a[1])

b = b.split(' ')

b = [int(x) for x in b]

b.sort()

summ = 0
cnt = 0
for i in b:
    summ += i
    if summ > money:
        print(cnt)
        break
    else:
        cnt += 1
