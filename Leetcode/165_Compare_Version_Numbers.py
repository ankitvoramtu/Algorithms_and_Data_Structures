class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list1 = version1.split('.')
        list2 = version2.split('.')

        n = abs(len(list1) - len(list2))

        if len(list1) < len(list2):
            for i in range(0, n):
                list1.append('0')
        else:
            for i in range(0, n):
                list2.append('0')

        i = 0
        while i < len(list1) and i < len(list2):
            if int(list1[i]) > int(list2[i]):
                return 1
            if int(list1[i]) < int(list2[i]):
                return -1
            else:
                i = i + 1
        return 0

# Time: O(n)
# Space: O(n)
