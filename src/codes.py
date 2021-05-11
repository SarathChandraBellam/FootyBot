LEAGUE_CODES = {
  "BL": 2002,     #Bundesliga
  "FL1": 2015,    #Ligue 1
  "PL": 2021,     #Premier League
  "SPA": 2014,    #La Liga
  "SA": 2019,     #Serie A
  "CL": 2001,     #Champions League
  "EC": 2018       # Euros
}

TOP_TEAM_CODES = ['LIV', 'MCI', 'FCB', 'RMA', 'JUV', 'PSG', 'BVB', 'INT', 'CHE']

NUM_MAP = {0: 'zero', 1: 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
           6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
           11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
           15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
           19 : 'nineteen', 20 : 'twenty'}

TEAM_CODES = {
  'Arsenal': 'ARS',
  'Aston Villa': 'AST',
  'Chelsea': 'CHE',
  'Everton': 'EVE',
  'Fulham': 'FUL',
  'Liverpool': 'LIV',
  'Man City': 'MCI',
  'Man United': 'MUN',
  'Newcastle': 'NEW',
  'Tottenham': 'TOT',
  'West Brom': 'WBA',
  'Wolverhampton': 'WOL',
  'Burnley': 'BUR',
  'Leicester City': 'LEI',
  'Southampton': 'SOU',
  'Leeds United': 'LEE',
  'Crystal Palace': 'CRY',
  'Sheffield Utd': 'SHE',
  'Brighton Hove': 'BHA',
  'West Ham': 'WHU',
  'Dortmund': 'BVB',
  'Bayern Munich': 'FCB',
  "M'gladbach": 'BMG',
  'Atleti': 'ATM',
  'Barça': 'FCB',
  'Real Madrid': 'RMA',
  'Atalanta': 'ATA',
  'Inter': 'INT',
  'Juventus': 'JUV',
  'Lazio': 'LAZ',
  'Porto': 'FCP',
  'Marseille': 'OM',
  'PSG': 'PSG',
  'Stade Rennais': 'REN',
  'Sevilla FC': 'SEV',
  'Beşiktaş': 'BES',
  'Qarabağ Ağdam': 'QAR',
  'Olympiakos': 'OLY',
  'Ajax': 'AJA',
  'AZ': 'AZ',
  'RB Leipzig': 'RBL',
  'Zenit': 'ZEN',
  'Celtic': 'CEL',
  'Dinamo Zagreb': 'DIN',
  'Dynamo Kyiv': 'DYN',
  'Club Brugge': 'CLU',
  'Slavia Praha': 'SLP',
  'KAA Gent': 'GEN',
  'Legia': 'LEG',
  'Young Boys': 'YOB',
  'Dundalk': 'DUN',
  'Europa': 'EUR',
  'RB Salzburg': 'RBS',
  'Sheriff': 'SHE',
  'Viktoria Plzeň': 'PLZ',
  'Astana FK': 'AST',
  'Budućnost': 'BUD',
  'Shaktar': 'SHD',
  'Linfield': 'LIN',
  'Başakşehir': 'BAS',
  'Ludogorets': 'LUD',
  'SL Benfica': 'BEN',
  'Rapid Wien': 'RAP',
  'Sarajevo': 'SAR',
  'Lok Zagreb': 'LOK',
  'Midtjylland': 'MID',
  'KuPS': None,
  'Flora': 'FLO',
  "Connah's Quay": 'COQ',
  'Djurgården': 'DIF',
  'Krasnodar': 'KRA',
  'Lok Moskva': 'LOK',
  'CFR Cluj': 'CLU',
  'Molde': 'MOL',
  'Floriana': 'FLO',
  'FK Sūduva': 'SUD',
  'Rīga FC': 'RFC',
  'Maccabi TA': 'MTA',
  'KR': 'KRR',
  'Ferencváros': 'FTC',
  'PAOK FC': 'PAO',
  'Drita Gjilan': 'DGJ',
  'Crvena Zvedza': 'CRV',
  'KÍ': 'KÍ',
  'SP Tre Fiori': 'TRF',
  'Fola Esch': 'FOL',
  'Dinamo Tbilisi': 'DIN',
  'Sl. Bratislava': 'SBA',
  'Dinamo Brest': 'BRE',
  'Ararat-Armenia': 'A-A',
  'Inter Club': 'INT',
  'Sileks': 'SIL',
  'Omonia': 'OMO',
  'Tirana': 'TIR',
  'Celje': 'CEL',
  'Germany': 'GER',
  'Spain': 'ESP',
  'Portugal': 'POR',
  'Slovakia': 'SVK',
  'England': 'ENG',
  'France': 'FRA',
  'Denmark': 'DEN',
  'Italy': 'ITA',
  'Switzerland': 'SUI',
  'Ukraine': 'UKR',
  'Sweden': 'SWE',
  'Poland': 'POL',
  'Czech Republic': 'CZE',
  'Croatia': 'CRO',
  'Turkey': 'TUR',
  'Belgium': 'BEL',
  'Russia': 'RUS',
  'Austria': 'AUT',
  'Hungary': 'HUN',
  'Wales': 'WAL',
  'Finland': 'FIN',
  'Macedonia': 'MKD',
  'Netherlands': 'NED',
  'Scotland': 'SCO',
  'Brest': 'SBR',
  'Montpellier': 'MON',
  'Lille': 'LIL',
  'Nice': 'NIC',
  'Olympique Lyon': 'LYO',
  'Lorient': 'FCL',
  'Bordeaux': 'BOR',
  'Saint-Étienne': 'STE',
  'Dijon FCO': 'DFC',
  'Angers SCO': 'ANG',
  'Nantes': 'NAN',
  'FC Metz': 'FCM',
  'RC Lens': 'RCL',
  'Stade de Reims': 'SDR',
  'Monaco': 'ASM',
  'Nîmes Ol.': 'NÎM',
  'Strasbourg': 'RCS',
  '1. FC Köln': None,
  'Hoffenheim': 'TSG',
  'Leverkusen': 'B04',
  'Schalke': 'S04',
  'Hertha BSC': 'BSC',
  'Stuttgart': 'VFB',
  'Wolfsburg': 'WOB',
  'Bremen': 'SVW',
  'Mainz': 'M05',
  'Augsburg': 'FCA',
  'Freiburg': 'SCF',
  'Frankfurt': 'SGE',
  'Union Berlin': 'UNB',
  'Bielefeld': 'BIE',
  'Milan': 'MIL',
  'Fiorentina': 'FIO',
  'Roma': 'ROM',
  'Bologna': 'BOL',
  'Cagliari': 'CAG',
  'Genoa': 'GEN',
  'Parma': 'PAR',
  'Napoli': 'NAP',
  'Udinese': 'UDI',
  'Verona': 'VER',
  'Sassuolo': 'SAS',
  'Crotone': 'CRO',
  'Spezia Calcio': 'SPE',
  'Sampdoria': 'SAM',
  'Torino': 'TOR',
  'Benevento': 'BEN',
  'Athletic': 'ATH',
  'Osasuna': 'OSA',
  'Getafe': 'GET',
  'Granada': 'GRA',
  'Levante': 'LEV',
  'Real Betis': 'BET',
  'Real Sociedad': 'RSO',
  'Villarreal': 'VIL',
  'Valencia': 'VAL',
  'Valladolid': 'VLD',
  'Alavés': 'ALA',
  'Cádiz CF': 'CAD',
  'Eibar': 'EIB',
  'Elche': 'ELC',
  'Huesca': 'HUE',
  'Celta': 'CEL'
}

