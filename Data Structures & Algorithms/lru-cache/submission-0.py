class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.next, self.prev = None,None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def delete(self,node):
        prv,nxt = node.prev,node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self,node):
        prv,nxt = self.right.prev,self.right
        prv.next = node
        nxt.prev = node
        node.prev = prv
        node.next = nxt



    
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
            lru = self.left.next
            self.delete(lru)
            del self.hm[lru.key]


