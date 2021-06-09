# banker

NUMERY KONT BANKOWYCH 
W Polsce numer IBAN ma następujący format:
``` PLNN NNNN NNNN NNNN NNNN NNNN NNNN ```

Pierwsze 2 znaki to symbol kraju, następnie 2 cyfry kontrolne. 8 następnych cyfr to ID banku. Ostatnie 16 cyfr to nr rachunku.

W jaki sposób wyliczyć cyfry kontrolne:
Weź pełny numer konta (z kodem kraju)
Długość ciągu musi wynosić dla Polski 28 znaków,
Przenosimy pierwsze 4 znaki alfanumeryczne na koniec,
Przekształcamy litery na cyfry według wzoru:
"A" to "10",
"B" to "11",
...
"Z" to "35",
W przypadku PL to 2521,
Otrzymany ciąg znaków dzielimy przez 97,
Jeśli w wyniku tego dzielenia reszta jest równa 1, to numer konta ma prawidłowe cyfry kontrolne.

Nr konta można zapisać w różnych formatach:
```PLNN NNNN NNNN NNNN NNNN NNNN NNNN
PL NN NNNN NNNN NNNN NNNN NNNN NNNN
PLNNNNNNNNNNNNNNNNNNNNNNNNNN
NN NNNN NNNN NNNN NNNN NNNN NNNN
NNNNNNNNNNNNNNNNNNNNNNNNNN```
