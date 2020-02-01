# Rhye's and Fall of Civilization - Constants


# globals

from CvPythonExtensions import *
gc = CyGlobalContext()


# initialise player variables to player IDs from WBs

iEgypt = 0
iSumeria = 1
iIndusValley = 2
iElam = 3
iMinoa = 4
iPhoenicia = 5
iBabylonia = 6
iHittites = 7
iMycenae = 8
iAssyria = 9
iIsrael = 10
iAthens = 11
iSparta = 12
iScythia = 13
iCarthage = 14
iCeltia = 15
iEtruria = 16
iNubia = 17
iPersia = 18
iRome = 19
iMacedonia = 20
iIndia = 21
iBactria = 22
iNumidia = 23
iGermania = 24
iSassanid = 25
iByzantium = 26
iHuns = 27
iNumPlayers = 28
iNumMajorPlayers = 28
iNumActivePlayers = 28
iIndependent = 28
iIndependent2 = 29
iNumTotalPlayers = 30
iBarbarian = 30
iNumTotalPlayersB = 31


l0Array = [0] * iNumPlayers
l0ArrayActive = [0] * iNumActivePlayers
l0ArrayTotal =  [0] * iNumTotalPlayersB

lm1Array = [-1] * iNumPlayers


# date waypoints

i4400BC = 0
i4100BC = 10
i4000BC = 13
i3900BC = 17
i3500BC = 30
i3400BC = 33
i3000BC = 47
i2800BC = 53
i2720BC = 56
i2686BC = 57
i2600BC = 60
i2540BC = 62
i2500BC = 64
i2400BC = 70
i2300BC = 77
i2200BC = 84
i2180BC = 85
i2055BC = 93
i2000BC = 97
i1990BC = 98
i1900BC = 107
i1800BC = 117
i1690BC = 128
i1680BC = 129
i1600BC = 137
i1550BC = 142
i1500BC = 147
i1400BC = 159
i1350BC = 166
i1300BC = 171
i1250BC = 178
i1244BC = 179
i1200BC = 184
i1070BC = 201
i1000BC = 210
i920BC = 223
i900BC = 226
i896BC = 227
i850BC = 235
i800BC = 243
i782BC = 246
i750BC = 251
i734BC = 254
i700BC = 260
i678BC = 263
i650BC = 268
i631BC = 271
i626BC = 272
i620BC = 273
i600BC = 276
i590BC = 278
i560BC = 283
i550BC = 285
i542BC = 286
i512BC = 291
i500BC = 293
i482BC = 296
i450BC = 301
i434BC = 304
i400BC = 310
i380BC = 313
i350BC = 318
i314BC = 324
i300BC = 326
i284BC = 329
i270BC = 331
i264BC = 332
i250BC = 335
i236BC = 337
i218BC = 340
i210BC = 341
i200BC = 343
i190BC = 345
i150BC = 351
i146BC = 352
i116BC = 357
i109BC = 358
i100BC = 360
i82BC = 363
i58BC = 367
i50BC = 368
i39BC = 370
i20BC = 373
i10AD = 378
i70AD = 388
i82AD = 390
i100AD = 393
i150AD = 401
i162AD = 403
i166AD = 404
i170AD = 405
i200AD = 410
i250AD = 418
i280AD = 423
i292AD = 425
i300AD = 426
i400AD = 450
i450AD = 462
i475AD = 469
i500AD = 475
i550AD = 488
i600AD = 500


# starting locations coordinates
tCapitals = (
(30, 8), #tThebes
(46, 19), #tUr
(61, 28), #tIndus Valley
(50, 23), #tSusa
(33, 21), #tKnossos
(41, 22), #tByblos
(46, 22), #tBabylon
(41, 30), #tHattusas
(30, 26), #tMycenae
(46, 25), #tAshur
(41, 18), #tJerusalem
(33, 26), #tAthens
(29, 24), #tSparta
(52, 44), #tScythia
(15, 20), #tCarthage
(15, 43), #tLutetia
(18, 33), #tVolterra
(32, 4), #tNubia
(53, 21), #tPersepolis
(19, 30), #tRome
(27, 33), #tArgos Orestikon
(61, 23), #tIndia
(60, 34), #tBactria
(8, 21), #tLol
(25, 47), #Germania
(52, 19), #tCtesiphon
(35, 34), #tByzantium
(31, 43) # Huns
)

(i4400BCScenario, i896BCScenario) = range(2)

tYear = (
("4400 ", "TXT_KEY_BC"),
("4400 ", "TXT_KEY_BC"),
("3300 ", "TXT_KEY_BC"),
("3000 ", "TXT_KEY_BC"),
("2500 ", "TXT_KEY_BC"),
("1895 ", "TXT_KEY_BC"),
("1800 ", "TXT_KEY_BC"),
("1600 ", "TXT_KEY_BC"),
("1100 ", "TXT_KEY_BC"),
("950 ", "TXT_KEY_BC"),
("900 ", "TXT_KEY_BC"),
("844 ", "TXT_KEY_BC"),
("814 ", "TXT_KEY_BC"),
("808 ", "TXT_KEY_BC"),
("753 ", "TXT_KEY_BC"),
("750 ", "TXT_KEY_BC"),
("500 ", "TXT_KEY_BC"),
("250 ", "TXT_KEY_BC"),
("285 ", "TXT_KEY_AD"),
("300 ", "TXT_KEY_AD"),
("980 ", "TXT_KEY_AD"),
("1130 ", "TXT_KEY_AD"),
("1150 ", "TXT_KEY_AD"),
("1190 ", "TXT_KEY_AD"),
("1200 ", "TXT_KEY_AD"),
("1280 ", "TXT_KEY_AD"),
("1775 ", "TXT_KEY_AD"))

