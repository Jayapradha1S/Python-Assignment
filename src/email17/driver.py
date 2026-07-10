from util import filter_emails

n = int(input())

emails = []
for _ in range(n):
    emails.append(input())

print(filter_emails(emails))