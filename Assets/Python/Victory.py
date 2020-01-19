# Rhye's and Fall of Civilization - Historical Victory Goals


from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Popup
import cPickle as pickle
import Consts as con
import RFCUtils
utils = RFCUtils.RFCUtils()

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer



### Constants ###

i4000BC = con.i4000BC
i3000BC = con.i3000BC
i2200BC = con.i2200BC
i2180BC = con.i2180BC
i2000BC = con.i2000BC
i1900BC = con.i1900BC
i1800BC = con.i1800BC
i1690BC = con.i1690BC
i1500BC = con.i1500BC
i1400BC = con.i1400BC
i1200BC = con.i1200BC
i1250BC = con.i1250BC
i1070BC = con.i1070BC
i1000BC = con.i1000BC
i900BC = con.i900BC
i600BC = con.i600BC
i500BC = con.i500BC
i250BC = con.i250BC
i100BC = con.i100BC



iAncient = con.iAncient
iClassical = con.iClassical
iMedieval = con.iMedieval

tCoreAreasTL = con.tCoreAreasTL
tCoreAreasBR = con.tCoreAreasBR
tNormalAreasTL = con.tNormalAreasTL
tNormalAreasBR = con.tNormalAreasBR
tLevantTL = (39, 18)
tLevantBR = (43, 26)
tIranTL = (48, 19)
tIranBR = (54, 28)
tNubiaTL = (24, 0)
tNubiaBR = (35, 4)
tMesopotamiaTL = (44, 18)
tMesopotamiaBR = (49, 27)
tEgyptTL = (26, 5)
tEgyptBR = (35, 17)
tNAfricaTL = (0, 17)
tNAfricaBR = (27, 24)
tCyprusTL = (37, 21)
tCyprusBR = (39, 23)
tIberiaTL = (2, 26)
tIberiaBR = (12, 38)


# initialise player variables
iEgypt = con.iEgypt
iSumeria = con.iSumeria
iIndusValley = con.iIndusValley
iElam = con.iElam
iMinoa = con.iMinoa
iPhoenicia = con.iPhoenicia
iBabylonia = con.iBabylonia
iHittites = con.iHittites
iMycenae = con.iMycenae
iAssyria = con.iAssyria
iIsrael = con.iIsrael
iAthens = con.iAthens
iSparta = con.iSparta
iScythia = con.iScythia
iCarthage = con.iCarthage
iCeltia = con.iCeltia
iEtruria = con.iEtruria
iNubia = con.iNubia
iPersia = con.iPersia
iRome = con.iRome
iMacedonia = con.iMacedonia
iIndia = con.iIndia
iBactria = con.iBactria
iNumidia = con.iNumidia
iGermania = con.iGermania
iSassanid = con.iSassanid
iByzantium = con.iByzantium
iHuns = con.iHuns
iNumPlayers = con.iNumPlayers
iNumMajorPlayers = con.iNumMajorPlayers
iNumActivePlayers = con.iNumActivePlayers
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iBarbarian = con.iBarbarian
iNumTotalPlayers = con.iNumTotalPlayers

pEgypt = gc.getPlayer(iEgypt)
pSumeria = gc.getPlayer(iSumeria)
pIndusValley = gc.getPlayer(iIndusValley)
pElam = gc.getPlayer(iElam)
pMinoa = gc.getPlayer(iMinoa)
pPhoenicia = gc.getPlayer(iPhoenicia)
pBabylonia = gc.getPlayer(iBabylonia)
pHittites = gc.getPlayer(iHittites)
pMycenae = gc.getPlayer(iMycenae)
pAssyria = gc.getPlayer(iAssyria)
pIsrael = gc.getPlayer(iIsrael)
pAthens = gc.getPlayer(iAthens)
pSparta = gc.getPlayer(iSparta)
pScythia = gc.getPlayer(iScythia)
pCarthage = gc.getPlayer(iCarthage)
pCeltia = gc.getPlayer(iCeltia)
pEtruria = gc.getPlayer(iEtruria)
pNubia = gc.getPlayer(iNubia)
pPersia = gc.getPlayer(iPersia)
pRome = gc.getPlayer(iRome)
pMacedonia = gc.getPlayer(iMacedonia)
pIndia = gc.getPlayer(iIndia)
pBactria = gc.getPlayer(iBactria)
pNumidia = gc.getPlayer(iNumidia)
pGermania = gc.getPlayer(iGermania)
pSassanid = gc.getPlayer(iSassanid)
pByzantium = gc.getPlayer(iByzantium)
pHuns = gc.getPlayer(iHuns)
pIndependent = gc.getPlayer(iIndependent)
pIndependent2 = gc.getPlayer(iIndependent2)
pBarbarian = gc.getPlayer(iBarbarian)

