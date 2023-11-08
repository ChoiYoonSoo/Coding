class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        lst = []
        answer = []
        check = set()
        index = []

        def back(cnt):
            if cnt == len(lst):
                if str(lst) not in check:
                    print(lst)
                    answer.append(lst.copy())
                    check.add(str(lst))
                return

            for i in range(len(tiles)):
                if i not in index:
                    index.append(i)
                    lst.append(tiles[i])
                    back(cnt)
                    lst.pop()
                    index.pop()

        for i in range(1,len(tiles)+1):
            back(i)
        
        return len(answer)