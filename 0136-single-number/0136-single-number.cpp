class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {
        int size = nums.size();
        map <int,int> freq;
        
        int result = 0;
        
        for (int i = 0; i < size; i++)
            if (freq.find(nums[i]) == freq.end())
                freq[nums[i]] = 1;
            else
                freq[nums[i]] += 1;
        
        for (int i = 0; i < size; i++)
            if (freq[nums[i]] == 1)
                return nums[i];
          
        return 0;
    }
};