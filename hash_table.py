class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.data[index] is None:
            self.data[index] = Node(key, value)
        else:
            current = self.data[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current = self.data[i]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(f"- {current.key}: {current.value.number} ", end="")
                    current = current.next
                print("")

table = HashTable(10)
table.insert("Mike", Contact("Mike", "910-291-4390"))
table.insert("Tyler", Contact("Tyler", "747-223-0556"))
table.insert("April", Contact("April", "111-222-3333"))
table.insert("May", Contact("May", "333-222-1111"))

table.print_table()
table.insert("Stacy", Contact("Stacy", "999-444-9999"))
table.print_table()

print(table.search("Jill"))


'''
Hash tables are particularly suitable for fast lookups as they provide average-case time complexity to search, insert, or remove data. This is 
because a hash function is used to calculate an index into an array of buckets/slots, where the value being searched can be instantly retrieved. 
Hash tables can reduce the number of comparisons needed by spreading the data evenly across the array.

Each entry of a hash table array refers to a node that is able to store all the keys that hash into the same index. When a collision happens, 
the new node is inserted at the end of the list. I search linearly in the list to find the target key. This is a useful method, especially if 
the load factor is maintained low to avoid long chains, making the performance go down to O(n) in the worst case.

Engineers would choose a hash table over a list when the data set is larger. Hash tables are preferable when order does not matter. If keys are 
poorly hashable or space is a concern, a tree may be more suitable. In Python, dictionaries are hash tables and are best for data that needs to be 
stored in key-value format.
'''
