class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""
        
        # Insert all words into the Trie
        for word in strings:
            self.insert(word)
        
        # Find the longest common prefix
        prefix = ""
        node = self.root
        
        while node and len(node.children) == 1 and not node.is_end_of_word:
            char = next(iter(node.children))  # Get the single child character
            prefix += char
            node = node.children[char]
        
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    
    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""
    
    trie = LongestCommonWord()
    strings = ["apple"]
    assert trie.find_longest_common_word(strings) == "apple"
    
    print("All tests passed!")