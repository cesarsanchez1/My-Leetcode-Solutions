class Solution {
public:
    int firstUniqChar(string s) 
    {
        map <char, int> freq;
        int size = s.size();
        
        for (int i = 0; i < size; i++)
            if (freq.find(s[i]) == freq.end())
                freq[s[i]] = 1;
            else
                freq[s[i]] += 1;
        
        for (int i = 0; i < size; i++)
            if (freq[s[i]] == 1)
                return i;
        return -1;
    }
};