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
        #optimal sliding window + 2 pointer 
        left=0
        seen={}
        max_len=0
        for right in range(len(s)):
            if seen[s[right]]==1 and seen[s[right]]>=left:
                left=seen[right]+1
            seen[s[right]]=right
            max_len=max(max_len,right-left+1)
        return max_len