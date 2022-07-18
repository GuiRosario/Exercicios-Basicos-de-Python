PopulaçaoPaisA = 80000
PopulaçaoPaisB = 200000
TaxadeCrescimentoPaisA = 1.03
TaxadeCrescimentoPaisB = 1.015
cont = 0
while PopulaçaoPaisA < PopulaçaoPaisB:
    cont = cont+1
    PopulaçaoPaisA = PopulaçaoPaisA*TaxadeCrescimentoPaisA
    PopulaçaoPaisB = PopulaçaoPaisB*TaxadeCrescimentoPaisB
    
print('A população do país A demorou',cont,'anos para ultrapassar a população do país B')
