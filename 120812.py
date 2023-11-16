# 최빈값 구하기
def solution(array):
	count = [0] * (max(array)+1) 
	for i in array:
		count[i] += 1
	m = 0 
	for c in count:
		if c == max(count):
			m += 1
	if m > 1: 
		return -1
	else: 
		return count.index(max(count))

arr=[1]
cnt=[0] * (max(arr)+1)
print(max(arr))

 
print(cnt,"1111111")
for i in arr:
    cnt[i]+=1
print(cnt)
print(max(cnt))
m = 0 
for j in cnt:
    print(j,"ttt")
    if j == max(cnt):
        m += 1

if m > 1: 
    print(-1) 
else: 
	print((max(cnt))) 