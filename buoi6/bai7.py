class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    if not head:
        return None

    seen_values = set()
    current = head
    previous = None

    while current:
        if current.value in seen_values:
            previous.next = current.next
        else:
            seen_values.add(current.value)
            previous = current

        current = current.next

    return head

head = ListNode(1, ListNode(2, ListNode(4, ListNode(3, ListNode(4, ListNode(2))))))

print("danh sach goc")
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

head = remove_duplicates(head)

print("\nket qua danh sach:")
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")