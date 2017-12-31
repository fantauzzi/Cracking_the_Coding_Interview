import random
import string
from tries_contacts import TrieNode

def test_not_found():
    trie = TrieNode()
    trie.add('shells')
    trie.add('shore')
    assert trie.find_prefix('shampoo') == 0

def test_exact_match():
    trie = TrieNode()
    trie.add('shells')
    assert trie.find_prefix('shells') == 1

def test_prefix():
    trie = TrieNode()
    trie.add('shells')
    assert trie.find_prefix('she') == 1
    trie.add('she')
    assert trie.find_prefix('sh') == 2


def get_random_string():
    length = random.randint(1, 21)
    res = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return res


def test_big():
    trie = TrieNode()

    for _ in range(100000):
        to_be_added = get_random_string()
        ''' Might add the same tring twice, and therefore find_prefix() may malfunction, but it is OK,
        as I am only load testing, and will not check values reported by find_prefix() for correctness '''
        trie.add(to_be_added)

    for i in range(100000):
        prefix = get_random_string()
        trie.find_prefix(prefix)
