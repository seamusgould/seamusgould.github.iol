import random
import time

def main():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ', "'", "!"]

    solution = "welcome to seamus' repository!" #end goal
    start = '' #starting string
    holder = ''# letter holder to pop
    i = 0

    while start != solution:
        holder = random.choice(alphabet)
        if holder != solution[i]:
            alphabet.remove(holder)
            print(start + holder)
            time.sleep(.05)
        else:
            alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ', "'", "!"]
            start += holder
            print(start)
            i += 1
            time.sleep(.05)

if __name__ == "__main__":
    main()

    