class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
    
    def add_node(self, node):
        self.next = node.next
        node.next = self
    
    def delete_node(self, prev_node):
        prev_node.next = prev_node.next.next


class DListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
    def add_node(self, node_to_add):
        pass
    


def sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    
    return ans

def recursive_sum(head):
    if not head:
        return 0
    
    return head.val + recursive_sum(head.next)



one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three
head = one

while True:
    print(head.val)
    if head.next == None:
        break
    head = head.next



head = one
print(sum(head))

head = one
print(recursive_sum(one))

