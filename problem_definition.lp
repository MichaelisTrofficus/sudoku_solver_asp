%% PROBLEM DEFINITION

%% Definimos un predicado para el indice de fila, otro para columnas y otro para el valor de cada celda.
%% Los tres predicados pueden ser generados mediante un intervalo 1..9 (son 9 los numeros y trabajamos con sudokus 9 x 9)

rowIndex(1..9).
colIndex(1..9).
cellValue(1..9).


%% GENERATE 

%% El planteamiento es casi identico al caso de la coloracion de un grafo
%% Asociamos a cada celda un unico valor

1 {state(X,Y,C): cellValue(C)} 1 :- rowIndex(X) ,colIndex(Y).


%% TEST

%% Creamos una serie de reglas auxiliares para ayudarnos a determinar si dos coordenadas 
%% pertenecen a la misma caja 3x3

sameRow(X, Z) :- rowIndex(X), rowIndex(Z), (X - 1)/3 == (Z - 1)/3.
sameCol(Y, W) :- colIndex(Y), colIndex(W), (Y - 1)/3 == (W - 1)/3.
sameBox(X, Y, Z, W) :- sameRow(X, Z), sameCol(Y, W).

%% Regla 1: No puede haber dos numeros iguales en la misma columna
:- state(X, Y, C), state(Z, Y, C),  X != Z.

%% Regla2: No puede haber dos numeros iguales en la misma fila
:- state(X, Y, C), state(X, W, C),  Y != W.

%% Regla3: No puede haber dos numeros iguales en la misma caja 3x3
:- state(X,Y,V), state(Z,W,V), sameBox(X, Y, Z, W), X != Z, Y != W.

#show state/3.
