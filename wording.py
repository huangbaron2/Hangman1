def function():
    lst = []
    with open ('words.txt', 'r') as f:
        for line in f:
            line = line.strip('\n')
            if len(line) > 0:
                lst.append(line)
                with open ('newwords.txt', 'a') as g:
                    g.write(line + '\n')
    print(lst)
function()