#core areas (for RiseAndFall and Victory)

tCoreAreasTL = (
(28, 8), #Egypt
(43, 19), #Sumer
(59, 25), #IndusValley
(49, 21), #Elam
(32, 21), #Minoa
(41, 21), #Phoenicia
(44, 21), #Babylonia
(38, 26), #Hittites
(27, 22), #Mycenae
(43, 23), #Assyria
(39, 17), #Israel
(31, 25), #Athens
(25, 21), #Sparta
(39, 38), #Scythia
(8, 18), #Carthage
(10, 39), #Celtia
(17, 31), #Etruria
(25, 0), #Nubia
(48, 19), #Persia
(18, 26), #Rome
(26, 31), #Macedonia
(59, 18), #India
(54, 28), #Bactria
(7, 19), #Numidia
(13, 39), #Germania
(49, 18), #Sassanids
(27, 16), #Byzantium
(23, 39) #Huns
)

tCoreAreasBR = (
(33, 16), #Egypt
(50, 27), #Sumer
(62, 34), #IndusValley
(53, 24), #Elam
(35, 30), #Minoa
(43, 24), #Phoenicia
(48, 25), #Babylonia
(41, 31), #Hittites
(33, 33), #Mycenae
(52, 31), #Assyria
(42, 20), #Israel
(35, 30), #Athens
(29, 31), #Sparta
(57, 49), #Scythia
(21, 22), #Carthage
(19, 46), #Celtia
(20, 34), #Etruria
(34, 6), #Nubia
(54, 28), #Persia
(24, 34), #Rome
(31, 34), #Macedonia
(62, 26), #India
(62, 40), #Bactria
(14, 21), #Carthage
(28, 45), #Germania
(58, 29), #Sassanids
(42, 36), #Byzantium
(32, 46) #Huns
)


tExceptions = (  #for RiseAndFall
(), #Egypt
(), #Sumer
(), #IndusValley
(), #Elam
(), #Minoa
(), #Phoenicia
(), #Babylonia
(), #Hittites
(), #Mycenae
(), #Assyria
(), #Israel
(), #Athens
(), #Sparta
(), #Scythia
(), #Carthage
(), #Celtia
(), #Etruria
(), #Nubia
(), #Persia
((24, 32),(24, 33),(24, 34),(23, 34),(17, 33),(17, 34),(18, 33),(18, 34)), #Rome
(), #Macedonia
(), #India
(), #Bactria
(), #Bactria
(), #Germania
(), #Sassanids
(), #Byzantium
(), #Huns
())



#normal areas (for Victory and resurrection)

tNormalAreasTL = (
(27, 6), #Egypt
(42, 18), #Sumer
(57, 23), #IndusValley
(49, 21), #Elam
(32, 25), #Minoa
(41, 21), #Phoenicia
(33, 17), #Babylonia
(39, 27), #Hittites
(25, 20), #Mycenae
(30, 14), #Assyria
(38, 15), #Israel
(17, 19), #Athens
(18, 20), #Sparta
(34, 37), #Scythia
(6, 18), #Carthage
(10, 39), #Celtia
(16, 31), #Etruria
(23, 0), #Nubia
(49, 19), #Persia
(15, 23), #Rome
(24, 29), #Macedonia
(54, 17), #India
(52, 26), #Bactria
(0, 18), #Numidia
(13, 39), #Germania
(40, 18), #Sassanids
(10, 15), #Byzantium
(23, 39) #Huns
)

tNormalAreasBR = (
(33, 17), #Egypt
(51, 28), #Sumer
(62, 36), #IndusValley
(53, 24), #Elam
(35, 30), #Minoa
(43, 24), #Phoenicia
(53, 31), #Babylonia
(47, 32), #Hittites
(36, 38), #Mycenae
(56, 33), #Assyria
(42, 20), #Israel
(41, 38), #Athens
(40, 39), #Sparta
(62, 50), #Scythia
(20, 25), #Carthage
(19, 46), #Celtia
(20, 35), #Etruria
(35, 15), #Nubia
(57, 30), #Persia
(24, 38), #Rome
(34, 35), #Macedonia
(62, 30), #India
(62, 48), #Bactria
(16, 24), #Numidia
(28, 45), #Germania
(60, 35), #Sassanids
(49, 44), #Byzantium
(32, 46) #Huns
)


tNormalAreasSubtract = (  #for resurrection and stability
(), #Egypt
(), #Sumer
(), #IndusValley
(), #Elam
(), #Minoa
(), #Phoenicia
(), #Babylonia
(), #Hittites
(), #Mycenae
(), #Assyria
(), #Israel
(), #Athens
(), #Sparta
(), #Scythia
(), #Carthage
(), #Celtia
(), #Etruria
(), #Nubia
(), #Persia
(), #Rome
(), #Macedonia
(), #India
(), #Bactria
(), #Numidia
(), #Germania
(), #Sassanids
(), #Byzantium
(), #Huns
()) #America


