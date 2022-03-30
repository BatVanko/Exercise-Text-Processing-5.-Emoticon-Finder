text = input()
[print(text[i] + text[i+1]) for i in range(len(text)) if text[i] == ":"]




