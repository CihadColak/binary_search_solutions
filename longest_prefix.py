def solve(words):
    shortestWord = min((word for word in words if word), key=len)
    print(shortestWord)
    for i, c in enumerate(shortestWord):
        for word in words:
            if word[i] is None:
                return shortestWord[:i]
            if word[i] != c:
                return shortestWord[:i]
    return


print(solve(["ant", "antho", "anthonis"]))
