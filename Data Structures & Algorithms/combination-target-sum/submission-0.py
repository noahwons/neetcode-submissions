class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # i determines which nums we are allowed to add
        # cur is a list of all values we have added so far
        # total is used to maintain the total sum
        def dfs(i, cur, total):
            if total == target:
                # don't directly return cur here
                # The reason is because if we return cur, we still
                # modify it later in the code. This would result in all
                # entries of res being the same array. 
                res.append(cur.copy())
                return
            
            # i >= len(nums) means there are no more nums to consider
            # total > target means it is impossible to reach total == target
            if i >= len(nums) or total > target:
                return
            
            # We can now choose if we will includs nums[i] or not

            # include current num
            cur.append(nums[i])
            # we pass in i here because we want to consider adding the same element
            # cur has been updated so we pass that here
            # total also has been updated
            dfs(i, cur, total + nums[i])
            
            # do not include nums[i]
            # remove value we added for the next decision
            cur.pop()
            # look at next value, keep total the same
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res