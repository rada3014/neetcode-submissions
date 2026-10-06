class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = dict()
        hash_map_t = dict()
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in hash_map_s:
                    hash_map_s[s[i]]=1
                else:
                    hash_map_s[s[i]]=hash_map_s[s[i]]+1
                if t[i] not in hash_map_t:
                    hash_map_t[t[i]]=1
                else:
                    hash_map_t[t[i]]=hash_map_t[t[i]]+1
        return hash_map_s==hash_map_t