#for messages
iDuration = 14
iWhite = 0
iRed = 7
iGreen = 8
iBlue = 9
iLightBlue = 10
iYellow = 11
iDarkPink = 12
iLightRed = 20
iPurple = 25
iCyan = 44
iBrown = 55
iOrange = 88
iTan = 90
iLime = 100

#neighbours
lNeighbours = [
[iBabylonia, iPersia, iSumeria, iAssyria, iPhoenicia, iHittites, iIsrael], #Egypt
[iEgypt, iIndusValley, iBabylonia, iPhoenicia, iElam], #Sumeria
[iSumeria], #IndusValley
[iSumeria, iBabylonia, iAssyria, iPersia], #Elam
[iEgypt, iMycenae, iPhoenicia, iSumeria], #Minoa
[iCarthage, iIsrael, iEgypt, iHittites, iMycenae, iBabylonia, iMinoa, iAssyria], #Phoenecia
[iSumeria, iAssyria, iEgypt, iIsrael, iPhoenicia, iHittites, iPersia], #Babylonia
[iEgypt, iMycenae, iAssyria, iBabylonia, iIsrael, iPhoenicia], #Hitites
[iEgypt, iBabylonia, iHittites, iMinoa, iAssyria, iPhoenicia], #Mycenae
[iSumeria, iBabylonia, iEgypt, iIsrael, iPhoenicia, iHittites, iScythia, iPersia], #Assyria
[iEgypt, iPhoenicia, iHittites, iBabylonia, iAssyria, iMacedonia, iRome, iPersia], #Israel
[iSparta, iMacedonia, iRome, iMycenae], #Athens
[iAthens, iMacedonia, iRome, iMycenae], #Sparta
[iPersia, iAssyria, iBactria], #Scythia
[iRome, iCeltia], #Carthage
[iCarthage, iRome, iEtruria, iAthens, iSparta, iMacedonia], #Celtia
[iRome, iCeltia, iAthens], #Etruria
[iEgypt], #Nubia
[iBabylonia, iPhoenicia, iIsrael, iEgypt, iAthens, iSparta, iMacedonia, iAssyria, iElam], #Persia
[iPersia, iCarthage, iCeltia, iGermania, iHuns, iByzantium, iSassanid, iAthens, iSparta, iMacedonia, iEgypt, iIsrael], #Rome
[iAthens, iEgypt, iCeltia, iSparta, iPersia, iIndia], #Macedonia
[iBactria, iSassanid], #India
[iIndia, iScythia], #Bactria
[iCarthage], #Numidia
[iRome, iByzantium, iHuns], #Germania
[iRome, iIndia, iByzantium], #Sassanids
[iRome, iHuns, iGermania, iSassanid], #Byzantium
[iRome], #Huns
[],
[],
[]
]

#for stability hit on spawn
lOlderNeighbours = [
[], #Egypt
[], #Sumer
[], #IndusValley
[iSumeria], #Elam
[], #Minoa
[], #Phoenicia
[iSumeria], #Babylonia
[], #Hittites
[iMinoa], #Mycenae
[iBabylonia, iSumeria], #Assyria
[], #Israel
[iMycenae, iMinoa, iHittites], #Athens
[], #Sparta
[], #Scythia
[iPhoenicia], #Carthage
[], #Celtia
[], #Etruria
[iEgypt], #Nubia
[iHittites, iAssyria, iIsrael, iEgypt, iIndusValley, iPhoenicia, iBabylonia, iNubia], #Persia
[iEtruria, iAthens, iSparta, iCarthage, iNubia, iAssyria, iIsrael, iCeltia], #Rome
[iMycenae, iAthens, iSparta, iPersia], #Macedonia
[iIndusValley], #India
[iMacedonia], #Bactria
[iCarthage], #Numidia
[iCeltia, iEtruria], #Germania
[iPersia, iScythia, iMacedonia, iIndia, iBactria, iNumidia], #Sassanids
[iRome, iBactria, iNumidia], #Byzantium
[iScythia, iRome, iIndia], #Huns
[],
[],
[]

]

#for minor civs
tReserveCapitals = (
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(),
(), #((57, 52), (56, 52), (58, 53)), #tAmsterdam
(),
(), #((49, 42), (49, 44)) #tLisboa
(),
(),
(),
(),
(),
)



# broader areas coordinates (top left and bottom right) (for RiseAndFall)
#TODO: what dis
tBroaderAreasTL = (
(60, 26), #Egypt
(85, 28), #India
(95, 38), #China
(95, 38), #Elam
(72, 37), #Babylonia
(62, 39), #Greece
(70, 37), #Persia
(49, 35), #Carthage
(49, 35), #Rome
(110, 40), #Japan
(67, 21), #Ethiopia
(19, 30), #Maya
(57, 55), #Vikings
(64, 30), #Arabia
(97, 25), #Khmer
(49, 38), #Spain
(49, 44), #France
(48, 53), #England
(55, 46), #Germany
(65, 48), #Russia
(56, 51), #Holland
(48, 21), #Mali
(49, 40), #Portugal
(24, 14), #Inca
(82, 44), #Mongolia
(14, 32), #Aztecs
(68, 42), #Turkey
(10, 42) #America
)

