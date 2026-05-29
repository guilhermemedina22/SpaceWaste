# ============================================================
# DETRITOS_POR_PAIS — 193 países membros da ONU
# Estimativas baseadas em dados ESA / Space-Track.org
# Países sem programa espacial têm estimativa 0
# ============================================================
 
DETRITOS_POR_PAIS = {
    # --- Grandes potências espaciais ---
    'russia':                    {'sigla': 'RU', 'estimativa': 6800, 'curiosidade': 'Maior gerador histórico; teste ASAT 2021 gerou ~1500 fragmentos rastreáveis'},
    'estados unidos':            {'sigla': 'US', 'estimativa': 5800, 'curiosidade': 'Segundo maior gerador; opera o maior sistema de rastreamento espacial do mundo (SSN)'},
    'china':                     {'sigla': 'CN', 'estimativa': 4200, 'curiosidade': 'Teste ASAT 2007 foi o maior evento isolado de geração de detritos da história'},
    'india':                     {'sigla': 'IN', 'estimativa': 420,  'curiosidade': 'Teste ASAT Mission Shakti em 2019 gerou detritos que ameaçaram a ISS'},
    'japão':                     {'sigla': 'JP', 'estimativa': 210,  'curiosidade': 'JAXA desenvolve tecnologia de captura de detritos com redes e anzóis magnéticos'},
    'frança':                    {'sigla': 'FR', 'estimativa': 580,  'curiosidade': 'Pioneira em legislação de mitigação de detritos espaciais na Europa'},
    'reino unido':               {'sigla': 'GB', 'estimativa': 90,   'curiosidade': 'Investe no projeto ClearSpace para remoção ativa de detritos'},
    'alemanha':                  {'sigla': 'DE', 'estimativa': 130,  'curiosidade': 'Centro ESOC em Darmstadt é o principal centro europeu de rastreamento de detritos'},
    'itália':                    {'sigla': 'IT', 'estimativa': 95,   'curiosidade': 'Participa ativamente dos programas ESA de mitigação de detritos'},
    'israel':                    {'sigla': 'IL', 'estimativa': 20,   'curiosidade': 'Possui satélites de observação militar em órbita polar'},
    'coreia do sul':             {'sigla': 'KR', 'estimativa': 35,   'curiosidade': 'Lançou seu primeiro foguete doméstico Nuri com sucesso em 2022'},
    'ira':                       {'sigla': 'IR', 'estimativa': 15,   'curiosidade': 'Possui programa espacial militar ativo desde 2009'},
    'coreia do norte':           {'sigla': 'KP', 'estimativa': 5,    'curiosidade': 'Lançou satélite espião Malligyong-1 em 2023'},
    'brasil':                    {'sigla': 'BR', 'estimativa': 30,   'curiosidade': 'Maioria dos fragmentos são do SGDC; base de Alcântara é estratégica por ser próxima ao equador'},
    'argentina':                 {'sigla': 'AR', 'estimativa': 12,   'curiosidade': 'CONAE opera satélites de observação da série SAC'},
    'canada':                    {'sigla': 'CA', 'estimativa': 75,   'curiosidade': 'Desenvolveu o Canadarm, usado na ISS para manobras orbitais'},
    'australia':                 {'sigla': 'AU', 'estimativa': 22,   'curiosidade': 'Abriga estações de rastreamento da Deep Space Network da NASA'},
    'espanha':                   {'sigla': 'ES', 'estimativa': 45,   'curiosidade': 'Participa de missões ESA e opera satélites de comunicação'},
    'holanda':                   {'sigla': 'NL', 'estimativa': 30,   'curiosidade': 'Sede da ESA ESTEC, principal centro técnico da agência europeia'},
    'belgica':                   {'sigla': 'BE', 'estimativa': 18,   'curiosidade': 'Abriga a sede administrativa da ESA e contribui com tecnologia de satélites'},
    'suecia':                    {'sigla': 'SE', 'estimativa': 25,   'curiosidade': 'Opera a base de lançamento Esrange, acima do círculo polar ártico'},
    'noruega':                   {'sigla': 'NO', 'estimativa': 14,   'curiosidade': 'Opera satélites meteorológicos e de comunicação ártica'},
    'suica':                     {'sigla': 'CH', 'estimativa': 10,   'curiosidade': 'EPFL desenvolveu o ClearSpace-1, missão de captura de detrito prevista para 2026'},
    'austria':                   {'sigla': 'AT', 'estimativa': 8,    'curiosidade': 'Participa de missões científicas da ESA'},
    'ucrania':                   {'sigla': 'UA', 'estimativa': 55,   'curiosidade': 'Herdou infraestrutura espacial soviética; produz foguetes Zenit'},
    'cazaquistao':               {'sigla': 'KZ', 'estimativa': 40,   'curiosidade': 'Abriga Baikonur, o cosmodromo mais famoso e mais antigo do mundo'},
    'turquia':                   {'sigla': 'TR', 'estimativa': 18,   'curiosidade': 'Lançou Turksat 5A e 5B; desenvolve foguete nacional'},
    'emirados arabes unidos':    {'sigla': 'AE', 'estimativa': 12,   'curiosidade': 'Enviou a sonda Hope a Marte em 2020; lançou satélite lunar'},
    'arabia saudita':            {'sigla': 'SA', 'estimativa': 8,    'curiosidade': 'Opera satélites de comunicação e observação'},
    'paquistao':                 {'sigla': 'PK', 'estimativa': 6,    'curiosidade': 'SUPARCO é uma das agências espaciais mais antigas da Ásia'},
    'bangladesh':                {'sigla': 'BD', 'estimativa': 2,    'curiosidade': 'Lançou seu primeiro satélite Bangabandhu-1 em 2018'},
    'tailandia':                 {'sigla': 'TH', 'estimativa': 4,    'curiosidade': 'Opera satélites de comunicação Thaicom'},
    'malasia':                   {'sigla': 'MY', 'estimativa': 3,    'curiosidade': 'Enviou o primeiro astronauta muculmano a ISS em 2007'},
    'indonesia':                 {'sigla': 'ID', 'estimativa': 5,    'curiosidade': 'Um dos primeiros países em desenvolvimento a operar satélite geoestacionário (1976)'},
    'filipinas':                 {'sigla': 'PH', 'estimativa': 2,    'curiosidade': 'Opera pequenos satélites de observação da Terra'},
    'vietna':                    {'sigla': 'VN', 'estimativa': 2,    'curiosidade': 'Lançou VNREDSat-1 para monitoramento ambiental'},
    'singapura':                 {'sigla': 'SG', 'estimativa': 3,    'curiosidade': 'Hub de startups espaciais no sudeste asiático'},
    'nova zelandia':             {'sigla': 'NZ', 'estimativa': 8,    'curiosidade': 'Base de lançamento da Rocket Lab fica em Mahia Peninsula'},
    'mexico':                    {'sigla': 'MX', 'estimativa': 10,   'curiosidade': 'Opera satélites Morelos e Mexsat de comunicação'},
    'colombia':                  {'sigla': 'CO', 'estimativa': 2,    'curiosidade': 'Possui agência espacial desde 2006; estuda lançamentos equatoriais'},
    'chile':                     {'sigla': 'CL', 'estimativa': 3,    'curiosidade': 'Abriga observatórios astronômicos de classe mundial (ALMA, VLT)'},
    'peru':                      {'sigla': 'PE', 'estimativa': 2,    'curiosidade': 'Opera o satélite PeruSAT-1 de observação'},
    'venezuela':                 {'sigla': 'VE', 'estimativa': 3,    'curiosidade': 'Opera satélites Venesat e Miranda com parceria chinesa'},
    'egito':                     {'sigla': 'EG', 'estimativa': 5,    'curiosidade': 'Opera EgyptSat e NileSat; agência NARSS ativa desde 1990'},
    'nigeria':                   {'sigla': 'NG', 'estimativa': 3,    'curiosidade': 'NigeriaSat-2 é um dos satélites de observação mais avançados da Africa'},
    'africa do sul':             {'sigla': 'ZA', 'estimativa': 4,    'curiosidade': 'Opera satélites de observação e abriga estações de rastreamento'},
    'etiopia':                   {'sigla': 'ET', 'estimativa': 1,    'curiosidade': 'Lançou seu primeiro satélite ETRSS-1 em 2019 com parceria chinesa'},
    'quenia':                    {'sigla': 'KE', 'estimativa': 1,    'curiosidade': 'Abriga base de Langata e estação de rastreamento da NASA'},
    'angola':                    {'sigla': 'AO', 'estimativa': 1,    'curiosidade': 'Opera o satélite AngoSat-2 de comunicações'},
    'marrocos':                  {'sigla': 'MA', 'estimativa': 2,    'curiosidade': 'Opera satélites Mohammed de observação da Terra'},
    'argelia':                   {'sigla': 'DZ', 'estimativa': 2,    'curiosidade': 'ASAL opera satélites Alsat de observação'},
    'tunisia':                   {'sigla': 'TN', 'estimativa': 1,    'curiosidade': 'Lançou CubeSats educacionais em parceria com universidades europeias'},
    'gana':                      {'sigla': 'GH', 'estimativa': 1,    'curiosidade': 'GhanaSat-1 foi o primeiro satélite ganense, lançado em 2017'},
    'ruanda':                    {'sigla': 'RW', 'estimativa': 1,    'curiosidade': 'Lançou RwaSat-1 como parte do programa africano de CubeSats'},
 
    # --- Países sem programa espacial próprio (estimativa 0) ---
    'afeganistao':               {'sigla': 'AF', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'albania':                   {'sigla': 'AL', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'andorra':                   {'sigla': 'AD', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'antigua e barbuda':         {'sigla': 'AG', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'armenia':                   {'sigla': 'AM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'azerbaijao':                {'sigla': 'AZ', 'estimativa': 1, 'curiosidade': 'Opera Azerspace-1 e 2 de comunicações'},
    'bahamas':                   {'sigla': 'BS', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'barein':                    {'sigla': 'BH', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'barbados':                  {'sigla': 'BB', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'belize':                    {'sigla': 'BZ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'benim':                     {'sigla': 'BJ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'bielorrussia':              {'sigla': 'BY', 'estimativa': 3, 'curiosidade': 'Opera satélites BKA de observação com parceria russa'},
    'bolivia':                   {'sigla': 'BO', 'estimativa': 1, 'curiosidade': 'Opera Tupac Katari, satélite de comunicações lançado em 2013'},
    'bosnia e herzegovina':      {'sigla': 'BA', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'botsuana':                  {'sigla': 'BW', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'brunei':                    {'sigla': 'BN', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'burkina fasso':             {'sigla': 'BF', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'burundi':                   {'sigla': 'BI', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'butao':                     {'sigla': 'BT', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'cabo verde':                {'sigla': 'CV', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'camaroes':                  {'sigla': 'CM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'cambodja':                  {'sigla': 'KH', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'catar':                     {'sigla': 'QA', 'estimativa': 1, 'curiosidade': 'Opera EsHail-2, satélite de comunicações e radioamador'},
    'chade':                     {'sigla': 'TD', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'comores':                   {'sigla': 'KM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'congo':                     {'sigla': 'CG', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'rep democratica do congo':  {'sigla': 'CD', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'costa do marfim':           {'sigla': 'CI', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'costa rica':                {'sigla': 'CR', 'estimativa': 0, 'curiosidade': 'Participa de projetos de CubeSats universitários'},
    'croacia':                   {'sigla': 'HR', 'estimativa': 0, 'curiosidade': 'Participa de missões ESA como estado membro associado'},
    'cuba':                      {'sigla': 'CU', 'estimativa': 1, 'curiosidade': 'Lançou CubeSats educacionais; herança do programa soviético Intercosmos'},
    'chipre':                    {'sigla': 'CY', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'dinamarca':                 {'sigla': 'DK', 'estimativa': 5, 'curiosidade': 'DTU Space é referência em instrumentação científica para satélites'},
    'djibuti':                   {'sigla': 'DJ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'dominica':                  {'sigla': 'DM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'rep dominicana':            {'sigla': 'DO', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'equador':                   {'sigla': 'EC', 'estimativa': 1, 'curiosidade': 'Lançou NEE-01 Pegasus, primeiro satélite equatoriano, em 2013'},
    'eritreia':                  {'sigla': 'ER', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'eslovaquia':                {'sigla': 'SK', 'estimativa': 1, 'curiosidade': 'Desenvolve CubeSats universitários'},
    'eslovenia':                 {'sigla': 'SI', 'estimativa': 1, 'curiosidade': 'Lançou TRISAT, primeiro satélite esloveno, em 2020'},
    'estonia':                   {'sigla': 'EE', 'estimativa': 1, 'curiosidade': 'ESTCube-1 foi o primeiro satélite estoniano (2013)'},
    'eswatini':                  {'sigla': 'SZ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'fiji':                      {'sigla': 'FJ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'finlandia':                 {'sigla': 'FI', 'estimativa': 4, 'curiosidade': 'Aalto-1 foi o primeiro satélite finlandês; setor espacial crescente'},
    'gabao':                     {'sigla': 'GA', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'gambia':                    {'sigla': 'GM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'georgia':                   {'sigla': 'GE', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'granada':                   {'sigla': 'GD', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'grecia':                    {'sigla': 'GR', 'estimativa': 2, 'curiosidade': 'Participa de missões ESA; desenvolve satélites acadêmicos'},
    'guatemala':                 {'sigla': 'GT', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'guine':                     {'sigla': 'GN', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'guine-bissau':              {'sigla': 'GW', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'guine equatorial':          {'sigla': 'GQ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'guiana':                    {'sigla': 'GY', 'estimativa': 0, 'curiosidade': 'Centro Espacial de Kourou (ESA/França) está em território da Guiana Francesa, vizinha'},
    'haiti':                     {'sigla': 'HT', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'honduras':                  {'sigla': 'HN', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'hungria':                   {'sigla': 'HU', 'estimativa': 2, 'curiosidade': 'Magyar Urkutatasi Iroda desenvolve pequenos satélites'},
    'iemen':                     {'sigla': 'YE', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'ilhas marshall':            {'sigla': 'MH', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'ilhas salomao':             {'sigla': 'SB', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'iraque':                    {'sigla': 'IQ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'irlanda':                   {'sigla': 'IE', 'estimativa': 2, 'curiosidade': 'Participa de missões ESA; empresa Realtra Space em crescimento'},
    'islandia':                  {'sigla': 'IS', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'jamaica':                   {'sigla': 'JM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'jordania':                  {'sigla': 'JO', 'estimativa': 1, 'curiosidade': 'Opera JY1-SAT e desenvolve capacidade espacial nacional'},
    'kiribati':                  {'sigla': 'KI', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'kuwait':                    {'sigla': 'KW', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'laos':                      {'sigla': 'LA', 'estimativa': 1, 'curiosidade': 'Opera Laosat-1, satélite de comunicações com parceria chinesa'},
    'lesoto':                    {'sigla': 'LS', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'letonia':                   {'sigla': 'LV', 'estimativa': 1, 'curiosidade': 'Venta-1 foi o primeiro satélite letão (2014)'},
    'libano':                    {'sigla': 'LB', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'liberia':                   {'sigla': 'LR', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'libia':                     {'sigla': 'LY', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'liechtenstein':             {'sigla': 'LI', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'lituania':                  {'sigla': 'LT', 'estimativa': 1, 'curiosidade': 'LituanicaSAT-1 foi o primeiro satélite lituano (2014)'},
    'luxemburgo':                {'sigla': 'LU', 'estimativa': 3, 'curiosidade': 'SES S.A. é um dos maiores operadores de satélites do mundo'},
    'madagascar':                {'sigla': 'MG', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'malaui':                    {'sigla': 'MW', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'maldivas':                  {'sigla': 'MV', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'mali':                      {'sigla': 'ML', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'malta':                     {'sigla': 'MT', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'mauritania':                {'sigla': 'MR', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'mauricio':                  {'sigla': 'MU', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'micronesia':                {'sigla': 'FM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'mocambique':                {'sigla': 'MZ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'moldavia':                  {'sigla': 'MD', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'monaco':                    {'sigla': 'MC', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'mongolia':                  {'sigla': 'MN', 'estimativa': 1, 'curiosidade': 'Lançou MongoliaSat-1 com parceria coreana'},
    'montenegro':                {'sigla': 'ME', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'mianmar':                   {'sigla': 'MM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'namibia':                   {'sigla': 'NA', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'nauru':                     {'sigla': 'NR', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'nepal':                     {'sigla': 'NP', 'estimativa': 1, 'curiosidade': 'NepaliSat-1 foi lançado da ISS em 2019'},
    'nicaragua':                 {'sigla': 'NI', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'niger':                     {'sigla': 'NE', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'oma':                       {'sigla': 'OM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'palau':                     {'sigla': 'PW', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'palestina':                 {'sigla': 'PS', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'panama':                    {'sigla': 'PA', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'papua nova guine':          {'sigla': 'PG', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'paraguai':                  {'sigla': 'PY', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'polonia':                   {'sigla': 'PL', 'estimativa': 3, 'curiosidade': 'PW-Sat2 testou vela de frenagem para deorbitação controlada'},
    'portugal':                  {'sigla': 'PT', 'estimativa': 2, 'curiosidade': 'Participa de missões ESA; desenvolve satélites universitários'},
    'quirguistao':               {'sigla': 'KG', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'rep centro-africana':       {'sigla': 'CF', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'republica checa':           {'sigla': 'CZ', 'estimativa': 2, 'curiosidade': 'Participa de missões ESA e desenvolve instrumentação espacial'},
    'romenia':                   {'sigla': 'RO', 'estimativa': 1, 'curiosidade': 'ROSA participa de programas ESA e desenvolve capacidade espacial'},
    'sao cristovao e nevis':     {'sigla': 'KN', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'sao marino':                {'sigla': 'SM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'sao tome e principe':       {'sigla': 'ST', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'sao vicente e granadinas':  {'sigla': 'VC', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'samoa':                     {'sigla': 'WS', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'senegal':                   {'sigla': 'SN', 'estimativa': 1, 'curiosidade': 'GaindeSat é o primeiro satélite senegalês, lançado em 2021'},
    'serra leoa':                {'sigla': 'SL', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'servia':                    {'sigla': 'RS', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'seychelles':                {'sigla': 'SC', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'siria':                     {'sigla': 'SY', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'somalia':                   {'sigla': 'SO', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'sri lanka':                 {'sigla': 'LK', 'estimativa': 1, 'curiosidade': 'SUSL-1 foi o primeiro satélite do Sri Lanka, lançado em 2019'},
    'sudao':                     {'sigla': 'SD', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'sudao do sul':              {'sigla': 'SS', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'suriname':                  {'sigla': 'SR', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'tajiquistao':               {'sigla': 'TJ', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'tanzania':                  {'sigla': 'TZ', 'estimativa': 1, 'curiosidade': 'Lançou TANSSAT em 2021 em parceria com a China'},
    'timor-leste':               {'sigla': 'TL', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'togo':                      {'sigla': 'TG', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'tonga':                     {'sigla': 'TO', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'trinidad e tobago':         {'sigla': 'TT', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'turcomenistao':             {'sigla': 'TM', 'estimativa': 1, 'curiosidade': 'Opera TurkmenAlem MonacoSAT de comunicações'},
    'tuvalu':                    {'sigla': 'TV', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'uganda':                    {'sigla': 'UG', 'estimativa': 1, 'curiosidade': 'PearlAfricaSat-1 foi lançado da ISS em 2022'},
    'uruguai':                   {'sigla': 'UY', 'estimativa': 1, 'curiosidade': 'AntelSat foi o primeiro satélite uruguaio (2014)'},
    'uzbequistao':               {'sigla': 'UZ', 'estimativa': 1, 'curiosidade': 'Opera UzbekSat com suporte da Russia'},
    'vanuatu':                   {'sigla': 'VU', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'vaticano':                  {'sigla': 'VA', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'zambia':                    {'sigla': 'ZM', 'estimativa': 0, 'curiosidade': 'Sem programa espacial ativo'},
    'zimbabue':                  {'sigla': 'ZW', 'estimativa': 1, 'curiosidade': 'ZimSat-1 foi lançado da ISS em 2022'},
}
 
 
# ============================================================
# FUNÇÃO lixo_pais — busca com normalização de entrada
# ============================================================
 
import unicodedata
 
def normalizar(texto):
    """Remove acentos e converte para minúsculas para comparação flexível."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto.lower())
        if unicodedata.category(c) != 'Mn'
    )
 
# Índice pré-computado sem acentos → chave original
_INDICE = {normalizar(k): k for k in DETRITOS_POR_PAIS}
 
def buscar_pais(entrada_usuario):
    """Retorna os dados do país ou None se não encontrado."""
    chave = normalizar(entrada_usuario)
    # Busca exata
    if chave in _INDICE:
        return DETRITOS_POR_PAIS[_INDICE[chave]]
    # Busca parcial (ex: "estados" encontra "estados unidos")
    resultados = [k for k in _INDICE if chave in k]
    if len(resultados) == 1:
        return DETRITOS_POR_PAIS[_INDICE[resultados[0]]]
    if len(resultados) > 1:
        return {'ambiguo': [_INDICE[r] for r in resultados]}
    return None
 
def lixo_pais():
    print('\nAqui você pode ver quantos detritos estão associados a cada país.')
    print('Digite o nome do país (com ou sem acentos).\n')
 
    pais_input = input('Lixo espacial em: ').strip()
    resultado = buscar_pais(pais_input)
 
    if resultado is None:
        print(f'⚠ País "{pais_input}" não encontrado. Verifique o nome e tente novamente.')
        return
 
    if 'ambiguo' in resultado:
        print(f'⚠ Encontrei mais de um resultado. Você quis dizer:')
        for nome in resultado['ambiguo']:
            print(f'   • {nome.title()}')
        return
 
    sigla   = resultado['sigla']
    estim   = resultado['estimativa']
    curiosi = resultado['curiosidade']
 
    print(f'\n--- Lixo espacial: {pais_input.title()} ({sigla}) ---')
    if estim == 0:
        print(f'  Detritos gerados: nenhum registrado')
    else:
        print(f'  Estimativa de objetos rastreáveis: ~{estim}')
    print(f'  Curiosidade: {curiosi}')
 