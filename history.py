def diagramma():
    tot = []
    slo_date = {}
    with open('kalkulator.txt', 'r') as f:
        all = f.read()
        sp_all = all.splitlines()
        for i in range(len(sp_all)):
            s = sp_all[i].split()
            date = s[0]
            if date in slo_date:
                slo_date[date].append(int(s[2]))
            else:
                slo_date[date] = []
                slo_date[date].append(int(s[2]))

            tot.append(int(s[2]))
    print(slo_date)
    for date in slo_date:
        slo_date[date] = math.fsum(slo_date[date])
    print(slo_date)
    print(tot)
    print('max=', max(tot))
    summer = math.fsum(tot)
    print('summer=', summer)