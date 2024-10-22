ind = list(map(int, input().split()))
if len(ind) != 26:
    print("error")
else:
    text = list(input())
    height_text = []
    alphabet = [chr(i) for i in range(97, 123)]
    height_dict = {alphabet[i]: ind[i] for i in range(26)}
    
    for char in text:
        if char in height_dict:
            height_text.append(height_dict[char])

    height_text.sort()
    result = height_text[len(text) - 1] * len(text)
    print(result)
