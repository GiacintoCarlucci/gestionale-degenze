:- dynamic(paziente/3).
:- dynamic(struttura/3).
:- dynamic(percorso/3).

%---REGOLE---

% paziente(id, idoneoTicket, percorso).
% struttura(reparto, piano, primario).
% percorso(codiceReparto, reparto, postiLetto).

%---DATI---

%---LISTA PAZIENTI---
paziente('dflcba77c05c670h', si, 'reu').
paziente('lmhvsx76m70a333z', si, 'car').
paziente('zplslv48p15b971s', no, null).
paziente('xqvhrn64t68i293k', si, 'psi').
paziente('rhbseu56e69e242f', no, null).
paziente('gvffmf56p25z352a', no, null).
paziente('rmbptp97b08d941j', si, 'onc').
paziente('lqvmbd63h26c541m', si, 'ema').
paziente('fqsfhp83b62l212d', no, null).
paziente('cmhrbn88m68f408l', si, 'gas').

%---LISTA STRUTTURE---
struttura('pediatria', '1', 'rossi').
struttura('ortopedia', 'plesso', 'ricci').
struttura('urologia', '3',  'gallo').
struttura('ginecologia', 'plesso', 'mancini').
struttura('cardiologia', '1', 'moretti').
struttura('psichiatria', '3', 'santoro').
struttura('pneumologia', '2', 'ferrara').
struttura('reumatologia', '1', 'martini').
struttura('oncologia', '2', 'gentile').
struttura('ematologia', '1', 'marchetti').
struttura('gastroenterologia', 'plesso', 'conte').
struttura('otorinolaringoiatria', '3', 'messina').
struttura('radiologia', '2', 'cattaneo').

%---LISTA PERCORSI---
percorso('gin', 'ginecologia', 2).
percorso('reu', 'reumatologia', 3).
percorso('oto', 'otorinolaringoiatria', 2).
percorso('car', 'cardiologia', 1).
percorso('rad', 'radiologia', 1).
percorso('ort', 'ortopedia', 4).