#TODO: what dis
tBroaderAreasBR = (
(74, 38), #Egypt
(99, 43), #India
(107, 50), #China
(107, 50), #Elam
(78, 44), #Babylonia
(77, 47), #Greece
(87, 49), #Persia
(59, 41), #Carthage
(73, 50), #Rome
(116, 56), #Japan
(77, 30), #Ethiopia
(26, 37), #Maya
(71, 65), #Vikings
(85, 44), #Arabia
(105, 39), #Khmer
(55, 46), #Spain
(61, 52), #France
(54, 60), #England
(67, 56), #Germany
(92, 59), #Russia
(58, 53), #Holland
(67, 32), #Mali
(51, 45), #Portugal
(30, 27), #Inca
(110, 62), #Mongolia
(24, 43), #Aztecs
(86, 49), #Turkey
(37, 56)) #America



#Mercenaries. Higher number = less likely to hire TODO
tHire = (
10, #Egypt
30, #India
30, #China
30, #Elam
30, #Babylonia
50, #Greece
20, #Persia
10, #Carthage
30, #Rome
60, #Japan
30, #Ethiopia
30, #Maya
60, #Viking
50, #Arabia
30, #Ethiopia
50, #Spain
50, #France
50, #England
60, #Germany
60, #Russia
10, #Holland
30, #Mali
60, #Portugal
30, #Inca
70, #Mongolia
30, #Aztec
50, #Turkey
50, #America
100,
100,
100,
100,
100) #Barbs

lEnemyCivsOnSpawn = [
[], #Egypt
[], #Sumer
[], #IndusValley
[iSumeria,iBabylonia,iAssyria,iPersia,iSassanid], #Elam
[], #Minoa
[], #Phoenicia
[iIndependent,iIndependent2,iSumeria,iEgypt,iPhoenicia], #Babylonia
[iEgypt,iBabylonia,iPhoenicia,iIndependent,iIndependent2,iSumeria], #Hittites
[iMinoa,iIndependent,iIndependent2], #Mycenae
[iIndependent,iIndependent2,iSumeria,iEgypt,iPhoenicia,iBabylonia,iHittites], #Assyria
[iEgypt,iPhoenicia], #Israel
[iMycenae,iIndependent,iIndependent2], #Athens
[iMycenae,iIndependent,iIndependent2], #Sparta
[iAssyria], #Scythia
[], #Carthage
[iAthens,iSparta], #Celtia
[iCeltia], #Etruria
[iEgypt], #Nubia
[iEgypt,iBabylonia,iPhoenicia,iHittites,iSumeria,iIndusValley,iAthens,iSparta,iAssyria,iIndependent,iIndependent2], #Persia
[iEtruria,iCarthage,iCeltia,iIndependent,iIndependent2,iAthens,iSparta], #Rome
[iAthens,iSparta,iHittites,iPersia,iBabylonia,iIsrael,iAssyria,iPhoenicia,iIndependent,iIndependent2], #Macedonia
[iPersia,iIndusValley], #India
[iPersia,iIndusValley,iIndia], #Bactria
[iCarthage], #Numidia
[iRome,iCeltia,iEtruria,iAthens,iSparta,iMacedonia,iIndependent,iIndependent2], #Germania
[iBabylonia,iSumeria,iIndusValley,iAssyria,iRome,iPersia,iIndependent,iIndependent2], #Sassanids
[iGermania,iPersia,iAthens,iSparta,iMacedonia,iSassanid,iIndependent,iIndependent2], #Byzantium
[iEgypt,iBabylonia,iPhoenicia,iHittites,iSumeria,iIndusValley,iAthens,iSparta,iAssyria,iRome,iByzantium,iCeltia,iIndependent,iIndependent2], #Huns
]


#AIWars
tAggressionLevel = (
1, #Egypt
0, #Sumer
0, #IndusValley
0, #Elam
0, #Minoa
0, #Phoenicia
1, #Babylonia
1, #Hittites
1, #Mycenae
2, #Assyria
0, #Israel
1, #Athens
1, #Sparta
1, #Scythia
1, #Carthage
2, #Celtia
0, #Etruria
1, #Nubia
2, #Persia
2, #Rome
2, #Macedonia
1, #India
1, #Bactria
0, #Numidia
2, #Germania
2, #Sassanids
1, #Byzantium
2, #Huns
0,
0,
0
)


#war during rise of new civs TODO
tAIStopBirthThreshold = (
	80, #Egypt
	80, #India
	60, #China
	60, #Elam
	50, #Babylonia
	50, #Greece #would be 80 but with Turks must be lower
	70, #Persia
	80, #Carthage
	80, #Rome
	80, #Japan
	80, #Ethiopia
	80, #Maya
	80, #Viking
	80, #Arabia
	80, #Khmer
	80, #Spain  #60 in vanilla and Warlords
	80, #France #60 in vanilla and Warlords
	50, #England
	80, #Germany #70 in vanilla and Warlords
	50, #Russia
	80, #Holland
	70, #Mali
	60, #Portugal
	70, #Inca
	70, #Mongolia
	50, #Aztec
	70, #Turkey
	50, #America
	100,
	100,
	100,
	100,
	100)


