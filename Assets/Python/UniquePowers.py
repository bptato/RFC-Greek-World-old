# Rhye's and Fall of Civilization - (a part of) Unique Powers

#Egypt in CvPlayer::canDoCivics() and in WBS
#India in CvPlayer::updateMaxAnarchyTurns()
#China (and England before the change) in CvPlayer::getProductionNeeded()
#Babylonia in CvPlayer.cpp::acquireCity()
#Greece CvCity:getGreatPeopleRate()
#Carthage in MercenaryUtils.py and CvMercenarymanager.py
#Persia (USED TO BE in CvHandicapInfo::getDistanceMaintenancePercentByID(); THEN in RiseAndFall.py, collapseCapitals()), NOW in Stability.py, onCityAcquired()
#Rome in CvPlot::movementCost()
#Japan, Spain and England in CvUnit::init(). Turkey used to be there as well
#Ethiopia in Congresses.py (USED TO BE in CvUnit::init() and CvUnit::upgrade())
#Maya in CvHandicapInfo::getResearchPercentByID()
#Khmer in CvUnit::canMoveInto()
#Germany (USED TO BE IN in CvUnit::init(), CvUnit::upgrade() and CvUnitAI::AI_pillageValue()); NOW IN CvUnit::upgradePrice()
#France in CvPlayerAI::AI_getAttitudeVal() and in Congresses.py
#Netherlands in CvUnit::canEnterTerritory()
#Mali in CvPlot::calculateYield() and Stability.py and CvInfos.cpp (CvHandicapInfo::getResearchPercentByID())
#Portugal in CvUnit::init()
#Inca in CvPlot::calculateNatureYield()
#Mongolia (USED TO BE IN in CvUnit::pillage()); now HERE and in CvRFCEventHandler.py (in OnCityRazed() and BeginPlayerTurn())
#Turkey HERE + in CvPlayer::canRazeCity()
#America HERE + in CvCity::getCulturePercentAnger()

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


# initialise player variables
iEgypt = con.iEgypt
iSumeria = con.iSumeria
iIndusValley = con.iIndusValley
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

iNumReligions = con.iNumReligions


#Buildings



iMongolianRadius = 4
iMongolianTimer = 1



