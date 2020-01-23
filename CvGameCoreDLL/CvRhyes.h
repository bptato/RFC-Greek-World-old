//Rhye
#ifndef CVRHYES_H
#define CVRHYES_H

// rhyes.h

#define MAX_COM_SHRINE			(20)
#define BASIC_TURN_MODIFIER     (500) //lower for stronger effect on late civs; higher for helping early civs more

#define EGYPT					(0)
#define SUMERIA					(1)
#define INDUSVALLEY				(2)
#define ELAM					(3)
#define MINOA					(4)
#define PHOENICIA				(5)
#define BABYLONIA				(6)
#define HITTITES				(7)
#define MYCENAE					(8)
#define ASSYRIA					(9)
#define ISRAEL					(10)
#define ATHENS					(11)
#define SPARTA					(12)
#define SCYTHIA					(13)
#define CARTHAGE				(14)
#define CELTIA					(15)
#define ETRURIA					(16)
#define NUBIA					(17)
#define PERSIA					(18)
#define ROME					(19)
#define MACEDONIA				(20)
#define INDIA					(21)
#define BACTRIA				    (22)
#define NUMIDIA 				(23)
#define GERMANIA			    (24)
#define SASSANID			    (25)
#define BYZANTIUM				(26)
#define HUNS					(27)
#define NUM_MAJOR_PLAYERS		(28)
#define INDEPENDENT				(28)
#define INDEPENDENT2			(29)
#define NUM_TOTAL_PLAYERS		(30)
#define BARBARIAN				(30)

#define GREATPALACE				(1)
#define SUMMERPALACE			(1)
#define VERSAILLES				(2)
#define FORBIDDENPALACE			(2)

#endif	// CVRHYES_H



/*extern int startingTurn[];
extern char loadingTime[34][4];
extern char loadingTime600AD[34][4];
extern char startingYear[34][6];
extern bool startingEra[34];
extern char startingYear600AD[34][6];
extern bool startingEra600AD[34];*/
//extern int militaryBonus[2][18];
extern char uniquePower[35][2][16];
extern char rating[34][6][15];

extern int turnPlayed[33];
extern int civSpreadFactor[33][7];
//extern int borders[27][27]; //RFGW
extern wchar civDynamicNames[28][22][19]; //(dynamic civ names - not jdog's)
extern int civDynamicNamesFlag[28];
extern int civDynamicNamesEraThreshold[28];
//extern int settlersMaps[][68][124]; //RFGW


