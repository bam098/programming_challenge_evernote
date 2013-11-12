""" Author: bam098
    URL: https://github.com/bam098
    Date: 11/10/2013
    Description:
        Circular buffer class that can hold elements up to a fixed size. If it 
        is tried to add new elements to a full buffer, the oldest elements in 
        the buffer are overwritten.
"""

class CircularBuffer:

  def __init__(self, bufferSize):
    """
    Initialze circular buffer
    @param bufferSize       Max size of the buffer
    """
    self.maxSize = bufferSize                       # Max size of the buffer
    self.data = [None for i in xrange(bufferSize)]  # The buffer
    self.head = 0                                   # Head buffer pointer
    self.tail = 0                                   # Tail buffer pointer
    self.overflow = False                           # Flag if overflow occured



  def append(self, elem):
    """
    Append an element at the circular buffer
    @param elem     The element that should be appended     
    """
    if self.maxSize == 0:                           # Check if in init state
        return
    
    if self.tail == self.head and self.data[self.head] != None:
        self.head = (self.head + 1) % self.maxSize  # Overflow (Overwrite)!
        self.overflow = True
        
    self.data[self.tail] = elem                     # Add element at tail pos.
    self.tail = (self.tail + 1) % self.maxSize      # Tail pointer to next pos.
    


  def remove(self):
    """
    Remove an element from the circular buffer
    """
    if self.maxSize == 0:                           # Check if in init state
        return
    
    if self.tail == self.head:
        if self.data[self.head] == None:
            return                                  # Initial case
        elif self.data[self.head] != None and self.overflow == True:
            self.data[self.head] = None             # Overflow buffer
            self.overflow = False
    
    self.head = (self.head + 1) % self.maxSize      # Remove by shifting head



  def getBufferContent(self):
    """
    Get content of the circular buffer
    """
    content = []
        
    if self.maxSize == 0:                           # Check if in init state
        return content
    
    next = self.head
    if self.data[self.head] != None:
        content = [self.data[self.head]]            # Get first element
        next = (self.head + 1) % self.maxSize
    
    while next != self.tail:                        # Get the rest of the elems
        content.append(self.data[next])
        next = (next + 1) % self.maxSize
    
    return content