class CacheItem:
    def __init__(self, key, val, freq, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = nxt
        
class LFUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.cache_dict = {}
        self.last_item_for_freq = {}
        self.capacity = capacity
        self.cur_capacity = 0
    
    def print_list(self):
        it = self.head
        print('[', end='')
        while it is not None:
            print(f'{it.key}:{it.val}:{it.freq}, ', end='')
            it = it.next
        print(']')
    
    def print_freq(self):
        for key, val in self.last_item_for_freq.items():
            print(key, f'{val.key}:{val.val}:{val.freq}')
            
    def update_order(self, item):
        prev_freq = item.freq - 1
        swap = True
        # print('before:', end='')
        # self.print_list()
        # self.print_freq()
        
        if prev_freq != 0 and self.last_item_for_freq[prev_freq] == item:
            swap = False
            if item.prev is not None and item.prev.freq == prev_freq:
                self.last_item_for_freq[prev_freq] = item.prev
            else:
                self.last_item_for_freq.pop(prev_freq)
        
        if item.next != None: # not the last element
            if item.freq in self.last_item_for_freq or (prev_freq in self.last_item_for_freq and swap):
                if item.prev is not None:
                    item.prev.next = item.next
                item.next.prev = item.prev
                if item.next.prev is None:
                    self.head = item.next
            
                if item.freq in self.last_item_for_freq:
                    last_item = self.last_item_for_freq[item.freq]
                else:
                    last_item = self.last_item_for_freq[prev_freq]
                
                item.next = last_item.next
                last_item.next = item
                item.prev = last_item

                if item.next is not None:
                    item.next.prev = item             
        
        self.last_item_for_freq[item.freq] = item
        # print('after: ', end='')
        # self.print_list()
        # self.print_freq()
        # print()

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            self.cache_dict[key].freq += 1
            self.update_order(self.cache_dict[key])
            return self.cache_dict[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache_dict:
            self.cache_dict[key].val = value
            self.cache_dict[key].freq += 1
            self.update_order(self.cache_dict[key])
        else:
            if self.cur_capacity == self.capacity:
                lfu_item = self.head
                self.head = lfu_item.next
                if self.head is not None:
                    self.head.prev = None
                
                self.cache_dict.pop(lfu_item.key)
                if self.last_item_for_freq[lfu_item.freq] == lfu_item:
                    self.last_item_for_freq.pop(lfu_item.freq)
                
                
                self.cur_capacity -= 1
                
            
            item = CacheItem(key, value, 1, None, self.head) # put as the first element
            if self.head is not None:
                self.head.prev = item
            self.head = item
            
            self.update_order(item)
            self.cache_dict[key] = item
            self.cur_capacity += 1
            
            
                
            

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# class CacheItem:
#     def __init__(self, key, val, freq, prev=None, nxt=None):
#         self.key = key
#         self.val = val
#         self.freq = freq
#         self.prev = prev
#         self.next = nxt
        
# class LFUCache:
#     def __init__(self, capacity: int):
#         self.head = None
#         self.cache_dict = {}
#         self.capacity = capacity
#         self.cur_capacity = 0
        
#     def update_order(self, item):
#         if item.next != None: # not the last element
#             if item.freq >= item.next.freq:
#                 temp_iter = item.next
#                 while temp_iter.next is not None and temp_iter.next.freq <= item.freq:
#                     temp_iter = temp_iter.next

#                 if item.prev is not None:
#                     item.prev.next = item.next
#                 item.next.prev = item.prev
#                 if item.next.prev is None:
#                     self.head = item.next

#                 item.next = temp_iter.next
#                 temp_iter.next = item
#                 item.prev = temp_iter

#                 if item.next is not None:
#                     item.next.prev = item

#     def get(self, key: int) -> int:
#         if key in self.cache_dict:
#             self.cache_dict[key].freq += 1
#             self.update_order(self.cache_dict[key])
#             return self.cache_dict[key].val
#         return -1
        

#     def put(self, key: int, value: int) -> None:
#         if self.capacity == 0:
#             return
        
#         if key in self.cache_dict:
#             self.cache_dict[key].val = value
#             self.cache_dict[key].freq += 1
#             self.update_order(self.cache_dict[key])
#         else:
#             if self.cur_capacity == self.capacity:
#                 lfu_item = self.head
#                 self.head = lfu_item.next
#                 if self.head is not None:
#                     self.head.prev = None
#                 self.cache_dict.pop(lfu_item.key)
#                 self.cur_capacity -= 1
                
            
#             item = CacheItem(key, value, 1, None, self.head) # put as the first element
#             if self.head is not None:
#                 self.head.prev = item
#             self.head = item
            
#             self.update_order(item)
#             self.cache_dict[key] = item
#             self.cur_capacity += 1
            
            
                
            

# # Your LFUCache object will be instantiated and called as such:
# # obj = LFUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)