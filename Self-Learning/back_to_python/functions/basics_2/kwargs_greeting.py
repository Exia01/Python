def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        #above, first check key and then check key value
        return "You get a special greeting David!"
    elif "David" in kwargs: # if not set to special
        return f"{kwargs['David']} David!"

    return "Not sure who this is..."

# print(special_greeting(David='Hello')) # Hello David!
# print(special_greeting(Bob='hello')) # Not sure who this is...
# print(special_greeting(David='special')) # You get a special greeting David!

print(special_greeting(Heather="hello", David="special"))