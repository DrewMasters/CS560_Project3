pages = {}
titles = {}
with open('ranks_process.txt','r') as f:
  for line in f:
    words = line.split()
    pages[words[0]] = words[1]

with open('titles.txt','r') as f:
  for line in f:
    words = line.split()
    titles[words[0]] = words[1]

for key in titles:
  if key in pages:
    print titles[key],
    print pages[key]
