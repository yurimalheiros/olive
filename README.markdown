# Olive

Olive is a controlled language to represent knowledge. It translates a subset of English to first-order logic.

## Program

A olive program is made by premises and questions.

The syntax of a premise is:
    
    Expression. (the period is important!)

For example,
    
    A and B.
    Beautiful iff Blue.

The syntax of a questions is:
    
    Expression? (the question mark is important!)

For example,
    
    A or B?
    Beautiful iff Red?

To run a program execute: python oliveask.py FILENAME

## Symbols

All symbols in the language starts with a capital letter.

Example:
    
    A and B. (A is a symbol, and B is a symbol too)
    Peter and Stewie. (Peter is a symbol, and Stewie is a symbol too)

## Operators

### And

In:
    
    A and B.

Out:
    
    A&B

### Or

In:
    
    A or B.

Out:
    
    A|B

### If-Then

In:
    
    if A then B.

Out:
    
    A->B

### Iff

In:
    
    A iff B.

Out:
    
    A<->B

## Predicates

### Is

In:
    
    John is tall

Out:
    
    tall(John)


### Transitive verbs

In:
    
    John watches Tv.

Out:
    
    watches(John, Tv)

In:
    
    John goes by Car.

Out:
    
    goes_by(John, Car)

### Intransitive verbs

In:
    
    John disappeared.

Out:
    
    disappeared(John)


### Open formula

In:
    
    He is tall.

Out:
    
    tall(x)

## Ask

Use a question mark in the end of the sentence to ask something.

In:
    
    Socrates is human.
    if he is human then he is hntelligent.
    Socrates is hntelligent?

Out:
    
    human(Socrates)
    human(x)->intelligent(x)
    True


