class Solution 
{
public:
    int removeDuplicates(vector<int>& nums) 
    {
        int j = 0;
        int size = nums.size();
        set<int>mySet;

        for(int i = 0; i < size; i++)
        {
            if (mySet.find(nums[i]) == mySet.end())
            {
                nums[j] = nums[i];
                j+=1;
            }
            mySet.insert(nums[i]);
        }
        return j;
    }
};