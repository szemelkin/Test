__author__ = 'User'
import sys
for line in sys.stdin:
    for token in line.strip().split():
        print(token + "\t1")
print ("test 123")
