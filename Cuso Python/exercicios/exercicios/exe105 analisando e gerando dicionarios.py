def notas(*num, s=False ):
    tnotas = dict()
    tnotas['total'] = len(num)
    tnotas['maior'] = max(num)
    tnotas['menor'] = min(num)
    tnotas['media'] = sum(num) / len(num)

    if s :
        if tnotas['media'] <= 5:
            tnotas['sit'] = 'Ruim'
        elif tnotas['media'] <=6:
            tnotas['sit'] = 'Razoavel'
        if tnotas['media'] >7:
            tnotas['sit'] = 'Boa'


    return tnotas



resp = notas(8, 2, 6.5, 2, 7, 8, s=True)
print(resp)
