import gc
import pdb

# pdb.set_trace()

def build_rank(T):
    rank_last_col = []
    rank = {}
    rank['A'] = 0
    rank['C'] = 0
    rank['G'] = 0
    rank['T'] = 0

    for i in T:
        if i == '$':
            rank_last_col.append([i,-1])
            continue

        rank[i] += 1
        rank_last_col.append([i, rank[i]])

    return rank_last_col, rank

def BuildLastToFirst(T):
    
    rank_last_col, counts = build_rank(T)
    ans = []

    for i in range(len(T)):
        c = rank_last_col[i]
        if c[0] == '$':
            ans.append(0)

        if c[0] == 'A':
            ans.append(c[1])

        if c[0] == 'C':
            ans.append(counts['A'] + c[1])

        if c[0] == 'G':
            ans.append(counts['A'] + counts['C'] + c[1])

        if c[0] == 'T':
            ans.append(counts['A'] + counts['C'] + counts['G'] + c[1])

    return ans

def BWMatching(FirstColumn, LastColumn, Pattern, LastToFirst):
    top = 0
    bottom = len(LastColumn)-1

    while top <= bottom:
        if len(Pattern) > 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]

            # if positions from top to bottom in LastColumn contain an occurrence of symbol
            topIndex = LastColumn.find(symbol, top, bottom+1)
            bottomIndex = LastColumn.rfind(symbol, top, bottom+1)
            # print topIndex, bottomIndex

            if topIndex != -1 and bottomIndex != -1:
                top = LastToFirst[topIndex]
                bottom = LastToFirst[bottomIndex]
                # print top, bottom
            else:
                return 0
        else:
            return bottom - top + 1

def main():
    # T = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
    # Patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]

    filename = "./data/rosalind_ba9l.txt"
    read_data = []

    with open(filename, 'r') as file:
        data = file.read()
    
    data = data.split('\n')
    T =  data[0]

    # T = ''.join(data[0].split('\r'))
    Patterns = data[1].split()
    # outputs = data[3].split()
    # print Patterns

    first = ''.join(sorted(T))
    lastToFirst = BuildLastToFirst(T)
    result = []

    for p in Patterns:
        print BWMatching(first, T, p, lastToFirst),

if __name__ == '__main__':
    main()