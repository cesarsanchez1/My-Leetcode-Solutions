class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        freq = {}
        j = 0
        res = 0
        ret = ""

        for message in messages:
            wordCount = 0
            message += " "
            for letter in message:
                if letter == " ":
                    wordCount += 1
            if senders[j] in freq:
                freq[senders[j]] += wordCount
            else:
                freq[senders[j]] = wordCount
            if res < freq[senders[j]]:
                res = freq[senders[j]]
                ret = senders[j]
            if res == freq[senders[j]]:
                if ret < senders[j]:
                    ret = senders[j]
            j+=1
        return ret
            


