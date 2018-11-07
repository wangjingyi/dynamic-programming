#given a valid sentence without any space between words and 
#a dictionary of valid English words, find all possible ways to 
#break the sentence.

def all_sentences(remaining, output, d, ret=None):

  if ret is None:
    ret = []

  if len(remaining) == 0 and len(output) > 0:
    ret.append(output.strip())

  for i in range(1, len(remaining) + 1):
    first = remaining[:i]
    if first in d:
      all_sentences(remaining[i:], f'{output} {first}', d, ret)

  return ret

d = { 'cream', 'go', 'i', 'ice', 'icecream', 'like', 'and', 'man', 'mango', 'mobile', 'sam', 'samsung', 'sung'}

r = all_sentences('ilikeicecreamandmango', '', d, [])

r = all_sentences('ilikesamsungmobile', '', d, [])
