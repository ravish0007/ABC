class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}
        
        for item in strs:
            sorted_string = ''.join(sorted(item))
            
            if sorted_string in hash_map:
                hash_map[sorted_string].append(item)
            else:
                hash_map[sorted_string] = [item]
        return list(hash_map.values())
