names=['fan','zhang','wu']
#修改列表元素
names[0]='zhou'
for name in names:
    print(name)
#列表添加元素
names.append('zheng')
for name in names:
    print(name)
#动态的创建列表
moto1=[]
for moto in range(1,6):
    print(moto)
    moto1.append(moto)
print(moto1)
#任意插入元素
names.insert(0,'li')
for name in names:
    print(name)
#删除元素
del names[0]
print(names)
#pop删除元素
names1=names.pop()
print(names1)
print(names)
#根据值删除元素
names.remove('zhou')
print(names)
names.append('zhou')
#永久排序
names.sort()
print(names)
names.sort(reverse=True)
print(names)
names2=sorted(names)
print(names2)
#列表的长度
print(len(names))