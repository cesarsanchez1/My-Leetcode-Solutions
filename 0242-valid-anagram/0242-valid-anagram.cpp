class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        int size = 26;
        int array1[26] = {0};
        int array2[26] = {0};
        int sub = (int)'a';

        for (int i = 0; i < s.size(); i++)
        {
            int ord = (int)s[i];
            array1[ord-sub]+=1;
        }

        for (int i = 0; i < t.size(); i++)
        {
            int ord = (int)t[i];
            array2[ord-sub]+=1;
        }
        
        for (int i = 0; i < size; i++)
            if (array1[i] != array2[i])
                return false;
        return true;
    }
};