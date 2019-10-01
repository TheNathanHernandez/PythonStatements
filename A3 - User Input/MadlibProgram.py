# Madlibs in Python, Nathan Hernandez
from ess import ask 

time = ask("What time is it?")

noun = ask("Give a noun.")

adjective = ask("Give an adjective.")

verb = ask("Give a verb.")

favoriteColor = ask("What's your favorite color?")

name = ask("Enter a name, it doesn't have to be yours.")

favoriteAnimal = ask("What's your favorite animal?")

favoriteSoda = ask("What's your favorite soda?")

favoriteHoliday = ask("What's your favorite holiday?")

print("It was {} and I had an idea to start {}, after a little bit of thinking. I didn't really think it was a good idea anymore. However, I noticed that the place where I was, looked like a {}. Of course, I had to {} for myself. But I got bored and started walking home, and on the way home I saw a beautiful flower that was the color {} and I also met my friend {} on the way as well. My friend was telling me about his new {}, he had a {} in his hand and started talking about how his family was celebrating {} earlier than anyone should.".format(time, noun, adjective, verb, favoriteColor, name, favoriteAnimal, favoriteSoda, favoriteHoliday))