# Scelte implementative

> Qui va la parte più **metacognitiva** del progetto: cosa avete scelto, perché, cosa avete scartato. Non può essere scritta dall'IA — è il ragionamento che mostra che avete capito quello che avete fatto.

## Scelte rilevanti

Per ciascuna scelta non banale che avete fatto, scrivete:

1. **Cosa**: la scelta in una riga.
2. **Perché**: la ragione. Vincoli? Pregi? Abitudine?
3. **Alternative considerate**: almeno una alternativa che avete valutato e scartato.
4. **Conseguenze**: cosa è diventato facile e cosa è diventato difficile per colpa di questa scelta.

### Esempio di formato

**Scelta**: rappresentiamo la posizione della carta con un `Enum` (`Position.TOP`, `Position.BOTTOM`) invece che con una stringa.

**Perché**: autocompletamento nell'IDE, impossibile passare un valore errato per sbaglio, codice più leggibile nei `match`.

**Alternative considerate**: stringhe ("top", "bottom"). Scartata perché troppo facile scrivere "Top" invece di "top" e introdurre un bug silenzioso.

**Conseguenze**: un import in più nei moduli che usano la posizione; nessuno svantaggio concreto.

---

## Sezioni da trattare

Non dovete coprire tutte queste sezioni in modo rigido: sceglietene le più rilevanti per il vostro progetto e approfonditele.

### Struttura del progetto

Perché quella decomposizione in moduli? Avete valutato un'unica libreria `game.py`? 
Abbiamo scelto una decomposizione modulare spinta (ui, rules, scoring, input_handler, states, generator) invece di un unico file game.py.
Perché: Questa scelta ci ha permesso di isolare la logica pura dalla grafica. È stato fondamentale per il debug: potevamo testare se le regole di rules.py funzionassero senza nemmeno far partire Pygame.
Alternativa scartata: Un'unica libreria game.py. L'abbiamo esclusa perché avrebbe creato un codice "a spaghetti" dove una modifica alla grafica rischiava di rompere il calcolo del punteggio.

### Scoring

Come avete tradotto la formula della specifica in codice? `dict` mutabile, `dataclass` mutabile, funzioni pure che restituiscono un nuovo stato?
Per tradurre la formula della specifica abbiamo usato una dataclass mutabile (GameState in models.py) gestita da una funzione in scoring.py.
Perché: La formula richiede di tenere traccia di troppe variabili (meter, streak, moltiplicatore, punteggio totale). Usare un dizionario sarebbe stato rischioso per la mancanza di autocompletamento, mentre una funzione pura che restituisce un nuovo stato ogni volta sarebbe stata eccessivamente pesante per un gioco così semplice.
Alternativa scartata: Variabili globali. Scartate perché rendono i test impossibili e il codice fragile.

### Generatore

Che algoritmo usate per bilanciare YES/NO? Rigenerate i trial sbilanciati o aggiustate dopo? Come gestite il seed?
Il bilanciamento tra YES/NO avviene tramite la generazione casuale dei singoli componenti della carta (posizione, lettera, numero) gestita da un oggetto random.Random (seed-friendly).
Perché: Passare un oggetto rng esterno ci permette di controllare il seed per il testing, rendendo i trial prevedibili se necessario.
Alternativa scartata: Una lista predefinita di trial. Scartata perché avrebbe reso il gioco ripetitivo e prevedibile per l'utente dopo poche partite.

### Gestione del tempo

Come tenete traccia del timer di sessione? `time.time()`, `pygame.time.get_ticks()`, `Clock`? Perché?
Usiamo time.time() per il timer di sessione, integrato con una variabile total_pause_time.
Perché: time.time() ci dà la precisione del cronometro di sistema. Rispetto a pygame.time.get_ticks(), ci permette di gestire la pausa in modo molto più intuitivo: quando mettiamo in pausa salviamo il timestamp d'inizio e, alla ripresa, aggiungiamo la differenza al "ritardo" totale.

Alternativa scartata: pygame.time.Clock. Ottimo per i FPS, ma meno comodo per gestire un timer di 60 secondi che deve "congelarsi".

### Inter-trial interval

Come lo realizzate senza bloccare il main loop? Variabile di stato + timer? Timestamp della prossima transizione?
Abbiamo evitato di bloccare il main loop usando una variabile di stato + timestamp (feedback_until).
Perché: Volevamo che il feedback (verde/rosso) durasse un istante preciso (150ms). Se avessimo usato un delay classico, il gioco si sarebbe "congelato" a ogni risposta. Con il timestamp, il loop continua a girare a 60 FPS e semplicemente smette di colorare la carta quando il tempo è scaduto.
Alternativa scartata: pygame.time.wait(). Scartata perché blocca l'aggiornamento dello schermo e l'input dell'utente.

### Input

Se avete input multipli, come li normalizzate? Dove avviene la normalizzazione?
La normalizzazione dell'input avviene in input_handler.py.
Perché: Qui traduciamo gli eventi di Pygame (come K_RIGHT o K_LEFT) in stringhe logiche come "YES" o "NO". Questo significa che il main.py non sa quale tasto è stato premuto, sa solo quale azione l'utente voleva compiere.
Alternativa scartata: Gestione diretta nel main. Scartata perché avrebbe reso il loop principale troppo lungo e difficile da leggere.