COUNTRY_TEAM_CODES = {
  'England': {
    'Arsenal': 'ARS',
    'Aston Villa': 'AST',
    'Chelsea': 'CHE',
    'Everton': 'EVE',
    'Fulham': 'FUL',
    'Liverpool': 'LIV',
    'Man City': 'MCI',
    'Man United': 'MUN',
    'Newcastle': 'NEW',
    'Tottenham': 'TOT',
    'West Brom': 'WBA',
    'Wolverhampton': 'WOL',
    'Burnley': 'BUR',
    'Leicester City': 'LEI',
    'Southampton': 'SOU',
    'Leeds United': 'LEE',
    'Crystal Palace': 'CRY',
    'Sheffield Utd': 'SHE',
    'Brighton Hove': 'BHA',
    'West Ham': 'WHU'
  },
  'Spain': {
    'Athletic': 'ATH',
    'Atleti': 'ATM',
    'Osasuna': 'OSA',
    'Barça': 'FCB',
    'Getafe': 'GET',
    'Granada': 'GRA',
    'Real Madrid': 'RMA',
    'Levante': 'LEV',
    'Real Betis': 'BET',
    'Real Sociedad': 'RSO',
    'Villarreal': 'VIL',
    'Valencia': 'VAL',
    'Valladolid': 'VLD',
    'Alavés': 'ALA',
    'Cádiz CF': 'CAD',
    'Eibar': 'EIB',
    'Elche': 'ELC',
    'Huesca': 'HUE',
    'Celta': 'CEL',
    'Sevilla FC': 'SEV'
  },
  'Italy': {
    'Milan': 'MIL',
    'Fiorentina': 'FIO',
    'Roma': 'ROM',
    'Atalanta': 'ATA',
    'Bologna': 'BOL',
    'Cagliari': 'CAG',
    'Genoa': 'GEN',
    'Inter': 'INT',
    'Juventus': 'JUV',
    'Lazio': 'LAZ',
    'Parma': 'PAR',
    'Napoli': 'NAP',
    'Udinese': 'UDI',
    'Verona': 'VER',
    'Sassuolo': 'SAS',
    'Crotone': 'CRO',
    'Spezia Calcio': 'SPE',
    'Sampdoria': 'SAM',
    'Torino': 'TOR',
    'Benevento': 'BEN'
  },
  'Germany': {
    '1. FC Köln': None,
    'Hoffenheim': 'TSG',
    'Leverkusen': 'B04',
    'Dortmund': 'BVB',
    'Bayern Munich': 'FCB',
    'Schalke': 'S04',
    'Hertha BSC': 'BSC',
    'Stuttgart': 'VFB',
    'Wolfsburg': 'WOB',
    'Bremen': 'SVW',
    'Mainz': 'M05',
    'Augsburg': 'FCA',
    'Freiburg': 'SCF',
    "M'gladbach": 'BMG',
    'Frankfurt': 'SGE',
    'Union Berlin': 'UNB',
    'Bielefeld': 'BIE',
    'RB Leipzig': 'RBL'
  },
  'France': {
    'Brest': 'SBR',
    'Marseille': 'OM',
    'Montpellier': 'MON',
    'Lille': 'LIL',
    'Nice': 'NIC',
    'Olympique Lyon': 'LYO',
    'PSG': 'PSG',
    'Lorient': 'FCL',
    'Bordeaux': 'BOR',
    'Saint-Étienne': 'STE',
    'Dijon FCO': 'DFC',
    'Stade Rennais': 'REN',
    'Angers SCO': 'ANG',
    'Nantes': 'NAN',
    'FC Metz': 'FCM',
    'RC Lens': 'RCL',
    'Stade de Reims': 'SDR',
    'Monaco': 'ASM',
    'Nîmes Ol.': 'NÎM',
    'Strasbourg': 'RCS'
  },
  'Europe': {
    'Dortmund': 'BVB',
    'Bayern M': 'FCB',
    "M'gladbach": 'BMG',
    'Chelsea': 'CHE',
    'Liverpool': 'LIV',
    'Man City': 'MCI',
    'Man United': 'MUN',
    'Atleti': 'ATM',
    'Barça': 'FCB',
    'Real Madrid': 'RMA',
    'Atalanta': 'ATA',
    'Inter': 'INT',
    'Juventus': 'JUV',
    'Lazio': 'LAZ',
    'Porto': 'FCP',
    'Marseille': 'OM',
    'PSG': 'PSG',
    'Stade Rennais': 'REN',
    'Sevilla FC': 'SEV',
    'Beşiktaş': 'BES',
    'Qarabağ Ağdam': 'QAR',
    'Olympiakos': 'OLY',
    'Ajax': 'AJA',
    'AZ': 'AZ',
    'RB Leipzig': 'RBL',
    'Zenit': 'ZEN',
    'Celtic': 'CEL',
    'Dinamo Zagreb': 'DIN',
    'Dynamo Kyiv': 'DYN',
    'Club Brugge': 'CLU',
    'Slavia Praha': 'SLP',
    'KAA Gent': 'GEN',
    'Legia': 'LEG',
    'Young Boys': 'YOB',
    'Dundalk': 'DUN',
    'Europa': 'EUR',
    'RB Salzburg': 'RBS',
    'Sheriff': 'SHE',
    'Viktoria Plzeň': 'PLZ',
    'Astana FK': 'AST',
    'Budućnost': 'BUD',
    'Shaktar': 'SHD',
    'Linfield': 'LIN',
    'Başakşehir': 'BAS',
    'Ludogorets': 'LUD',
    'SL Benfica': 'BEN',
    'Rapid Wien': 'RAP',
    'Sarajevo': 'SAR',
    'Lok Zagreb': 'LOK',
    'Midtjylland': 'MID',
    'KuPS': None,
    'Flora': 'FLO',
    "Connah's Quay": 'COQ',
    'Djurgården': 'DIF',
    'Krasnodar': 'KRA',
    'Lok Moskva': 'LOK',
    'CFR Cluj': 'CLU',
    'Molde': 'MOL',
    'Floriana': 'FLO',
    'FK Sūduva': 'SUD',
    'Rīga FC': 'RFC',
    'Maccabi TA': 'MTA',
    'KR': 'KRR',
    'Ferencváros': 'FTC',
    'PAOK FC': 'PAO',
    'Drita Gjilan': 'DGJ',
    'Crvena Zvedza': 'CRV',
    'KÍ': 'KÍ',
    'SP Tre Fiori': 'TRF',
    'Fola Esch': 'FOL',
    'Dinamo Tbilisi': 'DIN',
    'Sl. Bratislava': 'SBA',
    'Dinamo Brest': 'BRE',
    'Ararat-Armenia': 'A-A',
    'Inter Club': 'INT',
    'Sileks': 'SIL',
    'Omonia': 'OMO',
    'Tirana': 'TIR',
    'Celje': 'CEL',
    'Germany': 'GER',
    'Spain': 'ESP',
    'Portugal': 'POR',
    'Slovakia': 'SVK',
    'England': 'ENG',
    'France': 'FRA',
    'Denmark': 'DEN',
    'Italy': 'ITA',
    'Switzerland': 'SUI',
    'Ukraine': 'UKR',
    'Sweden': 'SWE',
    'Poland': 'POL',
    'Czech Republic': 'CZE',
    'Croatia': 'CRO',
    'Turkey': 'TUR',
    'Belgium': 'BEL',
    'Russia': 'RUS',
    'Austria': 'AUT',
    'Hungary': 'HUN',
    'Wales': 'WAL',
    'Finland': 'FIN',
    'Macedonia': 'MKD',
    'Netherlands': 'NED',
    'Scotland': 'SCO'
  }
}

