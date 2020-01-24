# Rhye's and Fall of Civilization - Main Scenario

from CvPythonExtensions import *
import CvUtil
import PyHelpers	# LOQ
import Popup
import cPickle as pickle
import CvTranslator
import RFCUtils
import Consts as con



################
### Globals ###
##############

gc = CyGlobalContext()	# LOQ
PyPlayer = PyHelpers.PyPlayer	# LOQ
utils = RFCUtils.RFCUtils()

iCheatersPeriod = 12
iBetrayalPeriod = 8
iBetrayalThreshold = 80
iRebellionDelay = 15
iEscapePeriod = 30
tAIStopBirthThreshold = con.tAIStopBirthThreshold
tBirth = con.tBirth

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


#for not allowing new civ popup if too close
tDifference = (0, 0, 0, 0, 0, 3, 2, 2, 1, 1, 1, 0, 8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 3, 2, 1, 0, 0, 0)
									    #ma po in mo az tu am

		


# starting locations coordinates
tCapitals = con.tCapitals



# core areas coordinates (top left and bottom right)

tCoreAreasTL = con.tCoreAreasTL
tCoreAreasBR = con.tCoreAreasBR

tExceptions = con.tExceptions

tNormalAreasTL = con.tNormalAreasTL
tNormalAreasBR = con.tNormalAreasBR

tBroaderAreasTL = con.tBroaderAreasTL
tBroaderAreasBR = con.tBroaderAreasBR

class RiseAndFall:


