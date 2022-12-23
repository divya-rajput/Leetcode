'''
    This is a Least Recently Used(LRU) problem.
    Definition:     An LRU cache is an efficient cache data structure that can be used to figure out what we should evict when the cache is full. 
                    The goal is to always have the least-recently used item accessible in O(1) time. 
    Task :          LRU will help you to quickly identify which item hasn't been used for longest amount if time.
    Implementation: LRU is often implemented by pairing a doubly link list with a hash map
    Strength:       1. Super fast access with O(1) time
                    2. Super fast update with O(1) time
    Weaknesses:     Space heavy-Contains alinked list with n length and a hash map holting n items.So, O(n) space
'''

