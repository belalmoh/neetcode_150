from typing import List
from collections import Counter, defaultdict


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

class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedWord = ''.join(sorted(s))
            res[sortedWord].append(s)

        return list(res.values())

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1

            result[tuple(count)].append(word)

        return list(result.values())

if __name__ == '__main__':
    print(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]))
    print(Solution2().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
    print(Solution3().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
