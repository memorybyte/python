# Use double underscore to make it private
# But it is not actually private
# We can still access it 
# cloud.__dict__ -> shows the list of attributes
# _TagCloud__tags is the priavte attribute renamed by python interpreter

class TagCloud:
    def __init__(self):
        self.__tags = {}
    
    def __str__(self):
        return f'{self.__tags}'

    def __len__(self):
        return len(self.__tags.key())
    
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    
    def __iter__(self): # To make it iterable
        return iter(self.__tags)
    
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1



cloud = TagCloud()
# print(cloud.__tags) # Error
# BUt
# print(cloud.__dict__)
# print(cloud._TagCloud__tags)
cloud.add('Python')
cloud.add('PYTHON')
cloud.add('python')

cloud['python'] = 50
print(cloud['pyThon'])