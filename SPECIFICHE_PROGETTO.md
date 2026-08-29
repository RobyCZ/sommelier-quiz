# Chi Vuol Essere Sommelier? — Game Design Document v1.0

> Documento di riferimento per lo sviluppo dell'app. Aggiornato: Maggio 2026

---

## 1. Concept & Vision

**Nome:** Chi Vuol Essere Sommelier?  
**Genere:** Quiz / Trivia educativo  
**Piattaforme:** Web App (fase 1) → iOS + Android (fase 2)  
**Ispirazione visiva:** Chi Vuol Essere Milionario (tensione, scala premi, aiuti) rielaborato in chiave enologica di lusso  
**Target:** Appassionati di vino, studenti di sommellerie, professionisti della ristorazione, curiosi

---

## 2. Struttura dei Livelli

| Livello | Nome | N° Domande | Tempo/risposta | Accesso | Scala premi |
|---------|------|-----------|---------------|---------|-------------|
| 1 | 🍇 Appassionato | 15 | 30 sec | **Gratis** | €100 → €100.000 (virtuale) |
| 2 | 🥂 Esperto | 20 | 25 sec | Premium | €500 → €500.000 |
| 3 | 🏅 Sommelier | 25 | 20 sec | Elite | €1.000 → €1.000.000 |

### Traguardi Sicuri (per livello)
- Domanda 2, 9, 14 (Appassionato)
- Domanda 3, 10, 17 (Esperto)
- Domanda 4, 12, 20 (Sommelier)

---

## 3. Fonti delle Domande

