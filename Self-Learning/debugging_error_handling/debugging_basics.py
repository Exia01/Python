# pdb it is a module that we can import and tracing it.
import pdb
second = "Second"
# We can place it anywhere
pdb.set_trace()  # preferably before it breaks
result = first + second
third = "Third"
result += third
print(result)



# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
