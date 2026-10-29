# Micro:bit game project

Projekt gry zręcznościowej opartej na micro:bit, z systemem zapisywania wyników i rankingiem dostępnym przez Internet oraz na urządzeniu fizycznym.

## O projekcie

Celem projektu jest stworzenie gry zręcznościowej, w której wyniki graczy są przesyłane do centralnego backendu, zapisywane w bazie danych i udostępniane w postaci rankingu.

System będzie składał się z gry uruchamianej na micro:bit-cie, backendu udostępniającego API w Python, relacyjnej bazy danych PostgreSQL oraz interfejsu umożliwiającego przeglądanie wyników.

## Architektura systemu

Planowana architektura opiera się na modelu klient–serwer.

1. **Micro:bit** — obsługa mechaniki gry i obliczanie wyniku.
2. **Warstwa komunikacyjna** — przekazywanie wyników z urządzenia do backendu.
3. **Backend** — obsługa żądań HTTP, walidacja danych i udostępnianie rankingu.
4. **Baza danych** — trwałe przechowywanie informacji o graczach i wynikach.
5. **Interfejs WWW** — prezentacja rankingu w przeglądarce.
6. **Urządzenie rankingowe** — pobieranie i wyświetlanie wyników na fizycznym urządzeniu.

### Przepływ danych

`Micro:bit → komunikacja → FastAPI → PostgreSQL`

`FastAPI → ranking → strona WWW / urządzenie fizyczne`

## Technologie

| Technologia | Zastosowanie |
|---|---|
| Python | Główny język programowania |
| FastAPI | Backend i REST API |
| PostgreSQL | Relacyjna baza danych |
| HTML / CSS | Interfejs strony internetowej |
| Micro:bit | Urządzenie uruchamiające grę |
| Docker / Docker Compose | Planowane uruchamianie usług w kontenerach |

Wykorzystane technologie mogą ulec zmianie podczas tworzenia projektu.

## Planowane endpointy API

| Metoda | Endpoint | Opis |
|---|---|---|
| `POST` | `/api/scores` | Zapis nowego wyniku |
| `GET` | `/api/leaderboard` | Pobranie rankingu |
| `GET` | `/api/players/{player_id}/scores` | Pobranie historii wyników gracza |

Szczegóły dotyczące API zostaną ustalone w trakcie implementacji projektu.

## Struktura projektu

```text
microbit-project/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── schemas.py
├── tests/
├── microbit/
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .env.example
└── README.md
```

Struktura może ulec zmianie w trakcie rozwoju projektu.

## Uruchomienie projektu

Instrukcja instalacji i uruchomienia zostanie uzupełniona po przygotowaniu pierwszej działającej wersji aplikacji.

Docelowo projekt będzie można uruchomić lokalnie lub za pomocą Docker Compose.

## Autor

Dawid Ołdak
