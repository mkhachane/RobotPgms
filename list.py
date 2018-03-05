
Mylist = [{'id':1,'name':'Harsh','address':'Kunal Icon'},
          {'id':2,'name':'Jon','address':'Rose Vally'},
          {'id':3,'name':'Harry','address':'RoseLand'},
          {'id': 4, 'name': 'Jak', 'address': 'Flora'}]


def Insert(x,y,z):
    for i in range(3):
        d = {}
        d['id'] = x
        d['name'] = y
        d['address'] = z
        Mylist.append(d)
        return d

def Search(a):
    item = a
    for i in Mylist:
        if i['id'] == item:
            return i

def Remove(m):
    Id = m
    for i in Mylist:
        if i['id'] == Id:
            Mylist.remove(i)
    return True