class UniquePowers:

     
##################################################
### Secure storage & retrieval of script data ###
################################################   

	def getImmigrationTurnLength( self ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		return scriptDict['iImmigrationTurnLength']

	def setImmigrationTurnLength( self, iNewValue ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		scriptDict['iImmigrationTurnLength'] = iNewValue
		gc.getGame().setScriptData( pickle.dumps(scriptDict) )

	def getImmigrationCurrentTurn( self ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		return scriptDict['iImmigrationCurrentTurn']

	def setImmigrationCurrentTurn( self, iNewValue ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		scriptDict['iImmigrationCurrentTurn'] = iNewValue
		gc.getGame().setScriptData( pickle.dumps(scriptDict) )	   

	def getLatestRazeData( self, i ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		return scriptDict['lLatestRazeData'][i]

	def setLatestRazeData( self, i, iNewValue ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		scriptDict['lLatestRazeData'][i] = iNewValue
		gc.getGame().setScriptData( pickle.dumps(scriptDict) )

	def getTempFlippingCity( self ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		return scriptDict['tempFlippingCity']

	def setTempFlippingCity( self, tNewValue ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		scriptDict['tempFlippingCity'] = tNewValue
		gc.getGame().setScriptData( pickle.dumps(scriptDict) ) 

	#for Victory

	def getEnslavedUnits( self ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		return scriptDict['iEnslavedUnits']
	    
	def setEnslavedUnits( self, iNewValue ):
		scriptDict = pickle.loads( gc.getGame().getScriptData() )
		scriptDict['iEnslavedUnits'] = iNewValue
		gc.getGame().setScriptData( pickle.dumps(scriptDict) )

#######################################
### Main methods (Event-Triggered) ###
#####################################  

       
	def checkTurn(self, iGameTurn):

##		if (iGameTurn >= con.i850BC):
 ##		       self.ScythianUP()

		#if (iGameTurn >= con.i850BC):
		if (iGameTurn >= 0): #debug
			for iTimer in range(iMongolianTimer+1):
				if (iGameTurn == self.getLatestRazeData(0)+iTimer):
					self.useMongolUP()

	def onBuildingBuilt(self, city, iOwner, iBuilding):
		if iOwner == iMinoa:
			self.MinoaUP(city, iBuilding)


#------------------ARABIAN U.P.-------------------

	def arabianUP(self, city):
		pByzantium = gc.getPlayer(iByzantium)
		iStateReligion = pByzantium.getStateReligion()
		if (iStateReligion >= 0):
			if (not city.isHasReligion(iStateReligion)):
				city.setHasReligion(iStateReligion, True, True, False)
			if (not city.hasBuilding(con.sbn('TEMPLE') + iStateReligion*4)):
				city.setHasRealBuilding((con.sbn('TEMPLE') + iStateReligion*4), True)
			if (not city.hasBuilding(con.sbn('CATHEDRAL') + iStateReligion*4)):
				city.setHasRealBuilding((con.sbn('CATHEDRAL') + iStateReligion*4), True)

#------------------AZTEC U.P.-------------------

	def aztecUP(self, argsList): #Real Slavery by Sevo
		pWinningUnit,pLosingUnit = argsList
		pWinningPlayer = gc.getPlayer(pWinningUnit.getOwner())

		if (pWinningPlayer.getID() != iAssyria):
			return

		pLosingPlayer = gc.getPlayer(pLosingUnit.getOwner())
		cLosingUnit = PyHelpers.PyInfo.UnitInfo(pLosingUnit.getUnitType())

		if (pLosingUnit.getUnitType() < con.un('warrior')):
			return

		# Only enslave land units!!
		if (cLosingUnit.getDomainType() == gc.getInfoTypeForString("DOMAIN_LAND")):
			iRandom = gc.getGame().getSorenRandNum(100, 'capture chance')
			if (iRandom < 50):
				pNewUnit = pWinningPlayer.initUnit(con.un('worker'), pWinningUnit.getX(), pWinningUnit.getY(), UnitAITypes.UNITAI_WORKER, DirectionTypes.DIRECTION_SOUTH)
				CyInterface().addMessage(pWinningPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_WIN", ()),'SND_REVOLTEND',1,'Art/Interface/Buttons/units/worker.dds',ColorTypes(8),pWinningUnit.getX(),pWinningUnit.getY(),True,True)
				CyInterface().addMessage(pLosingPlayer.getID(),True,15,CyTranslator().getText("TXT_KEY_UP_ENSLAVE_LOSE", ()),'SND_REVOLTEND',1,'Art/Interface/Buttons/units/worker.dds',ColorTypes(7),pWinningUnit.getX(),pWinningUnit.getY(),True,True)
				self.setEnslavedUnits(self.getEnslavedUnits() + 1)



#------------------ScythiaN U.P.-------------------

##	def ScythianUP(self):
##		pScythia = gc.getPlayer(iScythia)
##		teamScythia = gc.getTeam(pScythia.getTeam()) 
##		for x in range(tScythianTopLeft[0], tScythianBottomRight[0]):
##			for y in range(tScythianTopLeft[1], tScythianBottomRight[1]):
##				pCurrent = gc.getMap().plot( x, y )
##				if (pCurrent.getOwner() == iScythia):
##					iNumUnitsInAPlot = pCurrent.getNumUnits()
##				       if (iNumUnitsInAPlot):
##						for i in range(iNumUnitsInAPlot):
##							unit = pCurrent.getUnit(i)
##							if (teamScythia.isAtWar(unit.getOwner())):
##								print("hp", unit.currHitPoints() )
##								print("damage", unit.getDamage() )
##								unit.setDamage(unit.getDamage()+8, iScythia)
##								print("hp now", unit.currHitPoints() 
##								print("damage", unit.getDamage() )




#------------------TURKISH U.P.-------------------


	def turkishUP(self, city):
	       
		for x in range(city.getX()-2, city.getX()+3):
			for y in range(city.getY()-2, city.getY()+3):
				pCurrent = gc.getMap().plot( x, y )
				if (x == city.getX() and y == city.getY()):
					utils.convertPlotCulture(pCurrent, iMacedonia, 51, False)
				elif (pCurrent.isCity()):
					pass
				elif (utils.calculateDistance(x, y, city.getX(), city.getY()) == 1):
					utils.convertPlotCulture(pCurrent, iMacedonia, 80, True)
				else:
					utils.convertPlotCulture(pCurrent, iMacedonia, 20, False)





#------------------MONGOLIAN U.P.-------------------

	def setMongolAI(self):
		pCity = gc.getMap().plot( self.getLatestRazeData(3), self.getLatestRazeData(4) )
		city = pCity.getPlotCity()
		iOldOwner = self.getLatestRazeData(1)
		print ("Mongol AI", iOldOwner)

		if (pCity.getNumUnits() > 0):
			for i in range(pCity.getNumUnits()):
				unit = pCity.getUnit(i)
				if (unit.getOwner() == iHuns):
					if (unit.baseMoves() == 2):
						unit.setMoves(2)
					if (unit.baseMoves() == 1):
						unit.setMoves(1)

##		targetCity = -1
##		if (not pMongolia.isHuman()):
##			for x in range(self.getLatestRazeData(3) -3, self.getLatestRazeData(3) +1 +3):
##				for y in range(self.getLatestRazeData(4) -3, self.getLatestRazeData(4) +1 +3):
##					pCurrent = gc.getMap().plot( x, y )
##					if ( pCurrent.isCity()):
##						cityNear = pCurrent.getPlotCity()
##						iOwnerNear = cityNear.getOwner()
##						if (cityNear.getName() != city.getName()):
##							print ("iOwnerNear", iOwnerNear, "citynear", cityNear.getName())
##							if (iOwnerNear == iOldOwner):
##								if (cityNear != city):
##									if (cityNear.getPopulation() <= self.getLatestRazeData(2)):
##										targetCity = cityNear
##										print ("targetCity", targetCity)
##										break
##										break
##			if (targetCity != -1):
##				targetPlot = -1
##				for j in range(targetCity.getX() -1, targetCity.getX() +1 +2):
##					for k in range(targetCity.getY() -1, targetCity.getY() +1 +2):
##						pCurrentTarget = gc.getMap().plot( j, k )
##						if (pCurrentTarget.getNumUnits() == 0):
##							iDistance = gc.getMap().calculatePathDistance(pCurrentTarget, pCity)
##							if (iDistance <= 2):
##								targetPlot = pCurrentTarget
##								print ("pCurrentTarget", pCurrentTarget)
##								break
##								break
##				for m in range(city.getX() -1, city.getX() +1 +2):
##					for n in range(city.getY() -1, city.getY() +1 +2):
##						pMongol = gc.getMap().plot( m, n )
##						if (pMongol.getNumUnits() > 0):
##							print ("numunits>0")
##							for i in range(pCity.getNumUnits()):
##								unit = pCity.getUnit(i)
##								if (unit.getOwner() == iMongolia):
##									#if (unit.getMoves() >= 2):
##									print ("unit", unit)
##									unit.setXY(targetPlot.getX(), targetPlot.getY())
##									break
##									break
##									break



	def useMongolUP(self):
		iOldOwner = self.getLatestRazeData(1)
		pCity = gc.getMap().plot( self.getLatestRazeData(3), self.getLatestRazeData(4) )
		city = pCity.getPlotCity()
		print ("Mongol UP", iOldOwner)
		for x in range(self.getLatestRazeData(3) -iMongolianRadius, self.getLatestRazeData(3) +1 +iMongolianRadius):
			for y in range(self.getLatestRazeData(4) -iMongolianRadius, self.getLatestRazeData(4) +1 +iMongolianRadius):
				pCurrent = gc.getMap().plot( x, y )
				if ( pCurrent.isCity()):
					cityNear = pCurrent.getPlotCity()
					iOwnerNear = cityNear.getOwner()
					if (cityNear.getName() != city.getName()):
						print ("iOwnerNear", iOwnerNear, "citynear", cityNear.getName())
						if (iOwnerNear == iOldOwner or iOwnerNear == iIndependent or iOwnerNear == iIndependent2):
							print ("citynear", cityNear.getName(), "passed")
							if (cityNear.getPopulation() <= self.getLatestRazeData(2) and not cityNear.isCapital()):
								print ("citynear", cityNear.getName(), "passed")
								iApproachingUnits = 0
								for j in range(cityNear.getX() -1, cityNear.getX() +2):
									for k in range(cityNear.getY() -1, cityNear.getY() +2):
										pNear = gc.getMap().plot( j, k )
										if (pNear.getNumUnits() > 0):
											for l in range(pNear.getNumUnits()):
												if(pNear.getUnit(l).getOwner() == iHuns):
													iApproachingUnits += 1
													break
													break
													break								
								if (iApproachingUnits > 0):
									utils.flipUnitsInCityBefore((x,y), iHuns, iOwnerNear)
									self.setTempFlippingCity((x,y))
									utils.flipCity((x,y), 0, 0, iHuns, [iOwnerNear])
									utils.flipUnitsInCityAfter(self.getTempFlippingCity(), iHuns)
									utils.cultureManager(self.getTempFlippingCity(), 50, iOwnerNear, iHuns, False, False, False)
									CyInterface().addMessage(iOwnerNear, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_TERROR1", ()) + " " + cityNear.getName() + " " + CyTranslator().getText("TXT_KEY_UP_TERROR2", ()), "", 0, "", ColorTypes(con.iWhite), -1, -1, True, True)
									CyInterface().addMessage(iHuns, False, con.iDuration, CyTranslator().getText("TXT_KEY_UP_TERROR1", ()) + " " + cityNear.getName() + " " + CyTranslator().getText("TXT_KEY_UP_TERROR2", ()), "", 0, "", ColorTypes(con.iWhite), -1, -1, True, True)


# Minoa UP: receives 50% of building cost as culture when building is completed
	def MinoaUP(self, city, iBuilding):
	    iCost = gc.getPlayer(iMinoa).getBuildingProductionNeeded(iBuilding)
	    city.changeCulture(iMinoa, iCost / 2, True)
	    
#------------------Bactria UP---------------- (former Chalukya)

	def SiamUP(self, playerType, city, bConquest):

		if (bConquest):
			capital = gc.getPlayer(playerType).getCapitalCity()
			Artist =  gc.getInfoTypeForString("SPECIALIST_ARTIST")
			capital.setFreeSpecialistCount(Artist, capital.getFreeSpecialistCount(Artist) + 1)
 
 #------------------Mycenae UP---------------- (former Chalukya)
 
	