teamEgypt = gc.getTeam(pEgypt.getTeam())
teamSumeria = gc.getTeam(pSumeria.getTeam())
teamIndusValley = gc.getTeam(pIndusValley.getTeam())
teamElam = gc.getTeam(pElam.getTeam())
teamMinoa = gc.getTeam(pMinoa.getTeam())
teamPhoenicia = gc.getTeam(pPhoenicia.getTeam())
teamBabylonia = gc.getTeam(pBabylonia.getTeam())
teamHittites = gc.getTeam(pHittites.getTeam())
teamMycenae = gc.getTeam(pMycenae.getTeam())
teamAssyria = gc.getTeam(pAssyria.getTeam())
teamIsrael = gc.getTeam(pIsrael.getTeam())
teamAthens = gc.getTeam(pAthens.getTeam())
teamSparta = gc.getTeam(pSparta.getTeam())
teamScythia = gc.getTeam(pScythia.getTeam())
teamCarthage = gc.getTeam(pCarthage.getTeam())
teamCeltia = gc.getTeam(pCeltia.getTeam())
teamEtruria = gc.getTeam(pEtruria.getTeam())
teamNubia = gc.getTeam(pNubia.getTeam())
teamPersia = gc.getTeam(pPersia.getTeam())
teamRome = gc.getTeam(pRome.getTeam())
teamMacedonia = gc.getTeam(pMacedonia.getTeam())
teamIndia = gc.getTeam(pIndia.getTeam())
teamBactria = gc.getTeam(pBactria.getTeam())
teamNumidia = gc.getTeam(pNumidia.getTeam())
teamGermania = gc.getTeam(pGermania.getTeam())
teamSassanid = gc.getTeam(pSassanid.getTeam())
teamByzantium = gc.getTeam(pByzantium.getTeam())
teamHuns = gc.getTeam(pHuns.getTeam())
teamIndependent = gc.getTeam(pIndependent.getTeam())
teamIndependent2 = gc.getTeam(pIndependent2.getTeam())
teamBarbarian = gc.getTeam(pBarbarian.getTeam())

class Victory:


