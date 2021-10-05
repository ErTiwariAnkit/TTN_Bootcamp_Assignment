class list1:
    def __init__(self,num):
        self.num=num
        self.max=len(num)-1
    def __iter__(self):
        self.start=-1
        return self
    def __next__(self):
        while True:
            self.start = self.start + 1
            if(self.start>self.max):
                raise StopIteration
            else:
                return (self.num[self.start])*2
list2=list1([2,6,7,8])
for i in list2:
    print(i)