#RiseAndFall
tResurrectionProb = ( #TODO
80, #Egypt
100, #India
100, #China
100, #Elam
30, #Babylonia
60, #Greece
60, #Persia
30, #Carthage
65, #Rome
100, #Japan
80, #Ethopia
30, #Maya
60, #Viking
100, #Arabia
60, #Khmer
100, #Spain
100, #France
100, #England
100, #Germany
100, #Russia
100, #Holland
30, #Mali
100, #Portugal
70, #Inca
80, #Mongolia
70, #Aztec
100, #Turkey
100, #America
#	100, #Holland
#	100, #Portugal
100) #Barbs

#RnF Colonists
tMaxColonists = (
0, #Egypt
0, #India
0, #China
0, #Elam
0, #Babylonia
0, #Greece
0, #Persia
0, #Carthage
0, #Rome
0, #Japan
0, #Ethopia
0, #Maya
1, #Viking
0, #Arabia
0, #Khmer
6, #Spain
6, #France
6, #England
1, #Germany
0, #Russia
6, #Holland
0, #Mali
6, #Portugal
0, #Inca
0, #Mongolia
0, #Aztec
0, #Turkey
0) #America


# initialise religion variables to religion indices from XML
iJudaism = 0
iChristianity = 1
iIslam = 2
iHinduism = 3
iBuddhism = 4
iConfucianism = 5
iTaoism = 6
iNumReligions = 7

#bluepotato: replaced hardcoded tech ids with a potentially slower but much more convenient function. TODO: speed it up

def getNumTechs():
	return gc.getNumTechInfos()

def tn(techName): #get tech number
	numTechs = getNumTechs()
	techName = "TECH_" + techName.upper()
	for i in range(numTechs):
		techType = gc.getTechInfo(i).getType()
		if techType == techName:
			return i
	raise Exception("Consts.tn(): no tech found with name " + techName + "!!!")
	return None

def getNumUnits():
	return gc.getNumUnitInfos()

def un(unitName): #get unit number
	numUnits = getNumUnits()
	unitName = "UNIT_" + unitName.upper()
	for i in range(numUnits):
		unitType = gc.getUnitInfo(i).getType()
		if unitType == unitName:
			return i
	raise Exception("Consts.un(): no unit found with name " + unitName + "!!!")
	return None

def getNumCivics():
	return gc.getNumCivicInfos()

def cn(civicName): #get civic number
	numCivics = getNumCivics()
	civicName = "CIVIC_" + civicName.upper()
	for i in range(numCivics):
		civicType = gc.getCivicInfo(i).getType()
		if civicType == civicName:
			return i
	raise Exception("Consts.cn(): no civic found with name " + civicName + "!!!")
	return None

def civicOptionForCivic(civicName): #get civic option number for civic
	numCivics = getNumCivics()
	civicName = "CIVIC_" + civicName.upper()
	for i in range(numCivics):
		civic = gc.getCivicInfo(i)
		civicType = civic.getType()
		if civicType == civicName:
			return civic.getCivicOptionType()
	raise Exception("Consts.civicOptionForCivic(): no civic found with name " + civicName + "!!!")
	return None

# initialise bonuses variables to bonuses IDs from WBS
iAluminium = 0
iCoal = 1
iCopper = 2
iHorse = 3
iIron = 4
iMarble = 5
iOil = 6
iStone = 7
iUranium = 8
iBanana = 9
iClam = 10
iCorn = 11
iCow = 12
iCrab = 13
iDeer = 14
iFish = 15
iPig = 16
iRice = 17
iSheep = 18
iWheat = 19
iDye = 20
iFur = 21
iGems = 22
iGold = 23
iIncense = 24
iIvory = 25
iSilk = 26
iSilver = 27
iSpices = 28
iSugar = 29
iWine = 30
iWhales = 31
iDrama = 32
iMusic = 33
iMovies = 34
iCotton = 35
iSwamp = 36
iCamel = 37
iOlives = 38
iSalt = 39
iPearls = 40
iNumResources = 41

iluxuryresources = [iSalt, iPearls, iDye, iFur, iGems, iGold, iIncense, iIvory, iSilk, iCotton, iSilver, iSpices, iSugar, iOlives, iWhales]


#bluepotato: I removed these constants in favor of a function as well, see tn(szTechName) for further information

def bn(buildingName): #get building number
	numBuildings = gc.getNumBuildingInfos()
	buildingName = "BUILDING_" + buildingName.upper()
	for i in range(numBuildings):
		techType = gc.getBuildingInfo(i).getType()
		if techType == buildingName:
			return i
	raise Exception("Consts.bn(): no building found with name " + buildingName + "!!!")
	return None

def sbn(specialBuildingName): #get special building number
	numSpecialBuildings = gc.getNumSpecialBuildingInfos()
	specialBuildingName = "SPECIALBUILDING_" + specialBuildingName.upper()
	for i in range(numSpecialBuildings):
		techType = gc.getSpecialBuildingInfo(i).getType()
		if techType == specialBuildingName:
			return i
	raise Exception("Consts.sbn(): no special building found with name " + specialBuildingName + "!!!")
	return None

#Eras

iAncient = 0
iClassical = 1
iMedieval = 2

#Improvements

iHut = 3
iCottage = 19
iHamlet = 20
iVillage = 21
iTown = 22

#feature & terrain

