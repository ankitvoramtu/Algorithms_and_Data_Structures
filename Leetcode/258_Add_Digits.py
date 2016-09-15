class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:       	
	        s = str(num)
	        num = 0
	        for i in range(0, len(s)):
	        	num = num + int(s[i])
	    return num


???????????

Solution 1 – Time O (1) Space O (1)
public class Solution {
    public int addDigits(int num) {
		return 1 + ((num - 1) % 9);
    }
}
Solution 2 – Time O (1) Space O (1)
    public int addDigits(int num) {
        if (num == 0) {
            return 0;
        }
        if (num % 9 == 0) {
            return 9;
        }
        else {
            return num % 9;
        }
}
