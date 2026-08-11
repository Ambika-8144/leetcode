class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #bruteforce 
        max_len=0
        for i in range(len(s)):
            seen=set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                l=j-i+1
                max_len=max(max_len,l)
                seen.add(s[j])
        return max_len
        