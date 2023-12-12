Celem programu jest znalezienie za pomocą web scrapingu infromacje odnośnie liczby ludzi, którzy wykonali testy na covid 19 tylko w krajach europejskich. 

Do programu użyłem 3 bibliotek: requests, BeautifulSoup, matplotlib. 
Za pomocą biblioteki requests pobrałem stronę internetową, a za pomocą biblioteki BeautifulSoup wyszukałem dwie kolumny z nazwami krajów jak i liczbą zrobionych testów w poszczczególnych krajach. 

Stworzyłem trzy tablice. W dwóch z nich zapisują się dane wyszukane przez biblioteke BeautifulSoup. Po przez pętle for i funkcje find.all(). 
W pętli użyłem funkcji isdigit(), która sprawdza czy w zmiennej numer są same cyfry. Jeśli nie zamienia ona je na typ int. 
Użyłem również funkcji strip(), która usuwa białe znaki jak i replace() która ma za zadanie w zmiennej numer usunąć przecinki.

W trzeciej tablicy o nazwie Europa zapisałem wszystkie kraje europejskie, aby w kolejnym kroku po odnaleźieniu i przypisaniu do dwóch pozostałych tablic można było zweryfikować czy dany kraj należy do Europy. 
Jeśli należał został przypisany do zmiennych: liczba_testow i kraje. 

Otatnią biblioteke matplotlib wykorzystałem do stworzenia wykresu słupkowego. 

JAK WŁĄCZYĆ? 
Kliknąć dwa razy na plik web_scraping.py i powinien pokazać się terminal a po krótkim czasie powinien pojawić się wykres z listą zrobionych testów na Covid 19 w krajach europejskich.





