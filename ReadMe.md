## Table of Contents
- [Test Grader](#TestGrader)
- [Motivation](#Motivation)
- [Build Status](#BuildStatus)
- [Further Modification](#FurtherModification)
- [Built Using](#BuiltUsing)


## Test Grader
This project reads multiple choice questions for the SHSAT in the answer sheet of the provided.
The questions get transformed into a matrix, where 0s indicate the bubble is not filled and 1s indicate the bubble is filled.
This auxilary matrix is then transformed into A,B,C,D,E,F,G,H's. 
The algorithm here can be extended to other answer sheets with 4 choices each.

## Motivation
I was tired of grading papers at the tutoring center I work at. Many of the grading apps currently on the market were slightly different from what I need and not as convenient as they could be. I decided to design my own application for my specefic needs.

I can use the class I tutor once a week as a test of how the grader works in real life applications.
## Build Status
Currently in very early version.
At this stage, it is quite slow; each paper takes about 2 seconds to grade. 

## Further Modification
The most pressing modification is to add database integration by reading in ID numbers from the each answer sheet and pairing that up with a student name.

A potential optimization I have, is removing the need for the axuilary matrices.
It is possible to modify the algorithm so that it reads and grades at the same time, which would speed it up dramatically. 

Further modification for different answer sheets can be done easily after the base library is written by just changing the places the program reads.
You can make it read any rectangular region of an image.

Perhaps even further in the future, I can move the entire library to C++.

## Built Using
- Python 3.7
- OpenCV 3

