
:- use_module(library(clpfd)).
:- use_module(library(apply)).
:- use_module(library(lists)).

sudoku(Rows) :-
        /* For a 4x4 Sudoku all the rows (lists) must be of length 4 */
        length(Rows, 4), 
        /* Concatinate Rows (List of Lists) with  */
        append(Rows, Num), 
        /* An element of [1,4] Integer Domain */
        Num ins 1..4,
        /* True if "all distinct" applies on all of the rows */
        maplist(all_distinct, Rows),
        /* */
        transpose(Rows, Columns),
        /* True if "all distinct" applies on all of the columns */
        maplist(all_distinct, Columns),
        /* Rows are 4 Lists represented as A,B,C,D */
        Rows = [A,B,C,D],
        /* Rows is defined as A,B,C,D in which (A,B) and (C,D) pairs must satisfy the 2x2 sudoku */
        subsquarecheck(A, B),
        subsquarecheck(C, D).

/* For the last iteration of the function below, which is recursive, 
meaning that the empty lists satisfy the "distinct" condition */
subsquarecheck([], []).

/* A recursive function checking "all_distinct" on 2x2 squares inside adjacent rows */
subsquarecheck([N1,N2|Ns1], [N3,N4|Ns2]) :-
        all_distinct([N1,N2,N3,N4]),
        subsquarecheck(Ns1, Ns2).

/* Problems : sample sudoku tables 

It's used to declare Rows in the sudoku call

*/



/* 
It is impossible to solve the table below

Result: false

*/

problem(1, [[_,1,_,2],[3,_,_,4],[1,3,_,_],[4,_,_,1]]). 

problem(2, [[_,3,2,_],[4,2,_,_],[2,_,_,1],[_,_,4,_]]).


/* Run Command:

problem(1,Rows),sudoku(Rows).

Result:
false.

problem(2,Rows),sudoku(Rows).

Result:

[[1, 3, 2, 4], [4, 2, 1, 3], [2, 4, 3, 1], [3, 1, 4, 2]].

*/