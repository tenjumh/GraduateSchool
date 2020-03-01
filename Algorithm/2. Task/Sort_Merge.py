#마라토너의 수를 입력:
#마라토너의 기록을 초단위로 입력:
#경기기록을 기준으로 오름차순으로 정렬한다.
#1, 2, 3등에 대하여 번호, 시, 분, 초 단위로 출력한다.
#Merge sort
def merge(a, b, low, mid, high):
    i = low
    j = mid+1
    for k in range(low, high+1):
        if i > mid:
            b[k] = a[j]
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            b[k] = a[j]
            j += 1
        else:
            b[k] = a[i]
            i += 1
    for k in range(low, high+1):
        a[k] = b[k]

def merge_sort(a, b, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2
    merge_sort(a, b, low, mid)
    merge_sort(a, b, mid+1, high)
    merge(a, b, low, mid, high)
    print("Merge :{}".format(a))

player = int(input("마라토너의 수를 입력하시오:"))
records = [0]*player
for i in range(player):
    records[i] = int(input("마라토너의 기록을 초단위로 입력:"))
b = [None] * len(records)

print("**(Merge_sort)**")
print("정렬 전 :{}".format(records))
merge_sort(records, b, 0, player-1)
print("정렬 후 :{}\n".format(records))

for k in range(3):
    hour = records[k] // (60 * 60)
    min = (records[k] - hour * 60 * 60) // 60
    sec = records[k] % 60
    print("{} 등 : {}시간 {}분 {}초".format(k + 1, hour, min, sec))