from collections import defaultdict, OrderedDict
class Node: 
    def __init__(self, key=None, val=None): 
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
        
class DoublyLinkedList: 
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0 
    def length(self): 
        return self.size

    def insert_node(self, node, left, right):
        node.prev = left
        node.next = right
        left.next = node
        right.prev = node
        self.size += 1
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.size -= 1
    def remove_end(self):
        if self.length() == 0: 
            return None
        node = self.tail.prev
        self.delete_node(node)
        return node
    def insert_at_front(self, node):
        return self.insert_node(node, self.head, self.head.next)
        

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.nodeMap = {}
        self.lfuCnt = 0 
        self.listMap = defaultdict(DoublyLinkedList)

    def get(self, key: int) -> int:
        if key not in self.nodeMap: 
            return -1 
        node = self.nodeMap[key]
        self.counter(node)
        return node.val 
        
    def counter(self, node):
        cnt = node.freq
        self.listMap[cnt].delete_node(node)
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0: 
            self.lfuCnt +=1
        node.freq +=1 
        self.listMap[node.freq].insert_at_front(node)


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: 
            return 
        if key in self.nodeMap: 
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return 
        if len(self.nodeMap) == self.capacity: 
            node = self.listMap[self.lfuCnt].remove_end()
            del self.nodeMap[node.key]
        node = Node(key, value)
        self.nodeMap[key] = node
        self.listMap[node.freq].insert_at_front(node)
        self.lfuCnt = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# essentially we will have the same thing as LRU cache but with a hashmap key --> value and freq
# freq --> would be a DLL of keys 
# min_freq integer