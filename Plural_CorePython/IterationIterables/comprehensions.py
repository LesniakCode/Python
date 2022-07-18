'''
List comprehension syntax
[expr(item) for item in iterable]
direction     <---------

Comprehension with filters
[expr(item) for item in iterable if def()"isprime(item))]
'''

words = "Why sometimes I have believed as many as \
six impossible thngs before breakfast".split()

print([len(words) for word in words])
  