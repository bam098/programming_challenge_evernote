"""
author:   bam098
created:  11-06-2013
"""

from nose.tools import *
from tools.CircularBuffer import CircularBuffer


def test_init():
  """
  Tests if the buffer contains no data after creation.
  """

  buffer = CircularBuffer(2)
  assert_equal(buffer.getBufferContent(),[])



def test_append():
  """
  Tests if the buffer can append new elements.
  """

  buffer = CircularBuffer(2)
  buffer.append(1)
  buffer.append(2)
  assert_equal(buffer.getBufferContent(), [1,2])



def test_not_append():
  """
  Tests if the buffer does overwrite the oldest
  element when a new element should be added to 
  a full buffer.
  """

  buffer = CircularBuffer(2)
  buffer.append(1)
  buffer.append(2)
  buffer.append(3)
  assert_equal(buffer.getBufferContent(), [2,3])



def test_remove():
  """
  Tests if the buffer removes the oldest element.
  """

  buffer = CircularBuffer(2)
  buffer.append(1)
  buffer.append(2)
  buffer.remove()
  assert_equal(buffer.getBufferContent(), [2])




def test_no_remove():
  """
  Tests if the buffer does not try to remove elements
  when it is empty.
  """

  buffer = CircularBuffer(1)
  buffer.append(1)
  buffer.remove()
  buffer.remove()
  assert_equal(buffer.getBufferContent(), [])
