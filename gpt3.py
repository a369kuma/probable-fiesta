import math

class Code:
    def __init__(self, encodemap, decodemap, base):
        self.encodemap = {}
        self.decodemap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str):
        if not longUrl:
            raise ValueError("URL cannot be empty")
        if longUrl not in self.encodemap:
            shortUrl = self.base + str(len(self.encodemap) + 1)
            self.encodemap[longUrl] = shortUrl
            self.decodemap[shortUrl] = longUrl
        
        return self.encodemap[longUrl]

    def decode(self, shortUrl: str):
        if shortUrl not in self.decodemap:
            raise ValueError("Short URL not found")
        return self.decodemap[shortUrl]

