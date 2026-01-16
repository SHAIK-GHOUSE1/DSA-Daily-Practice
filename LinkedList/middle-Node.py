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
    # Brute force
    # def middle(self):
    #     curr=self.head
    #     count=0
    #     while curr is not None:
    #         count+=1
    #         curr=curr.next
    #     curr=self.head
    #     for i in range(count//2):
    #         curr=curr.next
    #     print(curr.value)
    # optimal solution tortice and hare method
    def middle(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow.value
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
print(sll.middle())
            
    
    