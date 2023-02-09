class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        prefix_dict = defaultdict(set)
        for name in ideas:
            prefix_dict[name[0]].add(name[1:])

        total_ideas = 0
        prefixes = list(prefix_dict.keys())
        for i in range(len(prefixes)):
            for j in range(i+1, len(prefixes)):
                len_prefixes_i = len(prefix_dict[prefixes[i]])
                len_prefixes_j = len(prefix_dict[prefixes[j]])
                len_intersect = len(prefix_dict[prefixes[i]].intersection(prefix_dict[prefixes[j]]))
                # print(prefixes[i], prefixes[j], len_intersect, len_prefixes_i, len_prefixes_j)
                total_ideas += (len_prefixes_i - len_intersect) * (len_prefixes_j - len_intersect) * 2
        return total_ideas
    
#     def distinctNames(self, ideas: List[str]) -> int:
#         suffix_dict = defaultdict(set)
#         for name in ideas:
#             suffix_dict[name[1:]].add(name[0])

#         total_ideas = 0
#         suffixes = list(suffix_dict.keys())
#         for i in range(len(suffixes)):
#             for j in range(i+1, len(suffixes)):
#                 len_suffixes_i = len(suffix_dict[suffixes[i]])
#                 len_suffixes_j = len(suffix_dict[suffixes[j]])
#                 len_intersect = len(suffix_dict[suffixes[i]].intersection(suffix_dict[suffixes[j]]))
#                 # print(suffixes[i], suffixes[j], len_intersect, len_suffixes_i, len_suffixes_j)
#                 total_ideas += (len_suffixes_i - len_intersect) * (len_suffixes_j - len_intersect) * 2
#         return total_ideas