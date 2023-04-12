class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        components = list(filter(lambda x: x != '' and x != '.', components))
        
        # start_found = False
        # first_stage_res = []
        # for i, component in enumerate(components):
        #     if component == '.' or (component == '..' and not start_found):
        #         continue
        #     elif component != '.':
        #         first_stage_res.append(component)
        #         start_found = True
                
        final_res = deque([])
        counter = 0
        for i in range(len(components) - 1, -1, -1):
            if components[i] != '..' and counter == 0:
                final_res.appendleft(components[i])
            elif components[i] != '..' and counter > 0:
                counter -= 1
            elif components[i] == '..':
                counter += 1
                
        final_res = '/'.join(final_res)
        final_res = '/' + final_res
        return final_res