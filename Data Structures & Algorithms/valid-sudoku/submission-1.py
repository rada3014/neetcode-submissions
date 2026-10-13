class Solution:

    def hasDuplicate(self,nums):
        hash_map = dict()
        for i in nums:
            if i !='.':
                if i not in hash_map:
                    hash_map[i]=1
                else:
                    return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
            hash_map = dict()
            columns =[]
            for i in range(9):
                columns.append(['.'])
                for j in range(9):
                    x= i//3
                    y = j//3
                    elem = board[i][j]
                    columns[i].extend(board[j][i])
                    if elem!='.':
                        if (x,y) not in hash_map:
                            hash_map[(x,y)]=[board[i][j]]
                        else:
                            if elem not in hash_map[(x,y)]:
                                hash_map[(x,y)].extend(board[i][j])
                            else:
                                #print(hash_map)
                                return False
                    else:
                        pass
            
            for i in board:
                if self.hasDuplicate(i):
                    return False

            for j in columns:
                if self.hasDuplicate(j):
                    return False
                
            return True 
        