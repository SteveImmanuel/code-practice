# https://leetcode.com/problems/lru-cache/

class DLLNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memory = {}
        self.first = None
        self.last = None

    def get(self, key: int) -> int:
        if key in self.memory:
            if self.memory[key].prev is not None and self.memory[key].next is not None: # in the middle
                self.memory[key].prev.next = self.memory[key].next
                self.memory[key].next.prev = self.memory[key].prev
                
                self.memory[key].prev = None
                self.first.prev = self.memory[key]
                self.memory[key].next = self.first
                self.first = self.memory[key]

            elif self.memory[key].prev is not None and self.memory[key].next is None: # in the last
                self.last = self.memory[key].prev
                self.last.next = None
                
                self.memory[key].prev = None
                self.first.prev = self.memory[key]
                self.memory[key].next = self.first
                self.first = self.memory[key]
                
            return self.memory[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.memory:
            self.memory[key].val = value
            if self.memory[key].prev is not None:
                if self.memory[key].next is None:
                    self.last = self.memory[key].prev
                else:
                    self.memory[key].next.prev = self.memory[key].prev
                self.memory[key].prev.next = self.memory[key].next
                
                self.memory[key].prev = None
                self.first.prev = self.memory[key]
                self.memory[key].next = self.first
                self.first = self.memory[key]

        else:
            if len(self.memory) >= self.capacity:
                del self.memory[self.last.key]
                if self.last.prev is not None:
                    self.last = self.last.prev
                    self.last.next = None
                else: # last is also first
                    self.last = None
                    self.first = None

            node = DLLNode(key, value)

            if self.first is None and self.last is None:
                self.first = node
                self.last = node
            else:
                self.first.prev = node
                node.next = self.first
                self.first = node
        
            self.memory[key] = node

        


cmds=["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
args=[[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]        

lRUCache = LRUCache(10)
for cmd,arg in zip(cmds,args):
    print(cmd,arg)
    if cmd == 'put':
        lRUCache.put(*arg)
    else:
        lRUCache.get(*arg)