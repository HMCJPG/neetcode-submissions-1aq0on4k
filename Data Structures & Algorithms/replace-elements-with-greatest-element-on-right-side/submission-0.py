class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Initialize with -1 as the rightmost element will always be replaced by -1
        max_so_far = -1
        
        # Traverse the array backwards (from last element to first)
        for i in range(len(arr) - 1, -1, -1):
            current_val = arr[i]
            
            # Replace current element with the greatest seen so far
            arr[i] = max_so_far
            
            # Update the max_so_far for the next iteration (the next element to the left)
            max_so_far = max(max_so_far, current_val)
            
        return arr