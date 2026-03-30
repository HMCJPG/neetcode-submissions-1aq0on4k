class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = []

        results = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                lastDay = stack.pop()
                results[lastDay] = i - lastDay

            stack.append(i)

        return results
