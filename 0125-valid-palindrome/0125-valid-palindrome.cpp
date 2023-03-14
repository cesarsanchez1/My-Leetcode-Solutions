class Solution {
public:
    bool isPalindrome(string s) 
    {
        string bank = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
        string numBank = "0123456789";
        set <char> mySet(bank.begin(), bank.end());
        set <char> myNumSet(numBank.begin(), numBank.end());

        int size = s.size();
        string check = "";
        char temp = ' ';

        for (int i = 0; i < size; i++)
            if ( (mySet.find(s[i]) != mySet.end()) || (myNumSet.find(s[i]) != myNumSet.end()) )
                check += tolower(s[i]);

        for (int i = 0; i < check.size(); i++)
            if (check[i] != check[check.size()-1-i])
                return false;
        return true;
    }
};