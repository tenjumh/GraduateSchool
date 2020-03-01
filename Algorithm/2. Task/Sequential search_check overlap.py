def sequential_search(arr, key, low, high):
    for i in range(low, high):
        if(arr[i] == key):
            return i
    return -1

def find_same(arr, index):
    n = len(arr)
    result = []
    for i in range(index+1, n):
        if arr[index] == arr[i]:
            result.append(i)
    return result

number = int(input('검색 값 입력:'))
arr = [17, 6, 7, 1, 11, 2, 7, 4, 5, 14, 10, 7, 18]

ret = sequential_search(arr, number, 0, len(arr))

if ret >= 0:
    print("탐색 성공: 숫자(%d) index = %d"%(number, ret))
    print("탐색 숫자(%d) 중복 위치:"%number, find_same(arr, ret))
else:
    print("숫자(%d) 탐색 실패"%number)