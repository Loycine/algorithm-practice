from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or not beginWord or not endWord: return 0
        size = len(beginWord)

        # build graph
        look_up = defaultdict(list)
        for word in wordList:
            for i, e in enumerate(word):
                key = word[:i] + '*' + word[i+1:]
                look_up[key].append(word)

        
        q = deque([(beginWord, 1)])
        vis = {beginWord: True}


        # bfs
        while q:
            cur, depth = q.popleft()
            vis[cur] = True
            if(cur == endWord):
                return depth

            for i in range(size):
                next_pattern = cur[:i] + "*" + cur[i+1:]

                if next_pattern in look_up:
                    for word in look_up[next_pattern]:
                        if(word not in vis):
                            q.append((word, depth+1))

        return 0