/* Main Sudoku Predicate */

:- use_module(library(clpfd)).

sudoku( A1, A2, A3, A4, B1, B2, B3, B4, C1, C2, C3, C4, D1, D2, D3, D4):- 
                
        solve(A1, A2, A3, A4, B1, B2, B3, B4, C1, C2, C3, C4, D1, D2, D3, D4), 

        printrow(A1,A2,A3,A4), printrow(B1,B2,B3,B4),  printrow(C1,C2,C3,C4),  printrow(D1,D2,D3,D4).


printrow(Num1,Num2,Num3,Num4):-
        write(Num1),write('  '),write(Num2),write('  '),write(Num3),write('  '),write(Num4),nl.


/* check if numbers in range and all are different */
allDistinct(A, B, C, D):-      
        valid(A),valid(B),valid(C),valid(D),

        /* From clpfd library, checks if all values are distinct  */
        /* all_distinct([A,B,C,D]). */
        A\=B, A\=C, A\=D, B\=C, B\=D, C\=D.
        
solve(A1, A2, A3, A4, B1, B2, B3, B4, C1, C2, C3, C4, D1, D2, D3, D4):-
        /* check rows */
        allDistinct(B1,B2,B3,B4),
        allDistinct(A1,A2,A3,A4),
        allDistinct(C1,C2,C3,C4),
        allDistinct(D1,D2,D3,D4),
        /* check columns */
        allDistinct(B1,A1,C1,D1),
        allDistinct(A2,B2,C2,D2),
        allDistinct(A3,B3,C3,D3),
        allDistinct(A4,B4,C4,D4),
        /* check 2x2 columns */
        allDistinct(B1,A1,A2,B2),
        allDistinct(A3,B3,A4,B4),
        allDistinct(C1,D1,C2,D2),
        allDistinct(C3,D3,C4,D4).


/* Its valid only if between 1 - 4 */
valid(1). 
valid(2). 
valid(3). 
valid(4).




/*

Sample Query : sudoku(_,3,2,_,_,2,_,3,2,4,_,_,_,1,4,_).

Result:

1  3  2  4
4  2  1  3
2  4  3  1
3  1  4  2

*/