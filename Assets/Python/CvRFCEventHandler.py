from CvPythonExtensions import *
import CvUtil
import CvEventManager #Mercenaries
import sys #Mercenaries
import PyHelpers 
import CvMainInterface #Mercenaries
import CvMercenaryManager #Mercenaries
import MercenaryUtils #Mercenaries
import CvScreenEnums  #Mercenaries
#import CvConfigParser #Mercenaries #Rhye
import Popup as PyPopup 

import StoredData
import RiseAndFall	
import Barbs			  
import CityNameManager  
import UniquePowers     
import AIWars	   
import Consts as con 
import RFCUtils
utils = RFCUtils.RFCUtils()
import CvScreenEnums #Mercenaries, Rhye
import Victory
import Stability
import Plague
import Communications
	
gc = CyGlobalContext()	
#iBetrayalCheaters = 15


#Rhye - start
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
#Rhye - end



#Mercenaries - start
objMercenaryUtils = MercenaryUtils.MercenaryUtils()

PyPlayer = PyHelpers.PyPlayer
PyGame = PyHelpers.PyGame()
PyInfo = PyHelpers.PyInfo

# Set g_bGameTurnMercenaryCreation to true if mercenary creation should happen during the 
# onBeginGameTurn method, false if it should happen during the onBeginPlayerTurn method
# Default value is true
g_bGameTurnMercenaryCreation = true

# Set g_bDisplayMercenaryManagerOnBeginPlayerTurn to true if the "Mercenary Manager" 
# screen should be displayed at the beginning of every player turn. 
# Default value is false
g_bDisplayMercenaryManagerOnBeginPlayerTurn = false

# This value also controls the "Mercenary Manager" button and when it should be displayed.
# Default value is "ERA_ANCIENT"
#Rhye - start (was causing an assert)
#g_iStartingEra = gc.getInfoTypeForString("ERA_ANCIENT")
g_iStartingEra = 0
#Rhye - end

# Change this to false if mercenaries should be removed from the global mercenary pool 
# at the beginning of the game turn. When set to true a number of mercenaries will 
# wander away from the global mercenary pool. This is another variable used to control 
# the load time for the "Mercenary Manager" screen.
# Default valus is true
g_bWanderlustMercenaries = true

# Change this to increase the max number of mercenaries that may wander away from the
# global mercenary pool.
# Default valus is 3
g_iWanderlustMercenariesMaximum = 7 #Rhye

# Default valus is 0 
g_iWanderlustMercenariesMinimum = 2 #Rhye

# Change this to false to supress the mercenary messages.
# Default value is true
g_bDisplayMercenaryMessages = false #Rhye

# Set to true to print out debug messages in the logs
g_bDebug = false

# Default valus is 1 
g_bUpdatePeriod = 5 #Rhye

# Default valus is 1 
g_bAIThinkPeriod = 6 #Rhye (5 in Warlords, 4 in vanilla)

# globals

#Mercenaries - end


###################################################
class CvRFCEventHandler:



	mercenaryManager = None #Mercenaries


	def __init__(self, eventManager):

		self.EventKeyDown=6 #Mercenaries

		# initialize base class
		eventManager.addEventHandler("GameStart", self.onGameStart) #Stability
		eventManager.addEventHandler("BeginGameTurn", self.onBeginGameTurn) #Stability
		eventManager.addEventHandler("cityAcquired", self.onCityAcquired) #Stability
		eventManager.addEventHandler("cityRazed", self.onCityRazed) #Stability
		eventManager.addEventHandler("cityBuilt", self.onCityBuilt) #Stability
		eventManager.addEventHandler("combatResult", self.onCombatResult) #Stability
		#eventManager.addEventHandler("changeWar", self.onChangeWar)
		eventManager.addEventHandler("religionFounded",self.onReligionFounded) #Victory
		eventManager.addEventHandler("buildingBuilt",self.onBuildingBuilt) #Victory
		eventManager.addEventHandler("projectBuilt",self.onProjectBuilt) #Victory
		eventManager.addEventHandler("BeginPlayerTurn", self.onBeginPlayerTurn) #Mercenaries
		#eventManager.addEventHandler("EndPlayerTurn", self.onEndPlayerTurn)
		eventManager.addEventHandler("EndGameTurn", self.onEndGameTurn) #Stability
		eventManager.addEventHandler("kbdEvent",self.onKbdEvent) #Mercenaries
		eventManager.addEventHandler("unitLost",self.onUnitLost) #Mercenaries
		eventManager.addEventHandler("unitKilled",self.onUnitKilled) #Mercenaries
		eventManager.addEventHandler("OnLoad",self.onLoadGame) #Mercenaries
		eventManager.addEventHandler("unitPromoted",self.onUnitPromoted) #Mercenaries
		eventManager.addEventHandler("techAcquired",self.onTechAcquired) #Mercenaries, Rhye #Stability
		#eventManager.addEventHandler("improvementDestroyed",self.onImprovementDestroyed) #Stability
		eventManager.addEventHandler("religionSpread",self.onReligionSpread) #Stability
		eventManager.addEventHandler("firstContact",self.onFirstContact)
		eventManager.addEventHandler("corporationFounded",self.onCorporationFounded) #Stability
		


	       
		self.eventManager = eventManager

		self.data = StoredData.StoredData()
		self.rnf = RiseAndFall.RiseAndFall()
		self.barb = Barbs.Barbs()
