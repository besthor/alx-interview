# 0x00-lookboxes
You have ```n``` number of locked boxes in front of you. Each box is numbered sequentially from ```0``` to ```n - 1``` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: ```def canUnlockAll(boxes)```
- ```boxes``` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
  - There can be keys that do not have boxes
- The first box ```boxes[0]``` is unlocked
- Return ```True``` if all boxes can be opened, else return ```False```

```sh
carrie@ubuntu:~/0x00-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x00-lockboxes$
```
```sh
carrie@ubuntu:~/0x00-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x00-lockboxes$
```

**Juliana Chois** :computer: :woman: 

- Github - [jchois](https://github.com/jchois)
- Twitter - [@julianachois](https://twitter.com/julianachois)
- LinkedIn - [julianachois](https://www.linkedin.com/in/julianachois)

