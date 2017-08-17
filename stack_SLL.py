# Stacks using SLL implementation

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        runner = self.head
        string = ''
        while runner:
            string += runner.val + ' -> '
            runner = runner.next
        string += 'None'
        return string

    def push(self, item):
        if not self.head:
            self.head = ListNode(item)
        else:
            node = ListNode(item)
            node.next = self.head
            self.head = node

    def pop(self):
        self.head = self.head.next

    def peek(self):
        return self.head

    def isEmpty(self):
        if not self.head:
            return True
        return False

    def size(self):
        size = 0
        runner = self.head
        while runner:
            size += 1
            runner = runner.next
        return size

aStack = Stack()
aStack

