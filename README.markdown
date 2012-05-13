# Olive

Olive is a controlled language to represent knowledge. It translates a subset of English to first-order logic.

## Operators

### And

In:
"A" and "B"

Out:
A&B

### Or

In:
"A" or "B"

Out:
A|B

### If-Then

In:
if "A" then "B"

Out:
A->B

### Iff

In:
"A" iff "B"

Out:
A<->B

## Predicates

### Is

In:
"John" is "something"

Out:
something(Joao)


### Transitive verbs

In:
"John" sees "something"

Out:
see(John, something)

### Intransitive verbs

In:
"John" disappear

Out:
disappear(John)


### Open formula

In:
He is "something"

Out:
something(x)

## Ask

Use a question mark in the end of the sentence to ask something.

In:
"Socrates" is "human"

if he is "human" then he is "intelligent"

"Socrates" is "intelligent"?

Out:
True



