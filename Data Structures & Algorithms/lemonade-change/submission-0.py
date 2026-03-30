class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        if bills[0] != 5:
            return False

        fives = 0
        tens = 0
        twenties = 0

        for bill in bills:

            if bill == 5:
                fives += 1

            # Scenario 1: Tens
            elif bill == 10:
                if fives >= 1:
                    fives -= 1
                    tens += 1
                else:
                    return False

            # Scenario 2: Twenty
            elif bill == 20:
                if fives >= 1 and tens >= 1:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False



        return True
                 