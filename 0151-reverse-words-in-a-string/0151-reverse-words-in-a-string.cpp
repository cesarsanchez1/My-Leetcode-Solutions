class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        vector<string>words;
        string res;
        
        while (ss >> word){
            words.push_back(word);
        }
        
        for (int i = words.size()-1; i>=0; i--)
        {
            cout << words[i] << endl;
             res+=words[i];
            if (i!=0)
                res+=" ";
                
        }
        
        return res;
        
    }
};