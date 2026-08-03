
class Node: 
    def __init__(self, key=None, value=None): 
        self.key = key 
        self.value = value
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
        
    def getSize(self):
        return self.size

    def insert_node(self, node, left, right):
        left.next = node
        right.prev = node
        node.prev = left
        node.next = right
        self.size +=1

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.right = None
        node.left = None
        self.size -= 1
    def remove_at_end(self):
        if self.size == 0: 
            return None 
        node = self.tail.prev
        self.delete_node(node)
        return node
        
    def insert_at_front(self, node):
        return self.insert_node(node, self.head, self.head.next)

    def update(self, node):
        self.delete_node(node)
        self.insert_at_front(node)
class LFUCache:

    def __init__(self, capacity: int):
        self.lfuCnt = 0 
        self.cap = capacity 
        self.nodeMap = {} #map key --> Node
        self.countMap = collections.defaultdict(int) #key to count
        self.listMap = collections.defaultdict(DoublyLinkedList)

    def counter(self, node): 

        cnt = node.freq
        key = node.key
        self.listMap[cnt].delete_node(node)
        self.countMap[key] += 1
        if cnt == self.lfuCnt and self.listMap[cnt].size == 0: 
            self.lfuCnt +=1
        node.freq +=1 
        self.listMap[node.freq].insert_at_front(node)
        
    def get(self, key: int) -> int:
        if key not in self.nodeMap: 
            return -1
        self.counter(self.nodeMap[key])
        return self.nodeMap[key].value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: 
            return 
        if key in self.nodeMap:
            self.nodeMap[key].value = value 
            self.counter(self.nodeMap[key])
        else:
            if len(self.nodeMap) == self.cap: 
                removed_node = self.listMap[self.lfuCnt].remove_at_end()
                del self.nodeMap[removed_node.key]
            newNode = Node(key=key, value = value)
            self.lfuCnt = 1
            self.nodeMap[key] = newNode
            self.listMap[1].insert_at_front(newNode)
        



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)