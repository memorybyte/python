class Text(str):
    def duplicate(self):
        return self + self
    
text = Text('Python')
print(text.duplicate().lower())

class TrackableList(list):

    def append(self, object):
        print('Append called')
        super().append(object)

l = TrackableList()
l.append(1)
l.append(2)
l.append(3)
print(l)