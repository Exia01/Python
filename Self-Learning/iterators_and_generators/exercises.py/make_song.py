# make_song
# Write a function called make_song, which takes a count and a beverage, and returns a generator that yields verses from a popular song
# about a the beverage. The number of verses in the song is determined by the count. 
# Each verse of the song should involve one fewer beverage, until there are no beverages remaining. (Check the examples for details on the
# structure of the lyrics.)
# The default count should be 99, and the default beverage should be soda



def make_song(count=None, beverage=None):
    if not count:
        count = 99
    if beverage is None:
        beverage = 'soda'
    while count >= 0:
        if count is 1:
            yield 'Only {} bottle of {} left!'.format(count, beverage)
        elif count is 0:
            yield 'No more {}!'.format(beverage)
        else:
             yield '{} bottles of {} on the wall.'.format(count, beverage)
        count -= 1
# Test Case:
kombucha_song = make_song(5, "kombucha")
for song in kombucha_song:
    print(song)
