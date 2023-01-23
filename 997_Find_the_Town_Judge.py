"""
997. Find the Town Judge

Easy

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town
judge. If the town judge exists, then: The town judge trusts nobody. Everybody (except for the town judge) trusts the
town judge. There is exactly one person that satisfies properties 1 and 2. You are given an array trust where trust[
i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1


Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        List1 = []
        List2 = []

        if trust == []:           #conditions are added in this block as per input defined & expected output by program
            if n == 1:
                return 1
            else:
                return -1

        else:
            def Extract(trust):          # defining function to extract elements from input list andadding it to new lists
                for i in trust:
                    List1.append(i[0])
                    List2.append(i[1])

            Extract(trust)              #Calling Function

            def most_frequent(List2):    # defining function to get  most frequent element from list
                return max(set(List2), key=List2.count)

            most_frequent(List2)
            resultt = most_frequent(List2)  # result

        if resultt in List1 or len(set(List1)) < (n - 1):  # len(set(List1)) != len(List1):# DO NOT USE COMMENTED
            # CONDITION
            return -1

        else:
            return resultt
