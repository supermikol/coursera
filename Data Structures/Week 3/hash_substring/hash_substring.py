# python3
from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyhash(string,p,x):
    ans = 0
    for c in reversed(string):
        ans = (ans * x + ord(c)) % p
    return ans

def precompute_hash(text, len_p, p, x):
  table = [None]*(len(text) - len_p + 1)
  string = text[len(text) - len_p:len(text)]
  table[len(text) - len_p] = polyhash(string,p,x)
  y = 1
  for i in range(1,len_p+1):
    y = (y * x) % p
  for i in range(len(text)-len_p-1,-1,-1):
    table[i] = (x*table[i+1] + ord(text[i]) - y*ord(text[i+len_p])) % p
  return table


def get_occurrences(pattern, text):
    prime = 1000003
    rand_num = randint(1, prime - 1)
    result = []
    p_hash = polyhash(pattern, prime, rand_num)
    table = precompute_hash(text, len(pattern),prime,rand_num)
    for i in range(len(text)-len(pattern)+1):
      if p_hash != table[i]:
        continue
      if pattern == text[i:i+len(pattern)]:
        result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

