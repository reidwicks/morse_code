#!usr/bin/python
# coding = utf-8

"""
Arduinos have limited memory, and it is divided into a section for the program,
and a section for values stored in variables. This program attempts to overcome 
that by instead writing Morse code messages into commands rather than a list
of variables to be read and interpreted. Rather crude, if I'm being honest.
"""

phrase = []
with open("input", 'r', encoding = "utf-8") as infile:
    for line in infile:
        phrase.append(line)
phrase = ''.join(phrase)
phrase = phrase.lower()
binary = []
conversion_chart = {
    " " : "3,", "a" : "0,1,2,", "b" : "1,0,0,0,2,", 
    "c" : "1,0,1,0,2,", "d" : "1,0,0,2,", "e" : "0,2,",
    "f" : "0,0,1,0,2,", "g" : "1,1,0,2,", "h" : "0,0,0,0,2,",
    "i" : "0,0,2,", "j" : "0,1,1,1,2,", "k" : "1,0,1,2,",
    "l" : "0,1,0,0,2,", "m" : "1,1,2,", "n" : "1,0,2,",
    "o" : "1,1,1,2,", "p" : "0,1,1,0,2,", "q" : "1,1,0,1,2,",
    "r" : "0,1,0,2,", "s" : "0,0,0,2,", "t" : "1,2,",
    "u" : "0,0,1,2,", "v" : "0,0,0,1,2,", "w" : "0,1,1,2,",
    "x" : "1,0,0,1,2,", "y" : "1,0,1,1,2,", "z" : "1,1,0,0,2,",
    "1" : "0,1,1,1,1,2,", "2" : "0,0,1,1,1,2,", "3" : "0,0,0,1,1,2,",
    "4" : "0,0,0,0,1,2,", "5" : "0,0,0,0,0,2,", "6" : "1,0,0,0,0,2,",
    "7" : "1,1,0,0,0,2,", "8" : "1,1,1,0,0,2,", "9" : "1,1,1,1,0,2,",
    "0" : "1,1,1,1,1,2,",
    }
for letter in phrase:
    if letter in conversion_chart:
        binary.append(conversion_chart[letter])
    else:
        pass
binary = ''.join(binary)
codeout = []
with open("output", "w") as outfile:
    for char in binary:
        if char == "0":
            outfile.write("digitalWrite(LED_BUILTIN, HIGH);\n")
            outfile.write("delay(100);\n")
            outfile.write("digitalWrite(LED_BUILTIN, LOW);\n")
            outfile.write("delay(100);\n")
        elif char == "1":
            outfile.write("digitalWrite(LED_BUILTIN, HIGH);\n")
            outfile.write("delay(300);\n")
            outfile.write("digitalWrite(LED_BUILTIN, LOW);\n")
            outfile.write("delay(100);\n")
        elif char == "2":
            outfile.write("delay(200);\n")
        elif char == "3":
            outfile.write("delay(600);\n")
    
print("Output has been saved to file \"output\"")
