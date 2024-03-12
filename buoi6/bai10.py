class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    while head and head.val == val:
        head = head.next

    current = head

    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return head

def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
print("Input:")
printList(head)

val_to_remove = 6
new_head = removeElements(head, val_to_remove)

print("\nOutput:")
printList(new_head)