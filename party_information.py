import json
CONSERVATIVE_COLOR = '#28B4FA'
MIDDLE_COLOR = '#FAF448'
LEFT_COLOR = '#FA253B'
CONSERVATIVE_SHADE = '#77D3F4'
MIDDLE_SHADE = '#F5E392'
LEFT_SHADE = '#F5777E'
COLOR_DICT = {'left': LEFT_COLOR,'middle': MIDDLE_COLOR,'conservative': CONSERVATIVE_COLOR, '': (1, 1, 1, 0)}
GREY_COLOR = '#D3D3D3'
METADATA_FILE = 'election_data/NRW2023-metadaten.json'
NATIONAL_COUNCIL_FILE = 'election_data/dataset_elections_bfs.json'
STATES_COUNCIL_FILE = 'election_data/states_council.json'
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

# Create a central source of truth of the party results on national level
with open(NATIONAL_COUNCIL_FILE) as f:
    election_results = json.load(f)

national_results = election_results['level_ch']
party_results_nc = {result['partei_id']: {
        'name': party_metadata[result['partei_id']]['name'],
        'vote_result': result['partei_staerke'],
        'vote_delta': result['differenz_partei_staerke'],
        'seats_result': result['anzahl_gewaehlte'],
        'seats_delta': result['differenz_anzahl_gewaehlte'],
        'seats_power': result['anzahl_gewaehlte']/200,
        'seats_power_delta': result['differenz_anzahl_gewaehlte']/200,
        'normalised_parliamentary_power_nc': result['anzahl_gewaehlte']/400,
        'group': party_metadata[result['partei_id']]['group']
    } for result in national_results
}
with open(STATES_COUNCIL_FILE) as f:
    states_concil_results = election_results = json.load(f)

party_results_sc = {next(key for key, value in party_metadata.items() if value['name'] == party): {
        'name': party,
        'seats_result': result,
        'seats_delta': states_concil_results['deltas'][party],
        'seats_power': result/46,
        'normalised_parliamentary_power_sc': result/92,
        'group': party_metadata[next(key for key, value in party_metadata.items() if value['name'] == party)]['group']
    } for party, result in states_concil_results['results'].items()
}
