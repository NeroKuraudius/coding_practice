text = "What The F*?k"
nt = text.lower()
sl = []
for f in nt:
    if f.islower():
        pass
    else:
        sl.append(nt.index(f))
print(sl)