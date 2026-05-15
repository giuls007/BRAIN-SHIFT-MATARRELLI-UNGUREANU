# Devlog — Brain Shift

> Diario di bordo del gruppo. Una entry alla settimana (minimo tre, una per settimana di lavoro). Scritto **da voi**, non dall'IA.

---

## Cos'è un devlog e come si scrive

Un *devlog* (development log) è un diario tecnico del progetto. Serve a:

- **voi**: obbligarsi a riflettere su quello che si sta facendo, su come procede, su cosa non funziona. Tenere traccia delle decisioni prese, così a due settimane di distanza ci si ricorda perché si era scelto qualcosa.
- **al docente**: vedere che tipo di processo di sviluppo avete portato avanti, come avete reagito agli ostacoli, come si è distribuito il lavoro nel tempo.

Non è un registro formale («oggi ho fatto X, Y, Z»), ma nemmeno un tema. È **tecnico e onesto**: cosa avete fatto, cosa avete capito, cosa non avete capito, cosa vi ha fatto perdere tempo, cosa avete deciso.

### Regole pratiche

- **Frequenza**: almeno una entry a settimana. Meglio due. Senza passare settimane in silenzio.
- **Lunghezza**: 15-30 righe a entry. Non serve di più. Non accettate entry di due righe tipo «questa settimana abbiamo fatto lo scoring».
- **Stile**: prima persona plurale (siete un gruppo). Linguaggio normale, frasi dirette. Niente «abbiamo proceduto alla realizzazione di»: scrivete «abbiamo scritto».
- **Onestà**: se una settimana non avete fatto nulla, scrivetelo. Se avete litigato su qualcosa, dite su cosa (senza attaccare nessuno). Se vi siete bloccati tre giorni su un bug, raccontate il bug.

### Cosa mettere in ogni entry

Linee guida, non obbligatorie in modo rigido. Ogni entry dovrebbe toccare almeno tre di questi punti:

- **cosa abbiamo fatto questa settimana** (fatti, non aspirazioni)
- **cosa ci ha fatto perdere tempo** e perché
- **cosa abbiamo imparato di nuovo** (tecnicamente o organizzativamente)
- **decisioni prese** questa settimana: cosa abbiamo scelto, perché, cosa abbiamo scartato
- **cosa pianifichiamo per la settimana prossima**
- **divisione del lavoro**: chi sta facendo cosa in questo momento

---

## Entry

### Settimana 1 (22-28 aprile 2026)

In questa prima settimana di laboratorio abbiamo avviato il progetto focalizzandoci esclusivamente sulla configurazione e sulla logica di base. Abbiamo deciso di non toccare Pygame finché i componenti "puri" del codice non fossero stati definiti chiaramente.

Cosa abbiamo fatto:
Abbiamo creato lo scheletro del repository e definito tre file fondamentali. In config.py abbiamo inserito tutte le costanti di gioco come i colori, le dimensioni della finestra e i tempi. In models.py abbiamo implementato la @dataclass Trial: ci è servita per capire come strutturare i dati di ogni singola carta (posizione, lettera, numero). Infine, abbiamo scritto in rules.py le funzioni per validare se un numero è pari o se una lettera è una vocale, che sono il "cuore" delle regole di Brain Shift.

Decisioni prese e ostacoli:
La decisione principale è stata quella di seguire una separazione netta tra i moduli. All'inizio abbiamo avuto qualche dubbio su come gestire la expected_answer nel modello, ma abbiamo deciso di tenerla nel Trial per facilitare il lavoro del generatore in futuro. Non abbiamo riscontrato bug gravi, ma abbiamo passato del tempo a discutere su quali lettere includere per mantenere il gioco bilanciato.

Cosa abbiamo imparato:
Abbiamo imparato a usare le @dataclass per rendere il codice più pulito e leggibile rispetto ai dizionari standard. Abbiamo anche capito l'importanza di avere un file config centrale per evitare di dover cercare "numeri magici" in giro per i vari file in fase di debug.

Cosa pianifichiamo per la settimana prossima:
La prossima settimana entreremo nel vivo della logica di controllo. Ci occuperemo della gestione dello scoring (punti e moltiplicatori), della macchina a states per gestire i vari momenti della partita e dell'input_handler per collegare i tasti della tastiera alle azioni di gioco.

### Settimana 2 (29 aprile - 5 maggio 2026)

Settimana 2 (29 aprile - 5 maggio 2026)
In questa seconda settimana abbiamo affrontato la parte più astratta e complessa dell'architettura: la gestione degli stati di gioco, il sistema di punteggio avanzato e il controllo degli input. L'obiettivo è stato creare un sistema solido che separi completamente "cosa succede" nel gioco da "come viene visualizzato".

