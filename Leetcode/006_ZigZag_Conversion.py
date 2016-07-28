def convert(s, numRows):
    if numRows == 1:  # extreme case
        return s
    step = 2 * (numRows - 1)
    ret = ''
    for i in range(numRows):
        j = 0  # Good initializaiton of j is the KEY
        while j < len(s):
            if j + i < len(s):  # Execute this line in every row
                ret = ret + s[j + i]
            if i != 0 and i != numRows - 1 and j + step - i < len(s): # middle rows execute this line
                ret = ret + s[j + step - i]
            j = j + step  # At the end, update 
    return ret