##		self.rel = Religions.Religions()
##		self.res = Resources.Resources()
		self.cnm = CityNameManager.CityNameManager()
		self.up = UniquePowers.UniquePowers()
		self.aiw = AIWars.AIWars()
		self.vic = Victory.Victory()
		self.sta = Stability.Stability()
		self.pla = Plague.Plague()
		self.com = Communications.Communications()
		
		
		#Mercenaries - start
		
		self.mercenaryManager = CvMercenaryManager.CvMercenaryManager(CvScreenEnums.MERCENARY_MANAGER)	

		global g_bGameTurnMercenaryCreation
		global g_bDisplayMercenaryManagerOnBeginPlayerTurn
		global g_iStartingEra
		global g_bWanderlustMercenaries
		global g_iWanderlustMercenariesMaximum
		global g_bDisplayMercenaryMessages 

		#Rhye - start comment
##		# Load the Mercenaries Mod Config INI file containing all of the configuration information		
##		config = CvConfigParser.CvConfigParser("Mercenaries Mod Config.ini")
##
##		# If we actually were able to open the "Mercenaries Mod Config.ini" file then read in the values.
##		# otherwise we'll keep the default values that were set at the top of this file.
##		if(config != None):
##			g_bGameTurnMercenaryCreation = config.getboolean("Mercenaries Mod", "Game Turn Mercenary Creation", true)
##			g_bDisplayMercenaryManagerOnBeginPlayerTurn = config.getboolean("Mercenaries Mod", "Display Mercenary Manager On Begin Player Turn", false)
##			g_iStartingEra = gc.getInfoTypeForString(config.get("Mercenaries Mod","Starting Era","ERA_ANCIENT"))
##			g_bWanderlustMercenaries = config.getboolean("Mercenaries Mod", "Wanderlust Mercenaries", true)
##			g_iWanderlustMercenariesMaximum = config.getint("Mercenaries Mod","Wanderlust Mercenaries Maximum", 5)
##			g_bDisplayMercenaryMessages = config.getboolean("Mercenaries Mod", "Display Mercenary Messages", true)
		#Rhye - end comment

		objMercenaryUtils = MercenaryUtils.MercenaryUtils()
		#Mercenaries - end


	def onGameStart(self, argsList):
		'Called at the start of the game'
		self.data.setupScriptData()
		self.rnf.setup()
		self.pla.setup()
		self.sta.setup()
		self.aiw.setup()
		self.rnf.warOnSpawn()

		

		#Mercenaries - start
		global objMercenaryUtils	
		objMercenaryUtils = MercenaryUtils.MercenaryUtils()
		#Mercenaries - end
		
		return 0


	def onCityAcquired(self, argsList):
		#'City Acquired'
		owner,playerType,city,bConquest,bTrade = argsList
		#CvUtil.pyPrint('City Acquired Event: %s' %(city.getName()))
		self.cnm.renameCities(city, playerType)

		#RFGW
		iPlayer = playerType
		feedUnits = con.getFeedUnits(iPlayer)
		if (feedUnits > 0):
			self.rnf.spawnUnits(iPlayer, (city.getX()-5,city.getY()-5), (city.getX()+5,city.getY()+5), feedUnits, 1, utils.outerInvasion, 1)

		
	       
		if (playerType == con.iByzantium):
			self.up.arabianUP(city)
		elif (playerType == con.iBactria):
			self.up.SiamUP(playerType, city, bConquest)
		elif (playerType == con.iMacedonia):
			self.up.turkishUP(city)
