class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int left = 0;
        int right = height.size()-1;
        int res = 0;
        
        while (left < right){
            res = max(res, (right-left)*min(height[left], height[right]));
            if (height[left] < height[right])
                left+=1;
            else
                right-=1;
        }
        return res;
    }
};