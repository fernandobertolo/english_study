import random

verbs = [["arise","arose","arisen"],
['awake','awoke','awoke'],
['be','was/were','been'],
['bear','bore','born'],
['beat','beat','beaten'],
['become','became','become'],
['begin','began','begun'],
['bet','bet','bet'],
['bid','bade','bidden'],
['bite','bit','bitten'],
['bleed','bled','bled'],
['break','broke','broken'],
['bring','brought','brought'],
['build','built','built'],
['burn','burnt','','burnt'],
['buy','bought','bought'],
['can','could','could'],
['catch','caught','caught'],
['choose','chose','chosen'],
['come','came','come'],
['cost','cost','cost'],
['cut','cut','cut'],
['do','did','done'],
['draw','drew','drawn'],
['dream','dreamt','dreamt'],
['drink','drank','drunk'],
['drive','drove','driven'],
['eat','ate','eaten'],
['fall','fell','fallen'],
['feed','fed','fed'],
['feel','felt','felt'],
['fight','fought','fought'],
['find','found','found'],
['flee','fled','fled'],
['fly','flew','flown'],
['forbit','forbade','forbidden'],
['forget','forgot','forgotten'],
['forgive','forgave','forgiven'],
['freeze','froze','frozen'],
['get','got','got'],
['give','gave','given'],
['go','went','gone'],
['grow','grew','grown'],
['have','had','had'],
['hear','heard','heard'],
['hide','hid','hidden'],
['hurt','hurt','hurt'],
['keep','kept','kept'],
['know','knew','known'],
['lay','laid','laid'],
['lead','led','led'],
['learn','learnt','learnt'],
['leave','left','left'],
['lend','lent','lent'],
['let','let','let'],
['lose','lost','lost'],
['make','made','made'],
['mean','meant','meant'],
['meet','met','met'],
['pay','paid','paid'],
['read','read','read'],
['ride','rode','ridden'],
['ring','rang','rung'],
['rise','rose','risen'],
['run','ran','run'],
['say','said','said'],
['see','saw','seen'],
['seek','sought','sought'],
['sell','sold','sold'],
['send','sent','sent'],
['shake','shook','shaken'],
['shave','shaved','shaven'],
['shoot','shot','shot'],
['show','showed','shown'],
['shut','shut','shut'],
['sing','sang','sung'],
['sink','sank','sunk'],
['sit','sat','sat'],
['sleep','slept','slept'],
['smell','smelt','smelt'],
['speak','spoke','spoken'],
['spell','spelt','spelt'],
['spend','spent','spent'],
['spill','spilt','spilt'],
['stand','stood','stood'],
['steal','stole','stolen'],
['strike','stuck','struck'],
['swear','swore','sworn'],
['swim','swam','swum'],
['swing','swung','swung'],
['take','took','taken'],
['teach','taught','taught'],
['tear','tore','torn'],
['tell','told','told'],
['think','thought','thought'],
['throw','threw','thrown'],
['understand','understood','understood'],
['wear','wore','worn'],
['win','won','won'],
['write','wrote','written']]


quantidade = int(input("how many verbs?: "))
pontos = 0
erros = []
sorteados = []

for i in range(0,quantidade):
	while True:
		verb_number = random.randint(0,99)
		if verb_number not in sorteados:
			sorteados.append(verb_number)
			break
			
	decisao = random.randint(0,1)
	
	if decisao == 0:
		answer = input("\nPresente of: {}\n".format(verbs[verb_number][1]))
		if answer == verbs[verb_number][0]:
			pontos += 1
		else:
			print("You missed! The answer is: {}".format(verbs[verb_number][0]))
			erros.append(verbs[verb_number])	

	else:
		answer = input("\nPast tense of: {}\n".format(verbs[verb_number][0]))
		if answer == verbs[verb_number][1]:
			pontos += 1
		else:
			print("You missed! The answer is: {}".format(verbs[verb_number][1]))
			erros.append(verbs[verb_number])	
	
print("\n\nPontuação: {}".format(pontos))
print("N verbos: {}".format(quantidade))
print("wrong verbs: \n{}".format(erros))
