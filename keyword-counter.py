import re
import pyperclip as pc

def main():
    try:
        file = open("./text.txt", "r", encoding='utf8')
        text = file.read()
        file.close()

        file = open("./keywords.txt", "r", encoding='utf8')
        keywords = file.read().splitlines()
        file.close()

        file = open("./count.csv", "w", encoding='utf8')
        regex = "(\s|\A)({key})(\s|\W|\Z)"

        for kw in keywords:
            line = kw.split("	")
            keyword = line[0].strip()
            total = int(line[1])
            curr_regex = regex.format(key=keyword)
            count = len(re.findall(curr_regex, text, re.IGNORECASE))
            needed = total - count
            if(needed > 0):
                file.write("\n" + keyword + "," + str(needed))
        file.close()
        
        file = open("./count.csv", "r", encoding='utf8')
        text = file.read()
        file.close()
        pc.copy(text)

        print("Done.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
