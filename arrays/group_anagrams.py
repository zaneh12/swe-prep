from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the together. You can return the answer in any order.
        """
        # O(m*n*log(n)) and O(m*n)
        # groups = defaultdict(str)

        # for string in strs:
        #     if "".join(sorted(string)) in groups:
        #         groups["".join(sorted(string))].append(string)
        #     else:
        #         groups["".join(sorted(string))] = [string]
        # return list(groups.values())

        # O(m*n)
        groups = defaultdict(list) # we want to be able to append the first object to the list

        for string in strs:
            arr = [0]*26
            for i in string:
                arr[ord(i) - ord('a')] +=1  
            groups[tuple(arr)].append(string)

        return list(groups.values())
        # return groups
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))