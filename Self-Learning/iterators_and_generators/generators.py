# generators are iterators


# example:
def count_up(max):
    count = 1
    while count <= max:
        yield count # yield has a next stores the most recent cycle
        count += 1
total_count = count_up(20)
print(list(total_count))

print(help(count_up))

counter = count_up(20)
print([x for x in counter])