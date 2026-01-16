class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
class singleLinkedList:
    def __init__(self):
        self.head=None
    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    # brute force actually we are not changing the links
    # we are changing the node values note we are not changing head here so return head only 
    # def reverse(self):
    #     stack=[]
    #     curr=self.head
    #     while curr is not None:
    #         stack.append(curr.value)
    #         curr=curr.next
    #     curr=self.head
    #     while curr is not None:
    #         e=stack.pop()
    #         curr.value=e
    #         curr=curr.next
    #     return self.head
    # optimal approach using three variable
    # prev_node , curr, front
    def reverse(self):
        prev_node=None
        curr=self.head
        while curr is not None:
            front=curr.next
            curr.next=prev_node
            prev_node=curr
            curr=front
        self.head=prev_node
        return prev_node
    def traversal(self):
        if self.head == None:
            print("singlyLinkedList is Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value, end=" ")
                curr = curr.next
sll=singleLinkedList()
sll.append(5)
sll.append(10)
sll.append(15)
sll.append(20)
sll.append(25)
sll.append(30)
sll.append(35)
sll.append(40)
sll.append(45)
sll.append(50)
sll.traversal()
print()
sll.reverse()
sll.traversal()

