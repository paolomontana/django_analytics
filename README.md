# django_analytics


Per avviare l’applicazione è consigliato utilizzare l’ambiente virtuale (https://docs.python.org/3/library/venv.html) evitando di installare i pacchetti direttamente a livello di sistema.

L’unico prerequisito richiesto è di aver installato una qualsiasi versione di Python 3 e il sistema di versionamento GIT per clonare la repository dell’applicazione.
I test di funzionamento sono stati effettuati utilizzando la versione di Python 3.11.3, installata su MacOS.
Un qualsiasi sistema UNIX dovrebbe essere compatibile con questa guida.

Creazione ambiente virtuale
Per creare un nuovo ambiente virtuale, aprire un terminale e creare una cartella di lavoro in una qualsiasi directory del proprio filesystem digitando il comando: 

mkdir workspace

quindi entrare dentro la directory creata 

cd workspace

creare un ulteriore cartella all’interno chiamata enviroment

mkdir enviroment

entrare dentro la cartella enviroment e digitare il comando 

python -m ven .

A questo punto l’ambiente è stato creato e successivamente verranno installati i pacchetti necessari al funzionamento dell’applicazione.



# Download dell’applicazione

Utilizzare il terminare per entrare della directory di lavoro “workspace”

Clonare la repository utilizzando il comando

git clone https://github.com/paolomontana/django_analytics.git

All’interno della directory di lavoro “workspace” saranno presenti due cartelle: 

1)	“enviroment” precedentemente creata per costruire l’ambiente virtuale
2)	“django_analytics” sorgente dell’applicazione


# Installazione pacchetti nell’ambiente virtuale

Entrare nella directory di lavoro “workspace” e attivare l’ambiente virtuale con il comando

source enviroment/bin/activate

Entrare nella cartella django_analytics e digitare il comando

pip install -r requirements.txt
il comando effettuerà il download dei pacchetti necessari per l’applicazione.


# Running dell’applicazione

Entrare nella directory di lavoro “workspace” e spostarsi all’interno della cartella django_analytics/webAnalytics

cd django_analytics/webAnalytics
Avviare l’applicazione digitando il comando

python manage.py runserver
L’applicazione aprirà la porta 8000 sul protocollo TCP/IP e a questo punto sarà sufficiente aprire il browser e digitare nella barra degli indirizzi: 

http://localhost:8000

