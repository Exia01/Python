# THE BASIC SYNTAX:
# try:
# except:

# try:
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")


def get(d, key): #d for dictionary
    try:
        return d[key] #if found return
    except KeyError:
        return None # if not "KeyError" retrun none


d = {"name": "Ricky"}
print(get(d, "city"))
d["city"] #none

# we can also add more then the basic two
# try:
# except:
# else:
# finally:
