# Rhye's and Fall of Civilization - Communications

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Popup
import Consts as con
import RFCUtils
utils = RFCUtils.RFCUtils()

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

### Constants ###

iNumMajorPlayers = con.iNumMajorPlayers

#scrambled pools
tPool1 = (con.iEgypt, -1, -1, -1, -1, -1,
	  con.iSumeria, -1, -1, -1, -1, -1,
	  -1, -1, -1, -1, -1, -1,
	  -1, -1, -1, -1, -1, -1,
	  -1, -1, -1, -1, -1, -1)

tPool2 = (con.iEgypt, -1,
	  con.iMinoa, -1,
	  con.iPhoenicia, -1,
	  con.iHittites, -1,	
	  con.iBabylonia, -1,
	  con.iMycenae, -1,	
	  con.iAthens, con.iIsrael,	
	  con.iBactria, -1,	
	  con.iRome, -1)

tPool3 = (con.iEgypt,
	  con.iSumeria,
	  con.iIndusValley,
	  con.iElam,
	  con.iMinoa,
	  con.iPhoenicia,
	  con.iBabylonia,
	  con.iHittites,	
	  con.iMycenae,
	  con.iAssyria,
	  con.iIsrael,
	  con.iAthens,
	  con.iSparta,
	  con.iScythia,
	  con.iCarthage,
	  con.iCeltia,
	  con.iEtruria,
	  con.iNubia,
	  con.iPersia,
	  con.iRome,
	  con.iMacedonia,
	  con.iIndia,
	  con.iBactria,	
	  con.iNumidia,
	  con.iGermania,
	  con.iSassanid,
	  con.iByzantium,
	  con.iHuns)


class Communications:

	def checkTurn(self, iGameTurn):
		#self.decay(con.iIndia) #debug
		if (iGameTurn >= 25 and iGameTurn <= 95):
			i = (iGameTurn + utils.getSeed()/10 - 5) % (len(tPool1))
			iCiv = tPool1[i]
##			#shuffle
##			if (i % 2 == 0):
##				iCiv = i/2
##			else:
##				iCiv = con.iNumMajorPlayers/2 + i/2
			if (iCiv >= 0 and iCiv < con.iNumMajorPlayers):
				if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= con.tBirth[iCiv]+15):
					if (not gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(con.iElectricity)):
						self.decay(iCiv)
		elif (iGameTurn > 95 and iGameTurn <= 168):
			i = (iGameTurn + utils.getSeed()/10 - 5) % (len(tPool2))
			iCiv = tPool2[i]

			if (iCiv >= 0 and iCiv < con.iNumMajorPlayers):
				if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= con.tBirth[iCiv]+15):
					if (not gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(con.iElectricity)):
						self.decay(iCiv)
		else:
			i = (iGameTurn + utils.getSeed()/10 - 5) % (len(tPool3))
			j = ((iGameTurn + utils.getSeed()/10 - 5)+13) % (len(tPool3))
			iCiv1 = tPool3[i]
			iCiv2 = tPool3[j]	
			if (iCiv1 >= 0 and iCiv1 < con.iNumMajorPlayers):
				if (gc.getPlayer(iCiv1).isAlive() and iGameTurn >= con.tBirth[iCiv1]+15):
					if (not gc.getTeam(gc.getPlayer(iCiv1).getTeam()).isHasTech(con.iElectricity)):
						self.decay(iCiv1)
			if (iCiv2 >= 0 and iCiv2 < con.iNumMajorPlayers):
				if (gc.getPlayer(iCiv2).isAlive() and iGameTurn >= con.tBirth[iCiv2]+15):
					if (not gc.getTeam(gc.getPlayer(iCiv2).getTeam()).isHasTech(con.iElectricity)):
						self.decay(iCiv2)



	def decay(self, iCiv):

		teamCiv = gc.getTeam(gc.getPlayer(iCiv).getTeam())
		cutList = []
		iRndnum = gc.getGame().getSorenRandNum(iNumMajorPlayers, 'starting index')
		iCounter = 0

		#initialise list
		#print ("iRndnum", iRndnum)
		for i in range(iRndnum, iNumMajorPlayers + iRndnum):
			#print ("i", i)
			if (iRndnum % 2 == 0): #randomize scan order
				j = i
				#print ("jA", j)
			else:
				j = iNumMajorPlayers + 2*iRndnum - i
				#print ("jB", j)
			iOtherCiv = j % iNumMajorPlayers
			#print ("iOtherCiv", iOtherCiv)
			if (gc.getPlayer(iOtherCiv).isAlive()):
				if (teamCiv.canContact(iOtherCiv)):
					if (not gc.getTeam(gc.getPlayer(iOtherCiv).getTeam()).isHasTech(con.iElectricity)):
						cutList.append(iOtherCiv)
		#print (iCiv, "cutList", cutList)
		#first browse our cities - if other civs can see our borders
		for pyCity in PyPlayer(iCiv).getCityList():
			city = pyCity.GetCy()
			for iOtherCiv in cutList:
				pCity = gc.getMap().plot( city.getX(), city.getY() )
				if (pCity.isVisible(iOtherCiv, False)): #in case it has a holy city
					if (iOtherCiv in cutList):
						cutList.remove(iOtherCiv)
			for x in range(city.getX()-4, city.getX()+5):
				for y in range(city.getY()-4, city.getY()+5):
					pCurrent = gc.getMap().plot( x, y )
					if (pCurrent.isVisible(iCiv, False)):
						for iOtherCiv2 in cutList:
							if (pCurrent.getOwner() == iOtherCiv2):
								cutList.remove(iOtherCiv2)

		#then browse their cities - if we can see their borders (view distance is asymmetrical)	
		for iOtherCiv in cutList:
			if (iCounter >= 4): #3 in vanilla and warlords
				return
			bNear = False
			for pyOtherCity in PyPlayer(iOtherCiv).getCityList():
				city = pyOtherCity.GetCy()
				pOtherCity = gc.getMap().plot( city.getX(), city.getY() )
				if (pOtherCity.isVisible(iCiv, False)): #in case I've got a holy city
					bNear = True
					break
				for x in range(city.getX()-4, city.getX()+5):
					for y in range(city.getY()-4, city.getY()+5):
						pCurrent = gc.getMap().plot( x, y )
						if (pCurrent.isVisible(iOtherCiv, False)):
							if (pCurrent.getOwner() == iCiv):
								bNear = True
								break
								break
			if (bNear == False):
				teamCiv.cutContact(iOtherCiv)
				iCounter += 1
				print ("Cutting contacts between", gc.getPlayer(iCiv).getCivilizationShortDescription(0), "and", gc.getPlayer(iOtherCiv).getCivilizationShortDescription(0))




	def onBuildingBuilt(self, iPlayer, iBuilding, city):
		return None

	def onCityAcquired(self, city):
		return None


