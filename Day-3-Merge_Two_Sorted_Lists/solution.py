class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    num_list_1 = []
    num_list_2 = []

    while list1 is not None:
        num_list_1.append(list1.val)
        list1 = list1.next
    while list2 is not None:
        num_list_2.append(list2.val)
        list2 = list2.next

    merged_list = []
    merged_list_length = len(num_list_1) + len(num_list_2)

    while len(merged_list) < merged_list_length:
        if len(num_list_1) == 0:
            merged_list += num_list_2
            break
        if len(num_list_2) == 0:
            merged_list += num_list_1
            break
        if num_list_1[0] <= num_list_2[0]:
            merged_list.append(num_list_1[0])
            num_list_1 = num_list_1[1:]
        else:
            merged_list.append(num_list_2[0])
            num_list_2 = num_list_2[1:]

    list_of_nodes = [ListNode(val) for val in merged_list]
    for i in range(len(list_of_nodes)-1):
        list_of_nodes[i].next = list_of_nodes[i+1]

    return list_of_nodes[0]



def print_llist(head):
    curr = head

    while curr:
        if not curr.next:
            print(curr.val)
        else:
            print(curr.val, end=" --> ")
        curr = curr.next


def main():
    # list1 = [1, 2, 4]
    # list2 = [1, 3, 4]
    node_3_1 = ListNode(val=4, next=None)
    node_2_1 = ListNode(val=2, next=node_3_1)
    head_1 = ListNode(val=1, next=node_2_1)
    node_3_2 = ListNode(val=4, next=None)
    node_2_2 = ListNode(val=3, next=node_3_2)
    head_2 = ListNode(val=1, next=node_2_2)
    print_llist(mergeTwoLists(head_1, head_2))
    print("Solution: [1, 1, 2, 3, 4, 4]")
    print("--" * 50)

    # list1 = []
    # list2 = []
    head_1 = None
    head_2 = None
    print_llist(mergeTwoLists(head_1, head_2))
    print("Solution: []")
    print("--" * 50)

    # list1 = []
    # list2 = [0]
    head_1 = None
    head_2 = ListNode(val=0, next=None)
    print_llist(mergeTwoLists(head_1, head_2))
    print("Solution: [0]")
    print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
