# Keyword Counter
This is a Keyword Counter which extracts keywords from a text as given by a keyword file and subtracts their occurence count with the needed amount given by the keyword file.

### Implementation ###
1. A "text.txt" file in the execution directory is read containing the text to be analysed.
2. A "keywords.txt" file in the execution directory is read containing the keywords and how often each should occur, separated by a tabulator symbol and each keyword in its own line.
3. The input text is analysed, the keywords counted and subtracted from the wanted occurence count. If a keyword appears more often than the necessary amount, it is excluded from the final output.
4. A string is created in a similar format to the "keywords.txt" (except with "," used as a separation symbol instead of a tabulator) containing the keywords with the number of times they still need to occur. This string is then saved as a "count.csv" file in the execution directory, as well as copied to the clipboard with the help of the pyperclip library.

### Files ###
The "text.txt", "keywords.txt" and "count.csv" files contain example inputs and outputs.
