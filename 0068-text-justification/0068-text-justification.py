class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        start_idx = 0
        while start_idx < len(words):
            start_idx, line = self.get_line(start_idx, words, maxWidth)
            result.append(line)
        return result
        
    def get_line(self, start_idx, words, max_width):
        cur_length = 0
        i = start_idx
        line = []
        while i < len(words) and (cur_length + len(words[i]) + i - start_idx) <= max_width:
            line.append(words[i])
            cur_length += len(words[i])
            i += 1
        
        # print(i, cur_length, line)
        if i == len(words):
            result = ' '.join(words[start_idx:])
            result += ' ' * (max_width - len(result))
            return i, result        
        else: # (cur_length + len(words[i]) + i - start_idx) > max_width:
            total_spaces = len(line) - 1
            if total_spaces == 0:
                return i, line[0] + ' ' * (max_width - len(line[0]))
            div, mod = divmod(max_width - cur_length, total_spaces)
            result = [line[0]]
            for j in range(1, len(line)):
                result.append(' ' * (div + (1 if j <= mod else 0)))
                result.append(line[j])
            # print(result)
            return i, ''.join(result)
