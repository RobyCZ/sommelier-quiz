# 🍷 Chi Vuol Essere Sommelier?

> Quiz interattivo sul mondo del vino ispirato a *Chi Vuol Essere Milionario?*

[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-gold)](https://tuonome.github.io/sommelier-quiz)
[![License](https://img.shields.io/badge/License-MIT-wine.svg)](LICENSE)

---

## 🎮 Struttura del gioco

| Livello | Nome | Domande/partita | Tempo | Accesso | Premio massimo |
|---------|------|----------------|-------|---------|----------------|
| 1 | 🍇 Appassionato | 15 | 30 sec | **Gratis** | € 100.000 |
| 2 | 🥂 Esperto | 15 | 25 sec | € 4,99 | € 500.000 |
| 3 | 🏅 Sommelier | 15 | 20 sec | € 7,99 | € 1.000.000 |

**Aiuti:** 50:50 · 📞 Chiedi al Produttore · 👥 Chiedi alla Cantina · 🔄 Cambia Domanda

---

## 📁 Struttura repository

```
sommelier-quiz/
│
├── index.html              # Web app (single-file, apri nel browser)
├── design_mockup.html      # Design system & schermate UI
│
├── questions/              # Database domande in JSON (per pack aggiornamenti)
│   ├── level1.json         # Appassionato — 40 domande
│   ├── level2.json         # Esperto — 40 domande
│   └── level3.json         # Sommelier — 40 domande
│
├── .github/
│   └── workflows/
│       └── export-questions.yml  # GitHub Actions: Sheets → JSON auto-export
│
├── SPECIFICHE_PROGETTO.md  # Game Design Document completo
└── README.md
```

---

## 🚀 Come eseguire localmente

```bash
# Clona il repo
git clone https://github.com/tuonome/sommelier-quiz.git
cd sommelier-quiz

# Apri nel browser (no build step necessario!)
open index.html
# oppure su Windows:
start index.html
```

---

## 🏗️ Architettura tecnica

### Fase 1 — Web App (attuale)
- **Stack:** HTML + CSS + JavaScript vanilla (single file, zero dipendenze)
- **Hosting:** GitHub Pages (gratis)
- **Domande:** JSON statici su GitHub Pages, caricati all'avvio

### Fase 2 — Backend & Auth (prossimo step)
- **Auth:** Supabase (email + Google login)
- **Pagamenti web:** Stripe Checkout (one-time payment)
- **Deploy:** Vercel / Netlify

### Fase 3 — App Mobile
- **Framework:** React Native (Expo)
- **Pagamenti mobile:** RevenueCat (App Store IAP + Google Play IAP)
- **CDN domande:** GitHub Pages (stesso JSON della web app)

---

## 💰 Modello di monetizzazione

**Nessun abbonamento.** Ogni acquisto è definitivo e permanente.

| Prodotto | Prezzo |
|---------|--------|
| Livello Esperto | **€ 4,99** una volta |
| Livello Sommelier | **€ 7,99** una volta |
| Bundle Esperto + Sommelier | **€ 9,99** una volta |
| Pack domande trimestrali | **€ 1,99** cad. |

---

## 📊 Database domande

Le domande sono gestite tramite **Google Sheets** e esportate automaticamente in JSON
tramite GitHub Actions ogni volta che viene fatto un commit sul branch `main`.

### Struttura JSON (`questions/level1.json`)
```json
{
  "version": "2026-Q2",
  "level": 1,
  "questions": [
    {
      "id": 101,
      "q": "In quale regione italiana si produce il Barolo?",
      "opts": ["Toscana", "Piemonte", "Veneto", "Sicilia"],
      "a": 1,
      "hint": "Il Barolo si produce nelle Langhe, nell'area di Alba (CN).",
      "cat": "Regioni",
      "difficulty": 1
    }
  ]
}
```

### Aggiunta di nuove domande
1. Apri il Google Sheet di riferimento
2. Aggiungi le domande nelle righe successive
3. Fai commit sul branch `main` — GitHub Actions esporta automaticamente i JSON
4. Gli utenti scaricano il nuovo pack dalla sezione Shop dell'app

---

## 🛣️ Roadmap

- [x] Design System & Mockup (7 schermate)
- [x] Web App prototipo funzionale
- [x] 120 domande (40 per livello)
- [ ] Supabase Auth + Stripe pagamenti
- [ ] Leaderboard e profili utente
- [ ] React Native / Expo app mobile
- [ ] App Store + Google Play submission

---

## 📄 Licenza

MIT © 2026 — Roberto Catanzariti
