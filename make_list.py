import argparse
import re


def make(file, lineLength=72, separator="\t"):
#    dataLines = []
    outLines = []

    for line in file:
        if line.startswith("#"):
            pass # This is a comment, skip over it.
        elif line.startswith("<--"): # This is a section title, print as-is.
            outLines.append(line)
        else:
            cols = re.split(r"\t+", line)
            # This is a data line -- extract it.
            if len(cols) == 2:
                pass

    # Now use the CSV parser.
#    reader = csv.reader(dataLines, csv.excel_tab, delimiter=separator)

#   for row in reader:
#       itemName = row[0]
#       expCount = int(row[1])
#       extra = row[2]

#       # The number of spaces between the last character of the name and the
#       # first character of the number of items to pack.
#       padLength = lineLength - len("    - ") - len("____/____  {  } [  ]") - len(itemName)
#       padding = None

#       if padLength < 0: # The name is too long and it must be truncated.
#           truncLen = lineLength - 6 - 20
#           itemName = itemName[:truncLen]
#           padding = " "
#       else:
#           padding = " " * padLength

#       outLine = "    - " + itemName + padding  + str(expCount).center(4) + "/____  {  } [  ]" + extra
#       outLines.append(outLine)

    return outLines


def run():
    argparser = argparse.ArgumentParser(
        description = "Parse a list source file into a (semi-)printable list format."
    )

    argparser.add_argument("--line-length", type=int, default=72,
        dest="lineLength", help="the width of the generated text, in columns " +
        "(default=72)")
    argparser.add_argument("--separator-code", type=int, default=ord("\t"),
        dest="separatorCode", help="the Unicode code point of the column " +
        "separator character (default=" + str(ord("\t")) + " (TAB))")
    argparser.add_argument("filename", type=str, nargs=1)
    argparser.add_argument("outfile", type=str, nargs="?", default=None)

    args = argparser.parse_args()
    fname = args.filename[0]
    oname = args.outfile[0]

    outLines = None

    with open(fname, "rt") as file:
        outLines = make(file)

    if oname != None:
        with open(oname, "wt", newline="\r\n") as file:
            for line in outLines:
                file.write(line + "\n")
                print(line)
    else:
        for line in outLines:
            print(line)


run()
