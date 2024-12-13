

class Blockchain():
    """A chain of space blocks.

    Attributes:
    position: int
    size: int
    id: int
    next: Blockchain
    """

    def __init__(self, position, size, id_):
        self.position = position
        self.size = size
        self.id = id_
        self.next = None
        self.previous = None
    
    def add_next(next_):
        self.next = next_
        next_.previous = self


class Memory():
    """The state of the memory.

    Attributes:
    full: Blockchain
    full_last: Blockchain
    empty: Blockchain
    empty_last: Blockchain
    """

    def __init__(self, string):
        self.full = None
        self.full_last = None
        self.empty = None
        self.empty_last = None

        alternate = False
        position = 0
        id_ = 0
        for size_s in string:
            size = int(size_s)
            alternate = not alternate
            new_block = Blockchain(position, size, id_ if alternate else -1)
            if alternate:
                if self.full is None:
                    self.full = new_block
                    self.full_last = new_block
                else:
                    self.full_last.add_next(new_block)
                    self.full_last = new_block
            else:
                if self.empty is None:
                    self.empty = new_block
                    self.empty_last = new_block
                else:
                    self.empty_last.add_next(new_block)
                    self.empty_last = new_block
    
    def rearrange():
        current = self.full
        while True:
            if self.full_last.size < self.empty.size:
                # Reduce empty space
                self.empty.position += self.full_last.size
                self.empty.size -= self.full_last.size
                # save new last



                

with open(0) as f:
    #memory = Memory(f.read().strip())
    full = False
    id_ = 0
    memory = []
    emptys = []
    files = []
    pos = 0
    for i, c in enumerate(f.read().strip()):
        full = not full
        size = int(c)
        if full:
            files.append((pos, size))
            for _ in range(size):
                memory.append(id_)
            id_ += 1

        else:
            emptys.append((pos, size))
            for _ in range(size):
                memory.append(-1)
        
        pos += size
    
    for file in files[::-1]:
        #print("".join(map(lambda x: str(x) if x >= 0 else '.', memory)))
        # find hole of good size
        i = 0
        while i < len(emptys) and emptys[i][1] < file[1]:
            i += 1
        if i == len(emptys) or file[0] < emptys[i][0]:
            continue
        
        # Move file in memory
        id_ = memory[file[0]]
        for k in range(file[1]):
            memory[emptys[i][0]+k] = id_
        for k in range(file[1]):
            memory[file[0]+k] = -1
        
        # change empty object
        if emptys[i][1] == file[1]:
            emptys.pop(i)
        else:
            emptys[i] = (emptys[i][0] + file[1], emptys[i][1] - file[1])


    
    check = 0
    for i, x in enumerate(memory):
        if x < 0:
            continue
        check += i*x
    print(check)




