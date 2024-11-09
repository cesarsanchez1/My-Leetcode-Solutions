class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        #string_lengths = [len(string) for string in strs]
        lengths = []
        for string in strs:
            lengths.append(len(string))
        #print(lengths)
        iterations = min(lengths)
        prefix = ''
        count = 1
        # outer loop inspects the character that might be in the prefix
        for i in range(iterations):
            # every time the ith character is the same in ALL strings
            # append to prefix
            count = 1
            current_character = strs[0][i]
            #print(prefix)
            #print(count)

            # inner loop is checking if the ith character is the same
            for string in strs[1:]:
                if string[i] == current_character:
                    count += 1
                else:
                    return prefix
            if count == len(strs):
                prefix += current_character
        return prefix
