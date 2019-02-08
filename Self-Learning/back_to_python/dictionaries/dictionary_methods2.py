
import random
sample = dict(name='John',
              has_pets=False,
              age=18,
              favorite_language='Python',
              favorite_color='Purple',
              favorite_sport='Soccer!',
              test=[1, 2, 3, 4, 5],)

# sample.popitem() #removes random value
sample.pop('age')
#removes key, value pair but returns only value
print(sample)

second_sample = {"city":"Vienna"}
 
second_sample.update(sample)  # takes everything in sample and add it or update values
second_sample['name'] = "Kenny" # if we run update it will override this 
print(second_sample)