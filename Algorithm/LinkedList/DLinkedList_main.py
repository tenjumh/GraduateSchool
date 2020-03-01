from DLinkedList import DList
if __name__ == '__main__':
    d = DList()

    d.insert_after(d.head, 'apple')
    d.insert_before(d.tail, 'orange')
    d.insert_before(d.tail, 'cherry')
    d.insert_after(d.head.next, 'pear')
    d.print_list()

    print('마지막 노드 삭제 후:\t', end='')
    d.delete(d.tail.prev)
    d.print_list()

    print('맨 끝에 포도 삽입 후:\t', end='')
    d.insert_before(d.tail, 'grape')
    d.print_list()

    print('첫 노드 삭제 후:\t', end='')
    d.delete(d.head.next)
    d.print_list()

    print('첫 노드 삭제 후:\t', end='')
    d.delete(d.head.next)
    d.print_list()

    print('첫 노드 삭제 후:\t', end='')
    d.delete(d.head.next)
    d.print_list()
    print('첫 노드 삭제 후:\t', end='')
    d.delete(d.head.next)
    d.print_list()