Limbaje-finite-si-automate
========

TEMA 1
======
Aplicatia determina dacă un cuvânt dat este acceptat sau nu de către un automat finit determinist (AFD), și în caz afirmativ, afișază drumului folosit pentru a ajunge la acceptare.

Un AFD este un model al unui sistem care procesează cuvinte. Acesta este definit de o mulțime finită de stări, o mulțime finită de simboluri (alfabetul de intrare), o funcție de tranziție care asociază fiecărei perechi (stare, simbol de intrare) o altă stare, o stare inițială și un set de stări finale.

Pentru a determina dacă un cuvânt este acceptat de către un AFD, vom începe prin a introduce cuvântul în AFD la starea inițială, și apoi urmăm funcția de tranziție pentru fiecare simbol din cuvânt, până când ajungem la sfârșitul cuvântului. Dacă am ajuns la sfârșit și starea curentă este o stare finală, atunci cuvântul este acceptat de AFD.

În caz contrar, cuvântul nu este acceptat, iar mesajul corespunzător va fi afișat.

Dacă cuvântul este acceptat, pentru a afișa drumul folosit pentru acceptare, vom înregistra stările prin care am trecut în timpul procesării cuvântului. Astfel, vom putea afișa secvența de stări care a fost urmată pentru a ajunge la o stare finală.

TEMA 2
======

Folosirea backtracking constă în explorarea recursivă a tuturor posibilităților de a construi cuvintele dorite. Algoritmul de backtracking începe cu un cuvânt vid și adaugă pe rând litere la acesta până când se ajunge la lungimea maximă dată. Algoritmul verifică dacă cuvântul construit se află într-o stare finală a automatului finit și, în caz afirmativ, adaugă cuvântul la lista de cuvinte acceptate.


Fișierul de input
-----------------

::

  q0       # stare initiala
  q1 q3    # stari finale
  q0 1 q0  # Tranziții
  q0 0 q1  
  q1 1 q0
  q1 0 q2
  q2 2 q3

