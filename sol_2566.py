class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)      #converting num into str
        for digit in num_str:
            if digit != '9':      #to get a max_str we need to replace any element which are not equal to 9
                max_str = num_str.replace(digit, '9')      #replace that digit into 9
                break
        else:
            max_str = num_str        #if all digits are 9 we simply mark it as max_str
        for digit in num_str:      
            if digit != '0':
                min_str = num_str.replace(digit, '0')      #to get min_str we need to replace element with 0 as it is the least element
                break
        else:
            min_str = num_str        #if elements are 0 we simply mark it as min_str

        return int(max_str) - int(min_str)      #then we return int(max_str) - int(min_str)  as it is in str we need to convert it into int

