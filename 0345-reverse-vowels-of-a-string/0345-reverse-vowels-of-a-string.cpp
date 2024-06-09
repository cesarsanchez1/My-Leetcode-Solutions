class Solution {
public:
    string reverseVowels(string s) 
    {
        set<char>vowels = {'a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        
        int size = s.size();
        
        string vowelString = "";
        
        for (int i = 0; i < size; i++){
            
            if (vowels.find(s[i]) != vowels.end()) 
                vowelString += s[i];
        }
        
        int j = vowelString.size()-1;
        
        for (int i = 0; i < size; i++){
            if (vowels.find(s[i]) != vowels.end()){
                s[i] = vowelString[j];
                j-=1;
            }  
        }
        return s;
    }
};