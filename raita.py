def raita_search(file_name, words):
    with open(file_name, 'r') as file:
        text = file.read()
    frequencies = {}
    for word in words:
        frequency = 0
        for i in range(len(text) - len(word) + 1):
            if text[i:i+len(word)] == word:
                frequency += 1
        frequencies[word] = frequency
    return frequencies

file_name = "alice_in_wonderland.txt"
words = ["upon", "sigh", "Dormouse", "jury-box", "swim"]
frequencies = raita_search(file_name, words)

for word, frequency in frequencies.items():
    print(f"'{word}' kelimesi {frequency} kez tekrar edildi.")
