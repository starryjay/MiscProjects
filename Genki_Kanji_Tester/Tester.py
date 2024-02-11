from DictDef import defdict
import random

while True:
    term, definition = random.choice(list(defdict.items()))
    print("Define", term, ": \n")
    inp = input()
    if inp.lower() in definition:
        print("Correct! Exact definition: ", definition, ". \nMoving on... \n")
    elif inp == "Done":
        break
    else:
        print("Not quite! Correct definition: ", definition)
