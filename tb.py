#!/usr/bin/env python3.6
import json
import time
import random

# This is our thinker function which utilizes the random module to return a string to the while loop.
def thinker():
    r = random.randint(0, 9)

    if r < 4:
        adjective = random.choice(adjectives)
        # Logic to determine the usage of `A` or `An`.
        article = 'A'
        if adjective[0] in 'aeiouAEIOU':
            article += 'n'
        return f"{ article } { adjective } { random.choice(animals) }"
    if r < 7:
        quote = random.choice(quotes)
        return f"{ quote['quote'] } - { quote['name'] }"

    if r == 8:
        r2 = random.randint(0, 5)
        # https://asciiart.website/index.php?art=holiday/thanksgiving
        with open(f'thankscii/{ r2 }', 'r') as f:
            return f.read()

    return f"{ random.choice(todo) }"

# We import our datasets below. Sources are provided before each `with` statement.

# https://gist.github.com/borlaym/585e2e09dd6abd9b0d0a
with open('animals.json', 'r') as animals_file:
    animals = json.loads(animals_file.read())

# https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go
with open('adjectives.json', 'r') as adjectives_file:
    adjectives = json.loads(adjectives_file.read())

# https://gist.github.com/dmakk767/9375ff01aff76f1788aead1df9a66338
with open('quotes.json', 'r') as quotes_file:
    quotes = json.loads(quotes_file.read())

with open('todo.json', 'r') as todo_file:
    todo = json.loads(todo_file.read())

# Using figlet for fancy printing. Screen should be wide enought to format this correctly...

# http://www.figlet.org/
print("""
==========================================
  _   _                       _     _
 | |_| |__   ___  _   _  __ _| |__ | |_
 | __| '_ \ / _ \| | | |/ _` | '_ \| __|
 | |_| | | | (_) | |_| | (_| | | | | |_
  \__|_| |_|\___/ \__,_|\__, |_| |_|\__|
                         |___/

             |----|
   O     O   |beep|     _           _
   |_____|  /|boop|    | |__   ___ | |_
   | _ _ | / |----|    | '_ \ / _ \| __|
   |  _  |/            | |_) | (_) | |_
   |_____|             |_.__/ \___/ \__|

==========================================
""")

try:
    while True:
        print(thinker())
        time.sleep(random.randint(0, 4))
# Graceful termination
except KeyboardInterrupt:
    print("\nKeyboard Interrupt found. Exiting...")