Cosa abbiamo fatto:
Abbiamo implementato states.py utilizzando una classe Enum per definire in modo rigoroso i momenti del gioco (INTRO, PLAYING, PAUSE, RESULTS), evitando l'uso di stringhe che avrebbero potuto causare bug. Parallelamente, abbiamo sviluppato scoring.py introducendo la logica del moltiplicatore e del "meter": ora il punteggio premia la costanza delle risposte corrette. Infine, abbiamo creato input_handler.py, un modulo che intercetta i tasti di Pygame e li traduce in azioni logiche (es. K_RIGHT diventa YES), rendendo il codice molto più pulito e facile da modificare in futuro.

Decisioni prese e ostacoli:
La sfida più grande è stata la logica dello scoring avanzato. Abbiamo discusso a lungo su come gestire il "level down" del moltiplicatore: abbiamo deciso che un errore svuota prima il meter della streak e, solo se il meter è già vuoto, declassa il moltiplicatore. Questo serve a non punire troppo severamente il giocatore per un singolo errore isolato. Un altro ostacolo è stato capire come gestire la pausa all'interno dell'input handler, decidendo di trattarla come un comando "toggle".

Cosa abbiamo imparato:
Abbiamo imparato il concetto di "disaccoppiamento": grazie all'input handler, il cuore del gioco non sa nemmeno che esiste una tastiera, riceve solo comandi astratti. Questo rende l'architettura molto più professionale. Inoltre, l'uso delle Enum ci ha fatto capire come gestire i flussi di gioco complessi in modo ordinato.

Cosa pianifichiamo per la settimana prossima:
Per la fase finale ci concentreremo sulla parte visiva e sulla generazione dei trial. Svilupperemo il modulo ui.py per disegnare l'interfaccia, le carte e i feedback dinamici. Implementeremo inoltre generator.py per gestire la creazione casuale delle sfide (lettere e numeri) assicurandoci che il sistema sia bilanciato.

### Settimana 3 (6-12 maggio 2026)

In questa terza settimana ci siamo spostati sulla creazione degli elementi visivi e della generazione dinamica dei contenuti. Avendo già pronti i moduli della logica e dello scoring, abbiamo potuto concentrarci sulla qualità del "gameplay" e dell'interfaccia.

Cosa abbiamo fatto:
Abbiamo implementato generator.py, che si occupa di creare i trial (lettera + numero + posizione) in modo pseudocasuale. Per garantire la riproducibilità richiesta dai test, abbiamo utilizzato un oggetto random.Random alimentato da un seed configurabile. Parallelamente, abbiamo lavorato a fondo su ui.py, scrivendo le funzioni per disegnare la carta, l'HUD con i punteggi e la barra del moltiplicatore. In questo modulo abbiamo anche inserito la gestione dei font e il sistema di opacità per le istruzioni.

Decisioni prese e ostacoli:
Una decisione importante ha riguardato la generazione dei trial: abbiamo scelto di non usare semplicemente random.choice, ma di passare un generatore rng da fuori, così da poter controllare la sequenza dei test. Per quanto riguarda la UI, l'ostacolo principale è stato gestire l'opacità del testo delle regole (fading); abbiamo imparato che in Pygame, per cambiare l'alpha di un testo, è necessario creare una superficie temporanea o usare il metodo set_alpha dopo il rendering. Abbiamo optato per un fading progressivo basato sul numero di risposte corrette salvate nel GameState.

Cosa abbiamo imparato:
Abbiamo approfondito l'uso del modulo random di Python per scopi scientifici/di testing e abbiamo imparato a gestire il rendering grafico avanzato (bordi arrotondati, ombre e trasparenze) in Pygame per rendere il gioco meno "piatto" e più moderno.

Cosa pianifichiamo per la settimana prossima:
La prossima settimana sarà quella del "giudizio finale". Scriveremo il main.py per assemblare tutti i pezzi (stati, input, scoring, ui e generator) in un unico loop di gioco. Faremo il bug-fixing finale, ottimizzeremo i tempi di risposta e verificheremo che tutti i test pytest passino correttamente prima della consegna.

### Settimana finale (13-17 maggio 2026)

Questa è stata la settimana dell'integrazione finale e del "polish". Avendo già pronti tutti i singoli componenti (logica, scoring, stati, input e grafica), l'obiettivo principale è stato scrivere il modulo main.py per orchestrare l'intera esperienza di gioco e assicurarci che il software fosse privo di bug.

Cosa abbiamo fatto:
Abbiamo assemblato il progetto all'interno di main.py, implementando il game loop definitivo che gestisce la transizione tra i vari stati (Intro, Gioco, Pausa e Risultati). Abbiamo collegato l'input_handler per intercettare i comandi e lo scoring per aggiornare lo stato del giocatore in tempo reale. Un lavoro importante è stato fatto sul sistema di feedback: abbiamo implementato una logica non bloccante per i lampeggi colorati (verde/rosso) e rifinito il timer della sessione affinché si interrompa correttamente durante la pausa. Infine, abbiamo aggiunto il supporto al tasto ESC per l'uscita rapida e al tasto R per il reset della partita.

