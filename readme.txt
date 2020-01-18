CURRENT VERSION:
1.6
Additions:
Added Elam
	They are intended to boost Persia by building up infrastructure in their core and collapsing before their spawn. Still needs balancing for this to work well.

Changes:
Altered some core areas
Buffed:
	Rome:
		Their UU now has 2 movement and 15% city attack instead of 10%
		More starting units
	Persia:
		Larsa is now in their core
		More starting units
	This makes them expand somewhat better, although they still get trampled by their older neighbors way too often
Nerfed Hittite starting units
Nerfed Assyria's core
Changed the unit AI of some civs' starting units
Moved Hadrian's Wall to Military Science
Moved Temple of Artemis to Record Keeping

Technical changes:
Removed vanilla RFC constants
Removed most non-researchable techs and other XML garbage
Replaced building and tech constants with functions
Temporarly disabled mercenaries, as the game was still using the old civ groups to determine their location

Fixes:
Removed leader traits as they were quite random and broke a few things (eg no anarchy on some civic changes)
Players' first city can now be founded in enemy territory: Babylon and Sparta can found their capital
Fixed the Hittite core
Fixed Greek civs' languages
Fixed religion buttons
Possibly fixed late-game CtDs (not sure though)
Completing three UHVs trigger victory

Known issues:
The Hittites no longer collapse by 1000BC because they have a core now
Old civs can still become way too powerful
The mod attempts to spawn units with an extremely high id sometimes (probably doesn't affect anything but I will have to look into it)
Vanilla RFC unit stacking bug
Vanilla RFC "dumb AI moves out of starting city with their entire army" bug

PREVIOUS VERSIONS:

Version 1.5 (EdmundIronside):
Fixed Egypts Nubia UHV
Edited City names to be more consistent as appropriate
Added more city names for Celts and Bactria
Modified Egypt UHVs to be slightly harder
Added UHVs for Sumeria
Made civs names consistent in scenario screen
Added UHVs for Indus Valley
Fixed Caanite religion video
Added more marshes to the game, and improved marsh graphics
Fixed Metal Casting so it is listed in the correct era.
Added UHVs for Minoa
Added UHV for Phoenicia
Changed in the dll how dynamic Civ names work
Fixed the dynamic civ names for all Civilizations
Added more conditional barbarian spawns
Increased strength of Byzantines and Sassanids

Version 1.4 (EdmundIronside):
Medieval era changed to Early Medieval Era
New music added to ancient, classical and early medieval eras
Some barbarian spawns modified so they can spawn inside civ territories
More barbarian spawns in 5th century AD
All historical barbarian spawns have unique units
4 new independent cities and 1 new barbarian city added (includes Massila, Thebes and Cyrene)
German unique unit and heavy swordsman have unique art
Historical wars, and additional civ spawns added for greater historical looking empire (includes Peleponesian wars, Punic wars, and Gallic wars)
Initial strength of unit spawns increased for various civs including Babylonians, Assyrians, Macedonians, Romans, Sassanids, Byzantines, Persians, Huns, and Goths
Initial strength of unit spawns decreased for Athens and Sparta
Changed some mountains to hills in Southern Spain and Northern Africa
Added Numidia as a new playable Civ
Modified and added several new civics
All civics are now researchable
All default starting civics have features
Added 4 new techs (Manorialism, Keel, Paper, and Advanced Agriculture)
Changed Crossbow to an Early Medieval Tech
Changed Story telling tech icon
All resources need techs researched before being revealed
Re-arranged what techs civics need in order to be playable
Slightly slowed tech rate down
Gave Sumeria and Indus Valley 1 extra tech each
Victory Screen fixed to display historical goals
Unique Historical Victories now functional
Goals completed for Egypt
Cultural victory enabled
Sphynx image fixed
Archery Range build sound changed
Zulus removed from mercenary names

Version 1.3 (EdmundIronside):
Unique Powers for Civs
Sassanids added
AI Settler map fixed
Civelopedia being finalized
Increased techs new spawning civs get
Changed Macedonia spawn date so that start after the period the spent as a Persian vassal
Slowed tech rate

Version 1.2 (EdmundIronside):
*Features include:
Unique units for all civilizations
Unique buildings for all civilizations
2 new wonders
A 900 BC Scenario
Historical spawn for historical events like Hannibal & Alexander the Great
More barbarian spawns
New images for main screen and loading screen
AI War Maps updated
*Fixes include:
Making all the old Settler maps compatible
Being able to irrigate flood plains
Statue of Liberty no longer on tech tree

Version 1.1 (EdmundIronside):
Spawn dates on main menu fixed
Spawn order changed
Revamped Tech tree (again)!
Added 3 new civilizations
Revamped Barbarian spawns and invasions
Fixed fog of war
Added multiple new units
Variety of changes made to the map

Version 1.0 (EdmundIronside):
-Fixed date display
-Added Mycenaeans
-Added new techs
-Added new buildings
-Made changes to map

Version 0.9 (EdmundIronside):
Increased mod length from 375 to 500 turns.
Added Minoa
Added Aryan barbarians
Added some new minor cities
Restored dynamic names
Worked on making civilizations be more historic in empire sizes

Version 0.8 (EdmundIronside):
Added Sumerians
Changed mod time span to 4000 BC to 500 AD.
Started fixing the main menu.
Changed some graphics on menu and loading screen.

Version 0.7 (Spaceman98):
Civs:
Added Bactrian Civilization with a leader, dynamic names, etc.
removed Athens from the Athenian city name list. It gets built in odd places. Same for Rome for the Roman city lists
Rome can now produce units slightly faster
hanged some of Persia&#8217;s dynamic names
Remove Socialist names now that they can show up. Replaced them with the names of late dynasties (like the Sassanids and the Kushans)
Carthage no longer becomes a caliphate if it converts to Egyptian mythology
Civics:
renamed &#8220;Nationhood&#8221; to &#8220;empire&#8221;, and make it accessible with the citizenship tech
Made Vassalage available with Aristocracy
Renamed Free Market to Trade (available with Trade)
Renamed State Property to Centralized Coinage (available with Currency)
Made Bureaucracy available with its own tech: Record Keeping, which is also a prereq for Education, that requires mathematics and alphabet
Made mercantilism available with Record Keeping
Techs:
made river trade accessible with fishing. Otherwise, you can currently trade along the coast earlier than along rivers, and trade is an OP tech
Added record keeping tech (see bureaucracy note)
give starting nations technologies for the appropriate starting religions.
Moved drama into the tech tree, make it researchable
Map
Replace Kashgar mountains with land for Bactria
Units:
Make Merchants a national unit (limited to three of them at a time). They are overpowered otherwise
Background Fixes:
Fixed the &#8220;tuple index out of range&#8221; error associated with the Indus Valley by adding another 0 to the end of tBirths in consts.py. Not sure why this helps, but for some reason it does. Not sure what the consequences would be. They still collapse, which is ok, I guess.
Fixed a tuple index out of range exception related to AI Wars

Version 0.6 (Spaceman98):
Units:
Made Pirates not go on Ocean
Gave triremes and Quinqueremes anti-pirate bonus
Make pirates also require trade.
Added battering ram unit as an early siege weapon, with logging
Merchant unit added. Functions like the great merchant, but its trade mission produces much less gold. I&#8217;m not sure if the AI knows how to use them.
Raised the strength of hoplites to 5. If they are suppose to be a technological upgrade of spearmen, then they have to actually be better than spearmen
Terrain Features/Resources
Made jungles passable
Made Jungles chopable with Iron Working
Fixed bug for the paved road
Added olives and pearls and salt resources
Pearl Resources are near: Bahrain (replace a clam), Red Sea, South India, Persia, Algeria (replace a clam)
Olive resources are near: Phoenician spawn zone, South Italy, Greece, Macedonia, North Iraq
Salt Resources are near: The dead sea (Israel), Romania, Salzburg, the Sahara, and Ethiopea, Venice
Added Sheep to Sardinia and Forests to Corsica
Added hills to Somalia
Expanded Arabia into the Ocean
Made Socotra smaller
Untrimmed Iberia
Shrunk Isle of Man, Moved Ireland to the South
Moved England West, adjusted it considerably so that its outline is better
Fix British Resources
Improve geography of Wales, added more hills, forests and rivers
Fixed bug: Wine was previously &#8220;enabled&#8221; by the tyranny tech, which meant that the resource was unobtainable&#8230; It is now enabled by the amphora tech, the same one as allows wineries and tabernas
Buildings:
Added trading post, which has the ability of the customs house, and art from the Viking trading post
Add Elder&#8217;s Council with storytelling, which gives a small science bonus
Fix the name of the Yazilikaya
Add Taberna building, with amphora and wine, which gives +1 happiness and culture, but -1 health
Fix Olympic park TXT_KEY
Fix Leaning tower TXT_KEY
Fix Flavian Amphitheatre TXT
Barbs and Independents:
Move Yemen City 3 South and 1 East
Give Saana starting archers
Added Libyan barbarian armies to weaken Egypt. Currently, 4 spawn on Monarch level, and this seems to be the optimal number, as Egypt sometimes survives, and is usually overwhelmed. I may want to decrease this later, as I still want Egypt to survive more often than it actually does
Adding Numidian Barbarians to pressure Carthage.
Civs:
Give Rome storytelling at start
The Nubian starting units are now Medjay instead of archers, and there are now 4 of them instead of 3. This should make Nubia harder to steamroll (before, an Egyptian player can take over them in a few turns)

Version 0.5 (Spaceman98):
Map:
Fixed Black Sea Coastline
Fixed terrain of the Indus valley
Moved Indus valley civilization onto Indus valley
Renamed Aleppo to Halab
Restore terrain yields of plains and grasslands to what they originally were
Added island of Socotra
Removed Tundra Jungle in Ethiopia
Added some hills to Ireland and Scandinavia
Added Isle of Man, and a river in Ireland
Move Nubian capital
Iron + hills to Nubia
Copper to Israel (http://en.wikipedia.org/wiki/Timna_Valley)
Added marble to Create
Game Balancing:
Gave Etruscans fishing and Archery and Agriculture
Gave Sparta Archery and agriculture and fishing
Gave Gauls Archery
Gave Israelis, Athenians, Macedonians, Persians, Romans, Carthaginians Agriculture
Archery to Germanics
Remove warrior +25% city defense
Gave Huns Strength 9 UU
Gave Germanics Strength 8 UU
Bugfixes:
Fixed Sparta/Rome Dynamic names issue
Fixed cotton and camel txtkeys
Add two movement to the Phoenician galley, which was currently slower than the normal galley
Fixed Byzantium typos (though they will just be replaced next patch so)
Copy RFC text for expansion civics
Other:
Add shipwright building
Add pirate unit
Add explorer (unit form civ 4, with Cartography)
Replace future tech with medieval tech, and make it researchable so the tech tree does not end
Move representation civic to republicanism
Gaul empire -> Gallic Empire
move medic promotion to Herbalism
add Paved Roads tile improvement

Version 0.42 (Spaceman98):
Idk what I changed with this since the changes were made many years ago (sorry :p) but apparently some bugs were fixed and camels were added

Version 0.41 (Spaceman98):
Civilizations: Nubia no longer collapses
Adding Indus Valley Civilization
Better Etruscan LH
Map:
I have expanded the map to fill in the blank areas. This added Ethiopea, Scotland, India and ussless Saharan and Siberian land. The reasons for this is are 1: to give the IVC more room. 2: To give Nubia more room. 3: To make Brittan worth colonizing. 4: For a future Vandal civ or barbs.
The red sea coast is now more fertile.
Religion: General bug and error fixing.
All religions now have holy shrines.
Other modifications were made.

Version 0.2 (Spaceman98):
Added Nubian Civilization. Leader: Taharqa, UU: Medjay, UB: Vaulted Granary
Fixed some city names
Gave Phoenicians UU: Briem
Gave Israel UB: Kotel
Replaced David with Solomon for Israel
Removed Swamp on Nile Delta (Egypt is stronger in the North Nile but weaker in the South Nile)
Moved Hittite spawn point
Israel now starts with Pottery since all neighbors are stronger
Phoenicians get fish instead of Sheep
Adjusted some city names
Changed some dynamic names to distinguish between large and small empires
Gave Hittites Animal Husbandry so it takes longer for barbs to overrun them (they are still overrun, as they historically should be, but they have time to become a threat to the South empires and a player can lead them easier (no chariots against warriors and swordsmen against chariots)
Britan is now one Island

Version 0.1 (Spaceman98):
City Name Map Working
Missionary renaming
All Python exceptions fixed
Added Cannanite Missionary to Carthage
Adjusted Hittite and Spartian starting units
Added copper to Greece and Cyprus
Added leaderheads for Germanics and Etruscans
Moved starting religions to earlier techs, which I will give to starting civilizations in next patch
Removed Spiritual Burial tech
Removed Archers from Hun and Germanic starting stacks (they were slowing the horde down) and replaced accordingly
Changed some dynamic names to distinguish between large and small empires

Version 0.05 (Spaceman98):
Religions: Cannanite Mythology, Egyptian Mythology, Mesopotamian Mythology, Judaism, Hellenism, Zoroastrianism, Christianity.
Readded Missionaries
Leaderheads for: Phoenicia, Israel, Hittites, Sparta, Huns
Dynamic Names for all civilizations
Healers Hut Building
Added technologies: Herbalism, Spiritual Burial (the first is for the Healers Hut, the second for Egyptian Mythology)
Strengthened Byzantine, Hun and Germanic starting armies greatly
Added City Name Maps from the forum
Added Settler Maps from the forum
Added City Lists (temporary)
Minor Bugfixes

Version 0.028a (Arkaeyn):
CHANGES:
Tech tree significantly altered. 
	New additions - Trade, Logging, Herbalism, Storytelling, Amphora, Citizenship, Democracy, Aristocracy, 		Naval Warfare, Standing Army, Republicanism
	Moved up or down the tree - Code of Laws, Philosophy, Military Science, Medicine, Education, Music, Drama
	Renamed - Monarchy to Tyranny, Meditation to Mythology

Map changes - several resources were on mountains, and have been moved to workable land.

Translation - French translation partially available.

New Units - Quinquireme (with Naval Warfare), Hoplite (with Military Science), Legion (with Standing Army), Noble Cavalry (with Aristocracy), Javelineer (with Military Science)

Leaderheads - Assigned temporary leaders to civs which will need custom leaderheads (Washington for the Hittites, for example).

Rhye's War Maps have been implemented

Since we don't have new buildings yet, the ability to built Wealth, Culture, and Research has been moved up the tech tree, to Trade, Storytelling, and Writing.

Version 0.025a (Arkaeyn):
CHANGES:
First public release
