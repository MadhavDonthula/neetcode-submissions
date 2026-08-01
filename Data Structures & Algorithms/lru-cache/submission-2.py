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
        self.size +=1
    def get_size(self):
        return self.size
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.size -=1
    def remove_from_head(self):
        if self.head.next == self.tail: 
            return None
        node = self.head.next
        self.remove_node(node)
        return node 
    def insert_at_tail(self, nodeToInsert):
        self.insert_node(nodeToInsert, self.tail.prev, self.tail)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.recency_list = DoublyLinkedList()
        self.hashmap = {}

        

    def get(self, key: int) -> int:
        if key not in self.hashmap: 
            return -1 
        keysNode = self.hashmap[key]
        self.recency_list.remove_node(keysNode)
        self.recency_list.insert_at_tail(keysNode)
        return keysNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap: 
            keysNode = self.hashmap[key]
            keysNode.val = value
            self.recency_list.remove_node(keysNode)
            self.recency_list.insert_at_tail(keysNode)
        else: 
            if self.recency_list.get_size() == self.capacity: 
                removedNode = self.recency_list.remove_from_head()
                removedNodeKey = removedNode.key 
                del self.hashmap[removedNode.key]
            newNode = Node(value, key)
            self.hashmap[key] = newNode
            self.recency_list.insert_at_tail(newNode)
        

        
