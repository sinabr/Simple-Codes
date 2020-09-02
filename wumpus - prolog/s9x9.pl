:- use_module(library(clpfd)).

sudoku(Rows) :-
        /* For a 4x4 Sudoku all the rows (lists) must be of length 4 */
        length(Rows, 9), 
        /* Concatinate Rows (List of Lists) with a Num (Filling Empty Spaces)  */
        append(Rows, Num), 
        /* An element of [1,9] Integer Domain */
        Num ins 1..9,
        /* True if "all distinct" applies on all of the rows */
        maplist(all_distinct, Rows),
        /* Transpose the Matrix -> Rows(lists) are Columns of the original table*/
        transpose(Rows, Columns),
        /* True if "all distinct" applies on all of the columns */
        maplist(all_distinct, Columns),
        /* Rows are 9 Lists represented as A,B,C,D,... */
        Rows = [A,B,C,D,E,F,G,H,I],
        /* Rows is defined as A,B,C,D,E,F,G,H,I in which (A,B,C) , (D,E,F) and (G,H,I) groups must satisfy the 3x3 sudoku */
        subsquarecheck(A, B, C),
        subsquarecheck(D, E, F),
        subsquarecheck(G, H, I).

/* For the last iteration of the function below, which is recursive 
meaning that the empty lists satisfy the "distinct" condition */
subsquarecheck([],[],[]).

/* A recursive function checking "all_distinct" on 3x3 squares inside adjacent rows */
subsquarecheck([A1,A2,A3|A],[B1,B2,B3|B],[C1,C2,C3|C]) :-
        /* True if all of the elements are Distinct */
        all_distinct([A1,A2,A3,B1,B2,B3,C1,C2,C3]),
        /* Recursive call for the rest of the rows */
        subsquarecheck(A,B,C).

/* Problems : sample sudoku tables 

It's used to declare Rows in the sudoku call

*/



/* 
It is impossible to solve the table 1 (problem 1)

Result_1: false

Result_2: true

*/

problem(1, [[_,1,_,2,9,_,_,7,_],
            [3,_,_,4,_,1,_,8,_],
            [1,3,_,_,6,_,9,_,_],
            [4,_,_,1,8,_,_,_,3],
            [8,_,_,5,_,7,_,_,_],
            [_,_,_,7,1,2,_,_,_],
            [5,_,_,3,_,_,8,_,_],
            [_,4,_,_,_,3,_,5,_],
            [_,8,_,_,_,_,1,_,6]]). 

problem(2, [[_,_,_,_,_,_,_,_,_],
            [_,_,_,_,_,3,_,8,5],
            [_,_,1,_,2,_,_,_,_],
            [_,_,_,5,_,7,_,_,_],
            [_,_,4,_,_,_,1,_,_],
            [_,9,_,_,_,_,_,_,_],
            [5,_,_,_,_,_,_,7,3],
            [_,_,2,_,1,_,_,_,_],
            [_,_,_,_,4,_,_,_,9]]).

/* Run Command:

problem(1,Rows),sudoku(Rows),maplist(writeln,Rows).

Result:
false.

problem(2,Rows),sudoku(Rows),maplist(writeln,Rows).

Result:
[9,8,7,6,5,4,3,2,1]
[2,4,6,1,7,3,9,8,5]
[3,5,1,9,2,8,7,4,6]
[1,2,8,5,3,7,6,9,4]
[6,3,4,8,9,2,1,5,7]
[7,9,5,4,6,1,8,3,2]
[5,1,9,2,8,6,4,7,3]
[4,7,2,3,1,9,5,6,8]
[8,6,3,7,4,5,2,1,9]

*/