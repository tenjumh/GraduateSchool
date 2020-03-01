from binaryheap import BHeap

if __name__ == '__main__':
    a = [None] * 1
    b = BHeap(a)
    while True:
        text = input('삽입(i), 삭제(d) :')
        str(text)

        if text == "i":
            worklist = input('할일 :')
            str(worklist)
            sort = input('우선순위 :')
            int(sort)
            b.insert([sort, worklist])
            #a.append([sort, worklist])

        elif text == "d":
            print('제일 우선순위가 높은 일은 "%s"\n'%a[1][1])
            b.delete_min()

        else:
            print("메뉴선택 다시 하세요")
            break

print(a)




