class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        results = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                lastDay = stack.pop()
                results[lastDay] = i - lastDay

            stack.append(i)

        return results