##
##		if (playerType < iNumMajorPlayers):
##			 utils.spreadMajorCulture(playerType, city.getX(), city.getY())
##
		self.sta.onCityAcquired(owner,playerType,city,bConquest,bTrade)

		self.pla.onCityAcquired(owner,playerType,city) #Plague
##
##		self.com.onCityAcquired(city) #Communications
##
		self.vic.onCityAcquired(owner, playerType, city, bConquest) #Victory
		
		return 0

	def onCityRazed(self, argsList):
		#'City Razed'
		city, iPlayer = argsList

		self.sta.onCityRazed(city.getOwner(),iPlayer,city)
		
##		if (iPlayer == con.iHuns):
##			self.up.setLatestRazeData(0, gc.getGame().getGameTurn())
##			owner = city.getOwner()
##			if (city.getOwner() == iPlayer):
##				if (city.getPreviousOwner() != -1):
##					owner = city.getPreviousOwner()			
##			self.up.setLatestRazeData(1, owner)
##			self.up.setLatestRazeData(2, city.getPopulation())
##			self.up.setLatestRazeData(3, city.getX())
##			self.up.setLatestRazeData(4, city.getY())
##			print ("city.getPopulation()", city.getPopulation())
##			print ("prev", city.getPreviousOwner(), "curr", city.getOwner())
##			self.up.setMongolAI()

		self.pla.onCityRazed(city,iPlayer) #Plague
		
		feedUnits = con.getFeedUnits(iPlayer)
		if (feedUnits > 0):
			self.rnf.spawnUnits(iPlayer, (city.getX()-5,city.getY()-5), (city.getX()+5,city.getY()+5), feedUnits, 1, utils.outerInvasion, 1)
		
		self.vic.onCityRazed(city, iPlayer, city.getOwner()) #Victory



	def onCityBuilt(self, argsList):
		'City Built'
		city = argsList[0]
		
		iOwner = city.getOwner()
		
		if (iOwner < con.iNumActivePlayers): 
			self.cnm.assignName(city)
##
##
##		#Rhye - delete culture of barbs and minor civs to prevent weird unhappiness
##		pCurrent = gc.getMap().plot(city.getX(), city.getY())
##		for i in range(con.iNumTotalPlayers - con.iNumActivePlayers):
##			iMinorCiv = i + con.iNumActivePlayers
##			pCurrent.setCulture(iMinorCiv, 0, True)
##		pCurrent.setCulture(con.iBarbarian, 0, True)
##
##		if iOwner < iNumMajorPlayers:
##			utils.spreadMajorCulture(iOwner, tCity)
##			if gc.getPlayer(iOwner).getNumCities() < 2:
##				gc.getPlayer(iOwner).AI_updateFoundValues(False); # fix for settler maps not updating after 1st city is founded
##
##
		if (iOwner == con.iMacedonia):
			self.up.turkishUP(city)
##		if iOwner == con.iIndusValley:
##			self.up.indusvalleyUP(city)
		if (iOwner == con.iEgypt):    
			self.vic.onCityBuilt(city, iOwner) #Victory
##
		if (iOwner < con.iNumPlayers):
			self.sta.onCityBuilt(iOwner, city.getX(), city.getY())		 

	def onCombatResult(self, argsList):
		pass
		self.up.aztecUP(argsList)
		self.vic.onCombatResult(argsList)
		self.sta.onCombatResult(argsList)
		self.rnf.immuneMode(argsList)



##	def onChangeWar(self, argsList):
##		print ("No cheaters1")
##		if (bIsWar):
##			print ("No cheaters2")
##			if (argsList[1] == utils.getHumanID() and gc.getGame().getGameTurn() <= con.tBirth[argsList[1]] + iBetrayalCheaters):
##				print ("No cheaters3")
##				self.rnf.setNewCivFlip(argsList[1])
##				self.rnf.setTempTopLeft(rnf.tCoreAreasTL[argsList[1]])
##				self.rnf.setTempBottomRight(rnf.tCoreAreasBR[argsList[1]])
##				self.rnf.setBetrayalTurns(rnf.iBetrayalPeriod)
##				self.rnf.initBetrayal()



	def onReligionFounded(self, argsList):
		'Religion Founded'
		iReligion, iFounder = argsList

		pass

