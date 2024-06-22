#Trie concept in python
#Basically trie is used to store dynamic string and mostly used for robust storing of strings
#It is used for search operaton ,inserting and finding the prefix

class TrieNode:
    def __init__(self):
        self.isEnding = False 
        self.store = dict()
 
class Trie:
    def __init__(self):
        self.root = TrieNode()
 
    def insertWord(self, word):
        currRoot = self.root 
        n = len(word)
        for index in range(n):
            if word[index] not in currRoot.store:
                currRoot.store[word[index]] = TrieNode()
 
            currRoot = currRoot.store[word[index]]
        currRoot.isEnding = True 
        print(word, "inserted successfully in the trie")
    def searchWord(self, word):
        currNode = self.root 
        n = len(word)
        for index in range(n):
            ch = word[index]
            if ch not in currNode.store:
                return False 
            currNode = currNode.store[ch]
        return currNode.isEnding 
    def startsWith(self, word):
        currNode = self.root 
        n = len(word)
        for index in range(n):
            ch = word[index]
            if ch not in currNode.store:
                return False 
            currNode = currNode.store[ch]
        return True
obj = Trie()
obj.insertWord("cat")
obj.insertWord("computer")
obj.insertWord("compute")

#insertion completed

print(obj.startsWith("com"))
print(obj.startsWith("comput"))
print(obj.startsWith("coma"))

#prefix finding completed 

if obj.searchWord("cat"):
    print("cat is present in trie")
else:
    print("cat is not present in trie")

if obj.searchWord("compute"):
    print("compute is present in trie")
else:
    print("compute is not present in trie") 

#searching the word will takes place    


##Tire concept(Problem 2)
##211. Design Add and Search Words Data Structure(Leetcode)

class TrieNode:
    def __init__(self):
        self.isEnding = False 
        self.store = dict()
 
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
 
    def addWord(self, word):
        currRoot = self.root 
        n = len(word)
        for index in range(n):
            if word[index] not in currRoot.store:
                currRoot.store[word[index]] = TrieNode()
 
            currRoot = currRoot.store[word[index]]
        currRoot.isEnding = True 

    def search(self, word):
        currRoot = self.root 
        n = len(word)
        def helper(currRoot, index):
            if index == n:
                return currRoot.isEnding
            elif word[index] != '.' and word[index] not in currRoot.store:
                return False
 
            if word[index] != '.':
                return helper(currRoot.store[word[index]], index + 1)
 
            for ch in currRoot.store.keys():
                if helper(currRoot.store[ch], index + 1):
                    return True
            return False
        
##KMP algorithm

def kmpAlgorithm(word, pattern):
    n, m = len(word), len(pattern)
    mainIndex, patternIndex = 1, 0
    lps = [0] * m
    while mainIndex < m:
        while mainIndex < m and pattern[mainIndex] == pattern[patternIndex]:
            lps[mainIndex] = patternIndex + 1 
            mainIndex += 1 
            patternIndex += 1 
        patternIndex = 0 
        mainIndex += 1
    wordIndex, patternIndex = 0, 0 
    while wordIndex < n:
        if word[wordIndex] == pattern[patternIndex]:
            wordIndex += 1 
            patternIndex += 1 
            if patternIndex == m:
                return wordIndex - m 
        else:
            while patternIndex > 0 and word[wordIndex] == pattern[patternIndex]:
                patternIndex = lps[patternIndex]
            wordIndex += 1 
    return -1
word = "abcdpqrsabcdemfabcder"
pattern = "abcdefabcd"
index = kmpAlgorithm(word, pattern)
if index == -1:
    print(pattern, "not found")
else:
    print(pattern, "found at index:", index)        