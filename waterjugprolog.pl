% State represented as state(Jug1, Jug2)

goal(state(2, _)).

move(state(Jug1, Jug2), state(4, Jug2)) :- Jug1 < 4.    % Fill Jug1
move(state(Jug1, Jug2), state(Jug1, 3)) :- Jug2 < 3.    % Fill Jug2
move(state(Jug1, Jug2), state(0, Jug2)) :- Jug1 > 0.    % Empty Jug1
move(state(Jug1, Jug2), state(Jug1, 0)) :- Jug2 > 0.    % Empty Jug2

move(state(Jug1, Jug2), state(NewJug1, NewJug2)) :-    % Pour Jug1 -> Jug2
    Jug1 > 0,
    Jug2 < 3,
    Transfer is min(Jug1, 3 - Jug2),
    NewJug1 is Jug1 - Transfer,
    NewJug2 is Jug2 + Transfer.

move(state(Jug1, Jug2), state(NewJug1, NewJug2)) :-    % Pour Jug2 -> Jug1
    Jug2 > 0,
    Jug1 < 4,
    Transfer is min(Jug2, 4 - Jug1),
    NewJug2 is Jug2 - Transfer,
    NewJug1 is Jug1 + Transfer.

solve(State, Moves) :-
    solve(State, [], Moves).

solve(State, Visited, [State]) :-
    goal(State).
solve(State, Visited, [State|Moves]) :-
    move(State, NextState),
    \+ member(NextState, Visited),
    solve(NextState, [State|Visited], Moves).
