# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section [maximumloop]) to find who
# has the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

filename = input("Enter a file name: ")
fhand = open(filename, 'r')
email_addresses = {}

for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1

max_address = None
max_emails = 0
for k in email_addresses:
    if email_addresses[k] > max_emails:
        max_address = k
        max_emails = email_addresses[k]

print(max_address, max_emails)
