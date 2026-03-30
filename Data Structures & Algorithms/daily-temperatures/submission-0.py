class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if not isinstance(temperatures,list):
            return []

        if len(temperatures) == 1:
            return [0]


        n = len(temperatures)
        answer = [0] * n
        stack = []

        stack.append(0)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            daysBefore = 1
            reversalIndex = i - 1
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index

            stack.append(i)

        return answer
