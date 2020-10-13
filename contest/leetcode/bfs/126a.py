from collections import deque

class Solution:
    def __init__(self):
        self.wordList = []
        self.wordLen = 0

        self.look_up = {}

        self.vis = []
        self.start = -1
        self.end = -1

        self.ret = []


    def bfsWithLayer(self):
        q = deque()
        q.append((self.start,1,[self.start]))

        min_depth = -1

        while(q):
            if(min_depth != -1):
                break

            layer_size = len(q)
            for _ in range(layer_size):
                x, depth, v = q.popleft()
                self.vis[x] = True

                if(x == self.end):
                    if(min_depth == -1):
                        min_depth = depth
                    self.ret.append(v)

                x_word = self.wordList[x]
                for i in range(self.wordLen):
                    next_pattern = x_word[:i] + "*" + x_word[i+1:]
                    if next_pattern in look_up:
                        for next_x in look_up[next_pattern]:
                            if(not self.vis[next_x]):
                                next_v = v[:]
                                next_v.append(next_x)
                                q.append((next_x, depth+1, next_v))
                    
        

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        self.wordLen = len(beginWord)

        self.wordList = wordList

        n = len(wordList)
        self.graph = [[] for i in range(n)]
        self.vis = [False for i in range(n)]

        for i in range(n):
            if(wordList[i] == beginWord):
                self.start = i
            elif(wordList[i] == endWord):
                self.end = i

        if(self.end == -1):
            return []

        # build graph
        self.look_up = {}
        word_idx = 0
        for word in wordList:
            for i, e in enumerate(word):
                key = word[:i] + '*' + word[i+1:]
                self.look_up.setdefault(key, []).append(word_idx)
            word_idx = word_idx + 1

        
        self.bfsWithLayer()

        word_ret = []
        if(len(self.ret) == 0):
            return []
        
        for v in self.ret:
            word_v = [wordList[x] for x in v]
            word_ret.append(word_v)
        return word_ret    
