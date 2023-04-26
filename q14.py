n = int(input())
persons = {}
for _ in range(n):
    name, family = input().split()
    persons[family] = name
values = list(persons.values())
cou = []
m = []
for i in values:
    if i not in cou:
        cou.append(i)
        m.append(values.count(i))
print(max(m))
