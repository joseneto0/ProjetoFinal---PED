import csv

computador = []
switch = []
with open('ProjetoFinal-PED/computador.csv') as csv_file:
    csv_compu = csv.reader(csv_file, delimiter=';')
    
    next(csv_compu, None)  # pula os cabeçalhos
    for row in csv_compu:
        computadores = dict()
        computadores['ip'] = row[0]
        computadores['nome'] = row[1]
        computadores['mac'] = row[2]
        computadores['tabela_arp'] = row[3]
        computador.append(computadores)

    with open('ProjetoFinal-PED/switch.csv') as csv_files:
        csv_switch = csv.reader(csv_files, delimiter=';')
        next(csv_switch, None)
        for rows in csv_switch:
            switchs = dict()
            switchs['ip'] = rows[0]
            switchs['mac'] = rows[1]
            switchs['tabela_roteamento'] = rows[2]
            switch.append(switchs)
