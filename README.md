# Opis zadania
Assembler tłumaczący instrukcje arytmetyczne procesora MIPS na kod maszynowy.
Assembler przetwarza plik tekstowy składający się z linii w następującym formacie:
```
instrukcja operand1, operand2, ... # komentarz
```

Instrukcje, które rozpoznaje assembler:
*lui, addi, addiu, slti, sltiu, andi, ori,
xori, lui, sll, srl, sra, sllv, srlv, srav, mfhi, mthi, mflo, mtlo, mult,
multu, div, divu, add, addu, sub, subu, and, or, xor, nor, slt, sltu.*

Na wyjściu znajduje się zawartość pliku źródłowego, gdzie do każdej linii zawierającej
instrukcję należy dołączony został w formie szesnastkowej jej adres i zapis binarny, np.:
```
.text
00000000 02328020 add $s0,$s1,$s2
00000004 2268FFF4 addi $t0,$s3,-12
```

# Zawartość
* pliki *Dockerfile, build.sh, run.sh* służą do uruchomienia programu na Dockerze, bez wymagania instalowania pythona ani potrzebnych bibliotek lokalnie na swoim komputerze

* *requirements.txt* - plik zawiera wymagane biblioteki (właściwie bibliotekę) pythona

* katalog *tests* zawiera kilka krótkich programów w assemblerze, które są używane w testach oraz pliki *e2e_test.py*, zawierający test sprawdzający działanie całego programu i *unit_test.py*, zawierający unit testy poszczególnych funkcji.

* *instructions_templates.py* zawiera słownik tłumaczący poszczególne instrukcje na odpowiadające im kodowanie oraz typy operandów, na przykład dla instrukcji *add*:
```
"add": [[REG, REG, REG], "000000{1}{2}{0}00000100000"]
```
* *parse_utils.py* zawiera funkcje, które parsują plik wejściowy, dla danej instrukcji i jej parametrów tłumaczą ją odpowiednio na zapis szesnastkowy

* *mipsasm.py* - plik, w którym znajduje się główna funkcja programu, która wczytuje plik wejściowy, wywołuje funkcję parsującą oraz zwraca wynik na wyjście

# Jak uruchomić:

## Lokalnie
### Wymagania
* python 2.7
* pytest
    
``` 
$ python mipsasm.py input_file_name 
```

## Za pomocą dockera

``` 
$ ./build.sh
$ ./run.sh input_file_name 
```

# Jak uruchomić testy:

## Lokalnie:
``` 
$ pytest 
```

## Na dockerze:
```
$ ./run_tests.sh
```





