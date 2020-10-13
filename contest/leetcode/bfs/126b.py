from collections import deque

# Word Ladder II
class Solution:
    def __init__(self):
        # The graph is implemented in adjacency list, and nodes are defined by words' number)
        self.graph = [[]]
        self.vis = []

        # The entrance node and the exit node number
        self.start = -1
        self.end = -1

        # The return paths in graph
        self.ret = []


    # BFS the graph with the order of level. Here I write layer which just means level. 
    def bfsWithLayer(self):
        q = deque()
        q.append((self.start,1,[self.start]))

        min_depth = -1

        while(q):
            # If found the level, then other levels will not be answers. 
            if(min_depth != -1):
                break
            
            # For each level
            layer_size = len(q)
            for _ in range(layer_size):
                x, depth, v = q.popleft()
                self.vis[x] = True

                if(x == self.end):
                    # Find the Level
                    if(min_depth == -1):
                        min_depth = depth
                    # Append it to answer
                    self.ret.append(v)

                for next_x in self.graph[x]:
                    if(not self.vis[next_x]):
                        next_v = v[:]
                        next_v.append(next_x)
                        q.append((next_x, depth+1, next_v))
        

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)

        n = len(wordList)
        self.graph = [[] for i in range(n)]
        self.vis = [False for i in range(n)]

        # Build graph in this way will tle. O(n^2)
        # for i in range(n):
        #     for j in range(i+1 ,n):
        #         if self.isOneLetterDifferent(i, j, wordList):
        #             self.graph[i].append(j)
        #             self.graph[j].append(i)

        # Build in this way is ok. O(n * log(n))
        # First build a pattern map
        wordLen = len(beginWord) 
        lookUp = {}
        for i in range(n):
            for j in range(wordLen):
                pattern = wordList[i][0:j] + "*" + wordList[i][j+1:]
                lookUp.setdefault(pattern, []).append(i)
        
        # Then build a graph by the map
        for i in range(n):
            for j in range(wordLen):
                pattern = wordList[i][0:j] + "*" + wordList[i][j+1:]
                for neiborhood in lookUp[pattern]:
                    if(neiborhood != i):
                        self.graph[i].append(neiborhood)

        # Find the start and the end
        for i in range(n):
            if(wordList[i] == beginWord):
                self.start = i
            elif(wordList[i] == endWord):
                self.end = i
        if(self.end == -1):
            return []
        

        self.bfsWithLayer()

        # Tranform the ret of graph paths to the ret of word paths
        word_ret = []
        if(len(self.ret) == 0):
            return word_ret
        
        for v in self.ret:
            word_v = [wordList[x] for x in v]
            word_ret.append(word_v)
        return word_ret   
