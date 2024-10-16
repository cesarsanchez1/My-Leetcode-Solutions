class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        HashSet<Character> charSet = new HashSet<>();
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            // Remove characters from the left until the current character is unique in the window
            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }
            
            // Add the current character to the set
            charSet.add(s.charAt(right));
            
            // Update the longest length found
            longest = Math.max(longest, right - left + 1);
        }

        return longest;
    }

}