##		if (not gc.getPlayer(0).isPlayable() and gc.getGame().getGameTurn() == 181): #late start condition
##			return
##	
		self.vic.onReligionFounded(iReligion, iFounder)
##	
		if (iFounder < con.iNumPlayers):
			self.sta.onReligionFounded(iFounder)


	def onCorporationFounded(self, argsList):
		'Corporation Founded'
		iCorporation, iFounder = argsList
		#player = PyPlayer(iFounder)
		
		if (iFounder < con.iNumPlayers):
			self.sta.onCorporationFounded(iFounder)


			

	def onBuildingBuilt(self, argsList):
		city, iBuildingType = argsList
		iOwner = city.getOwner()
		self.up.onBuildingBuilt(city, iOwner, iBuildingType)
		self.vic.onBuildingBuilt(city.getOwner(), iBuildingType)
		if (city.getOwner() < con.iNumPlayers):
			self.sta.onBuildingBuilt(iOwner, iBuildingType, city)
##			self.com.onBuildingBuilt(iOwner, iBuildingType, city)
##		self.cong.onBuildingBuilt(iOwner, iBuildingType, city)

	def onProjectBuilt(self, argsList):
		city, iProjectType = argsList
		self.vic.onProjectBuilt(city.getOwner(), iProjectType)
		if (city.getOwner() < con.iNumPlayers):
			self.sta.onProjectBuilt(city.getOwner(), iProjectType)

	def onImprovementDestroyed(self, argsList):
		pass
		#iImprovement, iOwner, iX, iY = argsList
		if (iOwner < con.iNumPlayers):
			self.sta.onImprovementDestroyed(iOwner)	   
		
	def onBeginGameTurn(self, argsList):
		iGameTurn = argsList[0]

		print ("iGameTurn", iGameTurn)
		self.printDebug(iGameTurn)

		
		self.rnf.checkTurn(iGameTurn)
		self.barb.checkTurn(iGameTurn)
##		self.rel.checkTurn(iGameTurn)
##		self.res.checkTurn(iGameTurn)
		self.up.checkTurn(iGameTurn)
		self.aiw.checkTurn(iGameTurn)
		self.pla.checkTurn(iGameTurn)
		self.sta.checkTurn(iGameTurn)

		#Mercenaries - start

		if (gc.getGame().getGameTurn() >= con.tBirth[utils.getHumanID()]):
			
			# Get the list of active players in the game
			playerList = PyGame.getCivPlayerList()
			
			# Go through each of the players and deduct their mercenary maintenance amount from their gold
			for i in range(len(playerList)):
				playerList[i].setGold(playerList[i].getGold()-objMercenaryUtils.getPlayerMercenaryMaintenanceCost(playerList[i].getID()))
				playerList[i].setGold(playerList[i].getGold()+objMercenaryUtils.getPlayerMercenaryContractIncome(playerList[i].getID()))
		
			# Have some mercenaries wander away from the global mercenary pool if 
			# g_bWanderlustMercenaries is set to true.	
			if(g_bWanderlustMercenaries):

				#Rhye - start (less frequent updates)
				#wanderingMercenaryCount = gc.getGame().getMapRand().get(g_iWanderlustMercenariesMaximum, "Random Num")
				#objMercenaryUtils.removeMercenariesFromPool(wanderingMercenaryCount)
				teamPlayer = gc.getTeam(gc.getActivePlayer().getTeam())
				if (iGameTurn % g_bUpdatePeriod == (g_bUpdatePeriod-1)):
					wanderingMercenaryCount = gc.getGame().getMapRand().get(g_iWanderlustMercenariesMaximum, "Random Num") + g_iWanderlustMercenariesMinimum
					objMercenaryUtils.removeMercenariesFromPool(wanderingMercenaryCount)
				#Rhye - end
			    
				
			# Add the mercenaries to the global mercenary pool if the g_bGameTurnMercenaryCreation 
			# is set to true
			if(g_bGameTurnMercenaryCreation):
			    
				#Rhye - start (less frequent updates)
				#objMercenaryUtils.addMercenariesToPool()		  
				if (iGameTurn % g_bUpdatePeriod == (g_bUpdatePeriod-1)):
					objMercenaryUtils.addMercenariesToPool()
				#Rhye - end		
		return 0



	def onBeginPlayerTurn(self, argsList):	
		iGameTurn, iPlayer = argsList

		#print ("PLAYER", iPlayer)