### Feedback visivo

Come evitate che le animazioni rallentino il loop? Se è un'animazione "a tempo" come la gestite (stato + timestamp)?
Per evitare rallentamenti, il feedback visivo non è un'animazione complessa ma un cambio di stato del colore di rendering.
Perché: È la soluzione computazionalmente più leggera. Usiamo il timestamp per determinare se disegnare la carta con il colore di feedback o con quello standard.
Alternativa scartata: Caricare sprite o immagini diverse per il feedback. Scartata per non appesantire il caricamento degli asset.

### Fading istruzioni

Interpolazione lineare, soglie discrete, funzione ease? Come l'avete implementato?
Abbiamo implementato il fading tramite soglie discrete di opacità (alpha).
Perché: Invece di un'interpolazione lineare (troppo distraente), abbiamo deciso di abbassare l'opacità delle scritte ogni 4 risposte corrette. Questo dà al giocatore la sensazione di "progresso" e pulisce l'interfaccia man mano che diventa esperto.
Alternativa scartata: Far sparire le istruzioni dopo un tempo fisso. Scartata perché ogni utente ha tempi di apprendimento diversi; legarlo alle risposte corrette è più "intelligente".

### Asset grafici / audio

Se ne avete usati, da dove vengono? Licenza? Come li caricate (a init, a richiesta)?
Non abbiamo usato asset esterni o audio.

Perché: Abbiamo scelto di puntare tutto su una grafica procedurale pulita e minimalista (forme geometriche e font di sistema). Questo garantisce che il gioco funzioni su qualsiasi PC senza dover gestire percorsi di file o licenze di terze parti.
Alternativa scartata: Uso di icone e suoni scaricati. Scartata per evitare problemi di copyright e dipendenze esterne.


## Cosa non siamo riusciti a fare e perché

Parte importante. Onestà, non scuse.

- cosa avete lasciato fuori: Comparto Audio: Avevamo pianificato l'inserimento di feedback sonori (un "ding" per le risposte corrette e un suono più sordo per l'errore). Abbiamo deciso di lasciarlo fuori perché la gestione delle librerie audio in Pygame spesso dà problemi di latenza o dipendenze su sistemi diversi. Abbiamo preferito investire quel tempo nel raffinare il sistema di moltiplicatori e lo scoring, che ritenevamo più critici per la valutazione.
Leaderboard Persistente: L'idea iniziale era salvare i record in un file JSON o CSV. Abbiamo desistito perché avrebbe richiesto la gestione di eccezioni (file corrotto, permessi di scrittura) che avrebbero sporcato il codice a ridosso della consegna. Ci siamo limitati a una schermata di risultati finale molto dettagliata ma volatile.

- cosa avete iniziato e poi abbandonato: Animazione di Transizione: Volevamo che le carte scorressero lateralmente (slide) alla risposta dell'utente. Avevamo iniziato a bozzare una gestione di "offset" x e y nel main.py, ma abbiamo capito subito che questo avrebbe complicato enormemente l'input handler (bisognava bloccare l'input durante l'animazione per evitare bug). Abbiamo abbandonato l'idea in favore di un cambio carta istantaneo, che risulta comunque molto reattivo per un gioco di velocità.
Livelli di Difficoltà: Avevamo pensato di diminuire il tempo a disposizione o aumentare la velocità man mano che il punteggio saliva. Abbiamo abbandonato l'idea perché il sistema di moltiplicatori e il "meter" creano già di per sé una sfida crescente basata sulla precisione, e aggiungere altri parametri avrebbe rischiato di rendere il gameplay frustrante invece che sfidante.

- cosa sapete che è fatto male ma non abbiamo avuto tempo di sistemare: Hard-coding dei Font: Nel modulo ui.py richiamiamo i font di sistema ("Segoe UI", "Arial"). Sappiamo che questa è una pratica rischiosa perché se il gioco gira su un sistema senza quei font (es. una distro Linux minimale), il risultato estetico potrebbe cambiare drasticamente. La soluzione corretta sarebbe stata includere un file .ttf nella cartella degli asset, ma per brevità abbiamo optato per i font di sistema.
Gestione del ridimensionamento: Il gioco è pensato per una finestra fissa di 800x600. Se l'utente prova a ridimensionare la finestra, l'interfaccia non è reattiva (non c'è un sistema di coordinate relative o percentuali). È un limite tecnico che avremmo risolto con un sistema di layout più complesso, ma data la natura del gioco "arcade", abbiamo ritenuto accettabile il vincolo della risoluzione fissa.

Riconoscere i limiti del proprio progetto è una competenza professionale, non una debolezza.


### Domande-guida

1. Un lettore capisce **perché** le cose sono come sono, o solo **come** sono? 
2. Ogni scelta descritta ha almeno un'alternativa scartata? 
3. Avete evitato frasi tipo «abbiamo scelto così perché è il modo migliore»? (Non è una spiegazione.) 
4. Questa pagina è scritta da voi, con il vostro stile, o sembra l'output di un'IA?
