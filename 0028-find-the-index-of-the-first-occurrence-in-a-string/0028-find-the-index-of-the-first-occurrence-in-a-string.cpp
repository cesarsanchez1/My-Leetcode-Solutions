class Solution {
public:
    int strStr(string haystack, string needle) 
    {
        int needleSize = needle.size();
        int haystackSize = haystack.size();
        
        if (needleSize > haystackSize)
            return -1;
        
        for (int i = 0; i < (haystackSize - needleSize)+1; i++)
            if (needle == haystack.substr(i, needleSize))
                return i;
        return -1;
    }
};