from dataclasses import dataclass

@dataclass
class Trial: #Rappresenta i dati di un singolo round o prova dell'esperimento.
    position: str  # Posizione dello stimolo (es. "TOP", "BOTTOM")
    letter: str  # Carattere visualizzato
    number: int  # Numero visualizzato
    expected_answer: bool  # La risposta corretta definita dal sistema
    user_answer: bool | None = None  # Risposta data dall'utente (inizialmente nulla)
    is_correct: bool = False  # Flag per segnare se il round è stato superato

@dataclass
class GameState: #Gestisce il progresso globale, il punteggio e le statistiche della sessione.

    # --- Punteggio e Moltiplicatori ---
    score: int = 0  # Punteggio totale accumulato
    multiplier: int = 1  # Moltiplicatore attivo (es. x2, x3) per premiare la precisione
    meter: int = 0  # Barra di caricamento per attivare potenziamenti o moltiplicatori

    # --- Statistiche Risposte ---
    correct_total: int = 0  # Conteggio totale di risposte esatte fornite
    wrong_total: int = 0  # Conteggio totale di errori commessi

    # --- Gestione Streak (Sequenze) ---
    best_streak: int = 0  # Il record di risposte corrette consecutive in questa sessione
    current_streak: int = 0  # Il numero di risposte corrette consecutive attuali
