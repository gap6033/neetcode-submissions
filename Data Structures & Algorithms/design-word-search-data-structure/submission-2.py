class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.end_of_word = True
        

    def search(self, word: str) -> bool:
        curr_node = self.root
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                for letter in curr_node.children:
                    if self.dfs(i + 1, word, curr_node.children[letter]):
                        return True
                return False
            else:
                if char not in curr_node.children:
                    return False
                curr_node = curr_node.children[char]
        return curr_node.end_of_word

    def dfs(self, start, word, node):
        curr_node = node
        for i in range(start, len(word)):
            char = word[i]
            if char == '.':
                for letter in curr_node.children:
                    if self.dfs(i + 1, word, curr_node.children[letter]):
                        return True
                return False
            else:
                if char not in curr_node.children:
                    return False
                curr_node = curr_node.children[char]
        return curr_node.end_of_word

        
