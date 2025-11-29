from typing import List

#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) > 0:
            result = strs.pop(0)

            for word in strs:
                while(not word.startswith(result)):
                    result = result[:-1]

                if result == "":
                    return ""

        return result
