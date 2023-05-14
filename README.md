# PYr2z

L'ormai anziano e superato [**r2z**](https://mozillaitalia.github.io/r2z/) (oggi archiviato e lasciato disponibile in sola lettura), tradotto in Python e automatizzato con GitHub Actions, da qui il nome **PYr2z** (anche se in questo caso l'archivio è un .7z e non un .zip come valeva per r2z batch!) :)

# Mozilla Firefox (Windows)

## Versioni stabili

- Versione a 64 bit, portable (7z): https://github.com/mozillaitalia/pyr2z/releases/tag/fx-win64
- Versione a 32 bit, portable (7z): https://github.com/mozillaitalia/pyr2z/releases/tag/fx-win32

### Versioni business (ESR)

- Versione a 64 bit, portable (7z): https://github.com/mozillaitalia/pyr2z/releases/tag/fx-esr-win64
- Versione a 32 bit, portable (7z): https://github.com/mozillaitalia/pyr2z/releases/tag/fx-esr-win32

# Thunderbird (Windows)

## Versioni stabili

- Versione a 64 bit, portable (7z): https://github.com/mozillaitalia/pyr2z/releases/tag/tb-win64
  *All'interno delle release stabili di Thunderbird a 64 bit potrai trovare anche gli archivi 7z delle nuove Nightly principali che vengono rilasciate (non degli aggiornamenti quotidiani, solo il ramo Alpha principale). Puoi identificarli tramite nome dell'archivio 7z (conterrà `thunderbird-nightly`)*
- Versione a 32 bit, portable (7z): https://github.com/mozillaitalia/pyr2z/releases/tag/tb-win32

------

# FAQ

- **Dove sono finiti tutti i vecchi file 7z delle precedenti versioni?**
  Ho fatto pulizia e cambiato buona parte del codice (e azioni utilizzate via GitHub) per sfruttare le Release di GitHub ed evitare di conservare i file generati nella root del repository, questo permette di effettuare fork più agilmente e tenere più snella la cartella di sviluppo.
  Ho lanciato una pulizia completa del repository e di tutti i commit precedenti il 13/5/23, letteralmente creando un "*main*" nuovo e portando così i commit a 1.
  - **E il precedente codice?**
    Gli script precedenti sono disponibili nella cartella **[pyr2z-starter](https://github.com/mozillaitalia/pyr2z/pyr2z-starter)** di questo repository, buon divertimento :-)
- **Questa è la versione definitiva di PYr2z?**
  Niente affatto.
  È solo un passaggio intermedio. Modificherò ulteriormente questo repository e cercherò di migliorare ancora il codice e tenere sempre il più pulito e ordinato possibile.
  Se hai suggerimenti o vuoi mettere mano direttamente al codice fatti avanti, sarò ben felice di portarti a bordo con me! :-)
- **A cosa serve la cartella "local"?**
  Contiene (a oggi solo uno) gli script che ho scritto per simulare il medesimo comportamento di PYr2z nativo, ma scompattando il file eseguibile all'interno di una cartella che posso già utilizzare come "*Portable*" dell'applicazione interessata.
  Il primo script pubblicato è stato [r2ztb-nightly-win64.py](https://github.com/MozillaItalia/pyr2z/blob/main/local/r2ztb-nightly-win64.py) e mi permette - alla bisogna - di scaricare la versione più aggiornata di Thunderbird Daily e scompattarla in una mia cartella sul disco C:\ (di una macchina Windows, appunto) sovrascrivendo file già presenti, usando solo la cartella "*core*" originale del setup di Mozilla e cancellando la cartella "*Uninstall*" che ovviamente non ha alcun senso in una versione Portable di un programma.

------

Problemi con i pacchetti e le pagine di download? [Apri una segnalazione](https://github.com/MozillaItalia/pyr2z/issues/new/choose)!
