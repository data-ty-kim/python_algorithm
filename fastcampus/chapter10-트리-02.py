# 이진 탐색 트리 삭제 코드 구현과 분석
# 머리 속으로 상상해서 코드 작성하지 말고 종이에 그림을 그려 작성한 뒤 코드를 작성하라

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        # 삭제할 Node 탐색
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        # 삭제할 Node가 없는 경우는 False를 반환하고 함수를 종료
        if searched == False:
            return False

        # 이후부터 case를 분리해서 코드 작성
        # case1: 삭제할 Node가 Leaf Node인 경우
        #        self.current_node가 삭제할 Node,
        #        self.parent는 삭제할 Node의 Parent Node인 상태
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # case2: 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left = None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # case3: 삭제할 Node가 Child Node를 두 개 가지고 있을 경우
        if self.current_node.left != None and self.current_node.right != None:
            # case 3-1: 삭제할 Node가 Parent Node 왼쪽에 있을 때
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # case 3-1-2: 삭제할 Node의 오른쪽 자식 중,
                #             가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                # case 3-1-1: 삭제할 Node의 오른쪽 자식 중,
                #             가장 작은 값을 가진 Node의 Child Node가 없을 때
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            # case 3-2: 삭제할 Node가 Parent Node 오른쪽에 있을 때
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
