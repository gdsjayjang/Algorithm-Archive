inp = input()

def func(str):
    dict = {}
    for i in str:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    
    if len(dict) >= 2:
        print('Yes')
    else:
        print('No')

func(inp)