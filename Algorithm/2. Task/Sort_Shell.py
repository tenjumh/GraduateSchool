#마라토너의 수를 입력:
#마라토너의 기록을 초단위로 입력:
#경기기록을 기준으로 오름차순으로 정렬한다.
#1, 2, 3등에 대하여 번호, 시, 분, 초 단위로 출력한다.
#Shell sort (gap = 4, gap =1)
def shell_sort(a):
    print("**(Shell_sort)**")
    print("정렬 전 :{}".format(a))
    h = 4
    while h >= 1:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        print("gap= {} :{}".format(h, a))
        h //= 3
    print("정렬 후 :{}\n".format(a))

    for k in range(3):
        hour = a[k] // (60*60)
        min = (a[k]-hour*60*60) // 60
        sec = a[k] % 60
        print("{} 등 : {}시간 {}분 {}초".format(k+1, hour, min, sec))

player = int(input("마라토너의 수를 입력하시오:"))
records = [0]*player
for i in range(player):
    records[i] = int(input("마라토너의 기록을 초단위로 입력:"))

shell_sort(records)