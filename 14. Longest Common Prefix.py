"""
14. Longest Common Prefix
url: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

def longestCommonPrefix(strs) -> str:
    s1 = strs[0]
    s2 = strs[1]
    s3 = strs[2]

    min_len = len(s1) if len(s1) < len(s2) else len(s2)
    min_len = len(s3) if len(s3) < min_len else min_len

    output = ""

    for i in range(min_len):
        if s1[i] == s2[i] == s3[i]:
            output = output + s1[i]
        else:
            break

    print(output)

longestCommonPrefix(["dog","racecar","car"])

