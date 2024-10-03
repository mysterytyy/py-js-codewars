def strip_comments(strng, markers):
    lines = strng.split("\n")

    for marker in markers:
        lines = [line.split(marker)[0].rstrip() for line in lines]
    return "\n".join(lines)

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))