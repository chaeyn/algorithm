n = int(input())
present = set()

for _ in range(n):
  name, status = input().split()
  if status == 'enter':
    present.add(name)
  elif status == 'leave':
    if name in present:
      present.remove(name)
sorted_present = sorted(present, reverse=True)
for person in sorted_present:
  print(person)