### Documenti caricati (Google Drive)
1. **558813661-Enografia-Italiana-1-2.pdf** — AIES, panoramica regioni italiane (Valle d'Aosta → Sardegna), DOC e DOCG
2. **272077148-Corso-I-Liv-Sommelier-Completo.pdf** — Viticoltura, Enologia, Tecniche di vinificazione, Servizio, Abbinamenti cibo-vino
3. **275058393-Appunti-Sommelier.pdf** — Appunti pratici, degustazione, vitigni
4. **87278295-Manuale-Del-Sommelier.pdf** — Manuale pratico completo

### Conoscenza AI + Internet
- Enografia mondiale (Francia, Spagna, Portogallo, Germania, USA, Argentina, Cile, Australia, Sud Africa)
- Aggiornamenti annate recenti
- News del settore (premi, concorsi)

---

## 4. Categorie Domande per Livello

### Livello 1 — Appassionato (Gratis)
- Regioni vinicole italiane principali
- Vitigni autoctoni famosi (Sangiovese, Nebbiolo, Glera, Primitivo…)
- Abbinamenti cibo-vino di base
- Denominazioni DOC/DOCG più note
- Temperatura di servizio
- Come si stappa una bottiglia

### Livello 2 — Esperto (Premium)
- Tecniche di vinificazione (rosso, bianco, rosato, spumante metodo classico/charmat)
- Disciplinari DOCG approfonditi
- Degustazione organolettica (colore, profumo, sapore)
- Enografia italiana completa (tutte le regioni)
- Principi base enografia europea
- Gestione cantina e carta dei vini

### Livello 3 — Sommelier (Elite)
- Enografia mondiale approfondita
- Annate storiche e verticali
- Denominazioni estere (AOC, AOP, AVA, DO…)
- Biodynamia e biodinamica
- Domande da Master Sommelier / WSET Level 4
- Curiosità storiche e produttori iconici

---

## 5. Esempi Domande per Livello

### Livello 1 — Appassionato

**D1:** In quale regione italiana si produce il Barolo?
- A: Toscana | B: **Piemonte** ✓ | C: Veneto | D: Sicilia

**D2:** Quale vitigno è alla base del Brunello di Montalcino?
- A: Nebbiolo | B: Glera | C: **Sangiovese Grosso** ✓ | D: Montepulciano

**D3:** A quale temperatura si serve generalmente un vino rosso strutturato?
- A: 6-8°C | B: 10-12°C | C: **16-18°C** ✓ | D: 22-24°C

**D4:** Quale regione produce il Prosecco DOC/DOCG?
- A: Friuli | B: Lombardia | C: Trentino | D: **Veneto** ✓

**D5:** Cosa significa la sigla DOCG?
- A: Denominazione di Origine Certificata e Garantita | B: **Denominazione di Origine Controllata e Garantita** ✓ | C: Distillato di Origine Controllato e Garantito | D: Denominazione di Qualità Certificata e Garantita

### Livello 2 — Esperto

**D1:** Quale metodo produttivo si usa per lo Champagne e il Franciacorta?
- A: Metodo Charmat | B: **Metodo Classico (rifermentazione in bottiglia)** ✓ | C: Metodo Ancestrale | D: Carbonatazione artificiale

**D2:** Il vitigno Corvina è il principale componente di quale vino?
- A: Soave | B: Lugana | C: **Amarone della Valpolicella** ✓ | D: Bardolino

**D3:** Cosa si intende per "macerazione carbonica"?
- A: Utilizzo di CO₂ per conservare il vino | B: Tecnica di chiarifica | C: **Fermentazione intera dell'acino in ambiente saturo di CO₂** ✓ | D: Aggiunta di anidride carbonica al termine della vinificazione

### Livello 3 — Sommelier

**D1:** In quale sotto-regione della Borgogna si trova il Clos de Vougeot?
- A: Côte de Beaune | B: Mâconnais | C: **Côte de Nuits** ✓ | D: Chablis

**D2:** Quale varietà costituisce la base del Tokaji Aszú ungherese?
- A: Welschriesling | B: **Furmint** ✓ | C: Hárslevelű | D: Zéta

**D3:** Quale disciplinare impone un invecchiamento minimo di 5 anni per il Barolo Riserva?
- A: 3 anni | B: 4 anni | C: **5 anni (di cui 18 mesi in botte)** ✓ | D: 7 anni

---

## 6. Aiuti di Gioco

| Aiuto | Icona | Funzione | Disponibili per partita |
|-------|-------|----------|------------------------|
| 50:50 | 50 | Elimina 2 risposte errate | 1 |
| Chiedi al Produttore | 📞 | Suggerimento testuale (AI hint) | 1 |
| Chiedi alla Cantina | 👥 | Sondaggio simulato del "pubblico" | 1 |
| Cambia Domanda | 🔄 | Sostituisce la domanda con una diversa dello stesso livello | 1 |

---

## 7. Modello di Monetizzazione

### Principio
**Nessun abbonamento.** Ogni acquisto è definitivo e permanente. L'utente paga una volta sola e non si trova mai sorprese in bolletta. I ricavi ricorrenti vengono generati dai pacchetti domande, non dai rinnovi automatici.

---

### Livello Base — Gratis
- Livello 1 (Appassionato) illimitato
- Classifiche locali
- 3 aiuti per partita
- Nessuna carta di credito richiesta

---

### Acquisti Livello (In-App Purchase permanente)

| Prodotto | Prezzo | Contenuto |
|---------|--------|-----------|
| Livello Esperto | **€4,99** una volta | 200+ domande, DOC/DOCG approfondite, classifiche globali |
| Livello Sommelier | **€7,99** una volta | 300+ domande, enografia mondiale, annate, Master Sommelier |
| Bundle Esperto + Sommelier | **€9,99** una volta | Entrambi i livelli (risparmio €2,99 vs singoli) |

---

### Pacchetti Aggiornamento Domande (IAP ricorrenti opzionali)

Ogni trimestre (circa) vengono rilasciati nuovi pack tematici acquistabili separatamente.

| Pack | Prezzo | Domande | Livelli compatibili |
|------|--------|---------|-------------------|
| Enografia Italiana (ed. 2026) | **€1,99** | 50 | Tutti |
| Enografia Francese | **€1,99** | 50 | Esperto + Sommelier |
| Spumanti & Bollicine | **€1,99** | 40 | Esperto + Sommelier |
| Nuovo Mondo del Vino | **€1,99** | 50 | Sommelier |
| *(pack futuri…)* | €1,99 | 40-60 | Da definire |

**Logica pack:** chi ha acquistato un livello vede i pack compatibili con quel livello. I pack sono cumulativi — si aggiungono al pool di domande esistente.

---

### Promozioni consigliate
- **Launch discount:** Bundle a €7,99 per i primi 30 giorni dal lancio
- **Notifiche push** all'uscita di ogni nuovo pack (opt-in)
- **Referral:** "Invita un amico e ottieni il prossimo pack gratis"

---

## 8. Architettura Tecnica

### Fase 1 — Web App
- **Frontend:** React.js + TypeScript
- **Styling:** Tailwind CSS + custom design tokens
- **State management:** Zustand
- **Animazioni:** Framer Motion
- **Backend:** Node.js + Express (o Next.js full-stack)
- **Database:** PostgreSQL (domande, utenti, punteggi, acquisti)
- **Auth:** Supabase Auth (email + Google + Apple)
- **Pagamenti:** Stripe (Checkout one-time payment, no subscription logic)

### Fase 2 — App Mobile
- **Framework:** React Native (Expo) o Flutter
- **Stesso backend della web app**
- **Pagamenti mobile:** RevenueCat (gestione IAP one-time purchase iOS/Android — senza subscription)

### Strategia di Autenticazione

**Auth opzionale — registrazione richiesta solo al momento dell'acquisto.**

Flusso utente:
1. L'utente apre l'app e gioca il Livello 1 (Appassionato) **senza account**
2. Al termine della prima partita compare il prompt: *"Crea account per salvare il punteggio in classifica"* (opzionale, può ignorare)
3. Appena tenta di acquistare un livello → **registrazione obbligatoria** (email o "Continua con Google" in un tap)
4. Da quel momento tutti gli acquisti sono legati all'account Supabase
5. L'utente ritrova i livelli sbloccati su qualsiasi dispositivo (web, iOS, Android)

**Canali di pagamento e sincronizzazione acquisti:**
```
Web App  →  Stripe Checkout  →  Stripe Webhook  →  Supabase purchases (legato a user_id)
iOS App  →  App Store IAP    →  RevenueCat       →  Supabase purchases (legato a user_id)
Android  →  Google Play IAP  →  RevenueCat       →  Supabase purchases (legato a user_id)
```

**Restore acquisti (mobile):** RevenueCat gestisce automaticamente il restore tramite Apple ID / Google Account. Se l'utente è loggato con lo stesso account Supabase, i livelli risultano sbloccati senza nessuna azione aggiuntiva.

**Infrastruttura:** Supabase Auth — gratis fino a 50.000 MAU, integrazione nativa con `@supabase/supabase-js` per web e React Native.

### Database Schema (semplificato)
```sql
-- Tabelle principali
users (id, email, name, created_at)
purchases (id, user_id, product_id, stripe_payment_id, purchased_at)
  -- product_id: 'level_esperto' | 'level_sommelier' | 'bundle_all' | 'pack_italia_2026' | …
user_unlocks (user_id, level, pack_id)  -- vista derivata da purchases
questions (id, text, options, correct_answer, level, category, pack_id, difficulty, source)
games (id, user_id, level, score, completed_at, answers_json)
leaderboard (id, user_id, level, score, week, month)
question_packs (id, name, price_eur, compatible_levels, release_date, question_count)
```

---

## 9. Roadmap

### Sprint 1 (2-3 settimane)
- [x] Design System & Mockup grafico
- [ ] Setup progetto React + backend
- [ ] Database domande (minimo 100 per livello)
- [ ] Schermata di gioco funzionale (livello 1)

### Sprint 2 (2-3 settimane)
- [ ] Sistema di autenticazione
- [ ] Tutti e 3 i livelli funzionanti
- [ ] Timer, aiuti, scala premi animata
- [ ] Leaderboard base

### Sprint 3 (2 settimane)
- [ ] Integrazione pagamenti (Stripe)
- [ ] Paywall e gestione subscription
- [ ] Ottimizzazione performance
- [ ] Testing e QA

### Sprint 4 — App Mobile (4-6 settimane)
- [ ] Porting React Native / Flutter
- [ ] RevenueCat per pagamenti
- [ ] Submit App Store + Google Play

---

## 10. KPI Principali

| Metrica | Target 3 mesi | Target 6 mesi |
|---------|--------------|--------------|
| Utenti registrati | 1.000 | 5.000 |
| Partite giocate/giorno | 200 | 1.000 |
| Conversione Free → acquisto livello | 5% | 8% |
| Acquisti pack domande (su utenti paganti) | 20% | 40% |
| Ricavi totali (one-shot + pack) | €500 | €3.000 |
| Domande nel database | 300 | 600+ |
| Pack domande rilasciati | 2 | 5 |

---

*Documento creato automaticamente sulla base dei materiali AIES/AIS presenti nella cartella Google Drive e delle best practice di game design per quiz app mobile.*
