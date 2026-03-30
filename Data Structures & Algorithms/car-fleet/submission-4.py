class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        stack = []


        for i in range(len(position)):

            cars.append([position[i], speed[i]])

        cars.sort(key = lambda x:x[0], reverse = True)

        for p,s in cars:
            tta = (target - p) / s

            if not stack or tta > stack[-1]:
                stack.append(tta)

        return len(stack)