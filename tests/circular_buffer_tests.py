""" Author: bam098
    URL: https://github.com/bam098
    Date: 11/10/2013
    Description:
        Test class to test the functionality of the CircularBuffer class.
"""

from nose.tools import *
from tools.CircularBuffer import CircularBuffer


def test_init():
    """
    Tests if the buffer is empty after its creation.
    """
    buffer = CircularBuffer(10)
    assert_equal(buffer.getBufferContent(), [])
    
def test_append_elem():
    """
    Tests if it is possible to add one element to the buffer.
    """
    buffer = CircularBuffer(5)
    buffer.append("Foo")
    assert_equal(buffer.getBufferContent(), ["Foo"])

def test_append_elems():
    """
    Tests if it is possible to add elements to the buffer.
    """
    buffer = CircularBuffer(5)
    buffer.append("Foo")
    buffer.append("Bar")
    buffer.append("Baz")
    assert_equal(buffer.getBufferContent(), ["Foo","Bar","Baz"])
    
def test_append_overwrite():
    """
    Tests if the oldest element is overwritten when a buffer overflow occures.
    """
    buffer = CircularBuffer(5)
    buffer.append("Foo")
    buffer.append("Bar")
    buffer.append("Baz")
    buffer.append("Fum")
    buffer.append("Blu")
    buffer.append("Boo")
    assert_equal(buffer.getBufferContent(), ["Bar","Baz","Fum","Blu","Boo"])
    
def test_append_multiple_overwrite():
    """
    Tests if multiple elements in the buffer can be overwritten by overflow.
    """
    buffer = CircularBuffer(3)
    buffer.append("Foo")
    buffer.append("Bar")
    buffer.append("Baz")
    buffer.append("Fum")
    buffer.append("Blu")
    buffer.append("Boo")
    buffer.append("Joo")
    assert_equal(buffer.getBufferContent(), ["Blu","Boo","Joo"])
    
def test_remove_init_buffer():
    """
    Tests if removing from a new (empty) buffer has no effect.
    """
    buffer = CircularBuffer(10)
    buffer.remove()
    assert_equal(buffer.getBufferContent(), [])
    
def test_remove_empty_buffer():
    """
    Tests if removing from an empty buffer has no effect.
    """
    buffer = CircularBuffer(10)
    buffer.append("Foo")
    buffer.append("Bar")
    buffer.remove()
    buffer.remove()
    buffer.remove()
    assert_equal(buffer.getBufferContent(), [])
    
def test_remove():
    """
    Tests if it is possible to remove the oldest element from the buffer.
    """
    buffer = CircularBuffer(5)
    buffer.append("Foo")
    buffer.append("Bar")
    buffer.append("Baz")
    buffer.remove()
    assert_equal(buffer.getBufferContent(), ["Bar","Baz"])
    
def test_remove_one_elem():
    """
    Tests if the only element of a buffer is removed.
    """
    buffer = CircularBuffer(5)
    buffer.append("Foo")
    buffer.remove()
    assert_equal(buffer.getBufferContent(), [])
    
def test_remove_all():
    """
    Tests if it is possible to remove all elements from a full buffer.
    """
    buffer = CircularBuffer(3)
    buffer.append("Foo")
    buffer.append("Bar")
    buffer.append("Baz")
    buffer.append("Fum")
    buffer.append("Blu")
    buffer.append("Boo")
    buffer.append("Joo")
    buffer.remove()
    buffer.remove()
    buffer.remove()
    assert_equal(buffer.getBufferContent(), [])
    
def test_remove_elem_full_buffer():
    """
    """
    buffer = CircularBuffer(3)
    buffer.append("Foo")
    buffer.append("Bar")
    buffer.append("Baz")
    buffer.append("Fum")
    buffer.remove()
    assert_equal(buffer.getBufferContent(), ["Baz","Fum"])