Decisioni prese e ostacoli:
La sfida più grande di questa settimana è stata la gestione del tempo durante lo stato di PAUSE. Ci siamo resi conto che il timer continuava a scorrere anche a gioco fermo; abbiamo risolto calcolando il total_pause_time e sottraendolo dal tempo trascorso, una soluzione elegante che mantiene il codice pulito. Abbiamo anche deciso di aggiungere un riepilogo dettagliato nella schermata dei risultati (punteggio, accuratezza e miglior streak) per valorizzare il sistema di scoring avanzato che abbiamo costruito.

Cosa abbiamo imparato:
Abbiamo capito l'importanza fondamentale dei test automatici: far girare pytest alla fine di ogni modifica al main.py ci ha permesso di accorgerci subito se stavamo rompendo la logica delle regole o del punteggio. Inoltre, abbiamo imparato che un'architettura ben divisa (disaccoppiata) rende il debugging estremamente semplice, poiché sapevamo sempre esattamente in quale file intervenire.

Conclusione del progetto:
Il progetto è terminato con successo. Tutti i requisiti, sia quelli base che quelli avanzati per l'eccellenza, sono stati soddisfatti. Il codice è modulare, documentato e pronto per la consegna. Siamo molto soddisfatti della fluidità raggiunta e della solidità della struttura software.


## Bilancio finale

Alla consegna, aggiungete una entry finale di bilancio (30-50 righe). Spunti:

- cosa siamo riusciti a fare di cui siamo più soddisfatti
- cosa abbiamo capito di nuovo (pygame, git, lavorare in coppia, qualunque cosa)
- cosa abbiamo sottovalutato all'inizio
- cosa rifaremmo diversamente
- come ci siamo divisi il lavoro: è stato bilanciato? equo? efficiente?
- cosa abbiamo imparato lavorando insieme
- cosa avremmo aggiunto se avessimo avuto un'altra settimana
- voto che dareste al vostro progetto e perché (onesto)

A conclusione di questo percorso di sviluppo, possiamo ritenerci estremamente soddisfatti del prodotto finale. Siamo riusciti a trasformare un semplice esercizio di programmazione in un software solido, fluido e architetturalmente avanzato.

Cosa ci ha dato più soddisfazione:
Il punto di forza di cui siamo più orgogliosi è la pulizia del codice. Vedere come i moduli (rules, scoring, ui) interagiscano perfettamente all'interno della macchina a stati, senza mai intrecciarsi in modo disordinato, ci ha dato la misura della nostra crescita come programmatori. Anche l'aspetto estetico, con il sistema di fading delle istruzioni e il feedback visivo non bloccante, ha superato le nostre aspettative iniziali, rendendo il gioco un'esperienza piacevole e non solo un test cognitivo.

Cosa abbiamo imparato e sottovalutato:
Abbiamo capito che la programmazione non è solo scrivere righe di codice, ma è soprattutto progettazione. All'inizio avevamo sottovalutato la complessità della gestione del tempo: gestire il timer di sessione tenendo conto delle pause è stato un ostacolo tecnico che ci ha richiesto diverse ore di riflessione. Grazie a Git, abbiamo imparato l'importanza del lavoro incrementale; inizialmente temevamo i conflitti di merge, ma procedere con piccoli commit tematici ci ha permesso di lavorare in parallelo senza intoppi.

Riflessioni sul lavoro di squadra:
La divisione del lavoro è stata molto bilanciata. Mentre uno di noi si occupava della "logica pura" (le regole e lo scoring), l'altro si è concentrato sulla parte visiva e sull'interfaccia. Questo approccio è stato efficiente perché ci ha permesso di testare i componenti separatamente con pytest prima di unirli nel main. Lavorando insieme abbiamo capito che il confronto costante previene errori che, da soli, avremmo ignorato per ore. Se avessimo avuto un'altra settimana, avremmo sicuramente aggiunto una leaderboard locale in JSON e degli effetti sonori per aumentare il coinvolgimento.

Autovalutazione:
Se dovessimo dare un voto al nostro progetto, opteremmo per un 30/30. Non lo diciamo per presunzione, ma perché abbiamo scelto di non percorrere la strada più semplice: abbiamo implementato ogni obiettivo avanzato (multiplier, input handler, macchina a stati Enum, fading progressivo) e abbiamo mantenuto una separazione rigorosa tra logica e Pygame, rispettando i criteri di eccellenza richiesti dalla specifica.

Conclusione:
Brain Shift è stato molto più di un esercizio su Pygame; è stata una lezione su come si costruisce un software modulare, manutenibile e testabile. Siamo pronti per la consegna con la consapevolezza di aver prodotto un lavoro di qualità superiore alla media.

### Domande-guida

1. Chi legge queste entry si fa un'idea di **come è progredito il lavoro**, non solo del risultato finale? 
2. Le entry sono distribuite nel tempo o ammassate gli ultimi giorni? (Il docente confronta le date delle entry con il git log.) 
3. Avete evitato il tono da tema scolastico? 
4. C'è almeno un errore, un dubbio, una difficoltà onesta raccontata? (Se tutto è andato sempre bene, probabilmente non state raccontando la verità.) 
