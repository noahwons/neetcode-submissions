class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False # init false
        
        # How Node insertion works
        # Example: insert a word beginnig with "a":
        # children["a"] = TrieNode()
        # Explanation: Maps "a" to a TrieNode which may contain a-z chars. O(1) lookup
 

class PrefixTree:
    def __init__(self):
       self.root = TrieNode() # Create empty tree


    def insert(self, word: str) -> None:
        # iterate through all chars in word

        cur = self.root # begin at root

        for c in word:
            # does this char exist in trie?
            if c not in cur.children:
                # if not yet in hashmap, has not been inserted yet
                # Note: This will generate the entire word regardless
                cur.children[c] = TrieNode()
            
            # Skip if character already exists
            cur = cur.children[c] # move to search the children of c

        # cur is set to last char of the word
        cur.endOfWord = True # mark as a word


    def search(self, word: str) -> bool:
        # iterate through all chars in word

        cur = self.root # start at root

        for c in word:
            if c not in cur.children:
                # we can return false here because
                # there are characters missing, thus
                # word not found
                return False
            
            # increment
            cur = cur.children[c]

        return cur.endOfWord # returns the flag


    def startsWith(self, prefix: str) -> bool:
        # find a word that starts at the prefix
        cur = self.root # start at root

        for c in prefix:
            if c not in cur.children:
                # Prefix does not exist
                return False
            
            # increment
            cur = cur.children[c]
        return True
