number_of_students, IDs, count = int(input()), list(map(int, input().split(' '))), int(input())
unique_IDs = set(IDs)

result = [[unique_ID, IDs.count(unique_ID)] for unique_ID in unique_IDs]

result = sorted(result, key=lambda x: x[0])
result = sorted(result, key=lambda x: x[1], reverse=True)

result = [result[i][0] for i in range(count)]
print(*result)


'''
7
1 2 3 1 2 3 4
3
'''