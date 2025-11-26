class TagCloud:
    def __init__(self):
        self.tags = {}
    
    def __str__(self):
        return f'{self.tags}'

    def __len__(self):
        return len(self.tags.key())
    
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    
    def __iter__(self): # To make it iterable
        return iter(self.tags)
    
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

        # if tag not in self.tags:
        #     self.tags[tag] = 1
        # else:
        #     self.tags[tag] += 1

cloud = TagCloud()
cloud.add('Python')
cloud.add('PYTHON')
cloud.add('python')

cloud['python'] = 50
print(cloud['pyThon'])