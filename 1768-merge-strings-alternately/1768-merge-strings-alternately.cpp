class Solution {
public:
    string mergeAlternately(string word1, string word2) {

        int size1 = word1.size();
        int size2 = word2.size();

        int minSize = min(size1, size2);
        int maxSize = max(size1, size2);
        string res = "";

        cout << minSize << endl;

        for (int i = 0; i < minSize; i++){
            res += word1[i];
            res += word2[i];
        }

        for (int i = minSize; i < maxSize; i++){
            if (size1 > minSize)
                res += word1[i];
            if (size2 > minSize)
                res += word2[i];
        }
        
        return res;
    }
};