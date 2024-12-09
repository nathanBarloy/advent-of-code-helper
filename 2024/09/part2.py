

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
    for c in f.read().strip():
        full = not full
        size = int(c)
        if full:
            for _ in range(size):
                memory.append(id_)
            id_ += 1

        else:
            for _ in range(size):
                memory.append(-1)
    
    empty_pos = 0
    while memory[empty_pos] >= 0:
        empty_pos += 1
    
    full_pos = len(memory)-1
    while memory[full_pos] < 0:
        full_pos -= 1

    while empty_pos < full_pos:
        memory[empty_pos] = memory[full_pos]
        memory[full_pos] = -1
        while memory[empty_pos] >= 0:
            empty_pos += 1
        while memory[full_pos] < 0:
            full_pos -= 1
    
    check = 0
    i = 0
    while memory[i] >= 0:
        check += i*memory[i]
        i += 1
    print(check)




