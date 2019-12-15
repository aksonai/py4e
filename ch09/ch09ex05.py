# Exercise 5: This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from (i.e., the whole email
# address). At the end of the program, print out the contents of your dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

filename = input("Enter a file name: ")
fhand = open(filename, 'r')
domains = {}

for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        domain = email.split("@")[1]
        domains[domain] = domains.get(domain, 0) + 1

print(domains)