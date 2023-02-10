class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        set1 = set(s)
        set2 = set(t)
        
        if set1 != set2:
            return False
        if len(s) != len(t):
            return False
        
        freq1 = {}

        for item in s:
            if item in freq1:
                freq1[item] += 1
            else:
                freq1[item] = 1

        freq2 = {}

        for item in t:
            if item in freq2:
                freq2[item] += 1
            else:
                freq2[item] = 1
        
        for item in set1:
            if freq1[item] != freq2[item]:
                return False
        return True



