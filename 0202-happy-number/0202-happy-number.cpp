class Solution {
public:
    bool isHappy(int n) 
    {
        string numStr = to_string(n);

        for (int j = 0; j < 100; j++)
        {
            int sum = 0;
            for (int i = 0; i < numStr.size(); i++)
            {
                int temp = int(numStr[i])-48;
                cout << temp << endl;
                sum += (temp*temp);
            }
            if (sum == 1)
                return true;
            numStr = to_string(sum);
        }
        return false;
    }
};