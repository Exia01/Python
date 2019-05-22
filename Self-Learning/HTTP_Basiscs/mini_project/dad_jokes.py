from program_title import program_greeter
from get_joke import request_jokes
from random import choice

program_greeter()


def get_Jokes():
    search_term = ""
    joke_count = None
    print("Let me tell you a joke!")
    while True:
        print("\nGive me a topic: ")
        search_term = input()
        if search_term == "q" or search_term == "n" or search_term =="quit":
            break
        try:
            if len(search_term) <= 0:
                raise ValueError
        except ValueError:
            print("No topic provided")
            print("Would you like to try again? Y/N ")
            try_again = input().lower()
            # print('from try again', try_again)
            if try_again == "n" or try_again == "q" or try_again=="quit":
                break
        else:
            data = request_jokes(search_term, joke_count)
            jokes_num = len(data.get('results', None))
            if jokes_num > 0:
                joke_lists = data['results']
                random_joke = choice(
                    list(map(lambda x: x.get('joke', "Not Found"), joke_lists)))
                if jokes_num == 1:
                    jokes_num = "one"

            if jokes_num == 1:
                print(f"I've got one joke about {search_term}. Here it is:")
                print(random_joke)
            elif jokes_num > 0:
                print(
                    f"I've got {jokes_num} jokes about {search_term}. Here is one:")
                print(random_joke)
            else:
                print(f'Sorry, I don\'t have any jokes about {search_term}')


get_Jokes()
print("Goodbye!")
