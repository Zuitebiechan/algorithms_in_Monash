# ====================================================== Hash Table using open addressing ======================================================
class HashTable_open_addressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
# -------------------------------------------------------linear probing-------------------------------------------------------
    def linear_probe(self, key):
        return key % self.size
    
    def insert_linear(self, key, value):
        hash_value = self.linear_probe(key)
        while self.table[hash_value] is not None:
            hash_value = (hash_value + 1) % self.size  # 线性探查
        self.table[hash_value] = (key, value)

    def search_linear(self, key):
        hash_value = self.linear_probe(key)
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                return self.table[hash_value][1]
            hash_value = (hash_value + 1) % self.size
        return None

# -------------------------------------------------------quadratic probing-------------------------------------------------------
    def quadratic_probe(self, key, i):
        # 二次探查的公式：h(k, i) = (h(k) + i^2) % m
        return (self.linear_probe(key) + i ** 2) % self.size

    def insert_quadratic(self, key, value):
        i = 0
        hash_value = self.quadratic_probe(key, i)
        # 找到一个空槽插入数据
        while self.table[hash_value] is not None:
            i += 1
            hash_value = self.quadratic_probe(key, i)
        self.table[hash_value] = (key, value)
    
    def search_quadratic(self, key):
        i = 0
        hash_value = self.quadratic_probe(key, i)
        # 寻找键所在的槽
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                return self.table[hash_value][1]
            i += 1
            hash_value = self.quadratic_probe(key, i)
        return None

# -------------------------------------------------------double hashing-------------------------------------------------------
    def hash_function1(self, key):
        """
        第一个哈希函数，使用简单的取模运算。
        :param key: 要哈希的键
        :return: 哈希值
        """
        return key % self.size

    def hash_function2(self, key):
        """
        第二个哈希函数，使用固定的步长，但确保不为 0。
        通常，哈希表的大小应该是质数以避免步长为 0。
        :param key: 要哈希的键
        :return: 第二个哈希值（步长）
        """
        # 确保 h2(k) 不是 0，通常使用取模后的固定常数
        return 1 + (key % (self.size - 1))

    def double_hash(self, key, i):
        """
        双重哈希的探查公式。
        :param key: 要插入或查找的键
        :param i: 探查次数
        :return: 探查的哈希值
        """
        return (self.hash_function1(key) + i * self.hash_function2(key)) % self.size

    def insert_double_hash(self, key, value):
        """
        在哈希表中插入键值对。
        :param key: 要插入的键
        :param value: 要插入的值
        """
        i = 0
        hash_value = self.double_hash(key, i)
        # 进行探查，直到找到空槽
        while self.table[hash_value] is not None:
            i += 1
            hash_value = self.double_hash(key, i)
        self.table[hash_value] = (key, value)

    def search_double_hash(self, key):
        """
        查找哈希表中的键。
        :param key: 要查找的键
        :return: 键对应的值，如果不存在则返回 None
        """
        i = 0
        hash_value = self.double_hash(key, i)
        # 继续探查直到找到元素或查找结束
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                return self.table[hash_value][1]
            i += 1
            hash_value = self.double_hash(key, i)
        return None

# Time Complexity of Hash Table using open addressing:
# Load Factor (λ) = n / m, where n is the number of elements and m is the size of the hash table
#
# Insert:
# - Best Case: O(1) - Inserting into an empty slot
# - Average Case: O(1 / (1 - λ)) - Inserting into a hash table with a load factor of λ
# - Worst Case: O(m) - Inserting into a hash table with all slots occupied
#
# Search:
# - Best Case: O(1) - Finding the element at the first slot
# - Average Case: O(1 / (1 - λ)) - Finding the element in a hash table with a load factor of λ
# - Worst Case: O(m) - Finding the element in a hash table with all slots occupied
#
# Delete:
# - Best Case: O(1) - Deleting the element at the first slot
# - Average Case: O(1 / (1 - λ)) - Deleting the element in a hash table with a load factor of λ
# - Worst Case: O(m) - Deleting the element in a hash table with all slots occupied
#
# Rehashing: (When the load factor exceeds a certain threshold, like 0.7)
# - O(m) - Rehashing requires creating a new hash table and inserting all elements into it


# ====================================================== Hash Table using separate chaining ======================================================

class HashTable_separate_chaining:
    """
    Hash table implementation using separate chaining

    Time Complexity:
        - Hashing is always O(1)
        - Traverse the linked list in the worst case is O(n)
    """
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # 使用链表存储

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_value = self.hash_function(key)
        # 在链表中插入键值对
        for pair in self.table[hash_value]:
            if pair[0] == key:
                pair[1] = value  # 如果键已经存在，则更新值
                return
        self.table[hash_value].append([key, value])

    def search(self, key):
        hash_value = self.hash_function(key)
        # 在链表中查找键
        for pair in self.table[hash_value]:
            if pair[0] == key:
                return pair[1]
        return None

