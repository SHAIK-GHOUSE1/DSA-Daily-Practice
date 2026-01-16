class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head == None:
            print("singlyLinkedList is Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value, end=" ")
                curr = curr.next

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr=self.head
            count=0
            prev_node=None
            while curr is not None and count<position:
                count+=1
                prev_node=curr
                curr=curr.next
            prev_node.next=new_node
            new_node.next=curr
    def deletion(self,val):
        # if self.head.value==val:
        #     self.head=self.head.next
        # prev_node=None
        # curr=self.head
        # while curr is not None:
        #     if curr.value==val:
        #         prev_node.next=curr.next
        #         break
        #     prev_node=curr
        #     curr=curr.next
        # if curr is None:
        #     print("Node not found")
        curr=self.head
        if self.head==None:
            print("linkedlist is empty")
            return
        if self.head.value==val:
            self.head=curr.next
            return
        prev_node=None
        while curr is not None:
            if curr.value==val:
                prev_node.next=curr.next
                return
            prev_node=curr
            curr=curr.next
        print("Node not found")



s1 = singlyLinkedList()
s1.append(5)
s1.append(10)
s1.append(15)
s1.append(20)
s1.append(25)
s1.append(30)
s1.insert_at(3, 0)
s1.insert_at(7,2)
s1.deletion(7)
s1.deletion(20)
s1.traversal()


