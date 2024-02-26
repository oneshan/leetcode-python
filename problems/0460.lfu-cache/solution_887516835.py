# 0460 - LFU Cache
# Date: 2023-01-29
# Runtime: 765 ms, Memory: 78.5 MB
# Submission Id: 887516835


from collections import OrderedDict, defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq2key = defaultdict(OrderedDict)
        self.key2freq = defaultdict()
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.key2freq:
            return -1
        
        freq = self.key2freq[key]
        value = self.freq2key[freq].pop(key)
        if self.min_freq == freq and len(self.freq2key[freq]) == 0:
            self.min_freq = freq + 1
            
        self.freq2key[freq+1][key] = value
        self.key2freq[key] += 1
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.key2freq:
            self.key2freq[key] = 1
            self.freq2key[1][key] = value
            if self.capacity:
                self.capacity -= 1
            else:
                key, value = self.freq2key[self.min_freq].popitem(last=False)
                self.key2freq.pop(key)
            self.min_freq = 1
            return
        
        freq = self.key2freq[key]
        self.freq2key[freq].pop(key)
        self.freq2key[freq+1][key] = value
        self.key2freq[key] += 1
        if self.min_freq == freq and len(self.freq2key[freq]) == 0:
            self.min_freq = freq + 1