class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        L = 0
        maxOutput = 0

        for R in range(len(fruits)):
            count[fruits[R]] = count.get(fruits[R], 0) + 1

            while len(count) > 2:
                count[fruits[L]] -= 1
                if count[fruits[L]] == 0:
                    del count[fruits[L]]
                L += 1

            maxOutput = max(maxOutput, R - L + 1)

        return maxOutput