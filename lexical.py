integers = []
floats = []
strings = []
table = []
def lex(line):
    for element in elements:
        try:
            int(element)
            integers.append(element)
    
        except ValueError:
            try:
                float(element)
                floats.append(element)
            except ValueError:
                strings.append(element)
        if element in integers:
            table.append(("INTEGER",element)) 
        elif element in floats:
            table.append(("FLOAT",element))
        else:
            try:
                int(element[0])
                table.append(("ERROR",element))
            except ValueError:
                if element == "if":
                    table.append(("IF_TOKEN",element))
                elif element == "while":
                    table.append(("WHILE_TOKEN",element))
                elif element == "for":
                    table.append(("FOR_TOKEN",element))
                elif "<" in element or ">" in element or "=" in element:
                    table.append(("RELOP",element))
                else:
                    if element not in table:
                        table.append(("ID",element))
                """elif element == ">":
                table.append(("IF_TOKEN",element))
            elif element == "<=":
                table.append(("IF_TOKEN",element))
            elif element == ">=":
                table.append(("IF_TOKEN",element))
            elif element == "==":
                table.append(("IF_TOKEN",element))"""

my_file = open("text.txt","r")

for line in my_file:
    elements = line.split()# this is only saving the last line. += needs to be done somehow
    lex(elements)
"""
print("\n")
print(integers)
print(floats)
print(strings)
print()
"""
for token in table:
    print("Token: ",token[0])
    print("Lexeme: ",token[1])
    print()