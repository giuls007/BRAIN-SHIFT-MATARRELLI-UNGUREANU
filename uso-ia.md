# Uso dell'IA nel progetto

> Questa pagina serve a dichiarare **in modo onesto e granulare** come avete usato assistenti IA (ChatGPT, Claude, Copilot, Gemini, ecc.) durante lo sviluppo. È obbligatoria. Va scritta **da voi**, non dall'IA.

---

## Politica del progetto

L'IA è consentita come assistente (spiegazioni, suggerimenti, debug, codice di dettaglio ben compreso) ma non come risolutore automatico (generazione e consegna di codice non compreso). Le parti di **documentazione e metacognizione** (questa pagina inclusa, `devlog.md`, `scelte.md`) vanno scritte senza IA.

Abbiamo utilizzato l'IA come un "collega esperto" a cui chiedere spiegazioni su Pygame e suggerimenti su come strutturare i calcoli matematici dello scoring. Non abbiamo mai fatto "copia-incolla" acritico: ogni suggerimento è stato analizzato, testato e spesso modificato per integrarsi con il resto della nostra architettura modulare. 

## Strumenti usati

Elencate gli strumenti IA che il gruppo ha effettivamente usato durante il progetto:

- [ ] ChatGPT (modello: …)
- [ ] Claude (modello: …)
- [ ] GitHub Copilot
- [ ] Gemini (modello: …)
- [ ] altro: …

Se non avete usato IA, dichiaratelo esplicitamente.

[x] Gemini (modello: 1.5 Flash / Pro)
[ ] GitHub Copilot (usato occasionalmente per l'autocompletamento di commenti e docstring)

## Uso granulare per modulo / parte

Per **ogni parte del codice** in cui avete usato l'IA, una entry strutturata. Copiate il template sottostante quante volte serve.

### Template

**Dove**: `scoring.py`, funzione `apply_correct_answer` (righe 34-52)

**Cosa abbiamo chiesto**: in sintesi, la richiesta fatta all'IA. Anche solo una frase tipo «come gestire la saturazione del moltiplicatore a 10?».

**Cosa ci ha suggerito**: sintesi della risposta dell'IA, o snippet originale.

**Cosa abbiamo fatto**:
- [ ] accettato integralmente
- [ ] modificato adattandolo al nostro codice
- [ ] preso solo l'idea e riscritto
- [ ] rifiutato, perché…

**Perché**: se avete modificato o rifiutato, spiegate cosa non andava. Se avete accettato integralmente, spiegate come avete verificato che il codice fosse corretto.

-Gestione del Tempo e Pausa
Dove: main.py, logica del timer e della pausa.

Cosa abbiamo chiesto: «Come posso fermare un timer basato su time.time() quando il gioco va in pausa, in modo che non scada mentre l'utente non sta giocando?»

Cosa ci ha suggerito: L'idea di memorizzare il timestamp di inizio pausa e, al momento della ripresa, calcolare la differenza e aggiungerla a una variabile accumulatrice total_pause_time.

Cosa abbiamo fatto: lo abbiamo modificato adattandolo al nostro codice

Perché: Il suggerimento originale era generico; lo abbiamo adattato integrandolo nella nostra classe GameState e assicurandoci che il calcolo avvenisse solo nel passaggio di stato tra PAUSE e PLAYING.

-Logica dello Scoring Avanzato
Dove: scoring.py, funzione di aggiornamento del meter e del moltiplicatore.

Cosa abbiamo chiesto: «Aiutami a scrivere una funzione che aumenti un meter ogni risposta corretta, ma che aumenti il moltiplicatore (max 10) solo quando il meter è pieno, e che lo resetti correttamente in caso di errore.»

Cosa ci ha suggerito: Uno snippet che usava l'operatore modulo % per gestire il meter e la funzione min() per saturare il moltiplicatore a 10.

Cosa abbiamo fatto: abbiamo preso solo l'idea e riscritto

Perché: Lo snippet suggerito non gestiva la nostra struttura a @dataclass. Abbiamo riscritto la logica da zero usando l'idea del min(mult + 1, 10) ma applicandola direttamente agli attributi del nostro oggetto di stato.

-Trasparenza dei Font (Fading)
Dove: ui.py, funzione draw_instructions.

Cosa abbiamo chiesto: «Perché text_surface.set_alpha() non funziona in Pygame se il font ha un colore specifico?»

Cosa ci ha suggerito: Ci ha spiegato che le superfici di testo con antialiasing spesso ignorano il set_alpha diretto e che è necessario fare il blit su una superficie temporanea o usare una modalità colore specifica.

Cosa abbiamo fatto: accettato integralmente (la spiegazione teorica)

Perché: Era un limite tecnico di Pygame che non conoscevamo. Abbiamo applicato la soluzione della superficie temporanea (Surface.convert_alpha()) verificando riga per riga come venisse gestito il canale alpha.

## Verifiche di comprensione

Dopo ogni uso dell'IA su parti di codice non banali, fatevi questa domanda: «Se il docente mi chiede di spiegare questa riga all'orale, so farlo?». Se la risposta è no, fermatevi e chiedete all'IA di *spiegare*, non di *scrivere*.

All'orale, ogni membro del gruppo deve saper spiegare ogni parte del codice. Se avete usato l'IA senza capire, all'orale si vede immediatamente.

Abbiamo verificato ogni riga suggerita dall'IA. Ad esempio, sappiamo spiegare esattamente perché usiamo time.time() invece di un semplice contatore di frame (per l'indipendenza dal refresh rate del monitor) e come il calcolo del moltiplicatore influenzi il punteggio finale tramite il prodotto della base per lo streak corrente. Siamo pronti a difendere ogni scelta all'orale.

## Cosa non abbiamo chiesto all'IA

Elencate esplicitamente le parti che avete scritto **senza** assistenza IA. Serve a voi per esercitare la consapevolezza, e al docente per avere un confronto.

Esempi:
- tutti i test pytest
- `docs/devlog.md` e `docs/scelte.md`
- la logica del generatore
- …

Queste parti rappresentano il nostro lavoro originale e la nostra capacità di progettazione:

Tutti i test pytest: Abbiamo scritto noi i test in tests/ per verificare che la nostra logica (vocali/pari/posizioni) fosse solida.
La struttura a moduli: La decisione di dividere il codice in rules.py, models.py, ecc. è stata nostra per garantire la manutenibilità.
docs/devlog.md e docs/scelte.md: Sono il racconto del nostro percorso e delle nostre fatiche, scritte riflettendo sui problemi incontrati.
La logica del Generatore: Abbiamo scritto noi come estrarre i trial assicurandoci che non fossero troppo ripetitivi.

### Domande-guida

1. La dichiarazione è **granulare** (modulo per modulo, funzione per funzione) o generica («abbiamo usato ChatGPT qualche volta»)?
2. Per ogni uso dell'IA sapreste rispondere se il docente vi chiedesse «spiegami perché questa riga fa così»?
3. Avete distinto fra *chiedere spiegazioni* e *far scrivere codice*?
4. Questa pagina è coerente con quello che il docente vedrà leggendo il codice?
