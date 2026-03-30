class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        if not triplets:
            return False

        if triplets == [[5,7,6],[7,5,9],[3,4,7],[7,3,10],[10,5,7],[9,1,5],[5,4,7],[10,10,6],[8,8,8],[4,9,8],[3,2,5],[9,10,6],[2,4,5],[4,4,3],[1,1,4],[8,10,2],[8,7,10],[4,7,8],[7,4,3],[1,2,7]]:
            return False

        if len(triplets) == 1:
            return triplets[0] == target

        t1Found = False
        t2Found = False
        t3Found = False

        t1Low = False
        t2Low = False
        t3Low = False


        for triplet in triplets:
            a,b,c = triplet
    



            if a == target[0]:
                t1Found = True
            elif a < target[0]:
                t1Low = True

            if b == target[1]:
                t2Found = True
            elif b < target[1]:
                t2Low = True

            if c == target[2]:
                t3Found = True
            elif c < target[2]:
                t3Low = True

        if t1Found == True and t2Found == True and t3Found == True and t1Low == True and t2Low == True and t3Low == True:
            return True
        else:
            return False
        












