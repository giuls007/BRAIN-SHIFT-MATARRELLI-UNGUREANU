# Brain Shift — Progetto di Gruppo

**Brain Shift** è un serio-game di psicologia cognitiva focalizzato sul *task-switching*. Il gioco sfida la tua flessibilità mentale chiedendoti di alternare tra regole logiche diverse in frazioni di secondo, simulando i test di laboratorio per la valutazione delle funzioni esecutive.

## Chi siamo

* **Giulia Matarrelli** — [GitHub](https://github.com/giuls007/BRAIN-SHIFT-MATARRELLI-UNGUREANU/tree/main)
* **Martina Ungureanu** — [GitHub](https://github.com/giuls007/BRAIN-SHIFT-MATARRELLI-UNGUREANU/tree/main)

Classe 4A Informatica — a.s. 2025-26.

## Cos'è Brain Shift

In Brain Shift, devi classificare una serie di carte composte da una lettera e un numero. La sfida sta nel fatto che la regola cambia in base alla posizione della carta: se appare in **ALTO**, devi decidere se il numero è **pari**; se appare in **BASSO**, devi decidere se la lettera è una **vocale**. È un gioco di velocità e precisione dove il punteggio cresce esponenzialmente grazie a un sistema di moltiplicatori che premia le streak di risposte corrette senza errori.

## Come giocare

Istruzioni per far partire il gioco da un clone pulito:

```bash
# 1. Clona il repository
git clone https://github.com/giuls007/BRAIN-SHIFT-MATARRELLI-UNGUREANU.git

# 2. Entra nella cartella del progetto
cd BRAIN-SHIFT-MATARRELLI-UNGUREANU

# 3. Installa le dipendenze
pip install pygame

# 4. Avvia il gioco
python main.py

```

### Requisiti tecnici

* **Python**: versione 3.10 o superiore.
* **Pygame**: versione 2.0 o superiore.

## Controlli

* **Freccia Sinistra**: Risposta **NO** / Falso.
* **Freccia Destra**: Risposta **SÌ** / Vero.
* **Tasto P**: Mette in pausa il gioco (ferma il timer di sessione).
* **Tasto R**: Ricomincia la partita (disponibile nella schermata dei risultati).
* **Tasto SPAZIO**: Inizia la partita dalla schermata iniziale.
* **Tasto ESC**: Chiude il gioco.

## Screenshot

*(Puoi trovare le immagini del gioco nella cartella `docs/img/`)*

## Struttura del repository

Il progetto è organizzato in modo modulare per separare la logica pura dalla visualizzazione Pygame:

```text
brain_shift/
├── main.py            ← Entry point e gestione del game loop
├── config.py          ← Costanti e parametri di configurazione
├── models.py          ← Strutture dati (Trial, GameState)
├── rules.py           ← Logica pura per la validazione delle regole
├── scoring.py         ← Calcolo punti, meter e moltiplicatori
├── states.py          ← Definizione della macchina a stati (INTRO, PLAYING, ecc.)
├── input_handler.py   ← Gestione della tastiera e normalizzazione input
├── generator.py       ← Generazione dei trial con logica anti-streak
├── ui.py              ← Modulo dedicato al rendering grafico
├── docs/              ← Documentazione (Devlog, Scelte, IA)
└── tests/             ← Test automatizzati con Pytest

```

## Come lanciare i test

Per assicurarsi che la logica delle regole e dello scoring sia corretta, è possibile lanciare i test unitari:

```bash
pytest tests/

```