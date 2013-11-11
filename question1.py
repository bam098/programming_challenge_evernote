""" Author: bam098
    URL: https://github.com/bam098
    Date: 11/10/2013
    Description:
        Solution to question 1 of the evernote challenge under the link:
        https://evernote.com/careers/challenge.php (see also README.md)
"""

from tools.CircularBuffer import CircularBuffer
import re

# Read in the size of the buffer that should be created
while True:
    input = raw_input()
    if re.match('^\d+$', input):
        buffer = CircularBuffer(int(input))
        break
    else:
        print "Invalid input. Type in the buffer size."

# Read in the commands to manipulate the circular buffer        
while True:
    input = raw_input()
    if re.match('^A \d+$', input):                  # Append an element
        n = int(re.findall('\d+', input)[0])
        for i in xrange(n):
            buffer.append(raw_input())              # Remove an element
    elif re.match('^R \d+$', input):        
        n = int(re.findall('\d+', input)[0])
        for i in xrange(n):
            buffer.remove()
    elif input == 'L':                              # Print out all elements
        for elem in buffer.getBufferContent():
            if elem != None:
                print elem
    elif input == 'Q':                              # Quit
        break
    else:
        print "Invalid input."
    
