class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums2)
        answer = []
        for i in nums1:
            if c[i]>0:
               answer.append(i)
               c[i] -= 1
            return answer 