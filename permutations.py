def permutation(l):
  def _permutation(sofar, remaining):
    num = len(remaining)

    if num == 0:
      yield sofar
    else:
      for i in range(num):
        yield from _permutation(sofar + [remaining[i]], remaining[:i] + remaining[i+1:])
  
  return _permutation([], l)

def permute(l):
  if len(l) == 0:
    yield l
  else:
    for i in range(len(l)):
      l[0], l[i] = l[i], l[0]
      for item in permute(l[1:]):
        yield [l[0]] + item

def combine(l):
  if len(l) == 0:
    yield l
  else:
    yield from combine(l[1:])
    for item in combine(l[1:]):
      yield [l[0]] + item

def combination(l):
  def _combination(sofar, remaining):
    if len(remaining) == 0:
      yield sofar
    else:
      yield from _combination(sofar + [remaining[0]], remaining[1:])
      yield from _combination(sofar, remaining[1:])
  return _combination([], l)

if __name__ == "__main__":
  for l in permute([1, 2, 3]):
    print(l)

  print("\n")
  for l in combine([1, 2, 3]):
    print(l)