iSeaIce = 0
iJungle = 1
iOasis = 2
iFloodPlains = 3
iForest = 4
iFallout = 5
iMud = 6

iGrass = 0
iPlains = 1
iDesert = 2
iTundra = 3
iSnow = 4
iCoast = 5
iOcean = 6
iTerrainPeak = 7
iTerrainHills = 8
iMarsh = 9

iSwamp = 36 #bonus


#Stability Parameters

iParCities3 = 0
iParCitiesE = 1
iParCivics3 = 2
iParCivics1 = 3
iParCivicsE = 4
iParDiplomacy3 = 5
iParDiplomacyE = 6
iParEconomy3 = 7
iParEconomy1 = 8
iParEconomyE = 9
iParExpansion3 = 10
iParExpansion1 = 11
iParExpansionE = 12
iNumStabilityParameters = 13

#Plague
iImmunity = 20

#RFGW - modifiers



tFeedUnits = [
[iGermania, 'germanic_swordsman'],
[iHuns, 'hun']
]

def getFeedUnits(civ):
	for i in range(len(tFeedUnits)):
		if tFeedUnits[i][0] == civ:
			return un(tFeedUnits[i][1])
	return 0

tRazeOnly = (
0, #Egypt
0, #Sumeria
0, #IndusValley
0, #Elam
0, #Minoa
0, #Phoenicia
0, #Babylonia
0, #Hittites
0, #Mycenae
0, #Assyria
0, #Israel
0, #Athens
0, #Sparta
1, #Scythia
0, #Carthage
0, #Celtia
0, #Etruria
0, #Nubia
0, #Persia
0, #Rome
0, #Macedonia
0, #India
0, #Bactria
0, #Bactria
0, #Germania
0, #Sassanids
0, #Byzantium
1, #Huns
0,
0,
0
)

tRefusePeaceAI = (
0, #Egypt
0, #Sumeria
0, #IndusValley
0, #Elam
0, #Minoa
0, #Phoenicia
0, #Babylonia
0, #Hittites
0, #Mycenae
0, #Assyria
0, #Israel
0, #Athens
0, #Sparta
0, #Scythia
0, #Carthage
0, #Celtia
0, #Etruria
0, #Nubia
0, #Persia
0, #Rome
0, #Macedonia
0, #India
0, #Bactria
0, #Bactria
1, #Germania
0, #Sassanids
0, #Byzantium
1, #Huns
0,
0,
0
)

#RFGW - modifiers for the SDK, in addition to gameturn rescaling

tUnitCostModifier = ( #lower the cheaper
110, #Egypt
110, #Sumeria
110, #IndusValley
150, #Elam
130, #Minoa
130, #Phoenicia
120, #Babylonia
100, #Hittites
100, #Mycenae
110, #Assyria
130, #Israel
100, #Athens
100, #Sparta
90, #Scythia
100, #Carthage
100, #Celtia
100, #Etruria
110, #Nubia
70, #Persia
70, #Rome
80, #Macedonia
100, #India
80, #Bactria
130, #Numidia
50, #Germania
100, #Sassanids
100, #Byzantium
50, #Huns
100,
100,
100
)



tResearchModifier = ( #lower the faster
100, #Egypt
100, #Sumer
100, #IndusValley
110, #Elam
85, #Minoa
90, #Phoenicia
110, #Babylonia
100, #Hittites
100, #Mycenae
100, #Assyria
100, #Israel
80, #Athens
100, #Sparta
130, #Scythia
100, #Carthage
120, #Celtia
100, #Etruria
100, #Nubia
100, #Persia
95, #Rome
100, #Macedonia
100, #India
100, #Bactria
130, #Numidia
130, #Germania
100, #Sassanids
100, #Byzantium
130, #Huns
100,
100,
100
)

tDistanceMaintenanceModifier = ( #lower the better
100, #Egypt
100, #Sumer
100, #IndusValley
100, #Elam
100, #Minoa
100, #Phoenicia
100, #Babylonia
100, #Hittites
100, #Mycenae
90, #Assyria
100, #Israel
100, #Athens
100, #Sparta
120, #Scythia
100, #Carthage
100, #Celtia
100, #Etruria
100, #Nubia
70, #Persia
80, #Rome
80, #Macedonia
100, #India
90, #Bactria
100, #Carthage
120, #Germania
100, #Sassanids
100, #Byzantium
120, #Huns
100,
100,
100
)

tNumCitiesMaintenanceModifier = ( #lower the better
100, #Egypt
100, #Sumer
100, #IndusValley
140, #Elam
110, #Minoa
100, #Phoenicia
100, #Babylonia
100, #Hittites
100, #Mycenae
90, #Assyria
130, #Israel
130, #Athens
130, #Sparta
120, #Scythia
100, #Carthage
100, #Celtia
100, #Etruria
100, #Nubia
80, #Persia
80, #Rome
100, #Macedonia
100, #India
100, #Bactria
100, #Carthage
120, #Germania
100, #Sassanids
100, #Byzantium
120, #Huns
100,
100,
100
)

