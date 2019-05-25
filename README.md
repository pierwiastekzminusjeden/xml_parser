# Zadanie - staż SolarWinds
# Autor: Krystian Molenda

## Uruchomienie programu
>Program należyh uruchomić poprzez skrypt swi.py.Plik wejściowy powinien się znajdować w tym samym katalogu co skrypt swi.py.

>Kod źródłowy znajduje się w katalogu soruce. Domyślnie ustawione są nazwy "input.xml" dla pliku wejściowego oraz "output.json" dla wyjściowego. Zmiana nazw plików jest możliwa poprzez prostą edycję pliku swi.py.

## Założenia projektowe
> W projekcie zakładam, że dane linia 54 przykładowego pliku gdzie znajduje się ``` <type>string</name> ``` to błąd. Plik taki nie przechodzi walidacji xml. Skorzystałem z narzędzi pozwalających mi na naprawienie tego błędu i zamienienie wspomnianego fragmentu na ``` <type>string</type> ```.<br> Zakładam również, że dane testowe będą w podobnej formie do danych przykładowych, tzn. nie będzie elementu głównego oraz nagłówka xml. Nagłówek do przetwarzania danych w mojej metodzie nie jest potrzebny. Ze względu na większą możliwość w wykorzystaniu narzędzi dodaję główny element ```<root>```
do pliku "input.xml" przed rozpoczęciem jego przetwarzania.
