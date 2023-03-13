class Solution {
public:
    vector<vector<int>> generate(int numRows) 
    {
        if (numRows == 1)
            return {{1}};
        if (numRows == 2)
            return {{1},{1,1}};

        vector <int> array = {1,1};
        vector<vector<int>>result = {{1},{1,1}};

        int size = array.size();
       
        for (int j = 0; j < numRows-2; j++)
        {
            vector <int> newArray = {1};
            for (int i = 0; i < size-1; i++)
            {
                int temp = array.at(i) + array.at(i+1);
                newArray.push_back(temp);
                //cout << temp << endl;
            }
            newArray.push_back(1);
            result.push_back(newArray);
            array = newArray;
            size = array.size();
        }
        return result;        
    }
};