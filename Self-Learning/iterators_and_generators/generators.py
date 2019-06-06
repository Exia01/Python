# generators are iterators


# example:
# def count_up(max):
#     count = 1
#     while count <= max:
#         yield count # yield has a next stores the most recent cycle
#         count += 1
# total_count = count_up(20)
# print(list(total_count))

# print(help(count_up))

# counter = count_up(20)
# print([x for x in counter])


from math import sqrt
def next_prime():
  candidate = 2
  while True:
    for divisor in range(2, round(sqrt(candidate))+1):
      yield f"     Candidate:\t{candidate}"
      yield f"       Divisor:\t{divisor}"
      yield f"        Modulo:\t{candidate%divisor}"
      if candidate%divisor == 0 and divisor != 1:
        yield f"Not a prime....\n"
        break
    else:
      yield f"\t\t{candidate} ← ← ← ← ← ← ← ← ← ← PRIME\n"
      # yield candidate
    candidate += 1
 
primes = next_prime()
for thing in [next(primes) for i in range(100)]:
  print(thing)