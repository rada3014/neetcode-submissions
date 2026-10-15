class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_str= ''
        for i in s:
            if i.isalnum():
                new_str = new_str+i.lower()


        start = 0
        end = len(new_str)-1

        while (start<end):

            if new_str[start] == new_str[end]:
                start=start+1
                end = end-1
            else:
                return False
        return True
        