##################################################
### Secure storage & retrieval of script data ###
################################################


	def getGoal(self, i, j):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lGoals'][i][j]

	def setGoal(self, i, j, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lGoals'][i][j] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))
		if iNewValue is 0:
			return
		if self.getGoal(i, 0) is 1 and self.getGoal(i, 1) is 1 and self.getGoal(i, 2) is 1:
			if gc.getGame().getWinner() == -1:
				gc.getGame().setWinner(i, 7)

	def getReligionFounded(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lReligionFounded'][iCiv]

	def setReligionFounded(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lReligionFounded'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getEnslavedUnits(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iEnslavedUnits']

	def getRazedByMongols(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iRazedByMongols']

	def setRazedByMongols(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iRazedByMongols'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getEnglishEras(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lEnglishEras'][i]

	def setEnglishEras(self, i, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lEnglishEras'][i] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getGreekTechs(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lGreekTechs'][i]

	def setGreekTechs(self, i, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lGreekTechs'][i] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getBabyloniaKilledCivs(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['babyloniaKilledCivs']

	def setBabyloniaKilledCivs(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['babyloniaKilledCivs'] = i
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getWondersBuilt(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lWondersBuilt'][iCiv]

	def setWondersBuilt(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lWondersBuilt'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def get2OutOf3(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['l2OutOf3'][iCiv]

	def set2OutOf3(self, iCiv, bNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['l2OutOf3'][iCiv] = bNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getNumSinks(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iNumSinks']

	def setNumSinks(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iNumSinks'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getSumerianTechs(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lSumerianTechs'][i]

	def setSumerianTechs(self, i, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lSumerianTechs'][i] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getMediterraneanColonies(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iMediterraneanColonies']

	def setMediterraneanColonies(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iMediterraneanColonies'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getPortugueseColonies(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iPortugueseColonies']

	def setPortugueseColonies(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iPortugueseColonies'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getNewWorld(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lNewWorld'][i]

	def setNewWorld(self, i, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lNewWorld'][i] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

#######################################
### Main methods (Event-Triggered) ###
#####################################


	def checkOwnedCiv(self, iActiveCiv, iOwnedCiv):
		dummy1, plotList1 = utils.squareSearch(tNormalAreasTL[iOwnedCiv], tNormalAreasBR[iOwnedCiv], utils.ownedCityPlots, iActiveCiv)
		dummy2, plotList2 = utils.squareSearch(tNormalAreasTL[iOwnedCiv], tNormalAreasBR[iOwnedCiv], utils.ownedCityPlots, iOwnedCiv)
		if ((len(plotList1) >= 2 and len(plotList1) > len(plotList2)) or (len(plotList1) >= 1 and not gc.getPlayer(iOwnedCiv).isAlive())):
			return True
		else:
			return False


	def checkOwnedArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
		dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv)
		if (len(plotList) >= iThreshold):
			return True
		else:
			return False


	def checkOwnedAreaAdjacentArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold, tPlotArea):
		dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.ownedCityPlotsAdjacentArea, [iActiveCiv, tPlotArea])
		if (len(plotList) >= iThreshold):
			print(len(plotList))
			return True
		else:
			print(len(plotList))
			return False


	def checkFoundedArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
		dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.foundedCityPlots, iActiveCiv)
		if (len(plotList) >= iThreshold):
			return True
		else:
			return False

	def checkNotOwnedArea(self, iActiveCiv, tTopLeft, tBottomRight):
		dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv)
		if (len(plotList)):
			return False
		else:
			return True

	def checkNotOwnedArea_Skip(self, iActiveCiv, tTopLeft, tBottomRight, tSkipTopLeft, tSkipBottomRight):
		dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv)
		if (not len(plotList)):
			return True
		else:
			for loopPlot in plotList:
				if not (loopPlot[0] >= tSkipTopLeft[0] and loopPlot[0] <= tSkipBottomRight[0] and \
				    loopPlot[1] >= tSkipTopLeft[1] and loopPlot[1] <= tSkipBottomRight[1]):
					return False
		return True


	def checkOwnedCoastalArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
		dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv)
		iCounter = 0
		for i in range(len(plotList)):
			x = plotList[i][0]
			y = plotList[i][1]
			plot = gc.getMap().plot(x, y)
			if (plot.isCity()):
			       if (plot.getPlotCity().isCoastalOld()):
				       iCounter += 1
		if (iCounter >= iThreshold):
			return True
		else:
			return False

	def checkOwnedCoastalAreaExceptions(self, iActiveCiv, tTopLeft, tBottomRight, tExceptionList, iThreshold):
		dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv)
		iCounter = 0
		for i in range(len(plotList)):
			x = plotList[i][0]
			y = plotList[i][1]
			plot = gc.getMap().plot(x, y)
			if (plot.isCity()):
			       if (plot.getPlotCity().isCoastalOld()):
				       bOK = True
				       for j in tExceptionList:
					       if (x == j[0] and y == j[1]):
						       bOK = False
						       break
				       if (bOK):
					       iCounter += 1
		if (iCounter >= iThreshold):
			return True
		else:
			return False

	def checkFoundedCoastalArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
		dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.foundedCityPlots, iActiveCiv)
		iCounter = 0
		for i in range(len(plotList)):
			x = plotList[i][0]
			y = plotList[i][1]
			plot = gc.getMap().plot(x, y)
			if (plot.isCity()):
			       if (plot.getPlotCity().isCoastalOld()):
				       iCounter += 1
		if (iCounter >= iThreshold):
			return True
		else:
			return False

	def checkPlayerTurn(self, iGameTurn, iPlayer):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		if (iPlayer == iEgypt):
			if (pEgypt.isAlive() and iGameTurn <= i1070BC):
				if (iGameTurn == i2180BC):
					if (pEgypt.countTotalCulture() >= 1000):
						self.setGoal(iEgypt, 0, 1)
					else:
						self.setGoal(iEgypt, 0, 0)
				elif (iGameTurn == i1690BC):
					if (gc.getGame().getTeamRank(iEgypt) == 0):
						self.setGoal(iEgypt, 1, 1)
					else:
						self.setGoal(iEgypt, 1, 0)
				elif (iGameTurn > i1690BC):
					bLevant = self.checkOwnedArea(iEgypt, tLevantTL, tLevantBR, 2)
					bNubia = self.checkOwnedArea(iEgypt, tNubiaTL, tNubiaBR, 2)
					bEgypt = self.checkOwnedArea(iEgypt, tEgyptTL, tEgyptBR, 2)
					if (bLevant and bNubia and bEgypt):
						self.setGoal(iEgypt, 2, 1)
					elif iGameTurn > i1070BC:
						self.setGoal(iEgypt, 2, 0)
		elif (iPlayer == iSumeria):
			if (pSumeria.isAlive()):
				if (iGameTurn == i2200BC):
					bLevant = self.checkOwnedArea(iSumeria, tLevantTL, tLevantBR, 2)
					bMesopotamia = self.checkOwnedArea(iSumeria, tMesopotamiaTL, tMesopotamiaBR, 2)
					if (bLevant and bMesopotamia):
						self.setGoal(iSumeria, 2, 1)
					else:
						self.setGoal(iSumeria, 2, 0)

				if (iGameTurn == i2000BC):
					bestCity = self.calculateTopCityCulture(46, 19)
					if (bestCity != -1):
						print ("bestCity.getOwner()", bestCity.getOwner())
						if (bestCity.getOwner() == iSumeria and bestCity.getX() == 46 and bestCity.getY() == 19):
							self.setGoal(iSumeria, 1, 1)
						else:
							self.setGoal(iSumeria, 1, 0)
					else:
						self.setGoal(iSumeria, 1, 0)

		elif (iPlayer == iIndusValley):
			if (pIndusValley.isAlive()):
				if (iGameTurn == i1250BC):
					iIndusValleyResource = 0
					bResources = True
					for iBonus in range(con.iPearls):
						if (pIndusValley.getNumAvailableBonuses(iBonus) > 0):
							iIndusValleyResource += 1
					for iCiv in range(iNumPlayers):
						if (iCiv != iIndusValley):
							pCiv = gc.getPlayer(iCiv)
							iElseResource = 0
							if (pCiv.isAlive()):
								for iBonusA in range(con.iPearls):
									if (pCiv.getNumAvailableBonuses(iBonusA) > 0):
										iElseResource += 1
								if (iElseResource > iIndusValleyResource):
									bResources = False
									break
					if (bResources):
						self.setGoal(iIndusValley, 1, 1)
					else:
						self.setGoal(iIndusValley, 1, 0)

				if (iGameTurn == i1500BC):
					iPop = pIndusValley.getRealPopulation()
					#iPop = pIndia.getTotalPopulation()
					#print ("india pop", pIndia.getTotalPopulation(), pIndia.getRealPopulation())
					bFirst = True
					for iCiv in range(iNumPlayers):
						#print ("other pop", iCiv, gc.getPlayer(iCiv).getTotalPopulation(), gc.getPlayer(iCiv).getRealPopulation())
						if (iPop < gc.getPlayer(iCiv).getRealPopulation()):
							bFirst = False
							break
					if (bFirst):
						self.setGoal(iIndusValley, 0, 1)
					else:
						self.setGoal(iIndusValley, 0, 0)

				if (iGameTurn == i1000BC):
					if (self.getGoal(iIndusValley, 2) == -1): #see onCityAcquired()
						self.setGoal(iIndusValley, 2, 1)


		elif (iPlayer == iMinoa):
			if (pMinoa.isAlive()):
				if (iGameTurn == i1400BC):
					if (teamMinoa.isHasTech(con.tn('calendar'))):
						self.setGoal(iMinoa, 0, 1)
					else:
						self.setGoal(iMinoa, 0, 0)

				if (iGameTurn == i1200BC):
					if (gc.getGame().getTeamRank(iMinoa) == 0):
						self.setGoal(iMinoa, 1, 1)
					else:
						self.setGoal(iMinoa, 1, 0)

				if (iGameTurn == i1000BC):
					bestCity = self.calculateTopCityCulture(33, 21)
					if (bestCity != -1):
						print ("bestCity.getOwner()", bestCity.getOwner())
						if (bestCity.getOwner() == iMinoa and bestCity.getX() == 33 and bestCity.getY() == 21):
							self.setGoal(iMinoa, 2, 1)
						else:
							self.setGoal(iMinoa, 2, 0)
					else:
						self.setGoal(iMinoa, 2, 0)


		elif (iPlayer == iPhoenicia):
			if (pPhoenicia.isAlive()):
				if (iGameTurn == i900BC):
					bLevant = self.checkOwnedArea(iPhoenicia, tLevantTL, tLevantBR, 1)
					bNAfrica = self.checkOwnedArea(iPhoenicia, tNAfricaTL, tNAfricaBR, 1)
					bCyprus = self.checkOwnedArea(iPhoenicia, tCyprusTL, tCyprusBR, 1)
					bIberia = self.checkOwnedArea(iPhoenicia, tIberiaTL, tIberiaBR, 1)
					if (bLevant and bNAfrica and bCyprus and bIberia):
						self.setGoal(iPhoenicia, 0, 1)
					else:
						self.setGoal(iPhoenicia, 0, 0)

				if (iGameTurn == i600BC):
					lRevealedMap = con.l0Array
					for iCiv in range(iNumPlayers):
						for x in range(63):
							for y in range(60):
								if (gc.getMap().plot(x, y).isRevealed(iCiv, False)):
								      lRevealedMap[iCiv] += 1
					bBestMap = True
					for iCiv in range(iNumPlayers):
						if (lRevealedMap[iPhoenicia] < lRevealedMap[iCiv]):
							bBestMap = False
							break

					if (bBestMap == True):
						self.setGoal(iPhoenicia, 1, 1)
					else:
						self.setGoal(iPhoenicia, 1, 0)

				if (iGameTurn == i500BC):
					iPhoeniciaResource = 0
					bResources = True
					for iBonus in range(con.iPearls):
						if (pPhoenicia.getNumAvailableBonuses(iBonus) > 0):
							iPhoeniciaResource += 1
					for iCiv in range(iNumPlayers):
						if (iCiv != iPhoenicia):
							pCiv = gc.getPlayer(iCiv)
							iElseResource = 0
							if (pCiv.isAlive()):
								for iBonusA in range(con.iPearls):
									if (pCiv.getNumAvailableBonuses(iBonusA) > 0):
										iElseResource += 1
								if (iElseResource > iPhoeniciaResource):
									bResources = False
									break
					if (bResources):
						self.setGoal(iPhoenicia, 2, 1)
					else:
						self.setGoal(iPhoenicia, 2, 0)
		elif iPlayer is iElam and iGameTurn <= i1000BC:
			if pElam.isAlive():
				if iGameTurn < i1900BC:
					if pElam.canContact(iIndusValley) and pElam.canTradeNetworkWith(iIndusValley):
						self.setGoal(iElam, 1, 1)
				elif iGameTurn is i1900BC and self.getGoal(iElam, 1) is -1:
					self.setGoal(iElam, 1, 0)
				elif iGameTurn < i1500BC and self.getGoal(iElam, 2) is -1:
					if self.checkOwnedArea(iElam, tIranTL, tIranBR, 5):
						self.setGoal(iElam, 2, 1)
				elif iGameTurn is i1500BC and self.getGoal(iElam, 2) is -1:
					if self.checkOwnedArea(iElam, tIranTL, tIranBR, 5):
						self.setGoal(iElam, 2, 1)
					else:
						self.setGoal(iElam, 2, 0)
		elif iPlayer is iBabylonia and pBabylonia.isAlive() and iGameTurn <= i600BC:
			if iGameTurn < i1000BC:
				babylonPlot = gc.getMap().plot(46, 22)
				if babylonPlot.isCity():
					if babylonPlot.getPlotCity().getNumWorldWonders() >= 6:
						self.setGoal(iBabylonia, 0, 1)
			elif iGameTurn is i1000BC:
				if not babylonPlot.isCity() or babylonPlot.getPlotCity().getNumWorldWonders() < 6:
					self.setGoal(iBabylon, 0, 0)
				else:
					self.setGoal(iBabylon, 0, 1)
			elif iGameTurn < i600BC:
				if self.getBabyloniaKilledCivs() >= 3:
					self.setGoal(iBabylonia, 2, 1)
			elif iGameTurn is i600BC:
				if self.getBabyloniaKilledCivs() < 3:
					self.setGoal(iBabylonia, 2, 0)
				else:
					self.setGoal(iBabylonia, 2, 1)


	def onCityBuilt(self, city, iPlayer): #see onCityBuilt in CvRFCEventHandler

		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()



	def onReligionFounded(self, iReligion, iFounder):

		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iPlayer = iFounder


	def onCityAcquired(self, owner, attacker, city, bConquest):

		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()
		print 'city acquired'
		
		if self.getGoal(iElam, 0) is -1 and city.getX() is 46 and city.getY() is 19: #Ur captured by Elam
			if attacker is iElam:
				self.setGoal(iElam, 0, 1)
			else:
				self.setGoal(iElam, 0, 0)

		if (owner == iIndusValley):
			if (pIndusValley.isAlive()):
				if (bConquest):
					if (self.getGoal(iIndusValley, 2) == -1):
						if (iGameTurn <= i1000BC):
							if (attacker == iBarbarian):
								self.setGoal(iIndusValley, 2, 0)
		if attacker is iBabylonia:
			if gc.getPlayer(owner).getNumCities() is 0:
				self.setBabyloniaKilledCivs(self.getBabyloniaKilledCivs()+1)
			else:
				print "cities: " + str(gc.getPlayer(owner).getNumCities())

	def onCityRazed(self, city, conqueror, owner):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		if self.getGoal(iElam, 0) is -1 and city.getX() is 46 and city.getY() is 19: #Ur captured by Elam
			if conqueror is iElam:
				self.setGoal(iElam, 0, 1)
			else:
				self.setGoal(iElam, 0, 0)


	def onTechAcquired(self, iTech, iPlayer):

		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()

		if (iPlayer == iSumeria):
			if (pSumeria.isAlive()):
				if (self.getGoal(iSumeria, 0) == -1): #eof error???
					if (iTech == con.tn('the_wheel')):
						self.setSumerianTechs(0, 1)
						for iCiv in range(iNumPlayers):
							if (iCiv != iSumeria):
								if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
									self.setSumerianTechs(0, 0)
					elif (iTech == con.tn('masonry')):
						self.setSumerianTechs(1, 1)
						for iCiv in range(iNumPlayers):
							if (iCiv != iSumeria):
								if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
									self.setSumerianTechs(1, 0)
					elif (iTech == con.tn('cunniform')):
						self.setSumerianTechs(2, 1)
						for iCiv in range(iNumPlayers):
							if (iCiv != iSumeria):
								if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
									self.setSumerianTechs(2, 0)
					if (self.getSumerianTechs(0) == 1 and self.getSumerianTechs(1) == 1 and self.getSumerianTechs(2) == 1):
						self.setGoal(iSumeria, 0, 1)
					elif (self.getSumerianTechs(0) == 0 or self.getSumerianTechs(1) == 0 or self.getSumerianTechs(2) == 0):
						self.setGoal(iSumeria, 0, 0)
		elif iPlayer is iBabylonia:
			if pBabylonia.isAlive():
				if self.getGoal(iBabylonia, 1) is -1:
					if iTech is con.tn('code_of_laws'):
						self.setGoal(iBabylonia, 1, 1)
						for iCiv in range(iNumPlayers):
							if iCiv is not iBabylonia:
								if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech):
									self.setGoal(iBabylonia, 1, 0)
									break

	def onBuildingBuilt(self, iPlayer, iBuilding):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()

	def onProjectBuilt(self, iPlayer, iProject):

		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()

	def onCombatResult(self, argsList):

		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		pWinningUnit,pLosingUnit = argsList
		pWinningPlayer = gc.getPlayer(pWinningUnit.getOwner())
		pLosingPlayer = gc.getPlayer(pLosingUnit.getOwner())
		cLosingUnit = PyHelpers.PyInfo.UnitInfo(pLosingUnit.getUnitType())
		iPlayer = pWinningPlayer.getID()

	def calculateTopCityCulture(self, x, y):
		iBestCityValue = 0
		pCurrent = gc.getMap().plot(x, y)
		if (pCurrent.isCity()):
			bestCity = pCurrent.getPlotCity()
			for iPlayerLoop in range(gc.getMAX_PLAYERS()):
				apCityList = PyPlayer(iPlayerLoop).getCityList()

				for pCity in apCityList:
					iTotalCityValue = pCity.GetCy().countTotalCultureTimes100()
					#iTotalCityValue = (pCity.getCulture() / 5) + (pCity.getFoodRate() + pCity.getProductionRate() \
					#	+ pCity.calculateGoldRate())) * pCity.getPopulation()
					if (iTotalCityValue > iBestCityValue and not pCity.isBarbarian()):
						bestCity = pCity
						iBestCityValue = iTotalCityValue
			return bestCity
		return -1

	def calculateTopCityPopulation(self, x, y):
		iBestCityValue = 0
		pCurrent = gc.getMap().plot(x, y)
		if (pCurrent.isCity()):
			bestCity = pCurrent.getPlotCity()
			for iPlayerLoop in range(gc.getMAX_PLAYERS()):
				apCityList = PyPlayer(iPlayerLoop).getCityList()

				for pCity in apCityList:
					iTotalCityValue = pCity.getPopulation()
					if (iTotalCityValue > iBestCityValue and not pCity.isBarbarian()):
						bestCity = pCity
						iBestCityValue = iTotalCityValue
			return bestCity
		return -1