LEAGUE_TEAM_CODES = {
  'PL': {
    'Arsenal': 'ARS',
    'Aston Villa': 'AST',
    'Chelsea': 'CHE',
    'Everton': 'EVE',
    'Fulham': 'FUL',
    'Liverpool': 'LIV',
    'Man City': 'MCI',
    'Man United': 'MUN',
    'Newcastle': 'NEW',
    'Tottenham': 'TOT',
    'West Brom': 'WBA',
    'Wolverhampton': 'WOL',
    'Burnley': 'BUR',
    'Leicester City': 'LEI',
    'Southampton': 'SOU',
    'Leeds United': 'LEE',
    'Crystal Palace': 'CRY',
    'Sheffield Utd': 'SHE',
    'Brighton Hove': 'BHA',
    'West Ham': 'WHU'
  },
  'CL': {
    'Dortmund': 'BVB',
    'Bayern M': 'FCB',
    "M'gladbach": 'BMG',
    'Chelsea': 'CHE',
    'Liverpool': 'LIV',
    'Man City': 'MCI',
    'Man United': 'MUN',
    'Atleti': 'ATM',
    'Barça': 'FCB',
    'Real Madrid': 'RMA',
    'Atalanta': 'ATA',
    'Inter': 'INT',
    'Juventus': 'JUV',
    'Lazio': 'LAZ',
    'Porto': 'FCP',
    'Marseille': 'OM',
    'PSG': 'PSG',
    'Stade Rennais': 'REN',
    'Sevilla FC': 'SEV',
    'Beşiktaş': 'BES',
    'Qarabağ Ağdam': 'QAR',
    'Olympiakos': 'OLY',
    'Ajax': 'AJA',
    'AZ': 'AZ',
    'RB Leipzig': 'RBL',
    'Zenit': 'ZEN',
    'Celtic': 'CEL',
    'Dinamo Zagreb': 'DIN',
    'Dynamo Kyiv': 'DYN',
    'Club Brugge': 'CLU',
    'Slavia Praha': 'SLP',
    'KAA Gent': 'GEN',
    'Legia': 'LEG',
    'Young Boys': 'YOB',
    'Dundalk': 'DUN',
    'Europa': 'EUR',
    'RB Salzburg': 'RBS',
    'Sheriff': 'SHE',
    'Viktoria Plzeň': 'PLZ',
    'Astana FK': 'AST',
    'Budućnost': 'BUD',
    'Shaktar': 'SHD',
    'Linfield': 'LIN',
    'Başakşehir': 'BAS',
    'Ludogorets': 'LUD',
    'SL Benfica': 'BEN',
    'Rapid Wien': 'RAP',
    'Sarajevo': 'SAR',
    'Lok Zagreb': 'LOK',
    'Midtjylland': 'MID',
    'KuPS': None,
    'Flora': 'FLO',
    "Connah's Quay": 'COQ',
    'Djurgården': 'DIF',
    'Krasnodar': 'KRA',
    'Lok Moskva': 'LOK',
    'CFR Cluj': 'CLU',
    'Molde': 'MOL',
    'Floriana': 'FLO',
    'FK Sūduva': 'SUD',
    'Rīga FC': 'RFC',
    'Maccabi TA': 'MTA',
    'KR': 'KRR',
    'Ferencváros': 'FTC',
    'PAOK FC': 'PAO',
    'Drita Gjilan': 'DGJ',
    'Crvena Zvedza': 'CRV',
    'KÍ': 'KÍ',
    'SP Tre Fiori': 'TRF',
    'Fola Esch': 'FOL',
    'Dinamo Tbilisi': 'DIN',
    'Sl. Bratislava': 'SBA',
    'Dinamo Brest': 'BRE',
    'Ararat-Armenia': 'A-A',
    'Inter Club': 'INT',
    'Sileks': 'SIL',
    'Omonia': 'OMO',
    'Tirana': 'TIR',
    'Celje': 'CEL'
  },
  'FL1': {
    'Brest': 'SBR',
    'Marseille': 'OM',
    'Montpellier': 'MON',
    'Lille': 'LIL',
    'Nice': 'NIC',
    'Olympique Lyon': 'LYO',
    'PSG': 'PSG',
    'Lorient': 'FCL',
    'Bordeaux': 'BOR',
    'Saint-Étienne': 'STE',
    'Dijon FCO': 'DFC',
    'Stade Rennais': 'REN',
    'Angers SCO': 'ANG',
    'Nantes': 'NAN',
    'FC Metz': 'FCM',
    'RC Lens': 'RCL',
    'Stade de Reims': 'SDR',
    'Monaco': 'ASM',
    'Nîmes Ol.': 'NÎM',
    'Strasbourg': 'RCS'
  },
  'BL': {
    '1. FC Köln': None,
    'Hoffenheim': 'TSG',
    'Leverkusen': 'B04',
    'Dortmund': 'BVB',
    'Bayern M': 'FCB',
    'Schalke': 'S04',
    'Hertha BSC': 'BSC',
    'Stuttgart': 'VFB',
    'Wolfsburg': 'WOB',
    'Bremen': 'SVW',
    'Mainz': 'M05',
    'Augsburg': 'FCA',
    'Freiburg': 'SCF',
    "M'gladbach": 'BMG',
    'Frankfurt': 'SGE',
    'Union Berlin': 'UNB',
    'Bielefeld': 'BIE',
    'RB Leipzig': 'RBL'
  },
  'SA': {
    'Milan': 'MIL',
    'Fiorentina': 'FIO',
    'Roma': 'ROM',
    'Atalanta': 'ATA',
    'Bologna': 'BOL',
    'Cagliari': 'CAG',
    'Genoa': 'GEN',
    'Inter': 'INT',
    'Juventus': 'JUV',
    'Lazio': 'LAZ',
    'Parma': 'PAR',
    'Napoli': 'NAP',
    'Udinese': 'UDI',
    'Verona': 'VER',
    'Sassuolo': 'SAS',
    'Crotone': 'CRO',
    'Spezia Calcio': 'SPE',
    'Sampdoria': 'SAM',
    'Torino': 'TOR',
    'Benevento': 'BEN'
  },
  'SPA': {
    'Athletic': 'ATH',
    'Atleti': 'ATM',
    'Osasuna': 'OSA',
    'Barça': 'FCB',
    'Getafe': 'GET',
    'Granada': 'GRA',
    'Real Madrid': 'RMA',
    'Levante': 'LEV',
    'Real Betis': 'BET',
    'Real Sociedad': 'RSO',
    'Villarreal': 'VIL',
    'Valencia': 'VAL',
    'Valladolid': 'VLD',
    'Alavés': 'ALA',
    'Cádiz CF': 'CAD',
    'Eibar': 'EIB',
    'Elche': 'ELC',
    'Huesca': 'HUE',
    'Celta': 'CEL',
    'Sevilla FC': 'SEV'
  }
}