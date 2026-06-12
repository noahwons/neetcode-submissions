class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Formula: index1 + index2 = target
        # numbers[index2] = target - numbers[index1]

        # Use hash map for O(1) look up, determine if target exists
        # Since sorted, 
        my_map = {}
        lp = 0
        rp = len(numbers) - 1
        result = []
        while lp < rp:
            # If lp + rp > target rp is not included in any pairs when rp = n and lp = 0
            if target < numbers[lp] + numbers[rp]:
                rp -= 1
            elif target > numbers[lp] + numbers[rp]:
                # This means that lp must be incremented because 0 + rp was too smapp
                lp += 1
            else:
                result.append(lp + 1)
                result.append(rp + 1)
                return result

        return result