##		if (iPlayer == con.iHuns):
##			if (iGameTurn == self.up.getLatestRazeData(0) +1):
##				self.up.setMongolAI()

##		if (self.rnf.getDeleteMode(0) != -1):
##			self.rnf.deleteMode(iPlayer)
##			
##
		print ("onBeginPlayerTurn", iPlayer)
		if (gc.getPlayer(iPlayer).isAlive() and not gc.getPlayer(iPlayer).isMinorCiv() and gc.getPlayer(iPlayer).getNumCities() > 0):
			print ("plague check ", iPlayer)
			self.pla.checkPlayerTurn(iGameTurn, iPlayer)
			print ("victory check ", iPlayer)
			self.vic.checkPlayerTurn(iGameTurn, iPlayer)
			print ("stability check ", iPlayer)
			self.sta.updateBaseStability(iGameTurn, iPlayer)
		print ("done ", iPlayer)
		return # TODO: mercenaries
##
##		if (gc.getPlayer(iPlayer).isAlive() and iPlayer < con.iNumPlayers and not gc.getPlayer(iPlayer).isHuman()):
##			self.rnf.checkPlayerTurn(iGameTurn, iPlayer) #for leaders switch

		#Mercenaries - start
	
		# This method will add mercenaries to the global mercenary pool, display the mercenary manager screen
		# and provide the logic to make the computer players think.
		player = gc.getPlayer(iPlayer)

		if (gc.getGame().getGameTurn() >= con.tBirth[utils.getHumanID()]): #Rhye

			# Debug code - start
			if(g_bDebug):
				CvUtil.pyPrint(player.getName() + " Gold: " + str(player.getGold()) + " is human: " + str(player.isHuman()))
			# Debug code - end	
			
			# Add the mercenaries to the global mercenary pool if the 
			# g_bGameTurnMercenaryCreation is set to false
			if(not g_bGameTurnMercenaryCreation):
				objMercenaryUtils.addMercenariesToPool()

			# if g_bDisplayMercenaryManagerOnBeginPlayerTurn is true the the player is human
			# then display the mercenary manager screen
			if(g_bDisplayMercenaryManagerOnBeginPlayerTurn and player.isHuman()):
				self.mercenaryManager.interfaceScreen()

			# if the player is not human then run the think method
			if(not player.isHuman()):
			    
				#Rhye - start
				#objMercenaryUtils.computerPlayerThink(iPlayer)					
				if (player.isAlive()):
					if (iPlayer % (g_bAIThinkPeriod) == iGameTurn % (g_bAIThinkPeriod)):
						print ("AI thinking (Mercenaries)", iPlayer) #Rhye
						objMercenaryUtils.computerPlayerThink(iPlayer)								
				#Rhye - end
		
			# Place any mercenaries that might be ready to be placed.
			#objMercenaryUtils.placeMercenaries(iPlayer)
		#print ("PLAYER FINE", iPlayer)

	
	def onEndPlayerTurn(self, argsList):

		iGameTurn, iPlayer = argsList
		print ("END PLAYER", iPlayer)
		
		'Called at the end of a players turn'

	def onEndGameTurn(self, argsList):
	    
		iGameTurn = argsList[0]
		print "sta.checkImplosion"
		self.sta.checkImplosion(iGameTurn)
		print "sta.checkImplosion done"


	def onReligionSpread(self, argsList):
	    
		iReligion, iOwner, pSpreadCity = argsList
		self.sta.onReligionSpread(iReligion, iOwner)	     

	def onFirstContact(self, argsList):
	    
		iTeamX,iHasMetTeamY = argsList
