class Solution:
    def __init__(self):
        self.output = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr_index = 0
        curr_seq = []
        self.helper(candidates, curr_seq, curr_index, target, 0)
        return self.output

    def helper(self, candidates, curr_seq, curr_index, target, curr_sum):
        if curr_sum == target:
            self.output.append(curr_seq.copy())
            return
        if curr_index == len(candidates):
            return
        if curr_sum > target:
            return
        
        curr_num = candidates[curr_index]
        curr_seq.append(curr_num)
        self.helper(candidates, curr_seq, curr_index + 1, target, curr_sum + curr_num)
        curr_seq.pop()
        while curr_index < len(candidates) and curr_num == candidates[curr_index]:
            curr_index += 1
        self.helper(candidates, curr_seq, curr_index, target, curr_sum)
