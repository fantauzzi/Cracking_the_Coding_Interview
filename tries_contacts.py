class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False;
        self.n_partials = 0

    def add(self, the_string):
        self.n_partials += 1
        if len(the_string) == 0:
            self.word_end = True
            return
        try:
            next = self.children[the_string[0]]
        except:
            next = TrieNode()
            self.children[the_string[0]] = next
        next.add(the_string[1:])

    def exact_find(self, the_string):
        if len(the_string) == 0 and self.word_end:
            return True
        try:
            next = self.children[the_string[0]]
        except:
            return False
        res = next.find(the_string[1:])
        return res

    def find_prefix(self, prefix):
        if len(prefix) == 0:
            return self.n_partials
        try:
            next = self.children[prefix[0]]
        except:
            return 0
        res = next.find_prefix(prefix[1:])
        return res


if __name__ == '__main__':
    n = int(input().strip())
    trie = TrieNode()
    for a0 in range(n):
        op, contact = input().strip().split(' ')
        if op=='add':
            trie.add(contact)
        elif op=='find':
            res = trie.find_prefix(contact)
            print(res)
        else:
            assert False
