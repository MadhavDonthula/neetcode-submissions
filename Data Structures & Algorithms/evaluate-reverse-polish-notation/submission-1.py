class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arithmetic_conversion = {"+": (lambda a, b: a + b), "*": (lambda a,b: a * b), "-": lambda a, b: a - b, "/": lambda a,b: a/b}
        nums = []
        for x in tokens: 
            if x in arithmetic_conversion.keys(): 
                second = nums.pop()
                first = nums.pop()
                res = arithmetic_conversion[x](first,second)
                nums.append(int(res))
            else:
                nums.append(int(x))
        return nums[-1]

