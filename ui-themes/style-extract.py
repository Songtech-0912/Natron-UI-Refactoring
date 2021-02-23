import re

with open("blender-style.qss") as file:
	filecontents = file.read()
	file.close()

match = re.findall(r"#\w\w\w\w\w\w", filecontents) 

# Remove duplicates from "match" list
res = [] 
for i in match: 
    if i not in res: 
        res.append(i) 

# Print out values
for n in res:
	print(n)
