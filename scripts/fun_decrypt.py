import os

if __name__ == "__main__":
    dir = os.listdir("/home/kali/Documents/funs")

    for file in dir:
        with open(file, "r") as f:
            display = nextline = afternextline = False
            for line in f:
                if line.startswith("//"):
                    if display:
                        print(line, "-"*70)
                        display = False
                    if "getme" in line or "return" in line:
                        print(line)
                        display = True
                elif line.startswith("char"):
                    print(line)
                    nextline = True
                    afternextline = "getme12" in line
                elif nextline:
                    print(line)
                    nextline = False
                elif afternextline:
                    print(line)
                    afternextline = False
