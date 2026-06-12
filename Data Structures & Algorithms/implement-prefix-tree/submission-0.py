class TrieNode:
    def __init__(self):
        self.children = {} # store all 26 chars in hashmap
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
       self.root = TrieNode()


    def insert(self, word: str) -> None:
        # Iterate through all chars in word
        cur = self.root # start at root

        for c in word:
            # Check if char exists in hashmap
            if c not in cur.children:
                # Char has not yet been inserted

                # Use char as key
                cur.children[c] = TrieNode()

            cur = cur.children[c]
        
        # by the end of the loop, cur is set to last char of word
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        # determine if a word exists or not
        cur = self.root

        for c in word:
            if c not in cur.children:
                # if char does not exists, immedietly return false
                return False
            
            # otherwise, move cursor to child node
            cur = cur.children[c]
        
        # cur is last char of word
        # if end of word is true this is an inserted word
        # Otherwise return false
        return cur.endOfWord 


    def startsWith(self, prefix: str) -> bool:
        # Same as search except we do not have to determine if is end
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return True
