class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
    val1 = processed(n)
    val2 = processed(processed(n))

    while True:
    	if  val2 == 1:
    		return True
    	if val2 == val1:
    		return False
    	val2 = processed(processed(n)):
    	val1 = processed(n)

	def processed(self,n):
        s = str(n)
        ret = 0
        for i in range(0, len(s)):
        	digit = int(s[i]) * int(s[i])
        	ret = ret + digit
        return ret