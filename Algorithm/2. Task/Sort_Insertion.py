#마라토너의 수를 입력:
#마라토너의 기록을 초단위로 입력:
#경기기록을 기준으로 오름차순으로 정렬한다.
#1, 2, 3등에 대하여 번호, 시, 분, 초 단위로 출력한다.
#Insertion sort
def insertion_sort(a):
    print("**(Insertion_sort)**")
    print("정렬 전 :{}".format(a))
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
        print("Step {} :{}".format(i, a))
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

insertion_sort(records)
