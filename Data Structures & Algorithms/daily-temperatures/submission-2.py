class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if not isinstance(temperatures,list):
            return []

        if len(temperatures) == 1:
            return [0]

        stack = []
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)

        return answer