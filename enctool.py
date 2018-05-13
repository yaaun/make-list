import argparse
import sys

def encode(string):
    ostr = ""
    for c in string:
        ostr += hex(ord(c)) + " "
    return ostr.rstrip()

def decode(string):
    codes = string.rstrip().split(" ")
    ostr = ""
    for c in codes:
        ostr += chr(int(c, 16))
    return ostr

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices={"c", "d"})
    parser.add_argument("infile", type=str)
    parser.add_argument("outfile", type=str, nargs="?", default=None)

    a = parser.parse_args()

    mode = a.mode
    ifname = a.infile
    ofname = a.outfile

    with open(ifname, "rt") as ifile:
        istr = ifile.read()
        ostr = None

        if mode == "c":
            ostr = encode(istr)
        elif mode == "d":
            ostr = decode(istr)

        if ofname:
            with open(ofname, "wt", newline=None) as ofile:
                ofile.write(ostr)
        else:
            print(ostr)
