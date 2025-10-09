# Laboration 3 – Linjär klassificering

Detta repo innehåller lösningen på Laboration 3 på godkänd nivå.

## Filer
- `lab3.py` – huvudprogrammet som läser in `unlabelled_data.csv`, klassificerar punkterna mot linjen **y = -1x + 0.47**,
  sparar resultat i `labelled_data.csv` och ritar en graf (`plot.png`).
- `unlabelled_data.csv` – indatan som ges i uppgiften.
- `labelled_data.csv` – skapas automatiskt efter körning av `lab3.py`.

## Körning
```bash
python3 lab3.py
```

## Utdata
- `labelled_data.csv` innehåller en extra kolumn `label`:
  - `0` = punkt under/vänster om linjen
  - `1` = punkt över/höger om linjen
- `plot.png` visar punkter + linjen.
