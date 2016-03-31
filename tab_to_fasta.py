import os
import shutil
from os import listdir
from os.path import isfile, join
import argparse
from datetime import datetime
import sys
import csv

def main():

	parser = argparse.ArgumentParser(prog="Tab to Fasta", description="This program converts a profile tab delimited file to a fasta file with the sequences of the profiles.")

	#parser.add_argument('-s', nargs='?', type=str, help="sam file path", required=True)
	parser.add_argument('-t', nargs='?', type=str, help='Tab file', required=True)
	parser.add_argument('-o', nargs='?', type=str, help='Output path', required=True)

	args = parser.parse_args()

	runParser(args)


def runParser(args):

	with open(args.o, 'w') as w:
		
		with open(args.t, 'r') as f:
			reader = csv.reader(f, delimiter='\t')
			firstLine = True
			for row in reader:
				if firstLine:
					firstLine = False
					continue
				w.write('>' + row[0] + '\n' + ''.join(row[1:len(row)]) + '\n')


if __name__ == "__main__":
	main()