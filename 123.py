
#!/usr/bin/python

f = open('INPUT.TXT')

line = [int(x) for x in f.readlines()[0].replace("\n","").split()]
jumps = [1,1] + [0]*(1 + line[1] - 2)

for i in range(2,line[0]+1):
    jumps[i] = (jumps[i-1] * 2)

for i in range(line[0]+1,line[1]+1):
    jumps[i]=(jumps[i-1] *2) - jumps[i - 1 - line[0]]

print(jumps[line[1]])