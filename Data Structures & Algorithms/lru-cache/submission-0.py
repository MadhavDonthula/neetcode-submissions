class Node:
    def __init__(self, val=None, key=None): 
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList: 
    def __init__(self): 
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert_node(self, node, left, right):
        node.prev = left
        node.next = right
        left.next = node
        right.prev = node
        self.size += 1

    def remove_node(self, remove_node):
        remove_node.prev.next = remove_node.next
        remove_node.next.prev = remove_node.prev
        remove_node.prev = None
        remove_node.next = None
        self.size -= 1
    
    def remove_from_head(self):
        if self.head.next == self.tail:
            return None
        node = self.head.next
        self.remove_node(node)
        return node

    def insert_at_tail(self, node_to_insert):
        self.insert_node(node_to_insert, self.tail.prev, self.tail)

    
class LRUCache: 
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.recency_list = DoublyLinkedList()

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self.recency_list.remove_node(node)
        self.recency_list.insert_at_tail(node)
        return node.val
    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.recency_list.remove_node(node)
            self.recency_list.insert_at_tail(node)
        else:
            node = Node(value, key)
            self.map[key] = node
            self.recency_list.insert_at_tail(node)

            if self.recency_list.size > self.capacity:
                lru_node = self.recency_list.remove_from_head()
                del self.map[lru_node.key]


                







    