class TrieNode:

    def __init__(self):
        self.next = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.root.next['$'] = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        ptr = self.root
        for c in word + '$':
            if c not in ptr.next:
                ptr.next[c] = TrieNode()
            ptr = ptr.next[c]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ptr = self.root
        for c in word + '$':
            if c not in ptr.next:
                return False
            ptr = ptr.next[c]
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ptr = self.root
        for c in prefix:
            if c not in ptr.next:
                return False
            ptr = ptr.next[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
