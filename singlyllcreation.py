class node:
    def __init__(self,x):
        self.data=x
        self.addrs=None
n1=node(500)
n2=node(200)
n3=node(100)
n4=node(400)
n5=node(300)

n3.addrs=n2
n2.addrs=n5
n5.addrs=n4
n4.addrs=n1
temp=n3
while temp:
    print(temp.data," ==> ",end='')
    temp=temp.addrs
