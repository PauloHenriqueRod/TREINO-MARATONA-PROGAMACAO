def strStr(haystack: str, needle: str) -> int:
    tam = len(needle)
    if haystack == needle:
        return 0
    for i in range(0, len(haystack) - tam + 1):
        if haystack[i:tam+i] == needle:
            return i
    return - 1

print(strStr("abc", "c"))