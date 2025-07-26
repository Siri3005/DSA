class Solution(object):
    def findEvenNumbers(self, digits):
        n = len(digits)
        result = set()
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        a, b, c = digits[i], digits[j], digits[k]
                        if a != 0 and c % 2 == 0:
                            num = a * 100 + b * 10 + c
                            result.add(num)
        
        return sorted(result)
