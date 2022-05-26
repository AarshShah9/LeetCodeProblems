from tkinter import N


class Solution:
    def findMedianSortedArrays(self, nums1: list[int],
                               nums2: list[int]) -> float:

        total_len = len(nums1) + len(nums2)
        new_list = sorted(nums1 + nums2)

        if ((total_len) % 2) != 0:
            median_index = (total_len // 2)
            return new_list[median_index]
        else:
            (median_index_1,
             median_index_2) = ((total_len // 2) - 1), (total_len // 2)
            return (((new_list[median_index_1] + new_list[median_index_2]) /
                     2))


newInstance = Solution()

test = newInstance.findMedianSortedArrays([1, 4], [7, 6, 7, 8, 10, 100])
print(test)
