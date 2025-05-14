with open("text.txt", "w", encoding="UTF-8") as file1:
    file1.write("Petrichor is a pleasant smell that frequently accompanies the first rain after a long period of warm, dry weather.")

with open("text.txt", "r", encoding="UTF-8") as file1:
    searched_word = file1.read().strip().upper()

def highlight(txt, word):
    return txt.replace(word, f"*{word}*")

def bin_search(word, target):
    l, r = 0, len(word) - 1
    while(l <= r):
        mid = (l + r) // 2
        if(word[mid] == target):
            return mid
        elif(word[mid] < target):
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(searched_word)
print("Hello, user! Please, type a word that you are looking for: ")

check = 0
while not check:
    user = input().strip().upper()
    words = sorted(searched_word.replace(",", "").replace(".", "").split())
    index = bin_search(words, user)
    if index != -1:
        highlighted = highlight(searched_word, user)
        print("\n Word found!")
        print(highlighted)
        check = 1
    else:
        print("Sorry, it seems that there is no such word :(. Please try again :)")
        continue
