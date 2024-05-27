# SimpleChat

Implementacja prostego czatu. Serwer może obsługiwać wielu klientów jednocześnie. Przekazuje wiadomości od jednego do wszystkich innych połączonych klientów.

## Wymagania

- Python 3.10

## Instalacja
1. Sklonuj repozytorium:
    ```
    git clone https://github.com/Weisjan/SimpleChat.git
    ```
2. Uruchom serwer
3. Uruchom klienta/klientów
4. Wprowadź swoje imię, gdy zostaniesz o to poproszony.
5. Zacznij wpisywać wiadomości, aby wysłać je do serwera. Wszyscy klienci otrzymają Twoje wiadomości.

## Opis działania

#### Serwer (`server.py`)

- Serwer używa biblioteki `socket` do obsługi połączeń TCP.
- Odbiera połączenia przychodzące na `localhost` na porcie `8885`.
- Kiedy nowy klient się połączy, tworzony jest nowy wątek do obsługi komunikacji.
- Funkcja `handle_client` czyta wiadomości od klienta i przekazuje je wszystkim innym połączonym klientom..

#### Klient (`client_1.py` i `client_2.py`)

- Klient łączy się z serwerem na `localhost` na porcie `8885`.
- Prosi użytkownika o wprowadzenie swojego imienia.
- Klient wysyła wiadomości do serwera (`handle_input`) i odbiera wiadomości od serwera (`handle_output`).

## Uwagi

- `client_1.py` i `client_2.py` są funkcjonalnie identyczne. Symulują działanie na wielu klientach.

## Autor

[Jan Weis](https://github.com/Weisjan)
