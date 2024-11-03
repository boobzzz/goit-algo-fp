class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_list(head)

current = reversed_head
while current:
    print(current.value, end=" -> ")
    current = current.next


def insertion_sort_list(head):
    if not head or not head.next:
        return head

    sorted_head = ListNode(0)
    current = head

    while current:
        prev_sorted = sorted_head
        next_sorted = sorted_head.next

        while next_sorted:
            if next_sorted.value > current.value:
                break
            prev_sorted = next_sorted
            next_sorted = next_sorted.next

        next_current = current.next
        current.next = next_sorted
        prev_sorted.next = current
        current = next_current

    return sorted_head.next


head = ListNode(3, ListNode(1, ListNode(2)))
sorted_head = insertion_sort_list(head)

current = sorted_head
print('\n')
while current:
    print(current.value, end=" -> ")
    current = current.next


def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next

l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = merge_two_sorted_lists(l1, l2)

current = merged_head
print('\n')
while current:
    print(current.value, end=" -> ")
    current = current.next
