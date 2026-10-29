% Experiment 25: Best First Search in Prolog
% Save as .pl and run in SWI-Prolog (this experiment is Prolog, not Python).

edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(e, g).
edge(f, g).

heuristic(a, 7).
heuristic(b, 5).
heuristic(c, 4).
heuristic(d, 6).
heuristic(e, 2).
heuristic(f, 1).
heuristic(g, 0).

best_first(Start, Goal, Path) :-
    best_first_loop([[Start]], Goal, [], RevPath),
    reverse(RevPath, Path).

best_first_loop([[Goal|Rest]|_], Goal, _, [Goal|Rest]).
best_first_loop([[Node|Rest]|Queue], Goal, Visited, Path) :-
    ( member(Node, Visited) ->
        best_first_loop(Queue, Goal, Visited, Path)
    ;
        findall([Next,Node|Rest],
                (edge(Node, Next), \+ member(Next, [Node|Rest]), \+ member(Next, Visited)),
                NewPaths),
        append(Queue, NewPaths, Combined),
        predsort(compare_paths, Combined, Sorted),
        best_first_loop(Sorted, Goal, [Node|Visited], Path)
    ).

compare_paths(Order, [A|_], [B|_]) :-
    heuristic(A, HA), heuristic(B, HB),
    compare(Order, HA, HB).

% Example query:
% ?- best_first(a, g, Path).
