# 파이썬 객체지향 프로그래밍으로 링크드리스트 구현하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next


# 링크드리스트 만들어보기
print('\n링크드리스트 만들어보기')
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# 데이터 추가해보기
print('\n데이터 추가해보기')
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()


# 테스트를 위해 1개 노드를 만들어 봄
print('\n테스트')
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# head가 살아있음을 확인
print(linkedlist1.head)
# head를 지워 봄 (경우의 수 1)
linkedlist1.delete(0)
print(linkedlist1.head)

# 이번에는 여러 노드를 더 추가해봄
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()

# 노드 중에 한 개를 삭제해 봄 (경우의 수 2)
linkedlist1.delete(4)
linkedlist1.desc()

# 마지막 노드를 삭제해 봄 (경우의 수 3)
linkedlist1.delete(9)
linkedlist1.desc()

# 특정 숫자 찾아보기
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)
node = node_mgmt.search_node(4)
print(node.data)
