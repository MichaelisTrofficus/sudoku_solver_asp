from io import StringIO
import sys

import clingo


class Capturing(list):

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


def on_model(m):
    print(m)


def solve(problem_instance):
    ctl = clingo.Control()

    # First we add the problem definition
    ctl.add("base", [], """
    rowIndex(1..9).
    colIndex(1..9).
    cellValue(1..9).

    1 {state(X,Y,C): cellValue(C)} 1 :- rowIndex(X) ,colIndex(Y).

    sameRow(X, Z) :- rowIndex(X), rowIndex(Z), (X - 1)/3 == (Z - 1)/3.
    sameCol(Y, W) :- colIndex(Y), colIndex(W), (Y - 1)/3 == (W - 1)/3.
    sameBox(X, Y, Z, W) :- sameRow(X, Z), sameCol(Y, W).

    :- state(X, Y, C), state(Z, Y, C),  X != Z.

    :- state(X, Y, C), state(X, W, C),  Y != W.

    :- state(X,Y,V), state(Z,W,V), sameBox(X, Y, Z, W), X != Z, Y != W.

    #show state/3.
    """)

    ctl.add("base", [], problem_instance)
    ctl.ground([("base", [])])

    with Capturing() as output:
        ctl.solve(on_model=on_model)

    return output[0].split(" ")
