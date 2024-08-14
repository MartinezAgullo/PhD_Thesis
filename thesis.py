#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script to modify thesis chapters to compile them individually or compile the entire thesis
# It justs comments or uncomments preambles in individual chapters
# Run "python thesis.py -c 1" to comment the preamble in the chapters and compile the entire thesis
# Run "python thesis.py -c 0" to uncomment the preamble in the chapters and compile them separately
# Author: Pablo Villanueva-Domingo

import argparse

parser = argparse.ArgumentParser(description='...')
parser.add_argument("-c", type=int, help='1 to compile the thesis, 0 otherwise',default=1)
args = parser.parse_args()

def substract(a, b):
    return "".join(a.rsplit(b))

compilethesis = args.c

# Modify here the chapter list, in the folder "Chapters"
chaps = ["Intro"]

for chap in chaps:
    namechap = "Chapters/Chapter_"+chap+"/Chapter_"+chap+".tex"

    with open(namechap,"r") as f:
        lines = f.readlines()

    newlines = lines

    if compilethesis==1:
        print("Compiling thesis (chapters together)")

        for n, lin in enumerate(lines):

            if lin=="%PREAMBLE\n" or lin=="%POSTAMBLE\n":
                lines[n+1]="\\begin{comment}\n"
            if lin=="%ENDPREAMBLE\n" or lin=="%ENDPOSTAMBLE\n":
                lines[n+1]="\\end{comment}\n"
            if lin.startswith("%\\chapter{"):
                lines[n] = substract(lin, "%")
            if lin.startswith("{\\LARGE \\textbf{"):
                lines[n] = "%"+lin
            if lin.startswith("\\tableofcontents"):
                lines[n] = "%"+lin


    else:
        print("Separating chapters")

        for n, lin in enumerate(lines):

            if lin=="%PREAMBLE\n" or lin=="%POSTAMBLE\n":
                lines[n+1]="%\\begin{comment}\n"
            if lin=="%ENDPREAMBLE\n" or lin=="%ENDPOSTAMBLE\n":
                lines[n+1]="%\\end{comment}\n"
            if lin.startswith("\\chapter{"):
                lines[n] = "%"+lin
            if lin.startswith("%{\\LARGE \\textbf{"):
                lines[n] = substract(lin, "%")
            if lin.startswith("%\\tableofcontents"):
                lines[n] = substract(lin, "%")




    with open(namechap, 'w') as f:
        f.write("".join(lines))
