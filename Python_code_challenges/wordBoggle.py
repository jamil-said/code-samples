
""" wordBoggle -- 35min.
Boggle is a popular word game in which players attempt to find words in 
sequences of adjacent letters on a rectangular board.

Given a two-dimensional array board that represents the character cells 
of the Boggle board and an array of unique strings words, find all the 
possible words from words that can be formed on the board.

Note that in Boggle when you're finding a word, you can move from a cell 
to any of its 8 neighbors, but you can't use the same cell twice in one 
word.

Example

For

board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
and words = ["CODE", "SOLO", "RULES", "COOL"], the output should be
wordBoggle(board, words) = ["CODE", "RULES"].

Example

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char board

A two-dimensional array of uppercase English characters representing a 
rectangular Boggle board.

Guaranteed constraints:
2 ≤ board.length ≤ 4,
2 ≤ board[i].length ≤ 4,
'A' ≤ board[i][j] ≤ 'Z'.

[input] array.string words

An array of unique English words composed only of uppercase English 
characters.

Guaranteed constraints:
0 ≤ words.length ≤ 100,
2 ≤ words[i].length ≤ 16,
'A' ≤ words[i][j] ≤ 'Z'.

[output] array.string

Words from words that can be found on the Boggle board without duplicates 
and sorted lexicographically in ascending order.
""" 

class TrieNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = [None] * 27
        self.isWord = False
        if parent is not None:
            parent.children[ord(value) - 65] = self

def wordBoggle(board, wrds):
    trieWords = buildTrie(wrds)
    if len(board[0]) < len(board):
        diffBoard = len(board) - len(board[0])
        for i in range(len(board)):
            board[i] += ['['] * diffBoard
    if len(board[0]) > len(board):
        board.append(['['] * len(board[0]))
    return checkBoggle(board, trieWords)

def buildTrie(wrds):
    wrdsCp = wrds
    root = TrieNode(None, '')
    for w in wrdsCp:
        curNode = root
        for letter in w:
            if 65 <= ord(letter) < 92:
                nextNode = curNode.children[ord(letter) - 65]
                if nextNode is None:
                    nextNode = TrieNode(curNode, letter)
                curNode = nextNode
        curNode.isWord = True
    return root

def checkBoggle(grid, wrdsCp):
    rows, cols = len(grid), len(grid[0])
    queue, words, results = [], [], []
    for y in range(cols):
        for x in range(rows):
            c = grid[y][x]
            node = wrdsCp.children[ord(c) - 65]
            if node is not None:
                queue.append((x, y, c, node))
    while queue:
        x, y, s, node = queue[0]
        s += str(y) + str(x)
        del queue[0]
        for dx, dy in ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < cols and 0 <= y2 < rows:
                s2 = s + grid[y2][x2]
                node2 = node.children[ord(grid[y2][x2]) - 65]
                if node2 is not None:
                    if node2.isWord:
                        words.append(s2 + str(y2) + str(x2))
                    queue.append((x2, y2, s2, node2))
    for w in words:
        wordTest = [w[i:i+3] for i in range(0, len(w), 3)]
        if len(wordTest) == len(set(wordTest)):
            wClean = ''.join([i for i in w if not i.isdigit()])
            results.append(wClean)
    results = list(set(results))
    return sorted(results)

print(wordBoggle([["N","L","L","I"], 
                 ["T","J","A","B"], 
                 ["L","E","T","S"]], ["STALL", 
                 "NOTHING", 
                 "ABSTRACTEDNESSES", 
                 "VITA", 
                 "SAIL", 
                 "ACTA", 
                 "STEAL", 
                 "JAIL"])) #["JAIL", "SAIL", "STALL", "STEAL"]

print(wordBoggle([['R', 'L', 'D'],
                ['U', 'O', 'E'],
                ['C', 'S', 'O']], ["CODE", 
                "SOLO", "RULES", "COOL"])) #["CODE", "RULES"]


print(wordBoggle([["S","A"], 
                 ["M","O"], 
                 ["W","E"], 
                 ["H","R"]], ["SOME", 
                 "DRONE", 
                 "WHERE", 
                 "SOMEWHERE", 
                 "WORD", 
                 "WE", 
                 "MORE"]))


print(wordBoggle([["A","Q","A","H"], 
                 ["A","X","V","W"], 
                 ["A","L","T","I"], 
                 ["T","T","J","I"]
                ], ["AXOLOTL", 
                 "TAXA", 
                 "ABA", 
                 "VITA", 
                 "VITTA", 
                 "GO", 
                 "AXAL", 
                 "LATTE", 
                 "TALA"]))

