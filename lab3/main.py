# while (n>0 and b=a[n]) do n:=n-1
# if c!=0 then b:=d else b:=2*a[n];
from pascal import pascal_lex
characters = ""
while characters != "quit":
    characters = input(">")
    tokens = pascal_lex(characters)
    for token in tokens:
        print(token[0] + " "*(7 - len(token[0])) + "| " + token[1])
