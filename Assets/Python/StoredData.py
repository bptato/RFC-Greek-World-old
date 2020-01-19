# Rhye's and Fall of Civilization - Stored Data

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
import cPickle as pickle

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer


class StoredData:

	def setupScriptData(self):
		"""Initialise the global script data dictionary for usage."""
		scriptDict = {      #------------RiseAndFall
				    'iNewCiv': -1,
				    'iNewCivFlip': -1,
				    'iOldCivFlip': -1,
				    'tTempTopLeft': -1,
				    'tTempBottomRight': -1,
				    'iSpawnWar': 0, #if 1, add units and declare war. If >=2, do nothing
				    'bAlreadySwitched': False,
				    'lColonistsAlreadyGiven': [0] * con.iNumPlayers, #active players
				    'lAstronomyTurn': [500] * con.iNumPlayers, #active players
				    'lNumCities': [0] * con.iNumTotalPlayers, #total players to contain Byzantium too
				    'lLastTurnAlive': [0] * con.iNumTotalPlayers, #total players to contain Byzantium too
				    'lSpawnDelay': [0] * con.iNumPlayers, #active players
				    'lFlipsDelay': [0] * con.iNumPlayers,
				    'iBetrayalTurns': 0,
				    'lLatestRebellionTurn': [0] * con.iNumPlayers,
				    'iRebelCiv': 0,
				    'lExileData': [-1, -1, -1, -1, -1],
				    'tTempFlippingCity': -1,
				    'lCheatersCheck': [0, -1],
				    'lBirthTurnModifier': [0] * con.iNumPlayers,
				    'lDeleteMode': [-1, -1, -1], #first is a bool, the other values are capital coordinates
				    'lFirstContactConquerors': [0, 0, 0], #maya, inca, aztecs
				    'bCheatMode': False,
				    'iCivsWithNationalism': 0,
				    #------------UP
				    'iImmigrationTurnLength': 0,
				    'iImmigrationCurrentTurn': 0,
				    'iLatestFlipTurn': 0,
				    'lLatestRazeData': [-1, -1, -1, -1, -1],
				    #------------AIWars
				    'lAttackingCivsArray': [0] * con.iNumPlayers,
				    'iNextTurnAIWar': -1,
				    #------------Plague
				    'lPlagueCountdown': [0] * con.iNumTotalPlayersB, #total players + barbarians
				    'lGenericPlagueDates': [-1, -1, -1, -1],# -1],
				    'lFirstContactPlague': [False] * con.iNumTotalPlayersB, #total players + barbarians
				     #------------Victories
				    'lGoals': [[-1 for i in range(con.iNumPlayers)] for j in range(con.iNumPlayers)], #bluepotato: [[-1,-1,-1]]*con.iNumPlayers would copy the same array over and over. see https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
				    'lReligionFounded': [-1, -1, -1, -1, -1, -1, -1],
				    'iEnslavedUnits': 0,
				    'iRazedByMongols': 0,
				    'lEnglishEras': [-1, -1],
				    'lGreekTechs': [-1, -1, -1],
				    'lNewWorld': [-1, -1], #first founded; circumnavigated (still unused)
				    'iNumSinks': 0,
				    'lSumerianTechs': [-1, -1, -1],
				    'babyloniaKilledCivs': 0,				
				    #'iMediterraneanColonies': 0,
				    'iPortugueseColonies': 0,
				    'iFrenchColonies': 0,
				    'lWondersBuilt': [0] * con.iNumTotalPlayers,
				    'l2OutOf3': [False] * con.iNumPlayers,
				    #------------Stability
				    'lBaseStabilityLastTurn': [0] * con.iNumTotalPlayersB,
				    'lPartialBaseStability': [0] * con.iNumTotalPlayersB,
				    'lStability': [0] * con.iNumTotalPlayersB,
				    'lOwnedPlotsLastTurn': [0] * con.iNumTotalPlayersB,
				    'lOwnedCitiesLastTurn': [0] * con.iNumTotalPlayersB,
				    'lCombatResultTempModifier': [0] * con.iNumTotalPlayersB,
				    'lGNPold': [0] * con.iNumTotalPlayersB,
				    'lGNPnew': [0] * con.iNumTotalPlayersB,
				    'lStatePropertyCountdown': [0] * con.iNumTotalPlayersB,
				    'lDemocracyCountdown': [0] * con.iNumTotalPlayersB,
				    'lStabilityParameters': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2+3+2+3+3 #bluepotato: TODO wat dis
				    'lLastRecordedStabilityStuff': [0, 0, 0, 0, 0, 0], # total + 5 parameters #bluepotato: TODO wat dis
				}
		gc.getGame().setScriptData(pickle.dumps(scriptDict))
