# KNN-Klassificerare: Pichu vs Pikachu (Labb 2)

(kNN) klassificerare som klassificerar Pokémon som **Pichu (0)** eller **Pikachu (1)** utifrån längd-/breddmätningar.

## Projektstruktur
pichu_pikachu_knn/
├── data/
│   ├── datapoints.txt       # träningsdata: bredd, längd, etikett
│   └── testpoints.txt       # testprover att klassificera
├── src/
│   ├── knn.py               # kärnlogik för kNN (ren Python)
│   └── main.py              # CLI-startpunkt
├── tests/
│   └── test_facit.py        # verifierar givet facit på fyra prover
├── .gitignore
└── README.md


## Snabbstart
```bash
# 1) Kör CLI:n på de angivna testpunkterna (k=1 som standard)
python -m src.main --data data/datapoints.txt --test data/testpoints.txt

# 2) Prova majoritetsröstning med de 10 närmaste grannarna
python -m src.main --data data/datapoints.txt --test data/testpoints.txt --k 10

# 3) Klassificera en enskild punkt du skriver in själv (med inmatningsvalidering)
python -m src.main --data data/datapoints.txt --interactive
Vad programmet gör
Laddar träningsdata från datapoints.txt (bredd, längd, etikett där 0=Pichu, 1=Pikachu).

Beräknar Euklidiskt avstånd för att hitta de k närmaste grannarna.

Förutsäger klassen med k=1 (närmaste granne) eller k=10 (majoritetsröstning).

Hanterar ogiltiga inmatningar (negativa tal / icke-numeriska) med vänliga meddelanden.

Skriver ut resultat i exakt det format som förväntas i labben.

Exempel på utdata (k=1)
Sample with (width, height): (25.0, 32.0) classified as Pikachu
Sample with (width, height): (24.2, 31.5) classified as Pikachu
Sample with (width, height): (22.0, 34.0) classified as Pikachu
Sample with (width, height): (20.5, 34.0) classified as Pichu
Testning (facit)


