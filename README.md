# Lab 5-7 - Students Register Management [FP]
#### Assignment for FP laboratory 5-7 (extended with lab 8 and lab 9)


For this lab assignment I had problem 1 - Students Register Management

If you want to read the problem statement check Laboratory.05-07.pdf --- Problem 1

Additionally this project uses 2 more lab assignments: Lab 8 and Lab 9

Check their requirements if you want to know the whole project structure.


## Known issues and bugs
1. Redo function will not work with a cascade delete(deleting a student/discipline must delete all
the grades and enrollments corresponding to that student/discipline):


    Solution: The cascade delete functionality is made at console level in the specific functions:
    delete student/discipline. The undo/redo functionality is operating at controllers level
    so the solution for this issue is to move the cascade delete feature at controller level.
