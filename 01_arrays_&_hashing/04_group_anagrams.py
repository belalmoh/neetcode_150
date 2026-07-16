from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        for s in strs:
            output.append("".join(sorted(s)))


        sortedMap = {}

        for i, v in enumerate(output):
            if v in sortedMap:
                sortedMap[v].append(i)
            else:
                sortedMap[v] = [i]

        result = []
        for values in sortedMap.values():
            temp = []
            for v in values:
                temp.append(strs[v])
            result.append(temp)

        return result



if __name__ == '__main__':
    print(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]))
