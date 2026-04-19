class Solution:

    def encode(self, strs: List[str]) -> str:
        self.split_points = []
        if not strs:
            return ""
        self.split_points = [len(strs[0]) - 1]
        encoded_str = strs[0]
        for i in range(1, len(strs)):
            next_split_point = self.split_points[-1] + len(strs[i])
            encoded_str += strs[i]
            self.split_points.append(next_split_point)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded = []
        prev_index = 0
        for index in self.split_points:
            decoded.append(s[prev_index:index + 1])
            prev_index = index + 1
        return decoded



