class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.leftD, self.rightD = Node(0,0),  Node(0,0)
        self.leftD.next,self.rightD.prev = self.rightD,self.leftD

    def delete(self, node):
        prv, nxt = node.prev,node.next
        prv.next = nxt
        nxt.prev = prv
        
    
    def insert(self, node):
        prv, nxt = self.rightD.prev,self.rightD
        node.next =nxt
        node.prev = prv
        prv.next = node
        nxt.prev = node

    
    def get(self, key: int) -> int:
        if key in self.hm:
            self.delete(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.delete(self.hm[key])
        self.hm[key] = Node(key,value)
        self.insert(self.hm[key])

        if len(self.hm) > self.capacity:
            lru = self.leftD.next
            self.delete(lru)
            del self.hm[lru.key]
