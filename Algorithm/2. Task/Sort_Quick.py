#마라토너의 수를 입력:
#마라토너의 기록을 초단위로 입력:
#경기기록을 기준으로 오름차순으로 정렬한다.
#1, 2, 3등에 대하여 번호, 시, 분, 초 단위로 출력한다.
#Quick sort
def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        print("Pivot {} :{}".format(a[pivot], a))
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high)

def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j

player = int(input("마라토너의 수를 입력하시오:"))
records = [0]*player
for i in range(player):
    records[i] = int(input("마라토너의 기록을 초단위로 입력:"))

print("**(Quick_sort)**")
print("정렬 전 :{}".format(records))
qsort(records, 0, player-1)
print("정렬 후 :{}\n".format(records))

for k in range(3):
    hour = records[k] // (60 * 60)
    min = (records[k] - hour * 60 * 60) // 60
    sec = records[k] % 60
    print("{} 등 : {}시간 {}분 {}초".format(k + 1, hour, min, sec))