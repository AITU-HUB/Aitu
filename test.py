#TASK 1

import struct

a = [10, 20, 30, 40, 50]
with open("data.bin", "wb") as f:
    for x in a:
        f.write(struct.pack("i", x))  # i = int (4 байта)
b = []
with open("data.bin", "rb") as f:
    while True:
        d = f.read(4)
        if not d:
            break
        b.append(struct.unpack("i", d)[0])

print("Stored values:", b)


#TASK 2

lines = [
    "System started successfully",
    "User logged in",
    "User opened settings",
    "Error occurred while loading file",
    "User logged out",
    "System warning detected",
    "User logged in again",
    "File saved successfully",
    "System running normally",
    "User closed application"
]

with open("log.txt", "w", encoding="utf-8") as f:
    for l in lines:
        f.write(l + "\n")

with open("log.txt", "r", encoding="utf-8") as f:
    t = f.read()

ls = t.splitlines()
ws = t.lower().split()

cnt = {}
for w in ws:
    cnt[w] = cnt.get(w, 0) + 1

m = max(cnt, key=cnt.get)

print("Total lines:", len(ls))
print("Total words:", len(ws))
print("Most frequent word:", m)


#TASK 3


import json
u = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(u, f, indent=4)

with open("users.json", "r", encoding="utf-8") as f:
    d = json.load(f)

print("User names:")
for x in d:
    print(x["name"])

sid = 2
for x in d:
    if x["id"] == sid:
        print("Found user:", x)

d.append({"id": 4, "name": "David", "email": "david@example.com"})

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(d, f, indent=4)