tCivicUpkeepModifier = ( #lower the better
90, #Egypt
100, #Sumer
100, #IndusValley
100, #Elam
100, #Minoa
100, #Phoenicia
100, #Babylonia
100, #Hittites
100, #Mycenae
100, #Assyria
100, #Israel
100, #Athens
100, #Sparta
100, #Scythia
100, #Carthage
100, #Celtia
100, #Etruria
100, #Nubia
90, #Persia
90, #Rome
100, #Macedonia
100, #India
100, #Bactria
100, #Carthage
100, #Germania
90, #Sassanids
100, #Byzantium
100, #Huns
100,
100,
100
)

tHealthBonusModifier = (
0, #Egypt
0, #Sumer
2, #IndusValley
0, #Elam
0, #Minoa
0, #Phoenicia
1, #Babylonia
0, #Hittites
0, #Mycenae
1, #Assyria
0, #Israel
0, #Athens
0, #Sparta
0, #Scythia
0, #Carthage
0, #Celtia
0, #Etruria
0, #Nubia
1, #Persia
1, #Rome
0, #Macedonia
1, #India
0, #Bactria
0, #Carthage
0, #Germania
1, #Sassanids
0, #Byzantium
0, #Huns
0,
0,
0
)

tGrowthModifier = ( #lower the faster
100, #Egypt
100, #Sumer
100, #IndusValley
100, #Elam
100, #Minoa
100, #Phoenicia
100, #Babylonia
100, #Hittites
100, #Mycenae
100, #Assyria
100, #Israel
100, #Athens
100, #Sparta
100, #Scythia
100, #Carthage
100, #Celtia
100, #Etruria
100, #Nubia
80, #Persia
90, #Rome
70, #Macedonia
100, #India
100, #Bactria
100, #Bactria
100, #Germania
100, #Sassanids
100, #Byzantium
100, #Huns
100,
100,
100

)

tUnitProductionModifier = ( #lower the faster
100, #Egypt
100, #Sumer
100, #IndusValley
100, #Elam
100, #Minoa
100, #Phoenicia
100, #Babylonia
100, #Hittites
100, #Mycenae
100, #Assyria
120, #Israel
100, #Athens
100, #Sparta
100, #Scythia
100, #Carthage
100, #Celtia
100, #Etruria
100, #Nubia
80, #Persia
90, #Rome
100, #Macedonia
100, #India
90, #Bactria
120, #Numidia
80, #Germania
100, #Sassanids
100, #Byzantium
80, #Huns
100,
100,
100

)

tWonderProductionModifier = ( #lower the faster
90, #Egypt
90, #Sumer
100, #IndusValley
100, #Elam
100, #Minoa
120, #Phoenicia
90, #Babylonia
100, #Hittites
100, #Mycenae
100, #Assyria
120, #Israel
70, #Athens
90, #Sparta
120, #Scythia
100, #Carthage
100, #Celtia
100, #Etruria
100, #Nubia
100, #Persia
100, #Rome
100, #Macedonia
100, #India
100, #Bactria
120, #Numidia
120, #Germania
100, #Sassanids
100, #Byzantium
120, #Huns
100,
100,
100
)


tBuildingProductionModifier = ( #lower the faster
100, #Egypt
100, #Sumer
100, #IndusValley
100, #Elam
90, #Minoa
100, #Phoenicia
100, #Assyria
100, #Hittites
100, #Mycenae
100, #Assyria
100, #Israel
100, #Athens
100, #Sparta
120, #Scythia
100, #Carthage
120, #Celtia
100, #Etruria
100, #Nubia
100, #Persia
80, #Rome
100, #Macedonia
100, #India
100, #Bactria
100, #Bactria
120, #Germania
90, #Sassanids
90, #Byzantium
120, #Huns
100,
100,
100
)


tInflationModifier = ( #lower the better
100, #Egypt
110, #Sumer
100, #IndusValley
100, #Elam
90, #Minoa
80, #Phoenicia
110, #Babylonia
110, #Hittites
100, #Mycenae
110, #Assyria
80, #Israel
80, #Athens
100, #Sparta
100, #Scythia
70, #Carthage
110, #Celtia
90, #Etruria
100, #Nubia
100, #Persia
130, #Rome
100, #Macedonia
100, #India
100, #Bactria
90, #Numidia
120, #Germania
100, #Sassanids
100, #Byzantium
100, #Huns
100,
100,
100
)

tGreatPeopleModifier = ( #lower the faster
90, #Egypt
90, #Sumer
100, #IndusValley
120, #Elam
110, #Minoa
120, #Phoenicia
90, #Babylonia
100, #Hittites
90, #Mycenae
110, #Assyria
90, #Israel
70, #Athens
90, #Sparta
120, #Scythia
90, #Carthage
100, #Celtia
100, #Etruria
100, #Nubia
90, #Persia
90, #Rome
90, #Macedonia
100, #India
100, #Bactria
110, #Numidia
90, #Germania
100, #Sassanids
100, #Byzantium
90, #Huns
100,
100,
100
)

tCitiesStartEraModifier = ( #higher the better
0, #Egypt
0, #Sumer
0, #IndusValley
0, #Elam
0, #Minoa
0, #Phoenicia
0, #Babylonia
0, #Hittites
0, #Mycenae
0, #Assyria
0, #Israel
0, #Athens
0, #Sparta
0, #Scythia
1, #Carthage
1, #Celtia
0, #Etruria
0, #Nubia
1, #Persia
1, #Rome
1, #Macedonia
1, #India
1, #Bactria
1, #Carthage
0, #Germania
2, #Sassanids
2, #Byzantium
0, #Huns
0,
0,
0
)


