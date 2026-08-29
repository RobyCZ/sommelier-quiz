#!/usr/bin/env python3
"""
Chi Vuol Essere Sommelier? — Google Sheets → JSON Exporter
----------------------------------------------------------
Legge le domande dal Google Sheet e genera i file JSON in questions/

Struttura del Google Sheet (un foglio per livello: Level1, Level2, Level3):
Colonne: id | q | opt_a | opt_b | opt_c | opt_d | a | hint | cat | difficulty | active

Secrets GitHub Actions richiesti:
  - GOOGLE_SHEETS_CREDENTIALS : JSON della service account Google (base64 o inline)
  - SPREADSHEET_ID             : ID del Google Sheet (da URL)

Uso locale:
  export GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
  export SPREADSHEET_ID=1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
  python scripts/export_questions.py
"""

import os
import json
import base64
from pathlib import Path
from datetime import datetime

# ─── Google Sheets client ────────────────────────────────────────────────────
def get_sheets_service():
    """Inizializza il client Google Sheets con le credenziali."""
    import google.auth
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    credentials_json = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')

    if credentials_json:
        # In CI: credenziali come variabile d'ambiente (JSON stringa o base64)
        try:
            cred_data = json.loads(credentials_json)
        except json.JSONDecodeError:
            # Prova base64
            cred_data = json.loads(base64.b64decode(credentials_json).decode())
        credentials = service_account.Credentials.from_service_account_info(
            cred_data,
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )
    else:
        # Locale: usa Application Default Credentials
        credentials, _ = google.auth.default(
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )

    return build('sheets', 'v4', credentials=credentials)


# ─── Config livelli ──────────────────────────────────────────────────────────
LEVELS = {
    1: { 'sheet': 'Level1', 'label': '🍇 Appassionato', 'time': 30 },
    2: { 'sheet': 'Level2', 'label': '🥂 Esperto',       'time': 25 },
    3: { 'sheet': 'Level3', 'label': '🏅 Sommelier',     'time': 20 },
}

VERSION = datetime.now().strftime('%Y-Q') + str((datetime.now().month - 1) // 3 + 1)


def parse_sheet_rows(rows):
    """Converte le righe del foglio in lista di domande."""
    if not rows or len(rows) < 2:
        return []

    headers = [h.strip().lower() for h in rows[0]]
    questions = []

    for row in rows[1:]:
        if len(row) < len(headers):
            row += [''] * (len(headers) - len(row))

        r = dict(zip(headers, row))

        # Salta righe non attive o vuote
        if not r.get('id') or r.get('active', '1').strip() == '0':
            continue

        try:
            q = {
                'id':   int(r['id']),
                'q':    r['q'].strip(),
                'opts': [
                    r.get('opt_a', '').strip(),
                    r.get('opt_b', '').strip(),
                    r.get('opt_c', '').strip(),
                    r.get('opt_d', '').strip(),
                ],
                'a':    int(r.get('a', 0)),
                'hint': r.get('hint', '').strip(),
                'cat':  r.get('cat', '').strip(),
                'difficulty': int(r.get('difficulty', 1)),
            }
            # Filtra opzioni vuote
            q['opts'] = [o for o in q['opts'] if o]
            questions.append(q)
        except (ValueError, KeyError) as e:
            print(f"  ⚠️  Riga ignorata (errore: {e}): {r.get('id', '?')}")

    return questions


def export_level(service, spreadsheet_id, level_num, level_cfg):
    """Esporta un livello dal foglio e salva il JSON."""
    sheet_name = level_cfg['sheet']
    range_name = f"{sheet_name}!A:K"

    print(f"\n📊 Esportando Livello {level_num} ({sheet_name})...")

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()

    rows = result.get('values', [])
    print(f"   {len(rows) - 1} righe trovate nel foglio")

    questions = parse_sheet_rows(rows)
    print(f"   {len(questions)} domande valide ed attive")

    output = {
        'version': VERSION,
        'level': level_num,
        'label': level_cfg['label'],
        'time_per_question': level_cfg['time'],
        'questions_per_game': 15,
        'total_questions': len(questions),
        'questions': questions
    }

    out_path = Path('questions') / f'level{level_num}.json'
    out_path.parent.mkdir(exist_ok=True)

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"   ✅ Salvato: {out_path} ({len(questions)} domande, versione {VERSION})")
    return len(questions)


def main():
    spreadsheet_id = os.environ.get('SPREADSHEET_ID')
    if not spreadsheet_id:
        print("❌ SPREADSHEET_ID non impostato. Imposta la variabile d'ambiente.")
        exit(1)

    print("🍷 Chi Vuol Essere Sommelier? — Exporter")
    print(f"   Spreadsheet ID: {spreadsheet_id}")
    print(f"   Versione target: {VERSION}")

    service = get_sheets_service()
    total = 0

    for level_num, level_cfg in LEVELS.items():
        try:
            count = export_level(service, spreadsheet_id, level_num, level_cfg)
            total += count
        except Exception as e:
            print(f"\n❌ Errore esportando Livello {level_num}: {e}")
            raise

    print(f"\n🎉 Export completato! {total} domande totali su 3 livelli.")
    print(f"   File generati in: questions/level1.json, level2.json, level3.json")


if __name__ == '__main__':
    main()
