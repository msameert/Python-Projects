from collections import Counter

file_name = input("Enter File name : ")

with open(f"{file_name}", "r") as f:
    data = f.read()
    characters = len(data)
    print(f"There are {characters} in this file")
    words1 = data.split()
    words2 = len(words1)
    print(f"There are {words2} in this file")
    lines1 = data.splitlines()
    lines2 = len(lines1)
    print(f"There are {lines2} in this file")

    word_count = Counter(words1)
    most_common = word_count.most_common(1)[0]
    print(f'The most common word in file is "{most_common[0]}" : it appeared {most_common[1]} times') 