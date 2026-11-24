class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.key_to_val = {}
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.right = self.tail
        self.tail.left = self.head
        self.curr_count = 0

    def get(self, key: int) -> int:
        if key in self.key_to_val:
            node = self.key_to_val[key]
            self._detach_node(node)
            self._move_to_front(node)
            return self.key_to_val[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_val:
            node = self.key_to_val[key]
            node.val = value
            self._detach_node(node)
        else:
            if self.curr_count == self.limit:
                last_node = self.tail.left
                second_last = last_node.left
                second_last.right = self.tail
                self.tail.left = second_last
                del self.key_to_val[last_node.key]
                self.curr_count -= 1

            node = Node(key, value)
            self.key_to_val[key] = node
            self.curr_count += 1

        self._move_to_front(node)


    def _move_to_front(self, node):
        node.left = self.head
        node.right = self.head.right
        self.head.right = node
        right_to_node = node.right
        right_to_node.left = node

    def _detach_node(self, node):
        left = node.left
        right = node.right
        left.right = right
        right.left = left

        
