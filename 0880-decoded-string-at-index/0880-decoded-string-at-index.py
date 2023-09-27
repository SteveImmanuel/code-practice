class Repeat:
    def __init__(self, non_repeat='', repeat='', k=1):
        self.repeat = repeat
        self.non_repeat = non_repeat
        self.k = k
    
    def repeat_len(self):
        return 0 if self.repeat == '' else len(self.repeat)
        
    def non_repeat_len(self):
        return len(self.non_repeat)
    
    def single_len(self):
        return len(self.repeat) + len(self.non_repeat)
    
    def __len__(self):
        return (len(self.repeat) + len(self.non_repeat)) * self.k

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        tape = Repeat()
        for char in s:
            if 48 <= ord(char) <= 57: # digit
                tape.k += int(char) - 1
                tape = Repeat(repeat=tape)
            else:
                tape.non_repeat += char
            
        return self.find_kth(tape, k)
    
    def find_kth(self, tape, k):
        k = k % tape.single_len()
        if k == 0:
            k += tape.single_len()
        
        if k <= tape.repeat_len() or tape.non_repeat_len() == 0:
            return self.find_kth(tape.repeat, k)
        else:
            k -= tape.repeat_len()
            return tape.non_repeat[k-1]
            
            