tWarDistanceModifier = ( #higher the closer, lower the further
3, #Egypt
3, #Sumer
3, #IndusValley
3, #Elam
3, #Minoa
3, #Phoenicia
3, #Babylonia
3, #Mycenae
3, #Hittites
2, #Assyria
3, #Israel
2, #Athens
3, #Sparta
2, #Scythia
2, #Carthage
1, #Celtia
3, #Etruria
3, #Nubia
1, #Persia
1, #Rome
1, #Macedonia
3, #India
1, #Bactria
3, #Numidia
1, #Germania
2, #Sassanids
2, #Byzantium
2, #Huns
0,
0,
0
)


tCityClosenessModifier = ( #higher the closer 7-14
12, #Egypt
12, #Sumer
12, #IndusValley
14, #Elam
14, #Minoa
14, #Phoenicia
12, #Babylonia
10, #Hittites
14, #Mycenae
12, #Assyria
14, #Israel
14, #Athens
14, #Sparta
9, #Scythia
12, #Carthage
9, #Celtia
12, #Etruria
11, #Nubia
9, #Persia
12, #Rome
10, #Macedonia
12, #India
9, #Bactria
12, #Carthage
9, #Germania
11, #Sassanids
9, #Byzantium
9, #Huns
0,
0,
0
)


tCompactEmpireModifier = ( #higher the more compact
40, #Egypt
40, #Sumer
40, #IndusValley
40, #Elam
40, #Minoa
5, #Phoenicia
40, #Babylonia
40, #Hittites
40, #Mycenae
30, #Assyria
20, #Israel
5, #Athens
40, #Sparta
30, #Scythia
20, #Carthage
20, #Celtia
40, #Etruria
40, #Nubia
9, #Persia
10, #Rome
30, #Macedonia
40, #India
10, #Bactria
30, #Scythia
10, #Germania
20, #Sassanids
30, #Byzantium
10, #Huns
0,
0,
0
)


tStabilityFoundModifier = ( #higher the more likely to use civic
0, #Egypt
0, #Sumer
0, #IndusValley
100, #Elam
180, #Minoa
180, #Phoenicia
0, #Babylonia
0, #Mycenae
0, #Hittites
0, #Assyria
0, #Israel
180, #Athens
60, #Sparta
0, #Scythia
60, #Carthage
0, #Celtia
60, #Etruria
0, #Nubia
0, #Persia
60, #Rome
60, #Macedonia
0, #India
0, #Bactria
0, #Bactria
0, #Germania
0, #Sassanids
0, #Byzantium
0, #Huns
0,
0,
0
)

tStabilityConquestModifier = ( #higher the more likely to use civic
0, #Egypt
0, #Sumer
0, #IndusValley
0, #Elam
0, #Minoa
0, #Phoenicia
0, #Babylonia
20, #Hittites
20, #Mycenae
20, #Assyria
0, #Israel
0, #Athens
0, #Sparta
0, #Scythia
0, #Carthage
0, #Celtia
0, #Etruria
0, #Nubia
0, #Persia
20, #Rome
30, #Macedonia
0, #India
0, #Bactria
0, #Bactria
0, #Germania
0, #Sassanids
0, #Byzantium
0, #Huns
0,
0,
0
)

tStabilityCommerceModifier = ( #higher the more likely to use civic
0, #Egypt
0, #Sumer
0, #IndusValley
20, #Elam
20, #Minoa
20, #Phoenicia
0, #Babylonia
0, #Hittites
0, #Mycenae
0, #Assyria
0, #Israel
50, #Athens
0, #Sparta
0, #Scythia
40, #Carthage
0, #Celtia
0, #Etruria
0, #Nubia
0, #Persia
20, #Rome
0, #Macedonia
0, #India
0, #Bactria
0, #Bactria
0, #Germania
0, #Sassanids
0, #Byzantium
0, #Huns
0,
0,
0
)


tCommerceGrowthModifier = ( #higher the faster
130, #Egypt
120, #Sumer
100, #IndusValley
100, #Elam
70, #Minoa
70, #Phoenicia
120, #Babylonia
70, #Hittites
70, #Mycenae
110, #Assyria
80, #Israel
100, #Athens
90, #Sparta
60, #Scythia
70, #Carthage
110, #Celtia
90, #Etruria
100, #Nubia
100, #Persia
100, #Rome
70, #Macedonia
110, #India
100, #Bactria
100, #Bactria
60, #Germania
100, #Sassanids
110, #Byzantium
60, #Huns
70,
70,
70
)

tWorkRateModifier = ( #higher the faster
100, #Egypt
100, #Sumer
100, #IndusValley
100, #Elam
100, #Minoa
100, #Phoenicia
100, #Babylonia
100, #Hittites
100, #Mycenae
100, #Assyria
100, #Israel
100, #Athens
100, #Sparta
70, #Scythia
100, #Carthage
100, #Celtia
100, #Etruria
100, #Nubia
100, #Persia
120, #Rome
100, #Macedonia
110, #India
100, #Bactria
100, #Bactria
70, #Germania
100, #Sassanids
100, #Byzantium
70, #Huns
70,
70,
70
)


#bestunit, besttech, bestbuilding still in the DLL
