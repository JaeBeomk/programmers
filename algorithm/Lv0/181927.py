# 마지막 두 원소
# 배열이 주어질때 마지막 원소가 그 전 원소보다 크면
# 마지막에서 그 전 원소를 뺸값을 
# 전보다 크지않으면 마지막 원소를 두 배 한값을 리턴
# 배열 슬라이싱으로 수를 두개 빼서 값을 계산하고 그 값을 변수에 담아서 배열에 추가
# 와.... 계속 틀리길래 뭔가했는데... 크면 은 > 이지만 크지않다면은 >=라니...
def solution(num_list):
    a = num_list[-2:]
    # print(a)
    if a[1]>a[0]:
        last=a[1]-a[0]
    elif a[1]<=a[0]:
        last=a[1]*2
    # print(last)
    num_list.append(last)
    return num_list


print(solution([2, 1, 6])) #[2,1,6,5]
print(solution([5, 2, 1, 7, 5])) #[5, 2, 1, 7, 5,10]	