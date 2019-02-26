from pascal import pascal_lex
from lex import hasNoErrors
from syntax import syntax_analysis

# while (n>0 and b=a[n]) do n:=n-1
# if c!=0 then b:=d else b:=2*a[n];
# b:= d!=0; b:=2*a[n];
# b:= d; b:=2*a[n];
# If (a>b) then begin a:=b; end else begin a:=b; end;

characters = ""
while characters != "q":
    characters = input(">")
    tokens = pascal_lex(characters)

    if hasNoErrors(tokens, characters):
        syntax_analysis(tokens, characters)

    # print(tokens)
    """
    for token in tokens:
        print(token[0] + " "*(7 - len(token[0])) + "| " + token[1])
    """
