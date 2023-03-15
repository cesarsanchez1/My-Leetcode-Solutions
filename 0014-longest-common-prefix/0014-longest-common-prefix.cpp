class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        int shortest = INT_MAX;
        int size = strs.size();
        
        for (int i = 0; i < size; i++)
            if (shortest > strs[i].size())
                shortest = strs[i].size();
        
        string result = "";
       
        for (int i = 0; i < shortest; i++)
        {
            bool accepted = true;
            char curr = strs[0][i];
            for (int j = 0; j < size; j++)
                if (strs[j][i] != curr)
                {
                    accepted = false;
                    break;
                }
            if (accepted == false)
                break;
            else
                result += curr;
        }
        return result;
    }
};