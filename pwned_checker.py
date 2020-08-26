#!/usr/bin/env python3
import argparse

parser=argparse.ArgumentParser(description="Shooter's pwned checker!!!")
parser.add_argument("-v",'--version',action='version',version='%(prog)s 1.0')
parser.add_argument("-u","--username",type=str,help='username to be checking')
parser.add_argument("-p",'--password',type=str,help='password to be checking')
parser.add_argument("-e",'--email',type=str,help='email to be checking')
parser.add_argument("-w","--wordlists",type=str,help='wordlists to be checking')
args=parser.parse_args()
if args.username==None and args.password==None and args.email==None:
	print("Please specify valid arguments!!!")
	exit(1)

if args.wordlists:
	wordlist=args.wordlists
else:
	wordlist="/usr/share/wordlists/rockyou.txt"
print("++++++ Welcome to pwned checker +++++++++")
print("checking........")
if args.password:
	args.password+='\n'
	with open('/usr/share/wordlists/rockyou.txt','r') as f:
		for line in f:
			if line==args.password:
				print("Oh no - Pwned!!!")
				exit(1)
		print("Good news — no pwnage found")
		exit(1)

if args.username:
	args.username+='\n'
	with open(wordlist,'r') as f:
		for line in f:
			if line==args.username:
				print("Oh no - Pwned!!!")
				exit(1)
		print("Good news — no pwnage found")
		exit(1)

if args.email:
	args.email+='\n'
	with open('/usr/share/wordlists/rockyou.txt','r') as f:
		for line in f:
			if line==args.email:
				print("Oh no - Pwned!!!")
				exit(1)
		print("Good news — no pwnage found")
		exit(1)
