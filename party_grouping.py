import json
CONSERVATIVE_COLOR = '#28B4FA'
MIDDLE_COLOR = '#FAF448'
LEFT_COLOR = '#FA253B'
METADATA_FILE = 'election_data/NRW2023-metadaten.json'
with open(METADATA_FILE) as f:
    metadata = json.load(f)

party_metadata = {party['partei_id']: {'name': party['partei_bezeichnung'][0]['text']} for party in
                  metadata['parteien']}
conservative = ['FDP.Die Liberalen', 'Schweizerische Volkspartei', 'Liberale Partei der Schweiz',
                'Landesring der Unabhängigen', 'Schweizer Demokraten', 'Eidgenössisch-Demokratische Union',
                'Lega dei Ticinesi', 'Mouvement Citoyens Romands']
middle = ['Christlichdemokratische Volkspartei der Schweiz', 'Evangelische Volkspartei der Schweiz',
          'Christlichsoziale Partei', 'Die Mitte', 'Grünliberale Partei', 'Bürgerlich-Demokratische Partei']
left = ['Sozialdemokratische Partei der Schweiz', 'Partei der Arbeit / Solidarität', 'Grün-Alternative (inkl. POCH)',
        'GRÜNE Schweiz']

conservative_id = [1, 4, 5, 6, 14, 16, 18, 33]
middle_id = [2, 7, 8, 31, 32, 34]
left_id = [3, 9, 12, 13]

for value in party_metadata.values():
    if value['name'] in conservative:
        value['group'] = 'conservative'
    elif value['name'] in middle:
        value['group'] = 'middle'
    elif value['name'] in left:
        value['group'] = 'left'
    else:
        value['group'] = 'unrelevant'
