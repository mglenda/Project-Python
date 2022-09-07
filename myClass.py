def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

data = 'amadeus mozartus kontextus'
r = range(len(data)-1,-1,-1)
res = list(data[i] for i in r)
print(res)