##		self.rnf.onFirstContact(iTeamX, iHasMetTeamY)
##		self.pla.onFirstContact(iTeamX, iHasMetTeamY)
		#RFGW
		if (con.getFeedUnits(iTeamX) > 0 and iHasMetTeamY<iNumMajorPlayers):
			if (gc.getGame().getGameTurn() > con.tBirth[iTeamX]):
				self.rnf.spawnUnits(iTeamX, con.tCoreAreasTL[iHasMetTeamY], con.tCoreAreasBR[iHasMetTeamY], con.getFeedUnits(iTeamX), 1, utils.outerInvasion, 1)


	#Rhye - start
	def onTechAcquired(self, argsList):

		#print ("onTechAcquired", argsList)
		iPlayer = argsList[2]

		iHuman = utils.getHumanID()
				
		if (gc.getGame().getGameTurn() > con.tBirth[iPlayer]):		    
			if (iPlayer == con.iPhoenicia or \
			    iPlayer == con.iMinoa or \
			    iPlayer == con.iSumeria):			    
				self.vic.onTechAcquired(argsList[0], argsList[2])
			self.cnm.onTechAcquired(argsList[2])
##		
		if (gc.getPlayer(iPlayer).isAlive() and gc.getGame().getGameTurn() > con.tBirth[iPlayer] and not gc.getPlayer(iPlayer).isMinorCiv()):
			self.sta.onTechAcquired(argsList[0], argsList[2])

		
		



	# This method creates a new instance of the MercenaryUtils class to be used later
	def onLoadGame(self, argsList):
		if gc.getGame().getGameTurn() >= con.tBirth[utils.getHumanID()]: #Rhye

			global objMercenaryUtils

			objMercenaryUtils = MercenaryUtils.MercenaryUtils()



	# This method will redraw the main interface once a unit is promoted. This way the 
	# gold/turn information will be updated.	
	def onUnitPromoted(self, argsList):
		'Unit Promoted'

		if (gc.getGame().getGameTurn() >= con.tBirth[utils.getHumanID()]): #Rhye	
			pUnit, iPromotion = argsList
			player = PyPlayer(pUnit.getOwner())

			if(objMercenaryUtils.isMercenary(pUnit)):
				CyInterface().setDirty(InterfaceDirtyBits.GameData_DIRTY_BIT, True)




	# This method will remove a mercenary unit from the game if it is killed
	def onUnitKilled(self, argsList):
		'Unit Killed'

		if (gc.getGame().getGameTurn() >= con.tBirth[utils.getHumanID()]): #Rhye
		    
			unit, iAttacker = argsList
			
			mercenary = objMercenaryUtils.getMercenary(unit.getNameNoDesc())

			if(mercenary != None and g_bDisplayMercenaryMessages and mercenary.getBuilder() != -1 and unit.isDead()):
				strMessage = mercenary.getName() + " has died under " + gc.getPlayer(mercenary.getOwner()).getName() + "'s service."
				# Inform the player that the mercenary has died.
				CyInterface().addMessage(mercenary.getBuilder(), True, 20, strMessage, "", 0, "", ColorTypes(0), -1, -1, True, True) 

			objMercenaryUtils.removePlayerMercenary(unit)


	# This method will remove a mercenary unit from the game if it is lost
	def onUnitLost(self, argsList):
		'Unit Lost'

		if (gc.getGame().getGameTurn() >= con.tBirth[utils.getHumanID()]): #Rhye
	
			unit = argsList[0]
			
			# Debug code - start
			if(g_bDebug):
				CvUtil.pyPrint("lost: " + unit.getName())
			# Debug code - end
			
			# If the unit being lost is a mercenary, check to see if they have been
			# replaced by an upgraded version of themselves. If they are then save
			# the new upgraded version of themselves and return immediately.
			if(objMercenaryUtils.isMercenary(unit)):

				# Debug code - start
				if(g_bDebug):	
					CvUtil.pyPrint("mercenary unit lost: " + unit.getName())
				# Debug code - end
					
				# Get the active player ID
				iPlayer = gc.getGame().getActivePlayer()
				
				# Get the reference of the actual player
				pyPlayer = PyPlayer(iPlayer)

				# Get the list of units for the player
				unitList = pyPlayer.getUnitList()
					
				# Go through the list of units to see if an upgraded version of 
				# the unit has been added. If it exists then save it and return
				# immediately.
				for unit in unitList:

					if(unit.getUnitType() != argsList[0].getUnitType() and unit.getNameNoDesc() == argsList[0].getNameNoDesc()):

						# Debug code - start
						if(g_bDebug):	
							CvUtil.pyPrint("mercenary unit upgraded: " + unit.getName())
						# Debug code - end
						
						tmpMerc = objMercenaryUtils.createBlankMercenary()
						tmpMerc.loadUnitData(unit)
						tmpMerc.iBuilder = -1
						objMercenaryUtils.saveMercenary(tmpMerc)
						return
						
			mercenary = objMercenaryUtils.getMercenary(unit.getNameNoDesc())

			if(mercenary != None and g_bDisplayMercenaryMessages and mercenary.getBuilder() != -1 and unit.isDead()):
				strMessage = mercenary.getName() + " was lost under " + gc.getPlayer(mercenary.getOwner()).getName() + "'s service."
				# Inform the player that the mercenary has died.
				CyInterface().addMessage(mercenary.getBuilder(), True, 20, strMessage, "", 0, "", ColorTypes(0), -1, -1, True, True) 
			unit = argsList[0]
			
			# Debug code - start
			if(g_bDebug):	
				CvUtil.pyPrint("lost??: " + unit.getNameNoDesc())	
			# Debug code - end

			objMercenaryUtils.removePlayerMercenary(unit)


	# This method handles the key input and will bring up the mercenary manager screen if the 
	# player has at least one city and presses the 'M' key.
	def onKbdEvent(self, argsList):
		'keypress handler - return 1 if the event was consumed'

		if (gc.getGame().getGameTurn() >= con.tBirth[utils.getHumanID()]): #Rhye
		
			# TO DO: REMOVE THE FOLLOWING LINE BEFORE RELEASE.
			#gc.getPlayer(0).setGold(20000)
			eventType,key,mx,my,px,py = argsList
				
			theKey=int(key)

			if (eventType == self.EventKeyDown and theKey == int(InputTypes.KB_M) and self.eventManager.bAlt and gc.getActivePlayer().getNumCities() > 0 and gc.getActivePlayer().getCurrentEra() >= g_iStartingEra):

				self.mercenaryManager.interfaceScreen()

		#Rhye - start debug
		eventType,key,mx,my,px,py = argsList
			
		theKey=int(key)

		if (eventType == self.EventKeyDown and theKey == int(InputTypes.KB_B) and self.eventManager.bAlt):


			iHuman = utils.getHumanID()
			iGameTurn = gc.getGame().getGameTurn()
			
			pass


		if (eventType == self.EventKeyDown and theKey == int(InputTypes.KB_N) and self.eventManager.bAlt):

			print("ALT-N")
			
			self.printEmbassyDebug()
			self.printPlotsDebug()
			self.printStabilityDebug()


		if (eventType == self.EventKeyDown and theKey == int(InputTypes.KB_C) and self.eventManager.bAlt and self.eventManager.bShift):
			print("SHIFT-ALT-C") #picks a dead civ so that autoplay can be started with game.AIplay xx
			iDebugDeadCiv = iCarthage #default iCarthage: often dead in 3000BC
			gc.getTeam(gc.getPlayer(iDebugDeadCiv).getTeam()).setHasTech(con.tn('calendar'), True, iDebugDeadCiv, False, False)
			utils.makeUnit(con.iAxeman, iDebugDeadCiv, (0,0), 1)
			gc.getGame().setActivePlayer(iDebugDeadCiv, False)
			gc.getPlayer(iDebugDeadCiv).setPlayable(True)

		if (eventType == self.EventKeyDown and theKey == int(InputTypes.KB_E) and self.eventManager.bAlt and self.eventManager.bShift):
			print("SHIFT-ALT-E") #picks a dead civ so that autoplay can be started with game.AIplay xx
			iDebugDeadCiv = iEthiopia #default iEthiopia: always dead in 600AD
			gc.getTeam(gc.getPlayer(iDebugDeadCiv).getTeam()).setHasTech(con.tn('calendar'), True, iDebugDeadCiv, False, False)
			utils.makeUnit(con.iAxeman, iDebugDeadCiv, (0,0), 1)
			gc.getGame().setActivePlayer(iDebugDeadCiv, False)
			gc.getPlayer(iDebugDeadCiv).setPlayable(True)
			
		if (eventType == self.EventKeyDown and theKey == int(InputTypes.KB_Q) and self.eventManager.bAlt and self.eventManager.bShift):
			print("SHIFT-ALT-Q") #enables squatting
			self.rnf.setCheatMode(True);
			CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, "EXPLOITER!!!", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
			
		#Rhye - end debug
	
	#Mercenaries - end



	#Rhye - start
	def printDebug(self, iGameTurn):

		
		#if (iGameTurn %10 == 1):
		#	self.printEmbassyDebug()

		if (iGameTurn %5 == 0):
			self.printPlotsDebug()

		#if (iGameTurn %5 == 0): 
		#	self.printStabilityDebug()


			
	def printPlotsDebug(self):

