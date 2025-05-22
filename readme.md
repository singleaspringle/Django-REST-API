## Uruchomienie

1. Zależności:

`pip install -r requirements.txt`

2. Utworzenie bazy w PostgreSQL i aktualizacja `settings.py`.

3. Migracja obiektów do bazy:

```
python manage.py makemigrations
python manage.py migrate
```

4. Utworzenie danych testowych:

`python manage.py mock_data`

5. Uruchomienie serwera:

`python manage.py runserver`

## Endpointy

- `GET /api/v1/hits` – lista hitów
- `GET /api/v1/hits/<title_url>` – szczegóły hitu
- `POST /api/v1/hits` – dodaj hit
- `PUT /api/v1/hits/<title_url>` – edytuj hit
- `DELETE /api/v1/hits/<title_url>` – usuń hit