# Brain Shift — Cognition Lab Game

**Brain Shift** è un serio-game di psicologia cognitiva sviluppato in Python utilizzando la libreria **Pygame**. Il progetto simula un compito di *task-switching*, progettato per testare e allenare la flessibilità cognitiva e la rapidità di risposta attraverso stimoli visivi dinamici.

---

## Il Gioco
Il giocatore deve rispondere a una serie di carte che appaiono in due posizioni diverse dello schermo. La regola da applicare cambia istantaneamente in base alla posizione della carta:

- **Posizione SUPERIORE (TOP):** Regola numerica. Verifica se il **NUMERO** è **PARI**.
- **Posizione INFERIORE (BOTTOM):** Regola alfabetica. Verifica se la **LETTERA** è una **VOCALE**.

L'obiettivo è ottenere il punteggio più alto in **60 secondi**, sfruttando il sistema di moltiplicatori basato sulla precisione e sulla velocità.

### Controlli
| Tasto | Azione |
| :--- | :--- |
| **Freccia DESTRA** | Risposta **SÌ** / VERO |
| **Freccia SINISTRA** | Risposta **NO** / FALSO |
| **Tasto P** | Pausa / Riprendi |
| **Tasto R** | Ricomincia la partita (Schermata Risultati) |
| **Tasto ESC** | Esci dal gioco |
| **SPAZIO** | Inizia il gioco (Schermata Intro) |

---

## Architettura del Progetto
Il codice segue un'architettura modulare e disaccoppiata, separando la logica di calcolo dal rendering grafico:

* `main.py`: Punto di ingresso che orchestra il loop principale e le transizioni tra gli stati.
* `states.py`: Gestione della macchina a stati (INTRO, PLAYING, PAUSE, RESULTS) tramite Enum.
* `input_handler.py`: Modulo di astrazione che traduce i tasti fisici in azioni logiche di gioco.
* `ui.py`: Gestione del rendering grafico, feedback visivi (verde/rosso) e fading delle istruzioni.
* `scoring.py`: Sistema di punteggio avanzato con gestione di streak, meter e moltiplicatori (max 10x).
* `generator.py`: Generatore di trial bilanciato con logica anti-streak (max 3 risposte uguali).
* `rules.py`: Logica pura per la validazione delle risposte (Vocali, Pari, Posizioni).
* `models.py`: Strutture dati tramite `@dataclass` per la gestione dello stato e dei trial.
* `config.py`: Parametri globali (colori, coordinate, timing e costanti di gioco).

---

## Installazione e Avvio

### Prerequisiti
- **Python 3.10** o superiore.
- Libreria **Pygame 2.x**.