##		for i in range(124):
##			for j in range(68):
##				print (i, j, gc.getMap().plot(i,j).getArea())
	    
		#countTotalUnits
		iTotal = 0
		iTotalCities = 0
##		lType = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
##		lOwner = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		
		#lOwnerLongbow = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	 0, 0, 0, 0, 0, 0, 0]
		#lOwnerCannon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	 0, 0, 0, 0, 0, 0, 0]
##		lPlotOwner = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			      0, 0]
		#lPlotOwner2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	      0, 0]
##		lCityOwner2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##			      0, 0]
		#lCityOwner_sb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
		#	      0, 0]
		for x in range(0, CyMap().getGridWidth()):
			for y in range(0, CyMap().getGridHeight()):
				pCurrent = gc.getMap().plot(x, y)
				iTotal += pCurrent.getNumUnits()
##				if (pCurrent.getNumUnits() > 0):
##					for i in range (pCurrent.getNumUnits()):
##						unit = pCurrent.getUnit(i)
##						lType[unit.getUnitType()] += 1
##						lOwner[unit.getOwner()] += 1
						#if (unit.getUnitType() == con.iLongbowman):
						#       lOwnerLongbow[unit.getOwner()] += 1
						#if (unit.getUnitType() == con.iCannon):
						#       lOwnerCannon[unit.getOwner()] += 1

				if (pCurrent.isCity()):
					iTotalCities += 1
					
		print ("TOTAL UNITS", iTotal)  
		print ("TOTAL CITIES", iTotalCities)

