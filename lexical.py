integers = [] #store integers of the text file
floats = [] #store floats of the text file
strings = [] #store strings of the text file
table = [] #used to store pairs of lexeme-token in a tuple
def lex(line):
    for element in elements:
        try: #if element is integer no error will occur, otherwise ValueError error will be caught by the except
            int(element)
            integers.append(element)
    
        except ValueError:
            try: #if element was float the first try block would cause an error so now we check whether that element was a string or a float
                float(element)
                floats.append(element)
            except ValueError: #if we reach this except block then the element was for sure neither an integer nor a float so we append the element to the string list
                strings.append(element)
        #now we fill the table of lexemes-tokens pairs by pairing the element(lexeme) with the correct token in a tuple and appending that tuple to the table list
        if element in integers:
            table.append(("INTEGER",element)) 
        elif element in floats:
            table.append(("FLOAT",element))
        else:
            try: #check if the first element in the string is an integer so we can assign it the "ERROR" token or not
                int(element[0])
                table.append(("ERROR",element))
            except ValueError:
                #check whether the string is one of "if", "while", or "for" or a variable(identifier) if none of those
                if element == "if":
                    table.append(("IF_TOKEN",element))
                elif element == "while":
                    table.append(("WHILE_TOKEN",element))
                elif element == "for":
                    table.append(("FOR_TOKEN",element))
                elif "<" in element or ">" in element or "==" in element:
                    table.append(("RELOP",element))
                else:
                    if element not in table:
                        table.append(("ID",element))

my_file = open("text.txt","r")

for line in my_file:
    elements = line.split()# this is only saving the last line. += needs to be done somehow
    lex(elements)

for token in table:
    print("Token: ",token[0])
    print("Lexeme: ",token[1])
    print()
