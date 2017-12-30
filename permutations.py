def permutation(l):
  def _permutation(sofar, remaining):
    num = len(remaining)

    if num == 0:
      yield sofar
    else:
      for i in range(num):
        yield from _permutation(sofar + [remaining[i]], remaining[:i] + remaining[i+1:])
  
  return _permutation([], l)

def combination(l):
  def _combination(sofar, remaining):
    if len(remaining) == 0:
      yield sofar
    else:
      yield from _combination(sofar + [remaining[0]], remaining[1:])
      yield from _combination(sofar, remaining[1:])
  return _combination([], l)

if __name__ == "__main__":
  for l in permutation([1, 2, 3]):
    print(l)

  print("\n")
  for l in combination([1, 2, 3]):
    print(l)
