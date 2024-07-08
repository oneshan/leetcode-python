# 0157 - Read N Characters Given Read4
# Date: 2024-06-01
# Runtime: 45 ms, Memory: 16.4 MB
# Submission Id: 1274011741


"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [''] * 4
        remains = n
        curr = 0

        while remains:
            new_chars = min(remains, read4(buf4))
            if new_chars == 0:
                break
            
            for i in range(new_chars):
                buf[curr+i] = buf4[i]
            
            curr += new_chars
            remains -= new_chars
        
        return curr