# Singly Linked List Class
class SList:
    class Node:  # 계속 생성될때마다 Node 사용해야 해서 class만들어줌
        # Node는 (1)정보가 저장되는 변수와 (2)다음 리스트를 지시하는 변수 필요
        def __init__(self, item, link):
            self.item = item
            self.next = link

    # 당연히 SLink 인스턴스가 만들어지면 무조건 시작점인 Head와 항목수 관리 필요
    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):
        p.next = SList.Node(item, p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError("Underflow")
        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):
        p = self.head  # 탐색할 경우 head부터 시작함
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, '-> ', end='')
            else:
                print(p.item)
            p = p.next


class EmptyError(Exception):
    pass