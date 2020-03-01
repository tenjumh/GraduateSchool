#마라토너의 수를 입력:
#마라토너의 기록을 초단위로 입력:
#경기기록을 기준으로 오름차순으로 정렬한다.
#1, 2, 3등에 대하여 번호, 시, 분, 초 단위로 출력한다.
#heap sort
def downheap(a, i, size):
    while 2*i <= size:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k += 1
        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k

def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2+1)):
        downheap(a, i, hsize)

def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(a, 1, N-1)
        print("DWheap:", a[1:])
        N -= 1

player = int(input("마라토너의 수를 입력하시오:"))
records = [0]*(player+1)
for i in range(1, player+1):
    records[i] = int(input("마라토너의 기록을 초단위로 입력:"))

print("**(Heap_sort)**")
print("정렬 전 :{}".format(records[1:]))
create_heap(records)
heap_sort(records)
print("정렬 후 :{}\n".format(records[1:]))

for k in range(3):
    hour = records[k+1] // (60 * 60)
    min = (records[k+1] - hour * 60 * 60) // 60
    sec = records[k+1] % 60
    print("{} 등 : {}시간 {}분 {}초".format(k + 1, hour, min, sec))