##		print ("Unit types")
##		for i in range (len(lType)):
##			print (i, lType[i])
##		print ("Unit owners")
##		for i in range (len(lOwner)):
##			print (i, lOwner[i])
		#print ("LB owners")
		#for j in range (len(lOwnerLongbow)):
		#	print (j, lOwnerLongbow[j])	       
		#print ("Cannon owners")
		#for j in range (len(lOwnerCannon)):
		#	print (j, lOwnerCannon[j])	       
	
		pass

	def printEmbassyDebug(self):
		for i in range(con.iNumPlayers):
			if (gc.getPlayer(i).isAlive()):
				apCityList = PyPlayer(i).getCityList()
				print (gc.getPlayer(i).getCivilizationShortDescription(0), gc.getTeam(gc.getPlayer(i).getTeam()).isHasTech(con.iCivilService), gc.getTeam(gc.getPlayer(i).getTeam()).isHasTech(con.iPaper))										     
				for j in range(con.iNumPlayers):
					if (gc.getTeam(gc.getPlayer(i).getTeam()).canContact(j)):   
						bEmb = False
						#TODO: re-add embassies?
						if (bEmb == False):
							print ("NO EMBASSY", gc.getPlayer(j).getCivilizationAdjective(0))


	def printStabilityDebug(self):
		print ("Stability")
		for iCiv in range(con.iNumPlayers):
			if (gc.getPlayer(iCiv).isAlive()):
				print ("Base:", utils.getBaseStabilityLastTurn(iCiv), "Modifier:", utils.getStability(iCiv)-utils.getBaseStabilityLastTurn(iCiv), "Total:", utils.getStability(iCiv), "civic", gc.getPlayer(iCiv).getCivics(5), gc.getPlayer(iCiv).getCivilizationDescription(0))
			else:
				print ("dead", iCiv)
		for i in range(con.iNumStabilityParameters):
			print("Parameter", i, utils.getStabilityParameters(i))
		for i in range(con.iNumPlayers):
			print (gc.getPlayer(i).getCivilizationShortDescription(0), "PLOT OWNERSHIP ABROAD:", self.sta.getOwnedPlotsLastTurn(i), "CITY OWNERSHIP LOST:", self.sta.getOwnedCitiesLastTurn(i))
