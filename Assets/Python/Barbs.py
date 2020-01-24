# Rhye's and Fall of Civilization - Barbarian units and cities

from CvPythonExtensions import *
import CvUtil
import PyHelpers	# LOQ
import Popup
import cPickle as pickle
import RFCUtils
import Consts as con

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer	# LOQ
utils = RFCUtils.RFCUtils()


### Constants ###

iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
pIndependent = gc.getPlayer(iIndependent)
pIndependent2 = gc.getPlayer(iIndependent2)
teamIndependent = gc.getTeam(pIndependent.getTeam())
teamIndependent2 = gc.getTeam(pIndependent2.getTeam())

iBarbarian = con.iBarbarian
pBarbarian = gc.getPlayer(iBarbarian)
teamBarbarian = gc.getTeam(pBarbarian.getTeam())

iCarthage = con.iCarthage
pCarthage = gc.getPlayer(iCarthage)
teamCarthage = gc.getTeam(pCarthage.getTeam())

iCeltia = con.iCeltia
pCeltia = gc.getPlayer(iCeltia)
teamCeltia = gc.getTeam(pCeltia.getTeam())

iRome = con.iRome
pRome = gc.getPlayer(iRome)
teamRome = gc.getTeam(pRome.getTeam())

iMacedonia = con.iMacedonia
pMacedonia = gc.getPlayer(iMacedonia)
teamMacedonia = gc.getTeam(pMacedonia.getTeam())

iEgypt = con.iEgypt
pEgypt = gc.getPlayer(iEgypt)
teamEgypt = gc.getTeam(pEgypt.getTeam())

iSumeria = con.iSumeria
pSumeria = gc.getPlayer(iSumeria)
teamSumeria = gc.getTeam(pSumeria.getTeam())

iMinoa = con.iMinoa
pMinoa = gc.getPlayer(iMinoa)
teamMinoa = gc.getTeam(pMinoa.getTeam())

iBabylonia = con.iBabylonia
pBabylonia = gc.getPlayer(iBabylonia)
teamBabylonia = gc.getTeam(pBabylonia.getTeam())

iAssyria = con.iAssyria
pAssyria = gc.getPlayer(iAssyria)
teamAssyria = gc.getTeam(pAssyria.getTeam())

iIsrael = con.iIsrael
pIsrael = gc.getPlayer(iIsrael)
teamIsrael = gc.getTeam(pIsrael.getTeam())

iPersia = con.iPersia
pPersia = gc.getPlayer(iPersia)
teamPersia = gc.getTeam(pPersia.getTeam())

iAthens = con.iAthens
pAthens = gc.getPlayer(iAthens)
teamAthens = gc.getTeam(pAthens.getTeam())

iSparta = con.iSparta
pSparta = gc.getPlayer(iSparta)
teamSparta = gc.getTeam(pSparta.getTeam())

iIndia = con.iIndia
pIndia = gc.getPlayer(iIndia)
teamIndia = gc.getTeam(pIndia.getTeam())

iEtruria = con.iEtruria
pEtruria = gc.getPlayer(iEtruria)
teamEtruria = gc.getTeam(pEtruria.getTeam())

iScythia = con.iScythia
pScythia = gc.getPlayer(iScythia)
teamScythia = gc.getTeam(pScythia.getTeam())

iPhoenicia = con.iPhoenicia
pPhoenicia = gc.getPlayer(iPhoenicia)
teamPhoenicia = gc.getTeam(pPhoenicia.getTeam())

iHittites = con.iHittites
pHittites = gc.getPlayer(iHittites)
teamHittites = gc.getTeam(pHittites.getTeam())


# city coordinates, spawn 1st turn and retries


##lTyre = [73, 40, 0, 0] #2700BC #turn10
##lInverness = [52, 60, 167, 0] #400AD

lJericho = [43, 20, con.i4400BC, 0]
lCatalHuyuk = [40, 27, con.i4400BC, 0]
lLarsa = [48, 21, con.i3500BC, 0]
lTanis = [33, 16, con.i3400BC, 0]
lAleppo = [42, 25, con.i3000BC, 0]
lTroy = [35, 31, con.i2400BC, 0]
lAlacaHuyuk = [41, 31, con.i2400BC, 0]
lSamarkand = [57, 32, con.i2000BC, 0]
lBactra = [55, 30, con.i2000BC, 0]
lPetra = [41, 14, con.i1350BC, 0]
lGordion = [38, 30, con.i1200BC, 0]
lTaxila = [58, 30, con.i1000BC, 0]
lThebes = [30, 29, con.i900BC, 0]
lTushpa = [46, 31, con.i850BC, 0]
lHasanlu = [50, 30, con.i850BC, 0]
lSardis = [38, 28, con.i800BC, 0]
lTayma = [42, 11, con.i800BC, 0]
lSyracuse = [20, 23, con.i734BC, 0]
lAmprakia = [26, 28, con.i700BC, 0]
lGerrha = [46, 14, con.i650BC, 0]
lCyrene = [25, 18, con.i631BC, 0]
lSanaa = [44, 6, con.i600BC, 0]
lMassilia = [14, 33, con.i600BC, 0]
lOlbia = [38, 44, con.i600BC, 0]
lPanticapaeum = [41, 41, con.i550BC, 0]
lHemeroscopeum = [9, 28, con.i550BC, 0]
lPattala = [58, 27, con.i500BC, 0]
lArtaxata = [48, 32, con.i190BC, 0]
lSarmizegetusa = [29, 41, con.i82BC, 0]




