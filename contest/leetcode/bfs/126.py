from collections import deque

class Solution:
    def __init__(self):
        self.wordList = []

        self.graph = [[]]
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

                for next_x in self.graph[x]:
                    if(not self.vis[next_x]):
                        next_v = v[:]
                        next_v.append(next_x)
                        q.append((next_x, depth+1, next_v))
        
    def isOneLetterDifferent(self, i, j):
        wordLen = len(self.wordList[i])

        different_cnt = 0
        for k in range(wordLen):
            if(self.wordList[i][k] != self.wordList[j][k]):
                different_cnt = different_cnt + 1

        return different_cnt == 1


    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        self.wordList = wordList

        n = len(wordList)
        self.graph = [[] for i in range(n)]
        self.vis = [False for i in range(n)]

        for i in range(n):
            for j in range(i+1 ,n):
                if self.isOneLetterDifferent(i, j):
                    self.graph[i].append(j)
                    self.graph[j].append(i)

        for i in range(n):
            if(wordList[i] == beginWord):
                self.start = i
            elif(wordList[i] == endWord):
                self.end = i
        
        if(self.end == -1):
            return []
        
        self.bfsWithLayer()

        word_ret = []
        if(len(self.ret) == 0):
            return []
        
        for v in self.ret:
            word_v = [wordList[x] for x in v]
            word_ret.append(word_v)
        return word_ret    