##################################################
### Secure storage & retrieval of script data ###
################################################


	def getNewCiv(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iNewCiv']

	def setNewCiv(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iNewCiv'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getNewCivFlip(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iNewCivFlip']

	def setNewCivFlip(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iNewCivFlip'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getOldCivFlip(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iOldCivFlip']

	def setOldCivFlip(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iOldCivFlip'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getTempTopLeft(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['tempTopLeft']

	def setTempTopLeft(self, tNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['tempTopLeft'] = tNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getTempBottomRight(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['tempBottomRight']

	def setTempBottomRight(self, tNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['tempBottomRight'] = tNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getSpawnWar(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iSpawnWar']

	def setSpawnWar(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iSpawnWar'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getAlreadySwitched(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['bAlreadySwitched']

	def setAlreadySwitched(self, bNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['bAlreadySwitched'] = bNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getColonistsAlreadyGiven(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lColonistsAlreadyGiven'][iCiv]

	def setColonistsAlreadyGiven(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lColonistsAlreadyGiven'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getAstronomyTurn(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lAstronomyTurn'][iCiv]

	def setAstronomyTurn(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lAstronomyTurn'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getNumCities(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lNumCities'][iCiv]

	def setNumCities(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lNumCities'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getSpawnDelay(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lSpawnDelay'][iCiv]

	def setSpawnDelay(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lSpawnDelay'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getFlipsDelay(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lFlipsDelay'][iCiv]

	def setFlipsDelay(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lFlipsDelay'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getBetrayalTurns(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iBetrayalTurns']

	def setBetrayalTurns(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iBetrayalTurns'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getLatestFlipTurn(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iLatestFlipTurn']

	def setLatestFlipTurn(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iLatestFlipTurn'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getLatestRebellionTurn(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lLatestRebellionTurn'][iCiv]

	def setLatestRebellionTurn(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lLatestRebellionTurn'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getRebelCiv(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iRebelCiv']

	def setRebelCiv(self, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['iRebelCiv'] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getExileData(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lExileData'][i]

	def setExileData(self, i, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lExileData'][i] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getTempFlippingCity(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['tempFlippingCity']

	def setTempFlippingCity(self, tNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['tempFlippingCity'] = tNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getCheatersCheck(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lCheatersCheck'][i]

	def setCheatersCheck(self, i, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lCheatersCheck'][i] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getBirthTurnModifier(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lBirthTurnModifier'][iCiv]

	def setBirthTurnModifier(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lBirthTurnModifier'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getDeleteMode(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lDeleteMode'][i]

	def setDeleteMode(self, i, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lDeleteMode'][i] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getFirstContactConquerors(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lFirstContactConquerors'][iCiv]

	def setFirstContactConquerors(self, iCiv, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lFirstContactConquerors'][iCiv] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))


	def getCheatMode(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['bCheatMode']

	def setCheatMode(self, bNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['bCheatMode'] = bNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

###############
### Popups ###
#############

	''' popupID has to be a registered ID in CvRhyesCatapultEventManager.__init__!! '''
	def showPopup(self, popupID, title, message, labels):
		popup = Popup.PyPopup(popupID, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setHeaderString(title)
		popup.setBodyString(message)
		for i in labels:
		    popup.addButton(i)
		popup.launch(False)


	def newCivPopup(self, iCiv):
		self.showPopup(7614, CyTranslator().getText("TXT_KEY_NEWCIV_TITLE", ()), CyTranslator().getText("TXT_KEY_NEWCIV_MESSAGE", (gc.getPlayer(iCiv).getCivilizationAdjectiveKey(),)), (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), CyTranslator().getText("TXT_KEY_POPUP_NO", ())))
		self.setNewCiv(iCiv)

	def eventApply7614(self, popupReturn):
		if(popupReturn.getButtonClicked() == 0): # 1st button
			iOldHandicap = gc.getActivePlayer().getHandicapType()
			gc.getActivePlayer().setHandicapType(gc.getPlayer(self.getNewCiv()).getHandicapType())
			gc.getGame().setActivePlayer(self.getNewCiv(), False)
			gc.getPlayer(self.getNewCiv()).setHandicapType(iOldHandicap)
			for i in range(con.iNumStabilityParameters):
				utils.setStabilityParameters(i, 0)
			utils.setLastRecordedStabilityStuff(0, 0)
			utils.setLastRecordedStabilityStuff(1, 0)
			utils.setLastRecordedStabilityStuff(2, 0)
			utils.setLastRecordedStabilityStuff(3, 0)
			utils.setLastRecordedStabilityStuff(4, 0)
			utils.setLastRecordedStabilityStuff(5, 0)
			for iMaster in range(con.iNumPlayers):
				if (gc.getTeam(gc.getPlayer(self.getNewCiv()).getTeam()).isVassal(iMaster)):
					gc.getTeam(gc.getPlayer(self.getNewCiv()).getTeam()).setVassal(iMaster, False, False)
			self.setAlreadySwitched(True)
			gc.getPlayer(self.getNewCiv()).setPlayable(True)
			#CyInterface().addImmediateMessage("first button", "")
		#elif(popupReturn.getButtonClicked() == 1): # 2nd button
			#CyInterface().addImmediateMessage("second button", "")


	def flipPopup(self, iNewCiv, tTopLeft, tBottomRight):
		iHuman = utils.getHumanID()
		flipText = CyTranslator().getText("TXT_KEY_FLIPMESSAGE1", ())
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				pCurrent = gc.getMap().plot(x, y)
				if (pCurrent.isCity()):
					if (pCurrent.getPlotCity().getOwner() == iHuman):
						#if (not pCurrent.getPlotCity().isCapital()): #exploitable
						if (not (x == tCapitals[iHuman] and y == tCapitals[iHuman]) and not (self.getCheatMode() == True and pCurrent.getPlotCity().isCapital())):
							flipText += (pCurrent.getPlotCity().getName() + "\n")
		#exceptions
		if (len(tExceptions[iNewCiv])):
			for j in range(len(tExceptions[iNewCiv])):
				pCurrent = gc.getMap().plot(tExceptions[iNewCiv][j][0], tExceptions[iNewCiv][j][1])
				if (pCurrent.isCity()):
					if (pCurrent.getPlotCity().getOwner() == iHuman):
						if (not pCurrent.getPlotCity().isCapital()):
							flipText += (pCurrent.getPlotCity().getName() + "\n")
		flipText += CyTranslator().getText("TXT_KEY_FLIPMESSAGE2", ())

		self.showPopup(7615, CyTranslator().getText("TXT_KEY_NEWCIV_TITLE", ()), flipText, (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), CyTranslator().getText("TXT_KEY_POPUP_NO", ())))
		self.setNewCivFlip(iNewCiv)
		self.setOldCivFlip(iHuman)
		self.setTempTopLeft(tTopLeft)
		self.setTempBottomRight(tBottomRight)

	def eventApply7615(self, popupReturn):
		iHuman = utils.getHumanID()
		tTopLeft = self.getTempTopLeft()
		tBottomRight = self.getTempBottomRight()
		iNewCivFlip = self.getNewCivFlip()

		humanCityList = []
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				pCurrent = gc.getMap().plot(x, y)
				if (pCurrent.isCity()):
					city = pCurrent.getPlotCity()
					if (city.getOwner() == iHuman):
						#if (not city.isCapital()): #exploitable
						if (not (x == tCapitals[iHuman] and y == tCapitals[iHuman]) and not (self.getCheatMode() == True and pCurrent.getPlotCity().isCapital())):
							humanCityList.append(city)
		#exceptions
		if (len(tExceptions[iNewCivFlip])):
			for j in range(len(tExceptions[self.getNewCivFlip()])):
				pCurrent = gc.getMap().plot(tExceptions[iNewCivFlip][j][0], tExceptions[iNewCivFlip][j][1])
				if (pCurrent.isCity()):
					city = pCurrent.getPlotCity()
					if (city.getOwner() == iHuman):
						if (not city.isCapital()):
							humanCityList.append(city)

		if(popupReturn.getButtonClicked() == 0): # 1st button
			print ("Flip agreed")
			CyInterface().addMessage(iHuman, True, con.iDuration, CyTranslator().getText("TXT_KEY_FLIP_AGREED", ()), "", 0, "", ColorTypes(con.iGreen), -1, -1, True, True)

			if (len(humanCityList)):
				for i in range(len(humanCityList)):
					city = humanCityList[i]
					print ("flipping ", city.getName())
					utils.cultureManager((city.getX(),city.getY()), 100, iNewCivFlip, iHuman, False, False, False)
					utils.flipUnitsInCityBefore((city.getX(),city.getY()), iNewCivFlip, iHuman)
					self.setTempFlippingCity((city.getX(),city.getY()))
					utils.flipCity((city.getX(), city.getY()), 0, 0, iNewCivFlip, [iHuman])
					utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCivFlip)

					#iEra = gc.getPlayer(iNewCivFlip).getCurrentEra()
					#if (iEra >= 2): #medieval
					#	if (city.getPopulation() < iEra):
					#		city.setPopulation(iEra) #causes an unidentifiable C++ exception

					#humanCityList[i].setHasRealBuilding(con.iPlague, False) #buggy

			#same code as Betrayal - done just once to make sure human player doesn't hold a stack just outside of the cities
			for x in range(tTopLeft[0], tBottomRight[0]+1):
				for y in range(tTopLeft[1], tBottomRight[1]+1):
					betrayalPlot = gc.getMap().plot(x,y)
					iNumUnitsInAPlot = betrayalPlot.getNumUnits()
					if (iNumUnitsInAPlot):								
						for i in range(iNumUnitsInAPlot):
							unit = betrayalPlot.getUnit(i)
							if (unit.getOwner() == iHuman):
								rndNum = gc.getGame().getSorenRandNum(100, 'betrayal')
								if (rndNum >= iBetrayalThreshold):
									if (unit.getDomainType() == 2): #land unit
										iUnitType = unit.getUnitType()
										unit.kill(False, iNewCivFlip)
										utils.makeUnit(iUnitType, iNewCivFlip, (x,y), 1)
										i = i - 1


			if (self.getCheatersCheck(0) == 0):
				self.setCheatersCheck(0, iCheatersPeriod)
				self.setCheatersCheck(1, self.getNewCivFlip())

		elif(popupReturn.getButtonClicked() == 1): # 2nd button
			print ("Flip disagreed")
			CyInterface().addMessage(iHuman, True, con.iDuration, CyTranslator().getText("TXT_KEY_FLIP_REFUSED", ()), "", 0, "", ColorTypes(con.iGreen), -1, -1, True, True)


			if (len(humanCityList)):
				for i in range(len(humanCityList)):
					city = humanCityList[i]
					#city.setCulture(self.getNewCivFlip(), city.countTotalCulture(), True)
					pCurrent = gc.getMap().plot(city.getX(), city.getY())
					oldCulture = pCurrent.getCulture(iHuman)
					pCurrent.setCulture(iNewCivFlip, oldCulture/2, True)
					pCurrent.setCulture(iHuman, oldCulture/2, True)
					iWar = self.getSpawnWar() + 1
					self.setSpawnWar(iWar)
					if (self.getSpawnWar() == 1):
						#CyInterface().addImmediateMessage(CyTranslator().getText("TXT_KEY_FLIP_REFUSED", ()), "")
						gc.getTeam(gc.getPlayer(iNewCivFlip).getTeam()).declareWar(iHuman, False, -1) ##True??
						self.setBetrayalTurns(iBetrayalPeriod)
						self.initBetrayal()





	def rebellionPopup(self, iRebelCiv):
		self.showPopup(7622, CyTranslator().getText("TXT_KEY_REBELLION_TITLE", ()), \
			       CyTranslator().getText("TXT_KEY_REBELLION_TEXT", (gc.getPlayer(iRebelCiv).getCivilizationAdjectiveKey(),)), \
			       (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), \
				CyTranslator().getText("TXT_KEY_POPUP_NO", ())))


	def eventApply7622(self, popupReturn):
		iHuman = utils.getHumanID()
		iRebelCiv = self.getRebelCiv()
		if(popupReturn.getButtonClicked() == 0): # 1st button
			gc.getTeam(gc.getPlayer(iHuman).getTeam()).makePeace(iRebelCiv)						
		elif(popupReturn.getButtonClicked() == 1): # 2nd button
			gc.getTeam(gc.getPlayer(iHuman).getTeam()).declareWar(iRebelCiv, False, -1)



#######################################
### Main methods (Event-Triggered) ###
#####################################

	def setup(self):
		#self.setupBirthTurnModifiers() (causes a crash on civ switch)
		iHuman = utils.getHumanID()
		if utils.getScenario() == con.i4400BCScenario:
		    self.create4400BCstartingUnits()
		else:
		    self.create900BCstartingUnits()
		#self.setEarlyLeaders()

		# set starting gold

		# display welcome message
		#self.displayWelcomePopup()

		#center camera on Egyptian units
		if (pEgypt.isHuman()):
			plotEgypt = gc.getMap().plot(tCapitals[iEgypt][0], tCapitals[iEgypt][1])
			unit = plotEgypt.getUnit(0)
			unit.centerCamera()
			#print (unit)

	def setupBirthTurnModifiers(self):
		for iCiv in range(iNumPlayers):
			if (iCiv >= iIndusValley and not gc.getPlayer(iCiv).isHuman()):
				self.setBirthTurnModifier(iCiv, (gc.getGame().getSorenRandNum(11, 'BirthTurnModifier') - 5)) # -5 to +5
		#now make sure that no civs spawn in the same turn and cause a double "new civ" popup
		for iCiv in range(iNumPlayers):
			if (iCiv > utils.getHumanID() and iCiv < iHuns):
				for j in range(iNumPlayers-1-iCiv):
					iNextCiv = iCiv+j+1
					if (con.tBirth[iCiv]+self.getBirthTurnModifier(iCiv) == con.tBirth[iNextCiv]+self.getBirthTurnModifier(iNextCiv)):
						self.setBirthTurnModifier(iNextCiv, (self.getBirthTurnModifier(iNextCiv)+1))

	def checkTurn(self, iGameTurn):
		print 'RiseAndFall.checkTurn()'
		#debug

		#Trigger betrayal mode
		if (self.getBetrayalTurns() > 0):
			self.initBetrayal()

		if (self.getCheatersCheck(0) > 0):
			teamPlayer = gc.getTeam(gc.getPlayer(utils.getHumanID()).getTeam())
			if (teamPlayer.isAtWar(self.getCheatersCheck(1))):
				print ("No cheaters!")
				self.initMinorBetrayal(self.getCheatersCheck(1))
				self.setCheatersCheck(0, 0)
				self.setCheatersCheck(1, -1)
			else:
				self.setCheatersCheck(0, self.getCheatersCheck(0)-1)

		if (iGameTurn % 20 == 0):
			if (pIndependent.isAlive()):				
				utils.updateMinorTechs(iIndependent, iBarbarian)
			if (pIndependent2.isAlive()):				
				utils.updateMinorTechs(iIndependent2, iBarbarian)

		#Colonists
		if (iGameTurn == con.i850BC):
			self.giveEarlyColonists(iPhoenicia)
		if (iGameTurn == con.i450BC):
			self.giveEarlyColonists(iCarthage)

		#birth of civs
		for iLoopCiv in range(iNumMajorPlayers):
			if (tBirth[iLoopCiv] > 0):
				if (iGameTurn >= con.tBirth[iLoopCiv] - 2 and iGameTurn <= con.tBirth[iLoopCiv] + 6):
					self.initBirth(iGameTurn, tBirth[iLoopCiv], iLoopCiv)
				if (con.getFeedUnits(iLoopCiv) > 0):
					if (iGameTurn >= con.tBirth[iLoopCiv] and iGameTurn <= con.tBirth[iLoopCiv]+50):
						if ((iGameTurn-con.tBirth[iLoopCiv])%5 == 4):
							self.spawnUnits(iLoopCiv, tCoreAreasTL[iLoopCiv], tCoreAreasBR[iLoopCiv], con.getFeedUnits(iLoopCiv), 3, utils.outerInvasion, 1)

		#flip Mesopotamia
		#if (iGameTurn == 1):
		#	self.convertSurroundingCities(iBabylonia, tBroaderAreasTL[iBabylonia], tBroaderAreasBR[iBabylonia])

		#RFGW

		#fragment utility
		if (iGameTurn >= con.i450BC and iGameTurn % 15 == 6):
			self.fragmentIndependents()
#		if (iGameTurn >= con.i450AD and iGameTurn % 30 == 12):
#			self.fragmentBarbarians(iGameTurn)

		#fall of civs
		if (iGameTurn >= con.i1500BC and iGameTurn % 4 == 0):
			self.collapseByBarbs(iGameTurn)
		if (iGameTurn >= con.i1800BC and iGameTurn % 18 == 0): #used to be 15 in vanilla, because we must give some time for vassal states to form
			self.collapseGeneric(iGameTurn)

		if (iGameTurn >= con.i1800BC and iGameTurn % 13 == 7): #used to be 8 in vanilla, because we must give some time for vassal states to form
			self.collapseMotherland(iGameTurn)
		if (iGameTurn > con.i450BC and iGameTurn % 10 == 6):
			self.secession(iGameTurn)
		#debug
		#self.collapseMotherland()

		#resurrection of civs
		iNumDeadCivs1 = 11 #5 in vanilla, 8 in warlords (that includes native and celt)
		iNumDeadCivs2 = 9 #3 in vanilla, 6 in Warlords: here we must count natives and celts as dead too
		#if (not gc.getPlayer(0).isPlayable()):  #late start condition
		#	iNumDeadCivs1 -= 2
		#	iNumDeadCivs2 -= 2
		if (gc.getGame().countCivPlayersEverAlive() - gc.getGame().countCivPlayersAlive() > iNumDeadCivs1):
			if (iGameTurn % 15 == 10): #in Warlords 14, in vanilla 13
				self.resurrection(iGameTurn)
		elif (gc.getGame().countCivPlayersEverAlive() - gc.getGame().countCivPlayersAlive() > iNumDeadCivs2):
			if (iGameTurn % 30 == 15): #in Warlords 25, in vanilla 20
				self.resurrection(iGameTurn)



		#debug
		#self.resurrection(iGameTurn)	
		#self.resurrectionFromBarbs(iGameTurn)

	def checkPlayerTurn(self, iGameTurn, iPlayer):
		return None

	def switchLateLeaders(self, iPlayer, iLeaderIndex):
		if (tLateLeaders[iPlayer][iLeaderIndex] != gc.getPlayer(iPlayer).getLeader()):
			iThreshold = tLateLeaders[iPlayer][iLeaderIndex+2]
			if (gc.getPlayer(iPlayer).getCurrentEra() >= tLateLeaders[iPlayer][iLeaderIndex+3]):
				iThreshold *= 2
			if (gc.getPlayer(iPlayer).getAnarchyTurns() != 0 or \
			    utils.getPlagueCountdown(iPlayer) > 0 or \
			    utils.getStability(iPlayer) <= -10 or \
			    gc.getGame().getSorenRandNum(100, 'die roll') < iThreshold):
				gc.getPlayer(iPlayer).setLeader(tLateLeaders[iPlayer][iLeaderIndex])
				print ("leader late switch:", tLateLeaders[iPlayer][iLeaderIndex], "in civ", iPlayer)
	

	def fragmentIndependents(self):
		if (pIndependent.getNumCities() > 8 or pIndependent2.getNumCities() > 8):
			iBigIndependent = -1
			iSmallIndependent = -1
			if (pIndependent.getNumCities() > 2*pIndependent2.getNumCities()):
				iBigIndependent = iIndependent
				iSmallIndependent = iIndependent2
			if (2*pIndependent.getNumCities() < 2*pIndependent2.getNumCities()):
				iBigIndependent = iIndependent2
				iSmallIndependent = iIndependent
			if (iBigIndependent != -1):
				iDivideCounter = 0
				iCounter = 0
				cityList = []
				apCityList = PyPlayer(iBigIndependent).getCityList()
				for pCity in apCityList:
					iDivideCounter += 1 #convert 3 random cities cycling just once
					if (iDivideCounter % 2 == 1):
						city = pCity.GetCy()
						pCurrent = gc.getMap().plot(city.getX(), city.getY())
						utils.cultureManager((city.getX(),city.getY()), 50, iSmallIndependent, iBigIndependent, False, True, True)
						utils.flipUnitsInCityBefore((city.getX(),city.getY()), iSmallIndependent, iBigIndependent)			
						self.setTempFlippingCity((city.getX(),city.getY()))
						utils.flipCity((city.getX(),city.getY()), 0, 0, iSmallIndependent, [iBigIndependent])   #by trade because by conquest may raze the city
						utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iSmallIndependent)
						iCounter += 1
						if (iCounter == 3):
							return

	def fragmentBarbarians(self, iGameTurn):
		iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
		for j in range(iRndnum, iRndnum + iNumPlayers):
			iDeadCiv = j % iNumPlayers
			if (not gc.getPlayer(iDeadCiv).isAlive() and iGameTurn > con.tBirth[iDeadCiv] + 50):
				pDeadCiv = gc.getPlayer(iDeadCiv)
				teamDeadCiv = gc.getTeam(pDeadCiv.getTeam())
				iCityCounter = 0
				for x in range(tNormalAreasTL[iDeadCiv][0], tNormalAreasBR[iDeadCiv][0]+1):
					for y in range(tNormalAreasTL[iDeadCiv][1], tNormalAreasBR[iDeadCiv][1]+1):
						pCurrent = gc.getMap().plot(x, y)
						if (pCurrent.isCity()):
							if (pCurrent.getPlotCity().getOwner() == iBarbarian):
								iCityCounter += 1
				if (iCityCounter > 3):
					iDivideCounter = 0
					for x in range(tNormalAreasTL[iDeadCiv][0], tNormalAreasBR[iDeadCiv][0]+1):
						for y in range(tNormalAreasTL[iDeadCiv][1], tNormalAreasBR[iDeadCiv][1]+1):
							pCurrent = gc.getMap().plot(x, y)
							if (pCurrent.isCity()):
								city = pCurrent.getPlotCity()
								if (city.getOwner() == iBarbarian):
									if (iDivideCounter % 4 == 0):
										iNewCiv = iIndependent
									elif (iDivideCounter % 4 == 1):
										iNewCiv = iIndependent2
									if (iDivideCounter % 4 == 0 or iDivideCounter % 4 == 1):
										utils.cultureManager((city.getX(),city.getY()), 50, iNewCiv, iBarbarian, False, True, True)
										utils.flipUnitsInCityBefore((city.getX(),city.getY()), iNewCiv, iBarbarian)			
										self.setTempFlippingCity((city.getX(),city.getY()))
										utils.flipCity((city.getX(),city.getY()), 0, 0, iNewCiv, [iBarbarian])   #by trade because by conquest may raze the city
										utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCiv)
										iDivideCounter += 1
					return






##	def collapseCapitals(self, iOldOwner, city, iNewOwner):
##	#Persian UP inside
##	#AI tweaked in CvCity::getCulturePercentAnger()
##
##		bCapital = False
##		bPersia = False
##		iModifier = 0
##		for i in range(iNumPlayers):
##			if (city.getX() == tCapitals[i][0] and city.getY() == tCapitals[i][1]):
##				if (city.getOwner() == i): #otherwise it's no longer a capital
##					bCapital = True
##		if (iNewOwner == iPersia):
##			bPersia = True
##			if (not bCapital):
##				iModifier = 1
##		if (iNewOwner == self.getRebelCiv() and gc.getGame().getGameTurn() == self.getLatestRebellionTurn(self.getRebelCiv())):
##			return #don't mess up with resurrection()
##		#print ("iNewOwner", iNewOwner, con.tBirth[iNewOwner])
##		if (iNewOwner == iBarbarian):
##			return
##		if (iNewOwner != iBarbarian):
##			if (gc.getGame().getGameTurn() <= con.tBirth[iNewOwner] + 2):
##				return #don't mess up with birth (case of delay still a problem...)
##		if (bCapital or bPersia):
##			for x in range(city.getX() -3 +iModifier, city.getX() +4 -iModifier):
##				for y in range(city.getY() -3 +iModifier, city.getY() +4 -iModifier):
##					pCurrent = gc.getMap().plot(x, y)
##					if (pCurrent.isCity()):
##						cityNear = pCurrent.getPlotCity()
##						iOwnerNear = cityNear.getOwner()
##						#print ("iOwnerNear", iOwnerNear, "citynear", cityNear.getName())
##						if (iOwnerNear != iNewOwner and iOwnerNear == iOldOwner):
##							if (cityNear != city):
##								if (cityNear.getPopulation() <= city.getPopulation() and not cityNear.isCapital()):
##									if (bPersia == True and iModifier == 1): #Persian UP - any city, 2x2 area
##										if (cityNear.getPopulation() <= 8):
##											if (self.getLatestFlipTurn() != gc.getGame().getGameTurn()):									
##												utils.flipUnitsInCityBefore((x,y), iNewOwner, iOwnerNear)
##												self.setTempFlippingCity((x,y))
##												utils.flipCity((x,y), 0, 0, iNewOwner, [iOwnerNear])
##												utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewOwner)
##												self.setLatestFlipTurn(gc.getGame().getGameTurn())
##												utils.cultureManager(self.getTempFlippingCity(), 50, iOwnerNear, iNewOwner, False, False, False)
##									else:
##										utils.flipUnitsInCityBefore((x,y), iNewOwner, iOwnerNear)
##										self.setTempFlippingCity((x,y))
##										utils.flipCity((x,y), 0, 0, iNewOwner, [iOwnerNear])
##										utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewOwner)
##										utils.cultureManager(self.getTempFlippingCity(), 50, iOwnerNear, iNewOwner, False, False, False)
##										print ("COLLAPSE: CAPITALS", gc.getPlayer(iOwnerNear).getCivilizationShortDescription(0))

	def collapseByBarbs(self, iGameTurn):
		for iCiv in range(iNumPlayers):
			if (gc.getPlayer(iCiv).isHuman() == 0 and gc.getPlayer(iCiv).isAlive()):
				if (iGameTurn >= con.tBirth[iCiv] + 25):
					iNumCities = gc.getPlayer(iCiv).getNumCities()
					iLostCities = 0
					for x in range(0, 124):
						for y in range(0, 168):
							if (gc.getMap().plot(x,y).isCity()):
								city = gc.getMap().plot(x,y).getPlotCity()
								if (city.getOwner() == iBarbarian):
									if (city.getOriginalOwner() == iCiv):
										iLostCities = iLostCities + 1
					if (iLostCities*2 > iNumCities and iNumCities > 0): #if more than one third is captured, the civ collapses
						print ("COLLAPSE BY BARBS", gc.getPlayer(iCiv).getCivilizationAdjective(0))
						utils.pickFragmentation(iCiv, iIndependent, iIndependent2, iBarbarian, False)

	def collapseGeneric(self, iGameTurn):
		#lNumCitiesNew = con.l0Array
		lNumCitiesNew = con.l0ArrayTotal #for late start
		for iCiv in range(iNumTotalPlayers):
			if (iCiv < iNumActivePlayers or (iCiv == iCeltia and not gc.getPlayer(0).isPlayable())): #late start condition
				pCiv = gc.getPlayer(iCiv)
				teamCiv = gc.getTeam(pCiv.getTeam())
				if (pCiv.isAlive()):
					if (iGameTurn >= con.tBirth[iCiv] + 25):
						lNumCitiesNew[iCiv] = pCiv.getNumCities()
						if (lNumCitiesNew[iCiv]*2 <= self.getNumCities(iCiv)): #if number of cities is less than half than some turns ago, the civ collapses
							print ("COLLAPSE GENERIC", pCiv.getCivilizationAdjective(0), lNumCitiesNew[iCiv]*2, "<=", self.getNumCities(iCiv))
							if (gc.getPlayer(iCiv).isHuman() == 0):
								bVassal = False
								for iMaster in range(con.iNumPlayers):
									if (teamCiv.isVassal(iMaster)):
										bVassal = True
										break
								if (not bVassal):
									utils.pickFragmentation(iCiv, iIndependent, iIndependent2, -1, False)
						else:
							self.setNumCities(iCiv, lNumCitiesNew[iCiv])

	def collapseMotherland(self, iGameTurn):
		#collapses if completely out of broader areas
		for iCiv in range(iNumPlayers):
			pCiv = gc.getPlayer(iCiv)
			teamCiv = gc.getTeam(pCiv.getTeam())
			if (pCiv.isHuman() == 0 and pCiv.isAlive()):
				if (iGameTurn >= con.tBirth[iCiv] + 25):
					bSafe = False
					for x in range(tCoreAreasTL[iCiv][0], tCoreAreasBR[iCiv][0]+1):
						for y in range(tCoreAreasTL[iCiv][1], tCoreAreasBR[iCiv][1]+1):
							pCurrent = gc.getMap().plot(x, y)
							if (pCurrent.isCity()):
								#print (pCurrent.getPlotCity().getOwner(), pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getX(), pCurrent.getPlotCity().getY())
								if (pCurrent.getPlotCity().getOwner() == iCiv):
									#print ("iCiv", iCiv, "bSafe", bSafe)
									bSafe = True
									break
									break
					if (bSafe == False):
						iCitiesOwned = 0
						iCitiesLost = 0
						for x in range(tNormalAreasTL[iCiv][0], tNormalAreasBR[iCiv][0]+1):
							for y in range(tNormalAreasTL[iCiv][1], tNormalAreasBR[iCiv][1]+1):
								pCurrent = gc.getMap().plot(x, y)
								if (pCurrent.isCity()):
									#print (pCurrent.getPlotCity().getOwner(), pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getX(), pCurrent.getPlotCity().getY())
									if (pCurrent.getPlotCity().getOwner() == iCiv):
										iCitiesOwned += 1
									else:
										iCitiesLost += 1
						if (iCitiesOwned > iCitiesLost):
							bSafe = True
					#print ("iCiv", iCiv, "bSafe", bSafe)
					if (bSafe == False):
						bVassal = False
						for iMaster in range(con.iNumPlayers):
							if (teamCiv.isVassal(iMaster)):
								bVassal = True
								break
						if (not bVassal):
							print ("COLLAPSE: MOTHERLAND", gc.getPlayer(iCiv).getCivilizationAdjective(0))
							utils.pickFragmentation(iCiv, iIndependent, iIndependent2, -1, False)
						return



	def collapseHuman(self, iOldOwner, city, iNewOwner):
		bEnabled = False
		bCapital = False
		bGeneric = False

		if (gc.getTeam(gc.getPlayer(iNewOwner).getTeam()).isHasTech(con.tn('code_of_laws'))):
			bEnabled = True
				
		iHuman = utils.getHumanID()
		if (city.getX() == tCapitals[iHuman][0] and city.getY() == tCapitals[iHuman][1]):
			bCapital = True

		print ("bEnabled:", bEnabled, "bCapital:", bCapital, "bGeneric:", bGeneric)

		#debug
		#iNumCitiesNew = gc.getPlayer(iHuman).getNumCities()
		#if (iNumCitiesNew*2 <= self.getNumCities(iHuman)):
		#	print ("HumanCollapseGeneric", iNumCitiesNew*2, "<=", self.getNumCities(iHuman))
		#	bGeneric = True

		#debug
		#bEnabled = True
		#bCapital = True

		if ((bCapital or bGeneric) and bEnabled):
			self.exile(iNewOwner)

	def exile(self, iWinner):
		iHuman = utils.getHumanID()
		pWinner = gc.getPlayer(iWinner)
		teamWinner = gc.getTeam(pWinner.getTeam())
		iDestination = -1
		iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'start index')
		for i in range(iRndnum, iNumPlayers + iRndnum):
			iCiv = i % iNumPlayers
			if (gc.getPlayer(iCiv).isAlive() and iCiv != iWinner):
				if (pWinner.canContact(iCiv)):
					if (not teamWinner.isAtWar(iCiv)):
						if (gc.getGame().getPlayerRank(iCiv) > gc.getGame().getPlayerRank(iHuman) + 1):
							iDestination = iCiv
							break					

		print (iDestination)
		popup = Popup.PyPopup()
		popup.setHeaderString(CyTranslator().getText("TXT_KEY_EXILE_TITLE", ()))	
		popup.setBodyString(CyTranslator().getText("TXT_KEY_EXILE_TEXT", (gc.getPlayer(iWinner).getCivilizationAdjectiveKey(), gc.getPlayer(iDestination).getCivilizationShortDescription(0))))
		popup.launch()
		self.setExileData(0, tCapitals[iHuman][0])
		self.setExileData(1, tCapitals[iHuman][1])
		self.setExileData(2, gc.getGame().getGameTurn())
		self.setExileData(3, iHuman)
		self.setExileData(4, iWinner)

		for iMaster in range(con.iNumPlayers):
			if (gc.getTeam(gc.getPlayer(iDestination).getTeam()).isVassal(iMaster)):
				gc.getTeam(gc.getPlayer(iDestination).getTeam()).setVassal(iMaster, False, False)

		iTempHumanLeader = gc.getPlayer(iHuman).getLeader()
		iTempDestinationLeader = gc.getPlayer(iDestination).getLeader()
		gc.getPlayer(iDestination).setLeader(iTempHumanLeader)
		gc.getGame().setActivePlayer(iDestination, False)
		gc.getPlayer(iHuman).setLeader(iTempDestinationLeader)
		teamWinner.makePeace(iHuman) #now managed by AI
		iTempLeader = gc.getPlayer(iHuman)

	def escape(self, city):
		if (gc.getGame().getGameTurn() <= self.getExileData(2) + iEscapePeriod):
			iOldHuman = self.getExileData(3)
			if (gc.getPlayer(iOldHuman).isAlive()):
				iHuman = utils.getHumanID()
				utils.flipCity((city.getX(),city.getY()), 0, 0, iOldHuman, [iHuman])
				popup = Popup.PyPopup()
				popup.setHeaderString(CyTranslator().getText("TXT_KEY_ESCAPE_TITLE", ()))	
				popup.setBodyString(CyTranslator().getText("TXT_KEY_ESCAPE_TEXT", (gc.getPlayer(iOldHuman).getCivilizationAdjectiveKey(),)))
				popup.launch()

				for iMaster in range(con.iNumPlayers):
					if (gc.getTeam(gc.getPlayer(iOldHuman).getTeam()).isVassal(iMaster)):
						gc.getTeam(gc.getPlayer(iOldHuman).getTeam()).setVassal(iMaster, False, False)

				iTempHumanLeader = gc.getPlayer(iHuman).getLeader()
				iTempOldHumanLeader = gc.getPlayer(iOldHuman).getLeader()
				gc.getPlayer(iOldHuman).setLeader(iTempHumanLeader)
				gc.getGame().setActivePlayer(iOldHuman, False)
				gc.getPlayer(iHuman).setLeader(iTempOldHumanLeader)
				city.setHasRealBuilding((0), True) #0 == palace
				teamWinner = gc.getTeam(gc.getPlayer(self.getExileData(4)).getTeam())
				teamWinner.declareWar(iOldHuman, True, -1)
				teamWinner.makePeace(iHuman) #now managed by AI
				self.setExileData(0, -1)
				self.setExileData(1, -1)
				self.setExileData(2, -1)
				self.setExileData(3, -1)
				self.setExileData(4, -1)

	def secession(self, iGameTurn):
		iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
		for j in range(iRndnum, iRndnum + iNumPlayers):
			iPlayer = j % iNumPlayers
			if (gc.getPlayer(iPlayer).isAlive() and iGameTurn >= con.tBirth[iPlayer] + 30):
				if (utils.getStability(iPlayer) >= -400 and utils.getStability(iPlayer) < -20): #secession (-400 for any very low value, instead of -40)

					cityList = []
					apCityList = PyPlayer(iPlayer).getCityList()
					for pCity in apCityList:
						city = pCity.GetCy()
						pCurrent = gc.getMap().plot(city.getX(), city.getY())

						if ((not city.isWeLoveTheKingDay()) and (not city.isCapital()) and (not (city.getX() == tCapitals[iPlayer][0] and city.getY() == tCapitals[iPlayer][1]))):
							if (gc.getPlayer(iPlayer).getNumCities() > 0): #this check is needed, otherwise game crashes
								capital = gc.getPlayer(iPlayer).getCapitalCity()
								iDistance = utils.calculateDistance(city.getX(), city.getY(), capital.getX(), capital.getY())
								if (iDistance > 3):											
							
									if (city.angryPopulation(0) > 0 or \
									    city.healthRate(False, 0) < 0 or \
									    city.getReligionBadHappiness() > 0 or \
									    city.getLargestCityHappiness() < 0 or \
									    city.getHurryAngerModifier() > 0 or \
									    city.getNoMilitaryPercentAnger() > 0 or \
									    city.getWarWearinessPercentAnger() > 0):
										cityList.append(city)
										continue

									for iLoop in range(iNumTotalPlayers+1):
										if (iLoop != iPlayer):
											if (pCurrent.getCulture(iLoop) > 0):
												cityList.append(city)
												break

					if (len(cityList)):
						iNewCiv = iIndependent
						iRndNum = gc.getGame().getSorenRandNum(2, 'random independent')
						if (iRndNum % 2 == 0):
							iNewCiv = iIndependent2
						if (iPlayer == con.iGermania or \
						    iPlayer == con.iHuns):
							if (iRndNum % 2 == 0):
								iNewCiv = iBarbarian
						splittingCity = cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
						utils.cultureManager((splittingCity.getX(),splittingCity.getY()), 50, iNewCiv, iPlayer, False, True, True)
						utils.flipUnitsInCityBefore((splittingCity.getX(),splittingCity.getY()), iNewCiv, iPlayer)			
						self.setTempFlippingCity((splittingCity.getX(),splittingCity.getY()))
						utils.flipCity((splittingCity.getX(),splittingCity.getY()), 0, 0, iNewCiv, [iPlayer])   #by trade because by conquest may raze the city
						utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCiv)
						if (iPlayer == utils.getHumanID()):
							CyInterface().addMessage(iPlayer, True, con.iDuration, splittingCity.getName() + " " + \
											   CyTranslator().getText("TXT_KEY_STABILITY_SECESSION", ()), "", 0, "", ColorTypes(con.iOrange), -1, -1, True, True)
						#print ("SECESSION", gc.getPlayer(iPlayer).getCivilizationAdjective(0), splittingCity.getName()) #causes c++ exception??
						utils.setStability(iPlayer, utils.getStability(iPlayer) + 2) #to counterbalance the stability hit on city acquired event, leading to a chain reaction
					return #just 1 secession per turn


	def resurrection(self, iGameTurn):
		iMinNumCities = 2
		bEnabled = False #TODO: revise resurrections
		if (bEnabled):
			iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
			cityList = []
			bDeadCivFound = False
			for j in range(iRndnum, iRndnum + iNumPlayers):
				iDeadCiv = j % iNumPlayers
				#iDeadCiv = iIndia #DEBUG
				cityList = []
				if (not gc.getPlayer(iDeadCiv).isAlive() and iGameTurn > con.tBirth[iDeadCiv] + 50 and iGameTurn > utils.getLastTurnAlive(iDeadCiv) + 20):
				#if (not gc.getPlayer(iDeadCiv).isAlive() and iGameTurn > con.tBirth[iDeadCiv] + 50): #DEBUG
					if (gc.getGame().getSorenRandNum(100, 'roll') >= con.tResurrectionProb[iDeadCiv]):
						#print("skip")
						continue
					pDeadCiv = gc.getPlayer(iDeadCiv)
					teamDeadCiv = gc.getTeam(pDeadCiv.getTeam())
					tTopLeft = tNormalAreasTL[iDeadCiv]
					tBottomRight = tNormalAreasBR[iDeadCiv]
					#if (self.getLatestRebellionTurn(iDeadCiv) > 0):
					#	tTopLeft = tNormalAreasTL[iDeadCiv]
					#	tBottomRight = tNormalAreasBR[iDeadCiv]
					#else:
					#	tTopLeft = tCoreAreasTL[iDeadCiv]
					#	tBottomRight = tCoreAreasBR[iDeadCiv]
					for x in range(tTopLeft[0], tBottomRight[0]+1):
						for y in range(tTopLeft[1], tBottomRight[1]+1):
							if ((x,y) not in con.tNormalAreasSubtract[iDeadCiv]):
								pCurrent = gc.getMap().plot(x, y)
								#print("plot",x,y)
								if (pCurrent.isCity()):
									city = pCurrent.getPlotCity()
									iOwner = city.getOwner()
									if (iOwner >= iNumActivePlayers): #if (iOwner == iBarbarian or iOwner == iIndependent or iOwner == iIndependent2): #remove in vanilla
										cityList.append(pCurrent.getPlotCity())
										#print (iDeadCiv, pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getOwner(), "1", cityList)
									else:
										iMinNumCitiesOwner = 3
										iOwnerStability = utils.getStability(iOwner)
										if (not gc.getPlayer(iOwner).isHuman()):
											iMinNumCitiesOwner = 2
											iOwnerStability -= 20
										if (gc.getPlayer(iOwner).getNumCities() >= iMinNumCitiesOwner):
											if (iOwnerStability < -20):
												if (not city.isWeLoveTheKingDay() and not city.isCapital()):
													    cityList.append(pCurrent.getPlotCity())
													    #print (iDeadCiv, pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getOwner(), "2", cityList)
											elif (iOwnerStability < 0):
												if (not city.isWeLoveTheKingDay() and not city.isCapital() and (not (city.getX() == tCapitals[iOwner][0] and city.getY() == tCapitals[iOwner][1]))):
													if (gc.getPlayer(iOwner).getNumCities() > 0): #this check is needed, otherwise game crashes
														capital = gc.getPlayer(iOwner).getCapitalCity()
														iDistance = utils.calculateDistance(x, y, capital.getX(), capital.getY())
														if ((iDistance >= 6 and gc.getPlayer(iOwner).getNumCities() >= 4) or \
														    city.angryPopulation(0) > 0 or \
														    city.healthRate(False, 0) < 0 or \
														    city.getReligionBadHappiness() > 0 or \
														    city.getLargestCityHappiness() < 0 or \
														    city.getHurryAngerModifier() > 0 or \
														    city.getNoMilitaryPercentAnger() > 0 or \
														    city.getWarWearinessPercentAnger() > 0):
															    cityList.append(pCurrent.getPlotCity())
															    #print (iDeadCiv, pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getOwner(), "3", cityList)
											if (iOwnerStability < 20):
												 if (city.getX() == tCapitals[iDeadCiv][0] and city.getY() == tCapitals[iDeadCiv][1]):
													 #print(pCurrent.getPlotCity(), cityList)
													 #if (pCurrent.getPlotCity() not in cityList):  #sadly, this doesn't work
													 bAlreadyAdded = False
													 for l in range(len(cityList)):
														 if (cityList[l].getName() == city.getName()):
															 bAlreadyAdded = True
															 break
													 #print("bAlreadyAdded",bAlreadyAdded)
													 if (not bAlreadyAdded):
														 cityList.append(pCurrent.getPlotCity())
														 #print (iDeadCiv, pCurrent.getPlotCity().getName(), pCurrent.getPlotCity().getOwner(), "4", cityList)
					#print("len(cityList)",len(cityList))
					if (len(cityList) >= iMinNumCities or (len(cityList) >= 1 and (iDeadCiv == iPhoenicia))): #TODO what is this
						bDeadCivFound = True
						break
			#print ("iDeadCiv", iDeadCiv)
			if (bDeadCivFound):
				self.setRebelCiv(iDeadCiv) #for popup and CollapseCapitals()

				for l in range(iNumPlayers):
					teamDeadCiv.makePeace(l)
				self.setNumCities(iDeadCiv, 0) #reset collapse condition

				#reset vassallage
				for iOtherCiv in range(iNumPlayers):
					if (teamDeadCiv.isVassal(iOtherCiv) or gc.getTeam(gc.getPlayer(iOtherCiv).getTeam()).isVassal(iDeadCiv)):
						teamDeadCiv.freeVassal(iOtherCiv)
						gc.getTeam(gc.getPlayer(iOtherCiv).getTeam()).freeVassal(iDeadCiv)
							
				iNewUnits = 2
				if (self.getLatestRebellionTurn(iDeadCiv) > 0):
					iNewUnits = 4
				self.setLatestRebellionTurn(iDeadCiv, iGameTurn)
				bHuman = False
				iHuman = utils.getHumanID()
				print ("RESURRECTION", gc.getPlayer(iDeadCiv).getCivilizationAdjective(0))

				for k0 in range(len(cityList)):
					iOwner = cityList[k0].getOwner()
					if (iOwner == iHuman):
						bHuman = True

				for t in range(con.getNumTechs()):
					if (teamBarbarian.isHasTech(t) or teamIndependent.isHasTech(t) or teamIndependent2.isHasTech(t)): #remove indep in vanilla
						teamDeadCiv.setHasTech(t, True, iDeadCiv, False, False)

				ownersList = []
				bAlreadyVassal = False
				for k in range(len(cityList)):
					if (cityList[k] != None): #once happened that it was = none
						#print ("INDEPENDENCE: ", cityList[k].getName()) #may cause a c++ exception				
						iOwner = cityList[k].getOwner()
						teamOwner = gc.getTeam(gc.getPlayer(iOwner).getTeam())
						bOwnerVassal = teamOwner.isAVassal()
						bOwnerHumanVassal = teamOwner.isVassal(iHuman)

						if (iOwner not in ownersList): #assignment of techs must be done before the creation of garrisons
							for t in range(con.getNumTechs()):
								if (teamOwner.isHasTech(t)):
									teamDeadCiv.setHasTech(t, True, iDeadCiv, False, False)

						if (iOwner == iBarbarian or iOwner == iIndependent or iOwner == iIndependent2):
							utils.cultureManager((cityList[k].getX(),cityList[k].getY()), 100, iDeadCiv, iOwner, False, True, True)
							utils.flipUnitsInCityBefore((cityList[k].getX(),cityList[k].getY()), iDeadCiv, iOwner)
							self.setTempFlippingCity((cityList[k].getX(),cityList[k].getY()))
							utils.flipCity((cityList[k].getX(),cityList[k].getY()), 0, 0, iDeadCiv, [iOwner])
							tCoords = self.getTempFlippingCity()
							utils.flipUnitsInCityAfter(tCoords, iOwner)
							utils.flipUnitsInArea((tCoords[0]-2, tCoords[1]-2), (tCoords[0]+2, tCoords[1]+2), iDeadCiv, iOwner, True, False)
						else:
							utils.cultureManager((cityList[k].getX(),cityList[k].getY()), 50, iDeadCiv, iOwner, False, True, True)
							utils.pushOutGarrisons((cityList[k].getX(),cityList[k].getY()), iOwner)
							utils.relocateSeaGarrisons((cityList[k].getX(),cityList[k].getY()), iOwner)
							self.setTempFlippingCity((cityList[k].getX(),cityList[k].getY()))
							utils.flipCity((cityList[k].getX(),cityList[k].getY()), 0, 0, iDeadCiv, [iOwner])   #by trade because by conquest may raze the city
							utils.createGarrisons(self.getTempFlippingCity(), iDeadCiv, iNewUnits)

						#cityList[k].setHasRealBuilding(con.iPlague, False)

						bAtWar = False #AI won't vassalise if another owner has declared war; on the other hand, it won't declare war if another one has vassalised
						if (iOwner != iHuman and iOwner not in ownersList and iOwner != iDeadCiv): #declare war or peace only once - the 3rd condition is obvious but "vassal of themselves" was happening
							rndNum = gc.getGame().getSorenRandNum(100, 'odds')
							if (rndNum >= tAIStopBirthThreshold[iOwner] and bOwnerHumanVassal == False and bAlreadyVassal == False): #if bOwnerHumanVassal is true, it will skip to the 3rd condition, as bOwnerVassal is true as well
								teamOwner.declareWar(iDeadCiv, False, -1)
								bAtWar = True
							elif (rndNum <= (100-tAIStopBirthThreshold[iOwner])/2):
								teamOwner.makePeace(iDeadCiv)
								if (bAlreadyVassal == False and bHuman == False and bOwnerVassal == False and bAtWar == False): #bHuman == False cos otherwise human player can be deceived to declare war without knowing the new master
									if (iOwner < iNumActivePlayers):
										gc.getTeam(gc.getPlayer(iDeadCiv).getTeam()).setVassal(iOwner, True, False)  #remove in vanilla
										bAlreadyVassal = True
							else:
								teamOwner.makePeace(iDeadCiv)

						if (iOwner not in ownersList):
							ownersList.append(iOwner)

				self.moveBackCapital(iDeadCiv)

				#add former colonies that are still free
				colonyList = []
				for iIndCiv in range(iNumTotalPlayers+1): #barbarians too
					if (iIndCiv >= iNumActivePlayers):
						if (gc.getPlayer(iIndCiv).isAlive()):
							apCityList = PyPlayer(iIndCiv).getCityList()
							for pCity in apCityList:
								indepCity = pCity.GetCy()
								if (indepCity.getOriginalOwner() == iDeadCiv):
									print ("colony:", indepCity.getName(), indepCity.getOriginalOwner())
									indX = indepCity.getX()
									indY = indepCity.getY()
									if (gc.getPlayer(iDeadCiv).getSettlersMaps(67-indY, indX) >= 90):
										if (indepCity not in cityList and indepCity not in colonyList):
											colonyList.append(indepCity)
				if (len(colonyList) > 0):
					for k in range(len(colonyList)):
						print ("INDEPENDENCE: ", colonyList[k].getName())
						iOwner = colonyList[k].getOwner()
						utils.cultureManager((colonyList[k].getX(),colonyList[k].getY()), 100, iDeadCiv, iOwner, False, True, True)
						utils.flipUnitsInCityBefore((colonyList[k].getX(),colonyList[k].getY()), iDeadCiv, iOwner)
						self.setTempFlippingCity((colonyList[k].getX(),colonyList[k].getY()))
						utils.flipCity((colonyList[k].getX(),colonyList[k].getY()), 0, 0, iDeadCiv, [iOwner])
						tCoords = self.getTempFlippingCity()
						utils.flipUnitsInCityAfter(tCoords, iOwner)
						utils.flipUnitsInArea((tCoords[0]-2, tCoords[1]-2), (tCoords[0]+2, tCoords[1]+2), iDeadCiv, iOwner, True, False)

				CyInterface().addMessage(iHuman, True, con.iDuration, \
							(CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT", (pDeadCiv.getCivilizationAdjectiveKey(),))), "", 0, "", ColorTypes(con.iGreen), -1, -1, True, True)
				if (bHuman == True):
					self.rebellionPopup(iDeadCiv)
				utils.setBaseStabilityLastTurn(iDeadCiv, 0)
				utils.setStability(iDeadCiv, 10) ##the new civs start as slightly stable
				utils.setPlagueCountdown(iDeadCiv, -10)
				utils.clearPlague(iDeadCiv)
				self.convertBackCulture(iDeadCiv)
				return

	def moveBackCapital(self, iCiv):
		apCityList = PyPlayer(iCiv).getCityList()
		if (gc.getMap().plot(tCapitals[iCiv][0], tCapitals[iCiv][1]).isCity()):
			oldCapital = gc.getMap().plot(tCapitals[iCiv][0], tCapitals[iCiv][1]).getPlotCity()
			if (oldCapital.getOwner() == iCiv):
				if (not oldCapital.hasBuilding(con.bn('palace'))):
					for pCity in apCityList:
						pCity.GetCy().setHasRealBuilding((con.bn('palace')), False)
					oldCapital.setHasRealBuilding((con.bn('palace')), True)
		else:
			iMaxValue = 0
			bestCity = None
			for pCity in apCityList:
				loopCity = pCity.GetCy()
				#loopCity.AI_cityValue() doesn't work as area AI types aren't updated yet
				loopValue = max(0,500-loopCity.getGameTurnFounded()) + loopCity.getPopulation()*10
				#print ("loopValue", loopCity.getName(), loopCity.AI_cityValue(), loopValue) #causes C++ exception
				if (loopValue > iMaxValue):
					iMaxValue = loopValue
					bestCity = loopCity
			if (bestCity != None):
				for pCity in apCityList:
					loopCity = pCity.GetCy()
					if (loopCity != bestCity):
						loopCity.setHasRealBuilding((con.bn('palace')), False)
				bestCity.setHasRealBuilding((con.bn('palace')), True)



	def convertBackCulture(self, iCiv):
		tTopLeft = tNormalAreasTL[iCiv]
		tBottomRight = tNormalAreasBR[iCiv]	
		cityList = []
		#collect all the cities in the region
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				pCurrent = gc.getMap().plot(x, y)
				if (pCurrent.isCity()):
					for ix in range(pCurrent.getX()-1, pCurrent.getX()+2):	# from x-1 to x+1
						for iy in range(pCurrent.getY()-1, pCurrent.getY()+2):	# from y-1 to y+1
							pCityArea = gc.getMap().plot(ix, iy)
							iCivCulture = pCityArea.getCulture(iCiv)
							iLoopCivCulture = 0
							for iLoopCiv in range(con.iNumTotalPlayers+1): #barbarians too
								if (iLoopCiv >= iNumPlayers):
									iLoopCivCulture += pCityArea.getCulture(iLoopCiv)
									pCityArea.setCulture(iLoopCiv, 0, True)
							pCityArea.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)

					city = pCurrent.getPlotCity()
					iCivCulture = city.getCulture(iCiv)
					iLoopCivCulture = 0
					for iLoopCiv in range(con.iNumTotalPlayers+1): #barbarians too
						if (iLoopCiv >= iNumPlayers):
							iLoopCivCulture += city.getCulture(iLoopCiv)
							city.setCulture(iLoopCiv, 0, True)
					city.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)


			
				
	def initBirth(self, iCurrentTurn, iBirthYear, iCiv):
		iHuman = utils.getHumanID()
		print ("inside initbirth1",iCurrentTurn,iBirthYear-1 + self.getSpawnDelay(iCiv) + self.getFlipsDelay(iCiv),iBirthYear-1,self.getSpawnDelay(iCiv),self.getFlipsDelay(iCiv))
		if (iCurrentTurn == iBirthYear-1 + self.getSpawnDelay(iCiv) + self.getFlipsDelay(iCiv)):

			print ("inside initbirth2", iCiv)
			tCapital = tCapitals[iCiv]
			tTopLeft = tCoreAreasTL[iCiv]
			tBottomRight = tCoreAreasBR[iCiv]
			tBroaderTopLeft = tBroaderAreasTL[iCiv]
			tBroaderBottomRight = tBroaderAreasBR[iCiv]		
			if (self.getFlipsDelay(iCiv) == 0): #city hasn't already been founded)
				#this may fix the -1 bug
				if (iCiv == iHuman):
					killPlot = gc.getMap().plot(tCapital[0], tCapital[1])
					iNumUnitsInAPlot = killPlot.getNumUnits()
					if (iNumUnitsInAPlot):
						for i in range(iNumUnitsInAPlot):
							unit = killPlot.getUnit(0)
							if (unit.getOwner() != iCiv):
								unit.kill(False, con.iBarbarian)

				gc.getMap().plot(tCapital[0], tCapital[1]).setFeatureType(-1, 0) #RFGW
				bDeleteEverything = False
				if (gc.getMap().plot(tCapital[0], tCapital[1]).isOwned()):
					if (iCiv == iHuman or not gc.getPlayer(iHuman).isAlive()):
						bDeleteEverything = True
						print ("bDeleteEverything 1")
					else:
						bDeleteEverything = True
						for x in range(tCapital[0] - 1, tCapital[0] + 2):	# from x-1 to x+1
							for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
								pCurrent=gc.getMap().plot(x, y)
								if (pCurrent.isCity() and pCurrent.getPlotCity().getOwner() == iHuman):
									bDeleteEverything = False
									print ("bDeleteEverything 2")
									break
									break
				print ("bDeleteEverything", bDeleteEverything)
				print("cap:",tCapital[0], tCapital[1],gc.getMap().plot(tCapital[0], tCapital[1]).isOwned())
				if (not gc.getMap().plot(tCapital[0], tCapital[1]).isOwned()):
					print("launch birthInFreeRegion")
					self.birthInFreeRegion(iCiv, tCapital, tTopLeft, tBottomRight)
				elif (bDeleteEverything):
					for x in range(tCapital[0] - 1, tCapital[0] + 2):	# from x-1 to x+1
						for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
							self.setDeleteMode(0, iCiv)
							#print ("deleting", x, y)
							pCurrent=gc.getMap().plot(x, y)
							#self.moveOutUnits(x, y, tCapital[0], tCapital[1])
							for iLoopCiv in range(con.iNumTotalPlayersB): #Barbarians as well
								if (iCiv != iLoopCiv):
									utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iLoopCiv, True, False)
							if (pCurrent.isCity()):
								pCurrent.eraseAIDevelopment() #new function, similar to erase but won't delete rivers, resources and features()
							for iLoopCiv in range(con.iNumTotalPlayersB): #Barbarians as well
								if (iCiv != iLoopCiv):
									pCurrent.setCulture(iLoopCiv, 0, True)
							pCurrent.setOwner(-1)
					self.birthInFreeRegion(iCiv, tCapital, tTopLeft, tBottomRight)
				else:
					self.birthInFreeRegion(iCiv, tCapital, tTopLeft, tBottomRight)
					#self.birthInForeignBorders(iCiv, tTopLeft, tBottomRight, tBroaderTopLeft, tBroaderBottomRight)
			else:
				print ("setBirthType again: flips")
				self.birthInFreeRegion(iCiv, tCapital, tTopLeft, tBottomRight)
				
		if (iCurrentTurn == iBirthYear + self.getSpawnDelay(iCiv)) and (gc.getPlayer(iCiv).isAlive()) and (self.getAlreadySwitched() == False) and (iHuman+tDifference[iHuman] < iCiv):
			self.newCivPopup(iCiv)


##	def moveOutUnits(self, x, y, tCapitalX, tCapitalY) #not used
##		pCurrent=gc.getMap().plot(x, y)
##		if (pCurrent.getNumUnits() > 0):
##			unit = pCurrent.getUnit(0)
##			tDestination = (-1, -1)
##			plotList = []
##			if (unit.getDomainType() == 2): #land unit
##				dummy, plotList = utils.squareSearch((tCapitalX-3, tCapitalY-3), (tCapitalX+4, tCapitalY+4), utils.goodPlots, [])
##				#dummy, plotList = utils.squareSearch((tCapitalX-3, tCapitalY-3), (tCapitalX+4, tCapitalY+4), utils.goodOwnedPlots, [])
##			else: #sea unit
##				dummy, plotList = utils.squareSearch((tCapitalX-3, tCapitalY-3), (tCapitalX+4, tCapitalY+4), utils.goodOwnedPlots, [])
##
##			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching another free plot')
##			if (len(plotList)):
##				result = plotList[rndNum]
##				if (result):
##					tDestination = result
##			print ("moving units around to", (tDestination[0], tDestination[1]))
##			if (tDestination != (-1, -1)):
##				for i in range(pCurrent.getNumUnits()):
##					unit = pCurrent.getUnit(0)
##					unit.setXY(tDestination[0], tDestination[1])




	def deleteMode(self, iCurrentPlayer):
		iCiv = self.getDeleteMode(0)
		print ("deleteMode after", iCurrentPlayer)
		tCapital = con.tCapitals[iCiv]
		if (iCurrentPlayer == iCiv):
			for x in range(tCapital[0] - 2, tCapital[0] + 3):	# from x-2 to x+2
				for y in range(tCapital[1] - 2, tCapital[1] + 3):	# from y-2 to y+2
					pCurrent=gc.getMap().plot(x, y)
					pCurrent.setCulture(iCiv, 300, True)
			for x in range(tCapital[0] - 1, tCapital[0] + 2):	# from x-1 to x+1
				for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
					pCurrent=gc.getMap().plot(x, y)
					utils.convertPlotCulture(pCurrent, iCiv, 100, True)
					if (pCurrent.getCulture(iCiv) < 3000):
						pCurrent.setCulture(iCiv, 3000, True) #2000 in vanilla/warlords, cos here Portugal is choked by spanish culture
					pCurrent.setOwner(iCiv)
			self.setDeleteMode(0, -1)
			return
		
		#print ("iCurrentPlayer", iCurrentPlayer, "iCiv", iCiv)
		if (iCurrentPlayer != iCiv-1):
			return

		bNotOwned = True
		for x in range(tCapital[0] - 1, tCapital[0] + 2):	# from x-1 to x+1
			for y in range(tCapital[1] - 1, tCapital[1] + 2):	# from y-1 to y+1
				#print ("deleting again", x, y)
				pCurrent=gc.getMap().plot(x, y)
				if (pCurrent.isOwned()):
					bNotOwned = False
					for iLoopCiv in range(iNumTotalPlayers+1): #Barbarians as well
						if(iLoopCiv != iCiv):
							pCurrent.setCulture(iLoopCiv, 0, True)
						#else:
						#	if (pCurrent.getCulture(iCiv) < 4000):
						#		pCurrent.setCulture(iCiv, 4000, True)
					#pCurrent.setOwner(-1)
					pCurrent.setOwner(iCiv)

		for x in range(tCapital[0] - 11, tCapital[0] + 12):	# must include the distance from Sogut to the Caspius
			for y in range(tCapital[1] - 11, tCapital[1] + 12):
				#print ("units", x, y, gc.getMap().plot(x, y).getNumUnits(), tCapital[0], tCapital[1])
				if (x != tCapital[0] or y != tCapital[1]):
					pCurrent=gc.getMap().plot(x, y)
					if (pCurrent.getNumUnits() > 0 and not pCurrent.isWater()):
						unit = pCurrent.getUnit(0)
						#print ("units2", x, y, gc.getMap().plot(x, y).getNumUnits(), unit.getOwner(), iCiv)
						if (unit.getOwner() == iCiv):
							print ("moving starting units from", x, y, "to", (tCapital[0], tCapital[1]))
							for i in range(pCurrent.getNumUnits()):
								unit = pCurrent.getUnit(0)
								unit.setXYOld(tCapital[0], tCapital[1])
							#may intersect plot close to tCapital
##							for farX in range(x - 6, x + 7):
##								for farY in range(y - 6, y + 7):
##									pCurrentFar = gc.getMap().plot(farX, farY)
##									if (pCurrentFar.getNumUnits() == 0):
##										pCurrentFar.setRevealed(iCiv, False, True, -1);




	
		
	def birthInFreeRegion(self, iCiv, tCapital, tTopLeft, tBottomRight):
		startingPlot = gc.getMap().plot(tCapital[0], tCapital[1])
		print("birthInFreeRegion1",self.getFlipsDelay(iCiv))
		if (self.getFlipsDelay(iCiv) == 0):
			print("birthInFreeRegion2")
			iFlipsDelay = self.getFlipsDelay(iCiv) + 2
##			if (startingPlot.getNumUnits() > 0):
##				unit = startingPlot.getUnit(0)
##				if (unit.getOwner() != utils.getHumanID() or iCiv == utils.getHumanID()): #2nd check needed because in delete mode it finds the civ's (human's) units placed
##					for i in range(startingPlot.getNumUnits()):
##						unit = startingPlot.getUnit(0)	# 0 instead of i because killing units changes the indices
##						unit.kill(False, iCiv)
##					iFlipsDelay = self.getFlipsDelay(iCiv) + 2
##					#utils.debugTextPopup('birthInFreeRegion in starting location')
##				else:   #search another place
##					dummy, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.goodPlots, [])
##					rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching another free plot')
##					if (len(plotList)):
##						result = plotList[rndNum]
##						if (result):
##							self.createStartingUnits(iCiv, result)
##							tCapital = result
##							print ("birthInFreeRegion in another location")
##							#utils.debugTextPopup('birthInFreeRegion in another location')
##							iFlipsDelay = self.getFlipsDelay(iCiv) + 1 #add delay before flipping other cities
##					else:
##						if (self.getSpawnDelay(iCiv) < 10):  #wait
##							iSpawnDelay = self.getSpawnDelay(iCiv) + 1
##							self.setSpawnDelay(iCiv, iSpawnDelay)
##			else:
##				iFlipsDelay = self.getFlipsDelay(iCiv) + 2

			if (iFlipsDelay > 0):
				#startingPlot.setImprovementType(-1)
			
				#gc.getPlayer(iCiv).found(tCapital[0], tCapital[1])
				#gc.getMap().plot(tCapital[0], tCapital[1]).setRevealed(iCiv, False, True, -1);
				#gc.getMap().plot(tCapital[0], tCapital[1]).setRevealed(iCiv, True, True, -1);

				print ("starting units in", tCapital[0], tCapital[1])
				self.createStartingUnits(iCiv, (tCapital[0], tCapital[1]))

				#if (self.getDeleteMode(0) == iCiv):
				#	self.createStartingWorkers(iCiv, tCapital) #XXX bugfix? no!

##				settlerPlot = gc.getMap().plot(tCapital[0], tCapital[1])
##				for i in range(settlerPlot.getNumUnits()):
##					unit = settlerPlot.getUnit(i)
##					if (unit.getUnitType() == un('settler')):
##						break
##				unit.found()
				utils.flipUnitsInArea((tCapital[0]-3, tCapital[1]-3), (tCapital[0]+3, tCapital[1]+3), iCiv, iBarbarian, True, True) #This is mostly for the AI. During Human player spawn, that area should be already cleaned
				utils.flipUnitsInArea((tCapital[0]-3, tCapital[1]-3), (tCapital[0]+3, tCapital[1]+3), iCiv, iIndependent, True, False) #This is mostly for the AI. During Human player spawn, that area should be already cleaned
				utils.flipUnitsInArea((tCapital[0]-3, tCapital[1]-3), (tCapital[0]+3, tCapital[1]+3), iCiv, iIndependent2, True, False) #This is mostly for the AI. During Human player spawn, that area should be already cleaned
				self.assignTechs(iCiv)
				utils.setPlagueCountdown(iCiv, -con.iImmunity)
				utils.clearPlague(iCiv)
				#gc.getPlayer(iCiv).changeAnarchyTurns(1)
				#gc.getPlayer(iCiv).setCivics(2, 11)
				self.setFlipsDelay(iCiv, iFlipsDelay) #save


		else: #starting units have already been placed, now the second part
			#RFGW

			#cover plots revealed by the lion
			plotZero = gc.getMap().plot(0, 0)
			if (plotZero.getNumUnits()):
				catapult = plotZero.getUnit(0)
				catapult.kill(False, iCiv)
			gc.getMap().plot(0, 0).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(0, 1).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(1, 1).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(1, 0).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(83, 0).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(83, 1).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(2, 0).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(2, 1).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(2, 2).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(1, 2).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(0, 2).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(82, 0).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(82, 1).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(82, 2).setRevealed(iCiv, False, True, -1);
			gc.getMap().plot(83, 2).setRevealed(iCiv, False, True, -1);
			print ("Plots covered")

			if (con.getFeedUnits(iCiv) == 0):
				iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iCiv, tTopLeft, tBottomRight)
				self.convertSurroundingPlotCulture(iCiv, tTopLeft, tBottomRight)
				utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iBarbarian, False, True) #remaining barbs in the region now belong to the new civ
				utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iIndependent, False, True) #remaining independents in the region now belong to the new civ
				utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iIndependent2, False, True) #remaining independents in the region now belong to the new civ
				print ("utils.flipUnitsInArea()")


				if (gc.getPlayer(iCiv).getNumCities() > 0):
					capital = gc.getPlayer(iCiv).getCapitalCity()
					self.createStartingWorkers(iCiv, (capital.getX(), capital.getY()))

				if (iNumHumanCitiesToConvert> 0):
					self.flipPopup(iCiv, tTopLeft, tBottomRight)

			else:
				teamCiv = gc.getTeam(gc.getPlayer(iCiv).getTeam())
				for iLoopWarCiv in range(iNumTotalPlayers):
					if (teamCiv.isAtWar(iLoopWarCiv)):
						teamCiv.AI_setWarPlan(iLoopWarCiv,5) #total


	def birthInForeignBorders(self, iCiv, tTopLeft, tBottomRight, tBroaderTopLeft, tBroaderBottomRight):

		iNumAICitiesConverted, iNumHumanCitiesToConvert = self.convertSurroundingCities(iCiv, tTopLeft, tBottomRight)
		self.convertSurroundingPlotCulture(iCiv, tTopLeft, tBottomRight)

		#now starting units must be placed
		if (iNumAICitiesConverted > 0):
			#utils.debugTextPopup('iConverted OK for placing units')
			dummy1, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.ownedCityPlots, iCiv)
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching any city just flipped')
			#print ("rndNum for starting units", rndNum)
			if (len(plotList)):
				result = plotList[rndNum]
				if (result):
					self.createStartingUnits(iCiv, result)
					#utils.debugTextPopup('birthInForeignBorders after a flip')
					self.assignTechs(iCiv)
					utils.setPlagueCountdown(iCiv, -con.iImmunity)
					utils.clearPlague(iCiv)
					#gc.getPlayer(iCiv).changeAnarchyTurns(1)
			utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iBarbarian, False, True) #remaining barbs in the region now belong to the new civ
			utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iIndependent, False, False) #remaining barbs in the region now belong to the new civ
			utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iIndependent2, False, False) #remaining barbs in the region now belong to the new civ

		else:   #search another place
			dummy, plotList = utils.squareSearch(tTopLeft, tBottomRight, utils.goodPlots, [])
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching another free plot')
			if (len(plotList)):
				result = plotList[rndNum]
				if (result):
					self.createStartingUnits(iCiv, result)
					#utils.debugTextPopup('birthInForeignBorders in another location')
					self.assignTechs(iCiv)
					utils.setPlagueCountdown(iCiv, -con.iImmunity)
					utils.clearPlague(iCiv)
			else:
				dummy1, plotList = utils.squareSearch(tBroaderTopLeft, tBroaderBottomRight, utils.goodPlots, [])
				rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching other good plots in a broader region')
				if (len(plotList)):
					result = plotList[rndNum]
					if (result):
						self.createStartingUnits(iCiv, result)
						self.createStartingWorkers(iCiv, result)
						#utils.debugTextPopup('birthInForeignBorders in a broader area')
						self.assignTechs(iCiv)
						utils.setPlagueCountdown(iCiv, -con.iImmunity)
						utils.clearPlague(iCiv)
			utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iBarbarian, True, True) #remaining barbs in the region now belong to the new civ
			utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iIndependent, True, False) #remaining barbs in the region now belong to the new civ
			utils.flipUnitsInArea(tTopLeft, tBottomRight, iCiv, iIndependent2, True, False) #remaining barbs in the region now belong to the new civ

		if (iNumHumanCitiesToConvert> 0):
			self.flipPopup(iCiv, tTopLeft, tBottomRight)





	def convertSurroundingCities(self, iCiv, tTopLeft, tBottomRight):
		iConvertedCitiesCount = 0
		iNumHumanCities = 0
		cityList = []
		self.setSpawnWar(0)

		#collect all the cities in the spawn region
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				pCurrent = gc.getMap().plot(x, y)
				if (pCurrent.isCity()):
					if (pCurrent.getPlotCity().getOwner() != iCiv):
						cityList.append(pCurrent.getPlotCity())

		#Exceptions
		if (len(tExceptions[iCiv])):
			for j in range(len(tExceptions[iCiv])):
				pCurrent = gc.getMap().plot(tExceptions[iCiv][j][0], tExceptions[iCiv][j][1])
				if (pCurrent.isCity()):
					if (pCurrent.getPlotCity().getOwner() != iCiv):
						print ("append", pCurrent)
						cityList.append(pCurrent.getPlotCity())

		print ("Birth", iCiv)
		#print (cityList)

		#for each city
		if (len(cityList)):
			for i in range(len(cityList)):
				loopCity = cityList[i]
				loopX = loopCity.getX()
				loopY = loopCity.getY()
				print ("cityList", loopCity.getName(), (loopX, loopY))
				iHuman = utils.getHumanID()
				iOwner = loopCity.getOwner()
				iCultureChange = 0 #if 0, no flip; if > 0, flip will occur with the value as variable for utils.CultureManager()

				#case 1: barbarian/independent city
				if (iOwner == iBarbarian or iOwner == iIndependent or iOwner == iIndependent2 or iOwner == iCeltia):
					#utils.debugTextPopup('BARB')
					iCultureChange = 100
				#case 2: human city
				#elif (iOwner == iHuman and not loopCity.isCapital()): #exploitable
				elif (iOwner == iHuman and not (loopX == tCapitals[iHuman] and loopY == tCapitals[iHuman]) and not gc.getPlayer(iHuman).getNumCities() <= 1 and not (self.getCheatMode() == True and loopCity.isCapital())):
				
					#utils.debugTextPopup('HUMAN')
	##				bForeigners = False
	##				cityPlot = gc.getMap().plot(cityList[i].getX(), cityList[i].getY())
	##				cityCulture = cityList[i].countTotalCulture()
	##				iCultureThreshold = 10
	##				for j in range(iNumPlayers+1):
	##					if (cityList[i].getCulture(j)*100 / cityCulture >= iCultureThreshold) and (j != iHuman):
	##						bForeigners = True
	##				humanCapital = gc.getPlayer(iHuman).getCapitalCity()
	##				iDistance = gc.getMap().calculatePathDistance(cityPlot, gc.getMap().plot(humanCapital.getX(),humanCapital.getY()))
	##				if (cityList[i].isOccupation()) or (cityList[i].isDisorder()) or (bForeigners == True) or (not cityPlot.getNumUnits()) or ((not cityList[i].isGovernmentCenter()) and (iDistance >= 8) and (gc.getPlayer(iHuman).getNumCities() >= 5)):
					if (iNumHumanCities == 0):
						iNumHumanCities += 1
						#iConvertedCitiesCount += 1
						#self.flipPopup(iCiv, tTopLeft, tBottomRight)
				#case 3: other
				elif (not loopCity.isCapital()):   #utils.debugTextPopup('OTHER')
					if (iConvertedCitiesCount < 6): #there won't be more than 5 flips in the area
						#utils.debugTextPopup('iConvertedCities OK')
						iCultureChange = 50
						if (gc.getGame().getGameTurn() <= con.tBirth[iCiv] + 5): #if we're during a birth
							rndNum = gc.getGame().getSorenRandNum(100, 'odds')
							if (rndNum >= tAIStopBirthThreshold[iOwner]):
								print (iOwner, "stops birth", iCiv, "rndNum:", rndNum, "threshold:", tAIStopBirthThreshold[iOwner])
								if (not gc.getTeam(gc.getPlayer(iOwner).getTeam()).isAtWar(iCiv)):
									gc.getTeam(gc.getPlayer(iOwner).getTeam()).declareWar(iCiv, False, -1)
									if (gc.getPlayer(iCiv).getNumCities() > 0): #this check is needed, otherwise game crashes
										print ("capital:", gc.getPlayer(iCiv).getCapitalCity().getX(), gc.getPlayer(iCiv).getCapitalCity().getY())
										if (gc.getPlayer(iCiv).getCapitalCity().getX() != -1 and gc.getPlayer(iCiv).getCapitalCity().getY() != -1):
											self.createAdditionalUnits(iCiv, (gc.getPlayer(iCiv).getCapitalCity().getX(), gc.getPlayer(iCiv).getCapitalCity().getY()))
										else:
											self.createAdditionalUnits(iCiv, tCapitals[iCiv])



				if (iCultureChange > 0):
					#print ("flipping ", cityList[i].getName())
					utils.cultureManager((loopX,loopY), iCultureChange, iCiv, iOwner, True, False, False)
					#gc.getMap().plot(cityList[i].getX(),cityList[i].getY()).setImprovementType(-1)

					utils.flipUnitsInCityBefore((loopX,loopY), iCiv, iOwner)
					self.setTempFlippingCity((loopX,loopY)) #necessary for the (688379128, 0) bug
					utils.flipCity((loopX,loopY), 0, 0, iCiv, [iOwner])
					#print ("cityList[i].getXY", cityList[i].getX(), cityList[i].getY())
					utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iCiv)

					#iEra = gc.getPlayer(iCiv).getCurrentEra()
					#if (iEra >= 2): #medieval
					#	if (loopCity.getPopulation() < iEra):
					#		loopCity.setPopulation(iEra) #causes an unidentifiable C++ exception
						#doesn't work (assigns UBs too)
						#for iLoopBuilding in range(con.iNumBuildingsPlague):
						#	if (gc.getBuildingInfo(iLoopBuilding).getFreeStartEra() >= 0):
						#		if (iEra >= gc.getBuildingInfo(iLoopBuilding).getFreeStartEra()):
						#			print (iEra, iLoopBuilding, gc.getBuildingInfo(iLoopBuilding).getFreeStartEra(), loopCity.canConstruct(iLoopBuilding, False, False, False))
						#			if (loopCity.canConstruct(iLoopBuilding, False, False, False)):
						#				if (not loopCity.hasBuilding(iLoopBuilding)):
						#					loopCity.setHasRealBuilding(iLoopBuilding, True)

					#cityList[i].setHasRealBuilding(con.iPlague, False)   #buggy

					iConvertedCitiesCount += 1
					print ("iConvertedCitiesCount", iConvertedCitiesCount)

		if (iConvertedCitiesCount > 0):
			if (gc.getPlayer(iCiv).isHuman()):
				CyInterface().addMessage(iCiv, True, con.iDuration, CyTranslator().getText("TXT_KEY_FLIP_TO_US", ()), "", 0, "", ColorTypes(con.iGreen), -1, -1, True, True)
		#print("converted cities", iConvertedCitiesCount)
		return (iConvertedCitiesCount, iNumHumanCities)



	def convertSurroundingPlotCulture(self, iCiv, tTopLeft, tBottomRight):

		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				pCurrent = gc.getMap().plot(x, y)
				if (not pCurrent.isCity()):
					utils.convertPlotCulture(pCurrent, iCiv, 100, False)

		if (len(tExceptions[iCiv])):
			for j in range(len(tExceptions[iCiv])):
				pCurrent = gc.getMap().plot(tExceptions[iCiv][j][0], tExceptions[iCiv][j][1])
				if (not pCurrent.isCity()):
					utils.convertPlotCulture(pCurrent, iCiv, 100, False)

	def findSeaPlots(self, tCoords, iRange, iCiv):
		"""Searches a sea plot that isn't occupied by a unit and isn't a civ's territory surrounding the starting coordinates"""
		seaPlotList = []
		for x in range(tCoords[0] - iRange, tCoords[0] + iRange+1):
			for y in range(tCoords[1] - iRange, tCoords[1] + iRange+1):
				pCurrent = gc.getMap().plot(x, y)
				if (pCurrent.isWater()):
					if (not pCurrent.isUnit()):
						#if (pCurrent.countTotalCulture() == 0):
						if (not (pCurrent.isOwned() and pCurrent.getOwner() != iCiv)):
							seaPlotList.append(pCurrent)
							# this is a good plot, so paint it and continue search
		if (len(seaPlotList) > 0):
			rndNum = gc.getGame().getSorenRandNum(len(seaPlotList), 'sea plot')
			result = seaPlotList[rndNum]
			if (result):
				    return ((result.getX(), result.getY()))
		return (None)


	def giveEarlyColonists(self, iCiv):
		pCiv = gc.getPlayer(iCiv)
		teamCiv = gc.getTeam(pCiv.getTeam())
		if (pCiv.isAlive() and pCiv.isHuman() == False):
			capital = gc.getPlayer(iCiv).getCapitalCity()
			tCapital = (capital.getX(), capital.getY())
			tSeaPlot = self.findSeaPlots(tCapital, 1, iCiv)
			if (tSeaPlot):
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_SETTLER_SEA, DirectionTypes.DIRECTION_SOUTH)
				utils.makeUnit(con.un('settler'), iCiv, tSeaPlot, 1)
				utils.makeUnit(con.un('archer'), iCiv, tSeaPlot, 1)

	def onFirstContact(self, iTeamX, iHasMetTeamY):
		return

	def warOnSpawn(self):
		for iCiv in range(iNumMajorPlayers):
			if (not gc.getPlayer(0).isPlayable() and con.tIsActiveOnLateStart[iCiv]==0): #late start condition
				continue #skip	
			pCiv = gc.getPlayer(iCiv)
			teamCiv = gc.getTeam(pCiv.getTeam())
			iMin = 20
			iMin = 0 #RFGW
			if (pCiv.isHuman()):
				iMin = 20 #can be set to 100 for skipping human player			
			#bluepotato: removed randomness TODO remove duplicated entries if this turns out well
			#if (gc.getGame().getSorenRandNum(100, 'first roll') >= iMin):
			for iLoopCiv in con.lEnemyCivsOnSpawn[iCiv]:
				if (not gc.getPlayer(0).isPlayable() and con.tIsActiveOnLateStart[iLoopCiv]==0): #late start condition
					continue #skip
				#iLoopMin = 50
				#if (iLoopCiv >= iNumMajorPlayers):
				#	iLoopMin = 30
				#if (pCiv.isHuman() or gc.getPlayer(iLoopCiv).isHuman()):
				#	iLoopMin += 25
				#iLoopMin = 0 #RFGW
				#if (gc.getGame().getSorenRandNum(100, 'loopCiv roll') >= iLoopMin):
				gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).setAtWar(iCiv, True)
				teamCiv.setAtWar(iLoopCiv, True)
				#print("civs will start at war:", iCiv, iLoopCiv)
			if (con.tRefusePeaceAI[iCiv] == 1):
				for iLoopCiv in range(iNumTotalPlayers):
					if (iLoopCiv != iCiv):
						gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).setAtWar(iCiv, True)
						teamCiv.setAtWar(iLoopCiv, True)




	def immuneMode(self, argsList):
		pWinningUnit,pLosingUnit = argsList
		iLosingPlayer = pLosingUnit.getOwner()
		iUnitType = pLosingUnit.getUnitType()
		if (iLosingPlayer < iNumMajorPlayers):
			if (gc.getGame().getGameTurn() >= con.tBirth[iLosingPlayer] and gc.getGame().getGameTurn() <= con.tBirth[iLosingPlayer]+2):
				if (pLosingUnit.getX() == tCapitals[iLosingPlayer][0] and pLosingUnit.getY() == tCapitals[iLosingPlayer][1]):
					print("new civs are immune for now")
					if (gc.getGame().getSorenRandNum(100, 'immune roll') >= 50):
						utils.makeUnit(iUnitType, iLosingPlayer, (pLosingUnit.getX(), pLosingUnit.getY()), 1)

	def initMinorBetrayal(self, iCiv):
		iHuman = utils.getHumanID()
		dummy, plotList = utils.squareSearch(tCoreAreasTL[iCiv], tCoreAreasBR[iCiv], utils.outerInvasion, [])
		rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot abroad human players borders')
		if (len(plotList)):
			result = plotList[rndNum]
			if (result):
				self.createAdditionalUnits(iCiv, result)
				self.unitsBetrayal(iCiv, iHuman, tCoreAreasTL[iCiv], tCoreAreasBR[iCiv], result)



	def initBetrayal(self):
		iHuman = utils.getHumanID()
		turnsLeft = self.getBetrayalTurns()
		dummy, plotList = utils.squareSearch(self.getTempTopLeft(), self.getTempBottomRight(), utils.outerInvasion, [])
		rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot abroad human players (or in general, the old civ if human player just swtiched) borders')
		if (not len(plotList)):
			dummy, plotList = utils.squareSearch(self.getTempTopLeft(), self.getTempBottomRight(), utils.innerSpawn, [self.getOldCivFlip(), self.getNewCivFlip()])
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot within human or new civs border but distant from units')
		if (not len(plotList)):
			dummy, plotList = utils.squareSearch(self.getTempTopLeft(), self.getTempBottomRight(), utils.innerInvasion, [self.getOldCivFlip(), self.getNewCivFlip()])
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'searching a free plot within human or new civs border')
		if (len(plotList)):
			result = plotList[rndNum]
			if (result):
				if (turnsLeft == iBetrayalPeriod):
					self.createAdditionalUnits(self.getNewCivFlip(), result)
				self.unitsBetrayal(self.getNewCivFlip(), self.getOldCivFlip(), self.getTempTopLeft(), self.getTempBottomRight(), result)
		self.setBetrayalTurns(turnsLeft - 1)



	def unitsBetrayal(self, iNewOwner, iOldOwner, tTopLeft, tBottomRight, tPlot):
		#print ("iNewOwner", iNewOwner, "iOldOwner", iOldOwner, "tPlot", tPlot)
		if (gc.getPlayer(self.getOldCivFlip()).isHuman()):
			CyInterface().addMessage(self.getOldCivFlip(), False, con.iDuration, CyTranslator().getText("TXT_KEY_FLIP_BETRAYAL", ()), "", 0, "", ColorTypes(con.iGreen), -1, -1, True, True)
		elif (gc.getPlayer(self.getNewCivFlip()).isHuman()):
			CyInterface().addMessage(self.getNewCivFlip(), False, con.iDuration, CyTranslator().getText("TXT_KEY_FLIP_BETRAYAL_NEW", ()), "", 0, "", ColorTypes(con.iGreen), -1, -1, True, True)
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				killPlot = gc.getMap().plot(x,y)
				iNumUnitsInAPlot = killPlot.getNumUnits()
				if (iNumUnitsInAPlot):								
					for i in range(iNumUnitsInAPlot):
						unit = killPlot.getUnit(i)
						if (unit.getOwner() == iOldOwner):
							rndNum = gc.getGame().getSorenRandNum(100, 'betrayal')
							if (rndNum >= iBetrayalThreshold):
								if (unit.getDomainType() == 2): #land unit
									iUnitType = unit.getUnitType()
									unit.kill(False, iNewOwner)
									utils.makeUnit(iUnitType, iNewOwner, tPlot, 1)
									i = i - 1



	def createAdditionalUnits(self, iCiv, tPlot):
		return #bluepotato: removed invalid constants

	def createStartingUnits(self, iCiv, tPlot):
		if (iCiv == iIndusValley):
			utils.makeUnit(con.un('harappan_city_builder'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('warrior'), iCiv, tPlot, 1)
		if (iCiv == iElam):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('elam_kassu_risa'), iCiv, tPlot, 1)
		if (iCiv == iMinoa):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('warrior'), iCiv, tPlot, 1)
			tSeaPlot = self.findSeaPlots(tPlot, 1, iCiv)
			if (tSeaPlot):
				gc.getPlayer(iCiv).initUnit(con.un('minoa_trireme'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_ESCORT_SEA, DirectionTypes.DIRECTION_SOUTH)
		if (iCiv == iPhoenicia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('warrior'), iCiv, tPlot, 1)
			tSeaPlot = self.findSeaPlots(tPlot, 1, iCiv)
			utils.makeUnit(con.un('spearman'), iCiv, tPlot, 1)
			if (tSeaPlot):
				utils.makeUnit(con.un('workboat'), iCiv, tSeaPlot, 1)
				gc.getPlayer(iCiv).initUnit(con.un('phoenicians_bireme'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_SETTLER_SEA, DirectionTypes.DIRECTION_SOUTH)
				utils.makeUnit(con.un('settler'), iCiv, tSeaPlot, 1)
				utils.makeUnit(con.un('warrior'), iCiv, tSeaPlot, 1)
		if (iCiv == iBabylonia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('babylon_bowman'), iCiv, tPlot, 2)
			utils.makeInvaderUnit(con.un('babylon_bowman'), iCiv, tPlot, 5)
			utils.makeInvaderUnit(con.un('spearman'), iCiv, tPlot, 5)
			utils.makeInvaderUnit(con.un('javelineer'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('hindu_missionary'), iCiv, tPlot, 1)
		if (iCiv == iHittites):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('hittite_huluganni'), iCiv, tPlot, 4)
		if (iCiv == iMycenae):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('mycenae_eqeta'), iCiv, tPlot, 5)
			utils.makeUnit(con.un('chariot'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('confucian_missionary'), iCiv, tPlot, 1)
			tSeaPlot = self.findSeaPlots(tPlot, 1, iCiv)
			if (tSeaPlot):
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_SETTLER_SEA, DirectionTypes.DIRECTION_SOUTH)
				utils.makeUnit(con.un('spearman'), iCiv, tSeaPlot, 1)
				utils.makeUnit(con.un('archer'), iCiv, tSeaPlot, 1)
		if (iCiv == iAssyria):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('spearman'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('assyria_ram'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('chariot'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('swordsman'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('hindu_missionary'), iCiv, tPlot, 1)
		if (iCiv == iIsrael):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('maccabee'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('warrior'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('jewish_missionary'), iCiv, tPlot, 1)
		if (iCiv == iAthens):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('greek_phalanx'), iCiv, tPlot, 2)
			utils.makeInvaderUnit(con.un('greek_phalanx'), iCiv, tPlot, 5)
			utils.makeUnit(con.un('confucian_missionary'), iCiv, tPlot, 1)
			tSeaPlot = self.findSeaPlots(tPlot, 1, iCiv)
			if (tSeaPlot):
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_SETTLER_SEA, DirectionTypes.DIRECTION_SOUTH)
				utils.makeUnit(con.un('warrior'), iCiv, tSeaPlot, 1)
		if (iCiv == iSparta):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('spartiates_hoplite'), iCiv, tPlot, 3) #3
			utils.makeUnit(con.un('confucian_missionary'), iCiv, tPlot, 1)
			utils.makeInvaderUnit(con.un('greek_phalanx'), iCiv, tPlot, 5)
			tSeaPlot = self.findSeaPlots(tPlot, 1, iCiv)
			if (tSeaPlot):
				#utils.makeUnit(con.un('workboat'), iCiv, tSeaPlot, 1)
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_SETTLER_SEA, DirectionTypes.DIRECTION_SOUTH)
				utils.makeUnit(con.un('warrior'), iCiv, tSeaPlot, 1)
		if (iCiv == iScythia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('scythia_scythian_rider'), iCiv, tPlot, 4)
			utils.makeUnit(con.un('noble_cavalry'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('javelineer'), iCiv, tPlot, 1)
		if (iCiv == iCarthage):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('spearman'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('war_elephant'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('carthage_numidian_cavalry'), iCiv, tPlot, 3)
			tSeaPlot = self.findSeaPlots(tPlot, 1, iCiv)
			utils.makeUnit(con.un('taoist_missionary'), iCiv, tPlot, 1)
			if (tSeaPlot):
				utils.makeUnit(con.un('workboat'), iCiv, tSeaPlot, 2)
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_SETTLER_SEA, DirectionTypes.DIRECTION_SOUTH)
				utils.makeUnit(con.un('settler'), iCiv, tSeaPlot, 1)
				utils.makeUnit(con.un('archer'), iCiv, tSeaPlot, 1)
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_ASSAULT_SEA, DirectionTypes.DIRECTION_SOUTH)
				gc.getPlayer(iCiv).initUnit(con.un('trireme'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_ESCORT_SEA, DirectionTypes.DIRECTION_SOUTH)
		if (iCiv == iCeltia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('celtic_gallic_warrior'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('chariot'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('light_cavalry'), iCiv, tPlot, 1)
		if (iCiv == iEtruria):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 2)
		if (iCiv == iNubia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('nubian_medjay'), iCiv, tPlot, 6)
			utils.makeInvaderUnit(con.un('swordsman'), iCiv, tPlot, 8)
		if (iCiv == iPersia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('chariot'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('light_cavalry'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('persia_immortal'), iCiv, tPlot, 8)
			utils.makeUnit(con.un('war_elephant'), iCiv, tPlot, 8)
			utils.makeUnit(con.un('catapult'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('buddhist_missionary'), iCiv, tPlot, 1)
		if (iCiv == iRome):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('hoplite'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('auxillia'), iCiv, tPlot, 1)
			utils.makeInvaderUnit(con.un('catapult'), iCiv, tPlot, 5)
			utils.makeInvaderUnit(con.un('rome_praetorian'), iCiv, tPlot, 10)
			tSeaPlot = self.findSeaPlots(tPlot, 1, iCiv)
			if (tSeaPlot):
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_SETTLER_SEA, DirectionTypes.DIRECTION_SOUTH)
				utils.makeUnit(con.un('settler'), iCiv, tSeaPlot, 1)
				utils.makeUnit(con.un('archer'), iCiv, tSeaPlot, 1)
				utils.makeUnit(con.un('workboat'), iCiv, tSeaPlot, 1)
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_ASSAULT_SEA, DirectionTypes.DIRECTION_SOUTH)
				gc.getPlayer(iCiv).initUnit(con.un('galley'), tSeaPlot[0], tSeaPlot[1], UnitAITypes.UNITAI_ASSAULT_SEA, DirectionTypes.DIRECTION_SOUTH)
		if (iCiv == iMacedonia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('swordsman'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('hoplite'), iCiv, tPlot, 4)
			utils.makeInvaderUnit(con.un('greek_phalanx'), iCiv, tPlot, 3)
			utils.makeInvaderUnit(con.un('companion_cavalry'), iCiv, tPlot, 6)
			utils.makeUnit(con.un('confucian_missionary'), iCiv, tPlot, 1)
		if (iCiv == iIndia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 5)
			utils.makeUnit(con.un('horse_archer'), iCiv, tPlot, 4)
			utils.makeUnit(con.un('war_elephant'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('axeman'), iCiv, tPlot, 5)
			utils.makeUnit(con.un('indian_fast_worker'), iCiv, tPlot, 1)
		if (iCiv == iBactria):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 5)
			utils.makeUnit(con.un('horse_archer'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('hoplite'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('camel_cataphract'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('axeman'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('confucian_missionary'), iCiv, tPlot, 1)
		if (iCiv == iNumidia):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('carthage_numidian_cavalry'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('imajaghan'), iCiv, tPlot, 4)
		if (iCiv == iGermania):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('germanic_swordsman'), iCiv, tPlot, 13)
			utils.makeUnit(con.un('heavy_axeman'), iCiv, tPlot, 13)
		if (iCiv == iSassanid):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 4)
			utils.makeUnit(con.un('hoplite'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('auxillia'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('sassanid_azadan'), iCiv, tPlot, 5)
			utils.makeUnit(con.un('noble_cavalry'), iCiv, tPlot, 4)
			utils.makeUnit(con.un('war_elephant'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('catapult'), iCiv, tPlot, 2)
			utils.makeUnit(con.un('buddhist_missionary'), iCiv, tPlot, 1)
		if (iCiv == iByzantium):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('archer'), iCiv, tPlot, 3)
			utils.makeUnit(con.un('legion'), iCiv, tPlot, 6)
			utils.makeUnit(con.un('heavy_axeman'), iCiv, tPlot, 6)
			utils.makeUnit(con.un('rome_praetorian'), iCiv, tPlot, 6)
			utils.makeUnit(con.un('byzantine_cataphract'), iCiv, tPlot, 7)
			utils.makeUnit(con.un('christian_missionary'), iCiv, tPlot, 5)
		if (iCiv == iHuns):
			utils.makeUnit(con.un('settler'), iCiv, tPlot, 1)
			utils.makeUnit(con.un('legion'), iCiv, tPlot, 9)
			utils.makeUnit(con.un('heavy_axeman'), iCiv, tPlot, 7)
			utils.makeInvaderUnit(con.un('hun'), iCiv, tPlot, 14)

		#bluepotato: adopted from RFCCW
		#immobilize all units exceept 1 settler to prevent wandering before the flip
		if iCiv != utils.getHumanID():
			bSettler = False
			plot = gc.getMap().plot(tPlot[0], tPlot[1])
			iNumUnitsInAPlot = plot.getNumUnits()
			if (iNumUnitsInAPlot):
				for i in range(iNumUnitsInAPlot):
					unit = plot.getUnit(i)
					if (unit.getOwner() == iCiv):
						unitType = unit.getUnitType()
						if (unitType == con.un('settler') or unitType == con.un('harappan_city_builder')) and not bSettler:
							bSettler = True
						elif unit.getUnitAIType() != UnitAITypes.UNITAI_ATTACK_CITY: #invader units shouldn't be immobilized
							unit.setImmobileTimer(2)

	def addMissionary(self, iCiv, tTopLeft, tBottomRight, tPlot, iNumber):
		lReligions = [0, 0, 0, 0, 0, 0, 0]
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				pCurrent = gc.getMap().plot(x, y)
				if (pCurrent.isCity()):
					city = pCurrent.getPlotCity()
					iOwner = city.getOwner()
					if (iOwner != iCiv):
						iStateReligion = gc.getPlayer(iOwner).getStateReligion()
						if (iStateReligion >= 0 and iStateReligion < con.iNumReligions):
							lReligions[iStateReligion] += 1
		iMax = 0
		iWinnerReligion = -1
		for i in range(1, len(lReligions)+1): #so that Christianity comes first
			iLoopReligion = i % con.iNumReligions
			if (lReligions[iLoopReligion] > iMax):
				iMax = lReligions[iLoopReligion]
				iWinnerReligion = iLoopReligion

		if (iWinnerReligion == -1):
			for iLoopCiv in range(iNumMajorPlayers):
				if (iLoopCiv != iCiv):
					if (gc.getMap().plot(tPlot[0], tPlot[1]).isRevealed(iLoopCiv, False)):
						iStateReligion = gc.getPlayer(iLoopCiv).getStateReligion()
						if (iStateReligion >= 0 and iStateReligion < con.iNumReligions):
							lReligions[iStateReligion] += 1

			for iLoopReligion in range(1, len(lReligions)+1): #so that Christianity comes first
				iLoopReligion = i % con.iNumReligions
				if (lReligions[iLoopReligion] > iMax):
					iMax = lReligions[iLoopReligion]
					iWinnerReligion = iLoopReligion

		if (iWinnerReligion != -1):
			utils.makeUnit(con.un('jewish_missionary') + iWinnerReligion, iCiv, tPlot, iNumber)



	def createStartingWorkers(self, iCiv, tPlot):
		amount = 0
		if (iCiv == iIndusValley):
			amount = 1
		if (iCiv == iMinoa):
			amount = 1
		if (iCiv == iPhoenicia):
			amount = 1
		if (iCiv == iBabylonia):
			amount = 1
		if (iCiv == iHittites):
			amount = 1
		if (iCiv == iMycenae):
			amount = 1
		if (iCiv == iAssyria):
			amount = 1
		if (iCiv == iIsrael):
			amount = 1
		if (iCiv == iAthens):
			amount = 2
		if (iCiv == iSparta):
			amount = 2
		if (iCiv == iCarthage):
			amount = 3
		if (iCiv == iEtruria):
			amount = 2
		if (iCiv == iNubia):
			amount = 2
		if (iCiv == iPersia):
			amount = 3
		if (iCiv == iRome):
			amount = 3
		if (iCiv == iMacedonia):
			amount = 3
		if (iCiv == iIndia):
			amount = 3
		if (iCiv == iCeltia):
			amount = 1
		if (iCiv == iBactria):
			amount = 3
		if (iCiv == iNumidia):
			amount = 1
		if (iCiv == iSassanid):
			amount = 2
		if (iCiv == iByzantium):
			amount = 3

		utils.makeUnit(con.un('worker'), iCiv, tPlot, amount)

	def create900BCstartingUnits(self):
		for iLoopCiv in range(iNumMajorPlayers):
			if (tBirth[iLoopCiv] > utils.getScenarioStartYear() and iLoopCiv == utils.getHumanID()):
				self.assign900BCTechs(iLoopCiv)

			elif (tBirth[iLoopCiv] > utils.getScenarioStartYear() or iLoopCiv == utils.getHumanID()):
				self.assign900BCTechs(iLoopCiv)


	def create4400BCstartingUnits(self):

		#RFGW
		for iLoopCiv in range(iNumMajorPlayers):
			if (tBirth[iLoopCiv] == 0 or iLoopCiv == utils.getHumanID()):
				utils.makeUnit(con.un('settler'), iLoopCiv, tCapitals[iLoopCiv], 1)
				utils.makeUnit(con.un('warrior'), iLoopCiv, tCapitals[iLoopCiv], 1)
				self.assignTechs(iLoopCiv)
	

	def assign900BCTechs(self, iCiv):
		#popup = Popup.PyPopup()
		#popup.setBodyString('assigning techs to civ #%d' %(iCiv))
		#popup.launch()

		tCiv = gc.getTeam(gc.getPlayer(iCiv).getTeam())
		techs = None
		if (iCiv == iEgypt):
			techs = ('fermentation','mysticism','warrior_code','the_wheel','pottery','hunting','bread_making','urban_culture','mining','copper_working','masonry','fishing','slash_and_burn','arrows','logging','boats','agriculture','animal_husbandry','spokes','polytheism')
		if (iCiv == iPhoenicia):
			techs = ('fishing','logging','boats','hunting','navigation','slash_and_burn','the_wheel','bread_making','spokes','trade','sailing','fermentation','mining','mysticism','polytheism','copper_working','bronze_working','pottery','urban_culture')
		if (iCiv == iBabylonia):
			techs = ('cunniform','trade','slash_and_burn','fermentation','the_wheel','spokes','urban_culture','mining','hunting','arrows','logging','copper_working','warrior_code','masonry','bronze_working','fishing','bread_making','archery')
		if (iCiv == iAssyria):
			techs = ('cunniform','fermentation','bread_making','slash_and_burn','the_wheel','spokes','hunting','warrior_code','mining','arrows','copper_working','urban_culture','fortification','archery','military_training','bronze_working','logging','agriculture','pottery','fishing','metal_casting','iron_working')
		if (iCiv == iIsrael):
			techs = ('mysticism','polytheism','slash_and_burn','monotheism','the_wheel','fermentation','trade','alphabet','writing','fishing','urban_culture','priesthood','mining','hunting','arrows','bread_making','logging')
		if (iCiv == iAthens):
			techs = ('mining','bronze_working','masonry','fishing','mysticism','polytheism','spokes','the_wheel','pottery','hunting','animal_husbandry','trade','philosophy','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working','warrior_code','logging','mythology','arrows','boats')
		if (iCiv == iSparta):
			techs = ('mining','bronze_working','fortification','mysticism','polytheism','the_wheel','pottery','hunting','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working','warrior_code','logging','fishing','arrows','archery','animal_husbandry','military_training','mythology')
		if (iCiv == iScythia):
			techs = ('arrows','archery','hunting','warrior_code','mining','slash_and_burn','agriculture','animal_husbandry','equine_domestication','horseback_riding','copper_working','bronze_working','logging','bread_making','fermentation','mysticism','mythology')
		if (iCiv == iCarthage):
			techs = ('slash_and_burn','the_wheel','spokes','logging','trade','fishing','sailing','boats','mining','hunting','agriculture','bread_making','navigation','animal_husbandry','copper_working','bronze_working','fermentation','mysticism','polytheism','warrior_code','arrows','archery','urban_culture')
		if (iCiv == iCeltia):
			techs = ('logging','mining','bronze_working','iron_working','the_wheel','pottery','hunting','fermentation','bread_making','copper_working','warrior_code','urban_culture','fortification','mysticism','polytheism','spokes','slash_and_burn','agriculture','animal_husbandry')
		if (iCiv == iEtruria):
			techs = ('mining','masonry','the_wheel','pottery','hunting','animal_husbandry','archery','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working','warrior_code','logging','arrows','bronze_working','fishing','fortification','mysticism')
		if (iCiv == iNubia):
			techs = ('logging','arrows','mining','mysticism','polytheism','copper_working','the_wheel','pottery','agriculture','hunting','archery','animal_husbandry','slash_and_burn','fermentation','bread_making','warrior_code','bronze_working','fishing','urban_culture','masonry','metal_casting')
		if (iCiv == iPersia):
			techs = ('slash_and_burn','the_wheel','spokes','trade','cunniform','alphabet','writing','fermentation','pottery','herbalism','code_of_laws','urban_culture','mysticism','polytheism','priesthood','tyranny','hunting','warrior_code','mining','arrows','logging','copper_working','metal_casting','bronze_working','iron_working','agriculture')
		if (iCiv == iRome):
			techs = ('logging','trade','mining','bronze_working','iron_working','metal_casting','mysticism','polytheism','masonry','sailing','the_wheel','pottery','writing','alphabet','hunting','animal_husbandry','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working','warrior_code','spokes','mathematics','fishing','arrows','fortification','archery','military_training')
		if (iCiv == iMacedonia):
			techs = ('mining','mysticism','the_wheel','pottery','hunting','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working','warrior_code','animal_husbandry','bronze_working','equine_domestication','metal_casting','iron_working','horseback_riding','fortification','arrows','archery','fishing','logging','boats','mythology')
		if (iCiv == iIndia):
			techs = ('logging','trade','mining','bronze_working','mysticism','polytheism','the_wheel','pottery','writing','hunting','archery','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working','warrior_code','animal_husbandry','fishing','arrows','herbalism','code_of_laws','record_keeping','priesthood','tyranny','citizenship','education','medicine','boats','spokes','mythology','masonry','pachyderm_domestication','equine_domestication','horseback_riding','alphabet','mathematics','currency','storytelling')
		if (iCiv == iBactria):
			techs = ('slash_and_burn','warrior_code','agriculture','animal_husbandry','equine_domestication','pachyderm_domestication','camel_domestication','logging','trade','mining','bronze_working','mysticism','masonry','the_wheel','pottery','hunting','iron_working','urban_culture','fermentation','bread_making','copper_working','fortification','arrows','alphabet','mathematics','currency','fishing','polytheism','mythology','storytelling','archery','spokes','horseback_riding','cunniform','writing','construction','monotheism','aesthetics')
		if (iCiv == iNumidia):
			techs = ('slash_and_burn','the_wheel','spokes','logging','trade','fishing','boats','mining','hunting','agriculture','bread_making','animal_husbandry','copper_working','bronze_working','fermentation','mysticism','polytheism','warrior_code','arrows','archery','urban_culture','equine_domestication','camel_domestication','metal_casting','horseback_riding','iron_working','navigation','mythology','storytelling','pottery')
		if (iCiv == iGermania):
			techs = ('mining','bronze_working','iron_working','metal_casting','mysticism','the_wheel','pottery','hunting','animal_husbandry','equine_domestication','archery','fermentation','bread_making','copper_working','warrior_code','arrows','military_training','logging','fishing','mythology','spokes','trade','herbalism','slash_and_burn','polytheism','monotheism','cunniform','alphabet','writing','code_of_laws','tyranny','boats','navigation','agriculture','storytelling','urban_culture')
		if (iCiv == iSassanid):
			techs = ('slash_and_burn','the_wheel','spokes','trade','cunniform','alphabet','writing','fermentation','pottery','herbalism','code_of_laws','urban_culture','mysticism','polytheism','priesthood','tyranny','hunting','warrior_code',
'mining','arrows','agriculture','animal_husbandry','horseback_riding','record_keeping','citizenship','education','aristocracy','fishing','bread_making','logging','masonry','copper_working','metal_casting','bronze_working','iron_working','archery','boats','fortification','equine_domestication')
		if (iCiv == iByzantium):
			techs = ('fermentation','mysticism','polytheism','mythology','storytelling','slash_and_burn','the_wheel','spokes','trade','cunniform','alphabet','writing','pottery','herbalism','code_of_laws','urban_culture','priesthood','tyranny','citizenship','philosophy','democracy','theology','agriculture','animal_husbandry','equine_domestication','mining','copper_working','bronze_working','logging','fishing','boats','hunting','warrior_code','fortification','arrows','archery','military_training','mathematics','navigation','sailing','cartography','naval_warfare','bread_making','masonry','metal_casting','iron_working')
		if (iCiv == iHuns):
			techs = ('arrows','archery','hunting','warrior_code','mining','slash_and_burn','agriculture','animal_husbandry','equine_domestication','horseback_riding','copper_working','bronze_working','iron_working','metal_casting','mysticism','the_wheel','pottery','record_keeping','military_training','bread_making','fermentation','mythology','spokes','polytheism','trade','storytelling','cunniform','alphabet','pachyderm_domestication','writing','code_of_laws','tyranny','citizenship','philosophy','military_science','standing_army','herbalism')

		if techs is None: #if civ has no starting techs; TODO: should this really be called then?
			return
		
		self.assignPlayerTechs(iCiv, techs)

		self.hitNeighboursStability(iCiv) #RFGW

	def assignPlayerTechs(self, iCiv, techs):
		tCiv = gc.getTeam(gc.getPlayer(iCiv).getTeam())
		for i in range(len(techs)):
			tCiv.setHasTech(con.tn(techs[i]), True, iCiv, False, False)

	def assignTechs(self, iCiv):
		tCiv = gc.getTeam(gc.getPlayer(iCiv).getTeam())
		techs = None
		if (iCiv == iEgypt):
			techs = ('hunting', 'fishing')
		if (iCiv == iSumeria):
			techs = ('fermentation', 'bread_making')
		if (iCiv == iIndusValley):
			techs = ('agriculture', 'slash_and_burn', 'bread_making', 'logging')
		if (iCiv == iElam):
			techs = ('mining', 'hunting', 'bread_making', 'mysticism', 'warrior_code', 'logging', 'fishing')
		if (iCiv == iMinoa):
			techs = ('fishing', 'bread_making', 'urban_culture', 'masonry', 'mysticism', 'logging', 'boats', 'slash_and_burn', 'agriculture', 'fermentation')
		if (iCiv == iPhoenicia):
			techs = ('fishing', 'logging', 'boats', 'hunting', 'navigation', 'slash_and_burn', 'the_wheel', 'bread_making')
		if (iCiv == iBabylonia):
			techs = ('cunniform','trade','slash_and_burn','fermentation','the_wheel','spokes','urban_culture','mining','hunting','arrows','logging','copper_working')
		if (iCiv == iHittites):
			techs = ('mining','bronze_working','the_wheel','hunting','slash_and_burn','copper_working','logging','iron_working',
				'spokes','warrior_code','bread_making','urban_culture','fortification','agriculture','animal_husbandry','arrows')
		if (iCiv == iMycenae):
			techs = ('fermentation','mysticism','warrior_code','the_wheel','pottery','hunting','bread_making',
				'urban_culture','mining','copper_working','spokes','mythology','logging','fishing','boats')
		if (iCiv == iAssyria):
			techs = ('fermentation', 'bread_making','slash_and_burn','the_wheel','spokes','hunting', 'warrior_code','mining','arrows','copper_working','urban_culture','fortification','archery',
				'military_training','bronze_working','logging','agriculture','pottery')
		if (iCiv == iIsrael):
			techs = ('mysticism','polytheism','slash_and_burn','monotheism','the_wheel','fermentation','trade',
				'alphabet','writing','fishing','urban_culture','priesthood','mining','hunting','arrows','bread_making')
		if (iCiv == iAthens):
			techs = ('Mining','bronze_working','Masonry','Fishing','Mysticism','Polytheism','Spokes','the_wheel','Pottery','Hunting','animal_husbandry','Trade','Philosophy','Agriculture',
				'slash_and_burn', 'urban_culture','Fermentation','bread_making','copper_working','warrior_code','Logging','Mythology','Arrows','Boats')
		if (iCiv == iSparta):
			techs = ('Mining','Bronze_Working','Fortification','Mysticism','Polytheism','The_Wheel','Pottery','Hunting','Agriculture','Slash_And_Burn','Urban_Culture','Fermentation','Bread_Making',
				'Copper_Working','Warrior_Code', 'Logging','Fishing','Arrows','Archery','Animal_Husbandry','Military_Training','Mythology')
		if (iCiv == iScythia):
			techs = ('arrows','archery','hunting','warrior_code','mining','slash_and_burn','agriculture','animal_husbandry','equine_domestication','horseback_riding','copper_working',
				'bronze_working','logging','bread_making','fermentation','mysticism','mythology')
		if (iCiv == iCarthage):
			techs = ('slash_and_burn','the_wheel','spokes','logging','trade','fishing','sailing','boats','mining','hunting','agriculture','bread_making','navigation','animal_husbandry',
				'copper_working','bronze_working','fermentation','mysticism','polytheism','warrior_code','arrows','archery','urban_culture')
		if (iCiv == iCeltia):
			techs = ('logging','mining','bronze_working','iron_working','the_wheel','pottery','hunting','fermentation','bread_making','copper_working','warrior_code','urban_culture','fortification',
				'mysticism','polytheism','spokes','slash_and_burn','agriculture','animal_husbandry')
		if (iCiv == iEtruria):
			techs = ('mining','masonry','the_wheel','pottery','hunting','animal_husbandry','archery','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working',
				'warrior_code','logging','arrows','bronze_working','fishing','fortification','mysticism')
		if (iCiv == iNubia):
			techs = ('logging','arrows','mining','mysticism','polytheism','copper_working','the_wheel','pottery','agriculture','hunting','archery','animal_husbandry','slash_and_burn','fermentation',
				'bread_making','warrior_code','bronze_working','fishing','urban_culture','masonry','metal_casting')
		if (iCiv == iPersia):
			techs = ('slash_and_burn','the_wheel','spokes','trade','cunniform','alphabet','writing','fermentation','pottery','herbalism','code_of_laws','urban_culture','mysticism','polytheism',
				'priesthood','tyranny','hunting','warrior_code','mining','arrows','logging','copper_working','metal_casting','bronze_working','iron_working','agriculture')
		if (iCiv == iRome):
			techs = ('logging','trade','mining','bronze_working','iron_working','metal_casting','mysticism','polytheism','masonry','sailing','the_wheel','pottery','writing','alphabet','hunting',
				'animal_husbandry','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working','warrior_code','spokes','mathematics','fishing','arrows',
				'fortification','archery','military_training')
		if (iCiv == iMacedonia):
			techs = ('mining','mysticism','the_wheel','pottery','hunting','agriculture','slash_and_burn','urban_culture','fermentation','bread_making','copper_working','warrior_code',
				'animal_husbandry','bronze_working','equine_domestication','metal_casting','iron_working','horseback_riding','fortification','arrows','archery','fishing','logging','boats',
				'mythology')
		if (iCiv == iIndia):
			techs = ('logging','trade','mining','bronze_working','mysticism','polytheism','the_wheel','pottery','writing','hunting','archery','agriculture','slash_and_burn','urban_culture',
				'fermentation','bread_making','copper_working','warrior_code','animal_husbandry','fishing','arrows','herbalism','code_of_laws','record_keeping','priesthood','tyranny',
				'citizenship','education','medicine','boats','spokes','mythology','masonry','pachyderm_domestication','equine_domestication','horseback_riding','alphabet','mathematics',
				'currency','storytelling')
		if (iCiv == iBactria):
			techs = ('slash_and_burn','warrior_code','agriculture','animal_husbandry','equine_domestication','pachyderm_domestication','camel_domestication','logging','trade','mining',
			'bronze_working','mysticism','masonry','the_wheel','pottery','hunting','iron_working','urban_culture','fermentation','bread_making','copper_working','fortification','arrows','alphabet',
			'mathematics','currency','fishing','polytheism','mythology','storytelling','archery','spokes','horseback_riding','cunniform','writing','construction','monotheism','aesthetics')
		if (iCiv == iNumidia):
			techs = ('slash_and_burn','the_wheel','spokes','logging','trade','fishing','boats','mining','hunting','agriculture','bread_making','animal_husbandry','copper_working','bronze_working',
				'fermentation','mysticism','polytheism','warrior_code','arrows','archery','urban_culture','equine_domestication','camel_domestication','metal_casting','horseback_riding',
				'iron_working','navigation','mythology','storytelling','pottery')
		if (iCiv == iGermania):
			techs = ('mining','bronze_working','iron_working','metal_casting','mysticism','the_wheel','pottery','hunting','animal_husbandry','equine_domestication','archery','fermentation',
				'bread_making','copper_working','warrior_code','arrows','military_training','logging','fishing','mythology','spokes','trade','herbalism','slash_and_burn','polytheism','monotheism',
				'cunniform','alphabet','writing','code_of_laws','tyranny','boats','navigation','agriculture','storytelling','urban_culture')
		if (iCiv == iSassanid):
			techs = ('slash_and_burn','the_wheel','spokes','trade','cunniform','alphabet','writing','fermentation','pottery','herbalism','code_of_laws','urban_culture','mysticism','polytheism',
				'priesthood','tyranny','hunting','warrior_code','mining','arrows','agriculture','animal_husbandry','horseback_riding','record_keeping','citizenship','education','aristocracy',
				'fishing','bread_making','logging','masonry','copper_working','metal_casting','bronze_working','iron_working','archery','boats','fortification','equine_domestication')
		if (iCiv == iByzantium):
			techs = ('fermentation','mysticism','polytheism','mythology','storytelling','slash_and_burn','the_wheel','spokes','trade','cunniform','alphabet','writing','pottery','herbalism',
				'code_of_laws','urban_culture','priesthood','tyranny','citizenship','philosophy','democracy','theology','agriculture','animal_husbandry','equine_domestication','mining',
				'copper_working','bronze_working','logging','fishing','boats','hunting','warrior_code','fortification','arrows','archery','military_training','mathematics','navigation','sailing',
				'cartography','naval_warfare','bread_making','masonry','metal_casting','iron_working')
		if (iCiv == iHuns):
			techs = ('arrows','archery','hunting','warrior_code','mining','slash_and_burn','agriculture','animal_husbandry','equine_domestication','horseback_riding','copper_working',
				'bronze_working','iron_working','metal_casting','mysticism','the_wheel','pottery','record_keeping','military_training','bread_making','fermentation','mythology','spokes',
				'polytheism','trade','storytelling','cunniform','alphabet','pachyderm_domestication','writing','code_of_laws','tyranny','citizenship','philosophy','military_science',
				'standing_army','herbalism')

		
		self.assignPlayerTechs(iCiv, techs)

		self.hitNeighboursStability(iCiv)

	def hitNeighboursStability(self, iCiv):
		if (len(con.lOlderNeighbours[iCiv])):
			bHuman = False
			for iLoop in con.lOlderNeighbours[iCiv]:
				if (gc.getPlayer(iLoop).isAlive()):
					if (iLoop == utils.getHumanID()):
						bHuman = True
					utils.setStability(iLoop, utils.getStability(iLoop)-3)
			if (bHuman):
				utils.setStabilityParameters(con.iParDiplomacyE, utils.getStabilityParameters(con.iParDiplomacyE)-3)

	def spawnUnits(self, iCiv, tTopLeft, tBottomRight, iUnitType, iNumUnits, function, iForceAttack):
		dummy, plotList = utils.squareSearch(tTopLeft, tBottomRight, function, [])
		if (len(plotList)):
			rndNum = gc.getGame().getSorenRandNum(len(plotList), 'Spawn units')
			result = plotList[rndNum]
			if (result):
				self.makeUnit(iUnitType, iCiv, result, iNumUnits, iForceAttack)

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


