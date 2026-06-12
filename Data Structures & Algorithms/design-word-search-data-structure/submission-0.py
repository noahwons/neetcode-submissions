class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    # "." could match any character,
                    # run dfs on all current characters
                    for child in cur.children.values():
                        # run dfs
                        if dfs(i + 1, child): # i + 1 to skip "."
                            # found matching path
                            return True
                    return False
                else:
                    if c not in cur.children:
                        # we know for sure word does not exist
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        
        return dfs(0, self.root)