#handicap level modifier
iHandicapOld = (gc.getGame().getHandicapType() - 1)



class Barbs:

	def makeUnit(self, iUnit, iPlayer, tCoords, iNum, iForceAttack):
		'Makes iNum units for player iPlayer of the type iUnit at tCoords.'
		for i in range(iNum):
			player = gc.getPlayer(iPlayer)
			if (iForceAttack == 0):
				player.initUnit(iUnit, tCoords[0], tCoords[1], UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			elif (iForceAttack == 1):
				player.initUnit(iUnit, tCoords[0], tCoords[1], UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
			elif (iForceAttack == 2):
				player.initUnit(iUnit, tCoords[0], tCoords[1], UnitAITypes.UNITAI_ATTACK_SEA, DirectionTypes.DIRECTION_SOUTH)

	def checkTurn(self, iGameTurn):
		#handicap level modifier
		iHandicap = (gc.getGame().getHandicapType() - 2) #RFCRAND
		if (iHandicap == 2):
			iHandicap = 1
		if (iHandicap == -2):
			iHandicap = -1

		self.foundCity(iIndependent, lJericho, "Jericho", iGameTurn, 1, con.un('town_guard'), 1)
		self.foundCity(iIndependent2, lCatalHuyuk, "Catal Huyuk", iGameTurn, 1, con.un('town_guard'), 1)
		self.foundCity(iIndependent, lLarsa, "Larsa", iGameTurn, 1, con.un('sumerian_vulture'), 1)
		self.foundCity(iBarbarian, lTanis, "Tanis", iGameTurn, 1, con.un('town_guard'), 1)
		self.foundCity(iIndependent2, lAleppo, "Aleppo", iGameTurn, 1, con.un('warrior'), 1)
		self.foundCity(iIndependent, lTroy, "Troy", iGameTurn, 1, con.un('spearman'), 1)
		self.foundCity(iIndependent2, lAlacaHuyuk, "Alaca Huyuk", iGameTurn, 1, con.un('warrior'), 1)
		self.foundCity(iIndependent, lSamarkand, "Samarkand", iGameTurn, 1, con.un('warrior'), 1)
		self.foundCity(iIndependent2, lBactra, "Bactra", iGameTurn, 1, con.un('warrior'), 1)
		self.foundCity(iIndependent, lPetra, "Petra", iGameTurn, 1, con.un('warrior'), 1)
		self.foundCity(iIndependent2, lGordion, "Gordion", iGameTurn, 1, con.un('chariot'), 1)
		self.foundCity(iIndependent, lTaxila, "Taxila", iGameTurn, 1, con.un('warrior'), 1)
		self.foundCity(iBarbarian, lThebes, "Thebes", iGameTurn, 1, con.un('spearman'), 1)
		self.foundCity(iBarbarian, lTushpa, "Tushpa", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iBarbarian, lHasanlu, "Hasanlu", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iIndependent2, lSardis, "Sardis", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iBarbarian, lTayma, "Tayma", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iIndependent, lSyracuse, "Syracuse", iGameTurn, 1, con.un('spearman'), 1)
		self.foundCity(iIndependent2, lAmprakia, "Amprakia", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iBarbarian, lGerrha, "Gerrha", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iIndependent, lCyrene, "Cyrene", iGameTurn, 1, con.un('spearman'), 1)
		self.foundCity(iIndependent2, lSanaa, "Sana'a", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iIndependent, lMassilia, "Massilia", iGameTurn, 1, con.un('spearman'), 1)
		self.foundCity(iIndependent2, lOlbia, "Olbia", iGameTurn, 1, con.un('spearman'), 1)
		self.foundCity(iIndependent, lPanticapaeum, "Panticapaeum", iGameTurn, 1, con.un('spearman'), 1)
		self.foundCity(iIndependent2, lHemeroscopeum, "Hemeroscopeum", iGameTurn, 1, con.un('spearman'), 1)
		self.foundCity(iIndependent, lPattala, "Patala", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iIndependent2, lArtaxata, "Artashat", iGameTurn, 1, con.un('archer'), 1)
		self.foundCity(iIndependent, lSarmizegetusa, "Sarmizegetusa", iGameTurn, 1, con.un('swordsman'), 1)


		#handicap level modifier
		iHandicap = (gc.getGame().getHandicapType() - 1)

		#debug
		#if (iGameTurn % 50 == 1):
		#	print ("iHandicap", iHandicap)
		#	print ("iHandicapOld", iHandicapOld)

		 #Animals
		if (iGameTurn >= con.i4000BC and iGameTurn <= con.i2000BC):
			if (iHandicap >= 0):
				self.spawnUnits(iBarbarian, (10, 38), (53, 56), con.un('warrior'), 1, iGameTurn, 12, 2, utils.outerInvasion, 0)

			self.spawnUnits(iBarbarian, (10, 38), (62, 56), con.un('wolf'), 1, iGameTurn, 4, 2, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (26, 28), (60, 38), con.un('bear'), 1, iGameTurn, 5, 4, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (10, 4), (34, 19), con.un('lion'), 1, iGameTurn, 6, 3, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (40, 17), (58, 36), con.un('panther'), 1, iGameTurn, 7, 3, utils.outerInvasion, 0)

		#Animals
		if (iGameTurn >= con.i2000BC and iGameTurn <= con.i500BC):
			self.spawnUnits(iBarbarian, (2, 36), (62, 59), con.un('wolf'), 1, iGameTurn, 6, 2, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (10, 30), (62, 55), con.un('bear'), 1, iGameTurn, 7, 4, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (4, 0), (61, 35), con.un('lion'), 1, iGameTurn, 8, 3, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (50, 19), (62, 37), con.un('panther'), 1, iGameTurn, 9, 3, utils.outerInvasion, 0)

		#Animals
		if (iGameTurn >= con.i500BC and iGameTurn <= con.i500AD):
			self.spawnUnits(iBarbarian, (22, 40), (62, 59), con.un('wolf'), 1, iGameTurn, 8, 2, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (26, 28), (51, 47), con.un('bear'), 1, iGameTurn, 9, 4, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (24, 0), (53, 25), con.un('lion'), 1, iGameTurn, 11, 3, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (52, 20), (62, 36), con.un('panther'), 1, iGameTurn, 12, 3, utils.outerInvasion, 0)

		#Barbarian nomads
		if (iGameTurn >= con.i1000BC and iGameTurn <= con.i250BC):
			self.spawnUnits(iBarbarian, (52, 34), (62, 50), con.un('warrior'), 1, iGameTurn, 10, 5, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (22, 40), (62, 59), con.un('horseman'), 1, iGameTurn, 10, 5, utils.outerInvasion, 0)

		#Barbarian nomads
		if (iGameTurn >= con.i250BC and iGameTurn <= con.i250AD):
			self.spawnUnits(iBarbarian, (52, 34), (62, 50), con.un('axeman'), 1, iGameTurn, 9, 5, utils.outerInvasion, 0)
			self.spawnUnits(iBarbarian, (22, 40), (62, 59), con.un('horse_archer'), 1, iGameTurn, 9, 5, utils.outerInvasion, 0)

		#Barbarian nomads
		if (iGameTurn >= con.i250AD and iGameTurn <= con.i500AD):
			self.spawnUnits(iBarbarian, (52, 34), (62, 50), con.un('heavy_axeman'), 1, iGameTurn, 8, 5, utils.outerInvasion, 1)
			self.spawnUnits(iBarbarian, (22, 40), (62, 59), con.un('noble_cavalry'), 1, iGameTurn, 8, 5, utils.outerInvasion, 1)

		#Barbarian handicap
		if (iGameTurn >= con.i4000BC and iGameTurn <= con.i3000BC):
			self.spawnUnits(iBarbarian, (0, 0), (62, 59), con.un('town_guard'), 1+iHandicap*2, iGameTurn, 10, 4, utils.outerInvasion, 0)

		#Barbarian handicap
		if (iGameTurn >= con.i3000BC and iGameTurn <= con.i2000BC):
			self.spawnUnits(iBarbarian, (0, 0), (62, 59), con.un('warrior'), 1+iHandicap*2, iGameTurn, 10, 4, utils.outerInvasion, 0)

		#Barbarian handicap
		if (iGameTurn >= con.i2000BC and iGameTurn <= con.i1000BC):
			self.spawnUnits(iBarbarian, (0, 0), (62, 59), con.un('warrior'), 1+iHandicap*2, iGameTurn, 10, 4, utils.outerInvasion, 0)

		#Barbarian handicap
		if (iGameTurn >= con.i1000BC and iGameTurn <= con.i500BC):
			self.spawnUnits(iBarbarian, (0, 0), (62, 59), con.un('axeman'), 1+iHandicap*2, iGameTurn, 10, 4, utils.outerInvasion, 0)

		#Barbarian handicap
		if (iGameTurn >= con.i500BC and iGameTurn <= con.i50BC):
			self.spawnUnits(iBarbarian, (0, 0), (62, 59), con.un('swordsman'), 1+iHandicap*2, iGameTurn, 10, 4, utils.outerInvasion, 0)

		#Barbarian handicap
		if (iGameTurn >= con.i50BC and iGameTurn <= con.i250AD):
			self.spawnUnits(iBarbarian, (0, 0), (62, 59), con.un('hoplite'), 1+iHandicap*2, iGameTurn, 10, 4, utils.outerInvasion, 0)

		#Barbarian handicap
		if (iGameTurn >= con.i250AD and iGameTurn <= con.i500AD):
			self.spawnUnits(iBarbarian, (0, 0), (62, 59), con.un('heavy_axeman'), 1+iHandicap*2, iGameTurn, 10, 4, utils.outerInvasion, 0)

		#Mesopotamia City States
		if (iGameTurn >= con.i3000BC and iGameTurn <= con.i2000BC):
			self.spawnUnits(iBarbarian, (45, 19), (48, 27), con.un('sumerian_vulture'), 1, iGameTurn, 8, 3, utils.inTerritoryInvasion, 0)

		#Indus Bandits
		if (iGameTurn >= con.i2800BC and iGameTurn <= con.i2300BC):
			self.spawnUnits(iBarbarian, (59, 26), (62, 32), con.un('bandit'), 1, iGameTurn, 6, 3, utils.inTerritoryInvasion, 0)

		#Egyptian Old Kingdom
		if (iGameTurn >= con.i2686BC and iGameTurn <= con.i2540BC):
			if (gc.getPlayer(con.iEgypt).isAlive()):
				self.spawnUnits(iEgypt, (29, 7), (31, 9), con.un('warrior'), 1, iGameTurn, 4, 0, utils.inTerritoryInvasion, 0)

		#Egypt 1st Intermediary Period
		if (iGameTurn >= con.i2180BC and iGameTurn <= con.i1990BC):
			self.spawnUnits(iBarbarian, (26, 6), (34, 16), con.un('bandit'), 1, iGameTurn, 7, 3, utils.inTerritoryInvasion, 0)

		#Egyptian Middle Kingdom
		if (iGameTurn >= con.i2055BC and iGameTurn <= con.i1990BC):
			if (gc.getPlayer(con.iEgypt).isAlive()):
				self.spawnUnits(iEgypt, (29, 7), (32, 10), con.un('warrior'), 1, iGameTurn, 4, 0, utils.inTerritoryInvasion, 0)
				self.spawnUnits(iEgypt, (29, 7), (32, 10), con.un('settler'), 1, iGameTurn, 4, 0, utils.inTerritoryInvasion, 0)

		#Aryans
		if (iGameTurn >= con.i2000BC and iGameTurn <= con.i1500BC):
			self.spawnUnits(iBarbarian, (58, 33), (60, 36), con.un('axeman_indian'), 3, iGameTurn, 4, 3, utils.outerInvasion, 1)

		#Hyskos
		if (iGameTurn >= con.i1800BC and iGameTurn <= con.i1550BC):
			self.spawnUnits(iBarbarian, (27, 10), (40, 19), con.un('hyskos'), 2, iGameTurn, 7, 3, utils.inTerritoryInvasion, 1)
			self.spawnUnits(iBarbarian, (27, 10), (40, 19), con.un('egypt_warchariot'), 1, iGameTurn, 7, 3, utils.inTerritoryInvasion, 1)

		#Egypt 2nd Intermediary Period
		if (iGameTurn >= con.i1680BC and iGameTurn <= con.i1550BC):
			self.spawnUnits(iBarbarian, (25, 4), (33, 16), con.un('bandit'), 1, iGameTurn, 7, 3, utils.outerInvasion, 0)

		#late bronze age
		if (iGameTurn >= con.i1600BC and iGameTurn <= con.i1000BC):
			self.spawnUnits(iBarbarian, (18, 20), (48, 35), con.un('warrior'), 2, iGameTurn, 7, 0, utils.outerInvasion, 1)
			self.spawnUnits(iBarbarian, (18, 20), (48, 35), con.un('chariot'), 3, iGameTurn, 8, 3, utils.outerInvasion, 1)
			self.spawnUnits(iBarbarian, (18, 20), (48, 35), con.un('axeman'), 4, iGameTurn, 9, 6, utils.outerInvasion, 1)

		#Egyptian New Kingdom
		if (iGameTurn >= con.i1550BC and iGameTurn <= con.i1500BC):
			if (gc.getPlayer(con.iEgypt).isAlive()):
				self.spawnUnits(iEgypt, (29, 7), (32, 11), con.un('warrior'), 1, iGameTurn, 4, 0, utils.inTerritoryInvasion, 0)
				self.spawnUnits(iEgypt, (29, 7), (32, 11), con.un('settler'), 1, iGameTurn, 4, 0, utils.inTerritoryInvasion, 0)
				self.spawnUnits(iEgypt, (29, 7), (32, 11), con.un('egypt_warchariot'), 1, iGameTurn, 4, 0, utils.inTerritoryInvasion, 0)

				#Sea Peoples
		if (iGameTurn >= con.i1200BC and iGameTurn <= con.i900BC):
			self.spawnUnits(iBarbarian, (27, 22), (34, 26), con.un('seapeople'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1) #Greece
			self.spawnUnits(iBarbarian, (31, 20), (39, 23), con.un('seapeople'), 6, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1) #Islands
			self.spawnUnits(iBarbarian, (36, 24), (38, 22), con.un('seapeople'), 6, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1) #Turkey
			self.spawnUnits(iBarbarian, (40, 19), (42, 26), con.un('seapeople'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1) #Levant
			self.spawnUnits(iBarbarian, (44, 31), (49, 33), con.un('seapeople'), 3, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1) #Syria
			self.spawnUnits(iBarbarian, (28, 16), (37, 17), con.un('seapeople'), 2, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1) #Egypt


				#Libyans.
		if (iGameTurn >= con.i1200BC and iGameTurn <= con.i850BC):
			self.spawnUnits(iBarbarian, (22, 15), (27, 17), con.un('libyan_camelarcher'), 2, iGameTurn, 7, 4, utils.outerInvasion, 0)

		#Berbers.
		if (iGameTurn >= con.i750BC and iGameTurn <= con.i500AD):
			self.spawnUnits(iBarbarian, (0, 0), (27, 16), con.un('arabia_camelarcher'), 1, iGameTurn, 5, 0, utils.outerInvasion, 1)

		#Scythians
		if (iGameTurn >= con.i700BC and iGameTurn <= con.i400BC):
			if (gc.getPlayer(con.iScythia).isAlive()):
				self.spawnUnits(iScythia, (35, 39), (62, 46), con.un('scythia_scythian_rider'), 1, iGameTurn, 10, 3, utils.inTerritoryInvasion, 0)

		#Celtic Raiders
		if (iGameTurn >= con.i650BC and iGameTurn <= con.i250BC):
			if (gc.getPlayer(con.iCeltia).isAlive()):
				self.spawnUnits(iCeltia, (15, 39), (27, 44), con.un('celtic_gallic_warrior'), 3, iGameTurn, 10, 2, utils.outerInvasion, 1)
				self.spawnUnits(iCeltia, (15, 39), (27, 44), con.un('settler'), 1, iGameTurn, 10, 2, utils.outerSpawn, 0)

		#NeoBabylonian Empire
		if (iGameTurn == con.i626BC):
			if (gc.getPlayer(con.iBabylonia).isAlive()):
				if (gc.getPlayer(con.iAssyria).isAlive()):
					teamBabylonia.declareWar(iAssyria, False, -1)

		if (iGameTurn == con.i626BC):
			if (gc.getPlayer(con.iBabylonia).isAlive()):
				if (gc.getPlayer(con.iIsrael).isAlive()):
					teamBabylonia.declareWar(iIsrael, False, -1)

		if (iGameTurn >= con.i620BC and iGameTurn <= con.i590BC):
			if (gc.getPlayer(con.iBabylonia).isAlive()):
				self.spawnUnits(iBabylonia, (45, 23), (47, 26), con.un('babylon_bowman'), 4, iGameTurn, 4, 0, utils.inTerritoryInvasion, 1)

		#Persia Indus Campaign
		if (iGameTurn >= con.i542BC and iGameTurn <= con.i512BC):
			if (gc.getPlayer(con.iIndusValley).isAlive()):
				self.spawnUnits(iPersia, (55, 25), (58, 29), con.un('war_elephant'), 5, iGameTurn, 4, 0, utils.inTerritoryInvasion, 1)

		#Peloponnesian War
		if (iGameTurn == con.i434BC):
			if (gc.getPlayer(con.iAthens).isAlive()):
				if (gc.getPlayer(con.iSparta).isAlive()):
					teamAthens.declareWar(iSparta, False, -1)

		#Celtic Britain
		if (iGameTurn >= con.i350BC and iGameTurn <= con.i200BC):
			if (gc.getPlayer(con.iCeltia).isAlive()):
				self.spawnUnits(iCeltia, (7, 48), (15, 55), con.un('celtic_gallic_warrior'), 1, iGameTurn, 9, 3, utils.outerInvasion, 0)
				self.spawnUnits(iCeltia, (7, 48), (15, 55), con.un('settler'), 1, iGameTurn, 9, 3, utils.outerSpawn, 0)

		#India Indus Campaign
		if (iGameTurn >= con.i314BC and iGameTurn <= con.i284BC):
			if (gc.getPlayer(con.iIndusValley).isAlive()):
				self.spawnUnits(iIndia, (60, 20), (62, 25), con.un('war_elephant'), 4, iGameTurn, 4, 0, utils.inTerritoryInvasion, 1)

		#Dacians
		if (iGameTurn >= con.i300BC and iGameTurn <= con.i100AD):
			self.spawnUnits(iBarbarian, (24, 36), (37, 44), con.un('dacian'), 3, iGameTurn, 10, 5, utils.outerInvasion, 0)

		#Hannibal
		if (iGameTurn >= con.i300BC and iGameTurn <= con.i200BC):
			if (gc.getPlayer(con.iCarthage).isAlive()):
				self.spawnUnits(iCarthage, (4, 26), (9, 28), con.un('war_elephant'), 1, iGameTurn, 5, 2, utils.outerInvasion, 1)
				self.spawnUnits(iCarthage, (4, 26), (9, 28), con.un('carthage_numidian_cavalry'), 1, iGameTurn, 5, 2, utils.outerInvasion, 1)
				self.spawnUnits(iCarthage, (4, 26), (9, 28), con.un('celtic_gallic_warrior'), 1, iGameTurn, 5, 2, utils.outerInvasion, 1)
				self.spawnUnits(iCarthage, (4, 26), (9, 28), con.un('spearman'), 1, iGameTurn, 5, 2, utils.outerInvasion, 1)
				self.spawnUnits(iCarthage, (4, 26), (9, 28), con.un('settler'), 1, iGameTurn, 5, 2, utils.outerSpawn, 0)

		#Roman Italy
		if (iGameTurn == con.i270BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				if (gc.getPlayer(con.iEtruria).isAlive()):
					teamRome.declareWar(iEtruria, False, -1)

		#Italian Campaign
		if (iGameTurn >= con.i264BC and iGameTurn <= con.i236BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				self.spawnUnits(iRome, (17, 31), (20, 36), con.un('rome_praetorian'), 5, iGameTurn, 4, 0, utils.inTerritoryInvasion, 1)

		#Punic Wars
		if (iGameTurn == con.i264BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				if (gc.getPlayer(con.iCarthage).isAlive()):
					teamRome.declareWar(iCarthage, False, -1)

		#Scipio
		if (iGameTurn >= con.i250BC and iGameTurn <= con.i218BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				self.spawnUnits(iRome, (14, 19), (18, 20), con.un('rome_praetorian'), 6, iGameTurn, 4, 0, utils.inTerritoryInvasion, 1)

				# Numidians Barbarians
		if (iGameTurn >= con.i250BC and iGameTurn <= con.i150BC):
			self.spawnUnits(iBarbarian, (7, 17), (14, 20), con.un('carthage_numidian_cavalry'), 3, iGameTurn, 6, 2, utils.outerInvasion, 0)

		#pirates in Mediterranean
		if (iGameTurn >= con.i210BC and iGameTurn <= con.i70AD):
			self.spawnUnits(iBarbarian, (7, 16), (41, 32), con.un('galley'), 1, iGameTurn, 7, 0, utils.outerSeaSpawn, 2)

		#Yuezhi Invasion
		if (iGameTurn >= con.i150BC and iGameTurn <= con.i50BC):
			self.spawnUnits(iBarbarian, (54, 36), (62, 44), con.un('yuezhi'), 4, iGameTurn, 5, 3, utils.inTerritoryInvasion, 1)

		#Germanic Tribes
		if (iGameTurn >= con.i150BC and iGameTurn <= con.i150AD):
			self.spawnUnits(iBarbarian, (19, 41), (31, 53), con.un('germanic_swordsman'), 4, iGameTurn, 10, 3, utils.outerInvasion, 1)

		#Roman Greece
		if (iGameTurn == con.i50BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				if (gc.getPlayer(con.iAthens).isAlive()):
					teamRome.declareWar(iAthens, False, -1)

		if (iGameTurn == con.i50BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				if (gc.getPlayer(con.iSparta).isAlive()):
					teamRome.declareWar(iSparta, False, -1)

		if (iGameTurn == con.i50BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				if (gc.getPlayer(con.iMacedonia).isAlive()):
					teamRome.declareWar(iMacedonia, False, -1)

		if (iGameTurn >= con.i146BC and iGameTurn <= con.i116BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				self.spawnUnits(iRome, (27, 25), (31, 27), con.un('rome_praetorian'), 7, iGameTurn, 4, 0, utils.inTerritoryInvasion, 1)

		#Gallic Wars
		if (iGameTurn == con.i58BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				if (gc.getPlayer(con.iCeltia).isAlive()):
					teamRome.declareWar(iCeltia, False, -1)

		if (iGameTurn >= con.i50BC and iGameTurn <= con.i20BC):
			if (gc.getPlayer(con.iRome).isAlive()):
				self.spawnUnits(iRome, (13, 40), (16, 43), con.un('rome_praetorian'), 8, iGameTurn, 4, 0, utils.inTerritoryInvasion, 1)

		#Vandals
		if (iGameTurn >= con.i400AD and iGameTurn <= con.i475AD):
			self.spawnUnits(iBarbarian, (27, 42), (31, 47), con.un('vandal'), 4, iGameTurn, 6, 2, utils.outerInvasion, 1)

		#Anglo-Saxons
		if (iGameTurn >= con.i400AD and iGameTurn <= con.i475AD):
			self.spawnUnits(iBarbarian, (7, 48), (19, 57), con.un('angle'), 4, iGameTurn, 7, 3, utils.outerInvasion, 1)

		#Sueves
		if (iGameTurn >= con.i400AD and iGameTurn <= con.i475AD):
			self.spawnUnits(iBarbarian, (2, 33), (28, 44), con.un('sueves'), 4, iGameTurn, 7, 4, utils.outerInvasion, 1)

		#Burgundians
		if (iGameTurn >= con.i400AD and iGameTurn <= con.i475AD):
			self.spawnUnits(iBarbarian, (13, 37), (29, 45), con.un('burgundian'), 4, iGameTurn, 7, 5, utils.outerInvasion, 1)

		 #Barbians for Balance
		if (iGameTurn >= con.i1400BC and iGameTurn <= con.i1244BC):
			if (gc.getPlayer(con.iSumeria).isAlive()):
				self.spawnUnits(iBarbarian, (44, 18), (47, 21), con.un('axeman'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

		if (iGameTurn >= con.i900BC and iGameTurn <= con.i782BC):
			if (gc.getPlayer(con.iIndusValley).isAlive()):
				self.spawnUnits(iBarbarian, (60, 25), (62, 32), con.un('horse_archer'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

		if (iGameTurn >= con.i678BC and iGameTurn <= con.i560BC):
			if (gc.getPlayer(con.iHittites).isAlive()):
				self.spawnUnits(iBarbarian, (37, 26), (41, 32), con.un('spearman'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

		if (iGameTurn >= con.i600BC and iGameTurn <= con.i482BC):
			if (gc.getPlayer(con.iMinoa).isAlive()):
				self.spawnUnits(iBarbarian, (31, 20), (35, 21), con.un('swordsman'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

		if (iGameTurn >= con.i500BC and iGameTurn <= con.i380BC):
			if (gc.getPlayer(con.iEgypt).isAlive()):
				self.spawnUnits(iBarbarian, (29, 6), (31, 14), con.un('persia_immortal'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

		if (iGameTurn >= con.i109BC and iGameTurn <= con.i10AD):
			if (gc.getPlayer(con.iAssyria).isAlive()):
				self.spawnUnits(iBarbarian, (44, 23), (48, 28), con.un('scythia_scythian_rider'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

		if (iGameTurn >= con.i39BC and iGameTurn <= con.i82AD):
			if (gc.getPlayer(con.iPhoenicia).isAlive()):
				self.spawnUnits(iBarbarian, (39, 18), (43, 26), con.un('greek_phalanx'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

		if (iGameTurn >= con.i162AD and iGameTurn <= con.i280AD):
			if (gc.getPlayer(con.iAthens).isAlive()):
				self.spawnUnits(iBarbarian, (30, 26), (34, 30), con.un('legion'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

		if (iGameTurn >= con.i170AD and iGameTurn <= con.i292AD):
			if (gc.getPlayer(con.iPersia).isAlive()):
				self.spawnUnits(iBarbarian, (49, 19), (55, 26), con.un('companion_cavalry'), 4, iGameTurn, 7, 2, utils.inTerritoryInvasion, 1)

##		if (iGameTurn >= con.i70AD and iGameTurn <= con.i600AD):
##			self.spawnUnits(iBarbarian, (10, 4), (49, 19), con.iCamelArcher, 3+iHandicap*1, iGameTurn, 6, 0, utils.innerSpawn, 0)
##			self.spawnUnits(iBarbarian, (47, 18), (60, 38), con.un('bandit'), 3+iHandicap*1, iGameTurn, 6, 0, utils.innerSpawn, 0)

		if (iGameTurn >= con.i100AD and iGameTurn <= con.i250AD):
			if (not gc.getPlayer(con.iGermania).isAlive()):
				self.spawnUnits(iBarbarian, (13, 36), (48, 45), con.un('swordsman'), 5, iGameTurn, 5, 0, utils.outerInvasion, 0)
		if (iGameTurn >= con.i450AD and iGameTurn <= con.i600AD):
			if (not gc.getPlayer(con.iHuns).isAlive()):
				self.spawnUnits(iBarbarian, (13, 36), (50, 43), con.un('horse_archer'), 5, iGameTurn, 5, 0, utils.outerInvasion, 0)



		#War Mechanis,
##	       if (iGameTurn == con.i4000BC):
##			if (gc.getPlayer(con.iSumeria).isAlive()):
##				if (gc.getPlayer(con.iEgypt).isAlive()):
##					teamSumeria.declareWar(iEgypt, False, -1)

		#barbarians in europe
		#nothing for now - if Germanic tribes work
##		if (iGameTurn >= con.i210BC and iGameTurn <= con.i470AD):
##			self.spawnUnits(iBarbarian, (50, 45), (63, 52), con.un('axeman'), 3 + iHandicap, iGameTurn, 10, 0, utils.outerInvasion, 0)
##			self.spawnUnits(iBarbarian, (64, 49), (69, 55), con.un('axeman'), 2 + iHandicap, iGameTurn, 14, 2, utils.outerInvasion, 0)
##		if (iGameTurn >= con.i50AD and iGameTurn <= con.i470AD):
##			self.spawnUnits(iBarbarian, (58, 45), (70, 55), con.un('swordsman'), 3, iGameTurn, 10, 5, utils.outerInvasion, 0)
##		if (iGameTurn >= con.i300AD and iGameTurn <= con.i550AD):
##			self.spawnUnits(iBarbarian, (49, 41), (56, 52), con.un('axeman'), 4 + iHandicap, iGameTurn, 6, 4, utils.outerInvasion, 0)
##			self.spawnUnits(iBarbarian, (49, 41), (57, 52), con.un('swordsman'), 4 + iHandicap, iGameTurn, 6, 2, utils.outerInvasion, 0)
##			self.spawnUnits(iBarbarian, (55, 49), (65, 53), con.un('horse_archer'), 3, iGameTurn, 6, 0, utils.outerInvasion, 0)
##		if (iGameTurn >= con.i300AD and iGameTurn <= con.i700AD):
##			self.spawnUnits(iBarbarian, (58, 50), (88, 53), con.un('horse_archer'), 3 + iHandicap, iGameTurn, 4, 2, utils.outerInvasion, 0)
##

	def getCity(self, tCoords): #by LOQ
		'Returns a city at coordinates tCoords.'
		return CyGlobalContext().getMap().plot(tCoords[0], tCoords[1]).getPlotCity()

	def foundCity(self, iCiv, lCity, name, iTurn, iPopulation, iUnitType, iNumUnits):
		if ((iTurn == lCity[2] + lCity[3]) and (lCity[3]<10)):
			#print self.checkRegion(tUr)
			bResult, lCity[3] = self.checkRegion(lCity)
			if (bResult == True):
				pCiv = gc.getPlayer(iCiv)
				pCiv.found(lCity[0], lCity[1])
				self.getCity((lCity[0], lCity[1])).setName(name, False)
				if (iPopulation != 1):
					self.getCity((lCity[0], lCity[1])).setPopulation(iPopulation)
				if (iNumUnits > 0):
					self.makeUnit(iUnitType, iCiv, (lCity[0], lCity[1]), iNumUnits, 0)
				return True
			if (bResult == False) and (lCity[3] == -1):
				return False


	def checkRegion(self, tCity):
		cityPlot = gc.getMap().plot(tCity[0], tCity[1])
		iNumUnitsInAPlot = cityPlot.getNumUnits()
##		print iNumUnitsInAPlot

		#checks if the plot already belongs to someone
		if (cityPlot.isOwned()):
			if (cityPlot.getOwner() != iBarbarian and cityPlot.getOwner() != iIndependent and cityPlot.getOwner() != iIndependent2): #RFGW
				return (False, -1)

##		#checks if there's a unit on the plot
		if (iNumUnitsInAPlot):
			for i in range(iNumUnitsInAPlot):
				unit = cityPlot.getUnit(i)
				iOwner = unit.getOwner()
				if (iOwner == iBarbarian):
					return (False, tCity[3]+1)
				#pOwner = gc.getPlayer(iOwner)
				#if (pOwner.isHuman()):
				#	return (False, tCity[3]+1)

		#checks the surroundings and allows only AI units
		for x in range(tCity[0]-1, tCity[0]+2):
			for y in range(tCity[1]-1, tCity[1]+2):
				currentPlot=gc.getMap().plot(x,y)
				if (currentPlot.isCity()):
					return (False, -1)
				iNumUnitsInAPlot = currentPlot.getNumUnits()
				if (iNumUnitsInAPlot):
					for i in range(iNumUnitsInAPlot):
						unit = currentPlot.getUnit(i)
						iOwner = unit.getOwner()
						pOwner = gc.getPlayer(iOwner)
						if (pOwner.isHuman()):
							return (False, tCity[3]+1)
		return (True, tCity[3])



	def spawnUnits(self, iCiv, tTopLeft, tBottomRight, iUnitType, iNumUnits, iTurn, iPeriod, iRest, function, iForceAttack):
		if (iTurn % iPeriod == iRest):
			dummy, plotList = utils.squareSearch(tTopLeft, tBottomRight, function, [])
			if (len(plotList)):
				rndNum = gc.getGame().getSorenRandNum(len(plotList), 'Spawn units')
				result = plotList[rndNum]
				if (result):
					self.makeUnit(iUnitType, iCiv, result, iNumUnits, iForceAttack)




	def killNeighbours(self, tCoords):
		'Kills all units in the neigbbouring tiles of plot (as well as plot itself) so late starters have some space.'
		print 'killing neighbors'
		for x in range(tCoords[0]-1, tCoords[0]+2):	# from x-1 to x+1
			for y in range(tCoords[1]-1, tCoords[1]+2):	# from y-1 to y+1
				killPlot = CyMap().getPlot(x, y)
				for i in range(killPlot.getNumUnits()):
					unit = killPlot.getUnit(0)	# 0 instead of i because killing units changes the indices
					unit.kill(False, iBarbarian)

