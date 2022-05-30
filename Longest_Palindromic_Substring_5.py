# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1 or not s:
#             return s

#         test = True
#         s_array = s.split()

#         while test:
#             if s_array.reverse() == s_array:
#                 test = False
#                 return s_array
#             else:
#                 del s_array[-1]
#                 del s_array[0]



# def longestPalindrome(s):
#         if len(s) == 1 or not s:
#             return s

#         test = True
#         s_array = s.split()

#         while test:
#             if s_array.reverse() == s_array:
#                 test = False
#                 print(s_array)
#             else:
#                 s_array.pop()
#                 s_array.pop(0)


# longestPalindrome('babad')


arr = 'aba'
array = arr.split()

if array.reverse() == array:
    print('true')

print(array.reverse(), array)