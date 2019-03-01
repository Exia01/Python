# Create a class called Comment.  Each comment should have the following attributes:
# username  - the username of the person who created the comment (like "bluethecat")
# text   - the actual comment itself (like "omg so cute!" or "hahah")
# likes   - the number of likes the comment has.  Likes should default to 0.


class Comment:
    def __init__(self, *args, **kwargs):
        print(args)
        self.username = args[0]
        self.text = args[1]
        try:
            if args[2]:
                self.likes = args[2]
        except IndexError:
            self.likes =0
   


c = Comment("davey123", "lol you're so silly", 3)
print(c.username)  # "davey123"
print(c.text)  # "lol you're so silly"
print(c.likes)  # 3

another_comment = Comment("rosa77", "soooo cute!!!")
print(another_comment.username)  # "rosa77"
print(another_comment.text)  # "soooo cute
