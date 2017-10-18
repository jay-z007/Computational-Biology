
def BuildFirstOcc(FirstColumn):
    first = {}

    prev = ''
    first['$'] = 0
    first['A'] = 0
    first['C'] = 0
    first['G'] = 0
    first['T'] = 0

    for i, val in enumerate(FirstColumn):
        if val != prev:
            first[val] = i
            prev = val

    return first

def BWMatching(FirstOccurrence, LastColumn, Pattern):
    top = 0
    bottom = len(LastColumn)-1

    while top <= bottom:
        if len(Pattern) > 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]

            # if positions from top to bottom in LastColumn contain an occurrence of symbol
            top_count = LastColumn.count(symbol, 0, top)
            bottom_count = LastColumn.count(symbol, 0, bottom+1)

            if bottom_count != 0:
                top =  FirstOccurrence[symbol] + top_count
                bottom = FirstOccurrence[symbol] + bottom_count - 1 
            else:
                return 0
        else:
            return bottom - top + 1

    if top > bottom:
        return 0

def main():
    # T = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
    # Patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]

    filename = "./data/rosalind_ba9m.txt"
    read_data = []

    with open(filename, 'r') as file:
        data = file.read()
    
    data = data.split('\n')
    T =  data[0]

    T = ''.join(data[0].split('\r'))
    Patterns = data[1].split()
    # outputs = data[3].split()
    print T
    print Patterns
    # print outputs

    first = ''.join(sorted(T))
    firstOccurrence = BuildFirstOcc(first)

    for p in Patterns:
        print BWMatching(firstOccurrence, T, p),

if __name__ == '__main__':
    main()