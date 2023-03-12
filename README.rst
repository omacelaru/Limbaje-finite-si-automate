Limbaje-finite-si-automate
========

Fișierul de input
-----------------

Monospaced text is marked with two backquotes "``" instead of asterisks;
no bold or italic is possible within it (asterisks just represent
themselves), although in some contexts, code syntax highlighting may be
applied.  Note that in monospaced text, multiple spaces are *not*
collapsed, but are preserved; however, flow and wrapping *do* occur, and
any number of spaces may be replaced by a line break.  Markdown allows
monospaced text within bold or italic sections, but not vice versa -
reStructuredText allows neither.  In summary, the common inline markup
is the following::

  | q0       # stare initiala
  | q1 q3    # stari finale
  | q0 1 q0  # Tranziții
  | q0 0 q1  
  | q1 1 q0
  | q1 0 q2
  | q2 2 q3

