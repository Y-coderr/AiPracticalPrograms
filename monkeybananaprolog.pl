% State: state(MonkeyPos, BoxPos, MonkeyStatus)
% MonkeyStatus = onBox / onFloor

goal(state(middle, middle, onBox)).

move(state(atDoor, Box, onFloor), walk(toMiddle), state(middle, Box, onFloor)).
move(state(atWindow, Box, onFloor), walk(toMiddle), state(middle, Box, onFloor)).
move(state(middle, Box, onFloor), climbBox, state(middle, Box, onBox)).
move(state(P, P, onFloor), pushBox(toMiddle), state(middle, middle, onFloor)).
move(state(atDoor, Box, onFloor), walk(toWindow), state(atWindow, Box, onFloor)).
move(state(atWindow, Box, onFloor), walk(toDoor), state(atDoor, Box, onFloor)).

solve(State, Moves) :-
    solve(State, [], Moves).

solve(State, Visited, [State]) :-
    goal(State).
solve(State, Visited, [State|Moves]) :-
    move(State, _, NextState),
    \+ member(NextState, Visited),
    solve(NextState, [State|Visited], Moves).
