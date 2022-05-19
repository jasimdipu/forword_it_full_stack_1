class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfterNode(self, prev_data, data):
        if prev_data is None:
            print("No previous data in here")
        new_node = Node(data)
        new_node.next = prev_data.next
        prev_data.next = new_node

    def deleteNode(self, data):
        temp = self.head

        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == data:
                break

            prev = temp
            temp = temp.next

        if temp == None:
            return
        prev.next = temp.next
        temp = None


lst = LinkedList()
# lst.head = Node(10)
# sec = Node(20)
# thrd = Node(30.50)
# f = Node(100)
# fifth = Node("six")
# sev = Node(11)
#
# lst.head.next = sec
# sec.next = thrd
# thrd.next = f
# f.next = fifth
lst.push(80)
lst.push(10)
lst.push(20)
lst.push(30)
lst.push(40)
lst.push(50)
lst.push(60)
lst.push(80)

# lst.insertAfterNode(sec, 200)

lst.printList()

lst.deleteNode(80)

lst.printList()
