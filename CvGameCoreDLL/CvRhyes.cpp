//Rhye

#include "CvGameCoreDLL.h"
#include "CvRhyes.h"

// rhyes.cpp



char uniquePower[35][2][16]  = {
	{"TXT_KEY_UP_AME", "TXT_KEY_UP_AME2"},
	{"TXT_KEY_UP_ARA", "TXT_KEY_UP_ARA2"},
	{"TXT_KEY_UP_AZT", "TXT_KEY_UP_AZT2"},
	{"TXT_KEY_UP_ELA", "TXT_KEY_UP_ELA2"},
	{"TXT_KEY_UP_BAB", "TXT_KEY_UP_BAB2"},
	{"TXT_KEY_UP_BYZ", "TXT_KEY_UP_BYZ2"},
	{"TXT_KEY_UP_CAR", "TXT_KEY_UP_CAR2"},
	{"TXT_KEY_UP_CEL", "TXT_KEY_UP_CEL2"},
	{"TXT_KEY_UP_CHI", "TXT_KEY_UP_CHI2"},
	{"TXT_KEY_UP_EGY", "TXT_KEY_UP_EGY2"},
	{"TXT_KEY_UP_ENG", "TXT_KEY_UP_ENG2"},
	{"TXT_KEY_UP_ETH", "TXT_KEY_UP_ETH2"},
	{"TXT_KEY_UP_FRA", "TXT_KEY_UP_FRA2"},
	{"TXT_KEY_UP_GER", "TXT_KEY_UP_GER2"},
	{"TXT_KEY_UP_GRE", "TXT_KEY_UP_GRE2"},
	{"TXT_KEY_UP_HRE", "TXT_KEY_UP_HRE2"},
	{"TXT_KEY_UP_INC", "TXT_KEY_UP_INC2"},
	{"TXT_KEY_UP_IND", "TXT_KEY_UP_IND2"},
	{"TXT_KEY_UP_JAP", "TXT_KEY_UP_JAP2"},
	{"TXT_KEY_UP_KHM", "TXT_KEY_UP_KHM2"},
	{"TXT_KEY_UP_KOR", "TXT_KEY_UP_KOR2"},
	{"TXT_KEY_UP_MAL", "TXT_KEY_UP_MAL2"},
	{"TXT_KEY_UP_MAY", "TXT_KEY_UP_MAY2"},
	{"TXT_KEY_UP_MON", "TXT_KEY_UP_MON2"},
	{"TXT_KEY_UP_NAM", "TXT_KEY_UP_NAM2"},
	{"TXT_KEY_UP_HOL", "TXT_KEY_UP_HOL2"},
	{"TXT_KEY_UP_TUR", "TXT_KEY_UP_TUR2"},
	{"TXT_KEY_UP_PER", "TXT_KEY_UP_PER2"},
	{"TXT_KEY_UP_POR", "TXT_KEY_UP_POR2"},
	{"TXT_KEY_UP_ROM", "TXT_KEY_UP_ROM2"},
	{"TXT_KEY_UP_RUS", "TXT_KEY_UP_RUS2"},
	{"TXT_KEY_UP_SPA", "TXT_KEY_UP_SPA2"},
	{"TXT_KEY_UP_SUM", "TXT_KEY_UP_SUM2"},
	{"TXT_KEY_UP_VIK", "TXT_KEY_UP_VIK2"},
	{"TXT_KEY_UP_ZUL", "TXT_KEY_UP_ZUL2"}};

char rating[34][6][15]  = {
//		    TRA				 PRO				CUL					GRO				S.S.
//America
	{"TXT_KEY_4STARS", "TXT_KEY_5STARS", "TXT_KEY_1STAR", "TXT_KEY_5STARS", "TXT_KEY_1STAR" },
//Arabia
	{"TXT_KEY_4STARS", "TXT_KEY_1STAR", "TXT_KEY_5STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS" },
//Aztec
	{"TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_1STAR" },
//Babylonia
	{"TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS" },
//Byzantium
	{"TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS"},
//Carthage
	{"TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS" },
//
	{"TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS"},
//China
	{"TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_5STARS", "TXT_KEY_2STARS", "TXT_KEY_3STARS" },
//Egypt
	{"TXT_KEY_3STARS", "TXT_KEY_1STAR", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS" },
//England
	{"TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS" },
//Ethiopia
	{"TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS"},
//France
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_2STARS" },
//Germany
	{"TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_3STARS" },
//Greece
	{"TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS" },
//
	{"TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS"},
//Inca
	{"TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_1STAR" },
//India
	{"TXT_KEY_4STARS", "TXT_KEY_1STAR", "TXT_KEY_5STARS", "TXT_KEY_1STAR", "TXT_KEY_4STARS" },
//Japan
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS" },
//Khmer
	{"TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS"},
//
	{"TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS"},
//Mali
	{"TXT_KEY_5STARS", "TXT_KEY_1STAR", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS" },
//Maya
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_1STAR"},
//Mongolia
	{"TXT_KEY_1STAR", "TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS" },
//
	{"TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS"},
//Netherlands
	{"TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_1STAR"},
//Turkey
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_5STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS" },
//Persia
	{"TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS" },
//Portugal
	{"TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_1STAR"},
//Rome
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS" },
//Russia
	{"TXT_KEY_1STAR", "TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_5STARS" },
//Spain
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS" },
//
	{"TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS"},
//Vikings
	{"TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS" },
//
	{"TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS"}};


int turnPlayed[33] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};


int civSpreadFactor[33][7]  = { //TODO huh?
//		JUD	 CHR  ISL  HIN  BUD  CON  TAO
//Egypt
	{	 70, 250, 350,  20,  20,  20,  20 },	//100, 200, 300,  20,  20,  20,  20  before removal of Aggressive trait
//India
	{	 20,  90, 180, 400, 180,  20,  60 },	// 20,  80, 150, 300, 100,  20,  40  before removal of Aggressive trait
//China
	{	 20,  80,  20,  20, 200, 300, 200 },
//Elam
	{	 20,  90, 180, 400, 180,  20,  60 },
//Babylonia
	{	 50, 200, 350,  20,  20,  20,  20 },
//Greece
	{	 40, 300,  40,  70,  50,  20,  20 },
//Persia
	{	 70,  20, 300,  40,  40,  20,  20 },
//Carthage
	{	 80, 200, 400,  20,  20,  20,  20 },
//Rome
	{	 40, 300,  40,  20,  40,  20,  20 },
//Japan
	{	 20,  40,  20,  20, 300, 120, 100 },
//Ethiopia
	{	200, 400, 400,  80,  80,  80,  80 }, //was 80, 300, 300,  20,  20,  20,  20 before; increased to help with their UHV
//Maya
	{	 70, 300,  80,  80,  80,  80,  80 },
//Viking
	{	 40, 300,  80,  20,  40,  20,  20 },
//Arabia
	{	 40,  30, 400,  20,  20,  20,  20 },
//Khmer
	{	 20,  40,  20,  80, 400,  80, 100 },
//Spain
	{	 80, 400, 100,  20,  40,  20,  20 },
//France
	{	 60, 300, 100,  20,  40,  20,  20 },
//England
	{	 70, 300,  80,  20,  40,  20,  20 },
//Germany
	{	 70, 300,  80,  20,  40,  20,  20 },
//Russia
	{	 70, 300,  40,  20,  40,  20,  20 },
//Holland
	{	120, 300,  40,  20,  20,  20,  20 },
//Mali
	{	 50,  90, 400,  20,  20,  20,  20 },
//Portugal
	{	 40, 400, 100,  20,  40,  20,  20 },
//Inca
	{	 70, 300,  80,  80,  80,  80,  80 },
//Mongolia
	{	 20,  80,  80,  20, 300, 150, 100 },
//Aztec
	{	 70, 400,  90,  90,  90,  90,  90 },
//Turkey
	{	 50,  80, 400,  20,  20,  20,  20 },
//America
	{	100, 300,  20,  20,  20,  20,  20 },
//Independent
	{	 80, 250, 250,  50, 100,  50,  40 },
//Independent2
	{	 80, 200, 200,  80, 150,  80,  80 },
//Native
	{	120, 200, 200,  80,  80,  80,  80 },
//Celtia
	{	 80, 300,  80,  20,  40,  20,  20 },
//Barbarian
	{	100, 100, 100, 100, 100, 100, 100 }};

// (dynamic civ names - not jdog's)
wchar civDynamicNames[28][22][19]  = { //TODO
//				//people		monarchy		monarchy ext		monarchy mod		monarchy ext mod		republic			communism			fascism				islam monarchy		islam republic			vas. Persia			vas. Rome			vas. Arabia			vas. Spain				vas. France			vas. England		vas. Germany			vas. Russia			vas. Mongolia			vas. Turkey			vas. Chi/Jap/Khm	vassal generic
//Egypt
	{	 L"TXT_KEY_DN_EGY00", L"TXT_KEY_DN_EGY01", L"TXT_KEY_DN_EGY02", L"TXT_KEY_DN_EGY03",  L"TXT_KEY_DN_EGY04",  L"TXT_KEY_DN_EGY05",  L"TXT_KEY_DN_EGY06",  L"TXT_KEY_DN_EGY07",  L"TXT_KEY_DN_EGY08",  L"TXT_KEY_DN_EGY09",  L"TXT_KEY_DN_EGY10",  L"TXT_KEY_DN_EGY11",  L"TXT_KEY_DN_EGY12",  L"TXT_KEY_DN_EGY13",  L"TXT_KEY_DN_EGY14",  L"TXT_KEY_DN_EGY15",  L"TXT_KEY_DN_EGY16",  L"TXT_KEY_DN_EGY17",  L"TXT_KEY_DN_EGY18",  L"TXT_KEY_DN_EGY19",  L"TXT_KEY_DN_EGY20",  L"TXT_KEY_DN_EGY21" },
//India
	{	 L"TXT_KEY_DN_IND00", L"TXT_KEY_DN_IND01", L"TXT_KEY_DN_IND02", L"TXT_KEY_DN_IND03",  L"TXT_KEY_DN_IND04",  L"TXT_KEY_DN_IND05",  L"TXT_KEY_DN_IND06",  L"TXT_KEY_DN_IND07",  L"TXT_KEY_DN_IND08",  L"TXT_KEY_DN_IND09",  L"TXT_KEY_DN_IND10",  L"TXT_KEY_DN_IND11",  L"TXT_KEY_DN_IND12",  L"TXT_KEY_DN_IND13",  L"TXT_KEY_DN_IND14",  L"TXT_KEY_DN_IND15",  L"TXT_KEY_DN_IND16",  L"TXT_KEY_DN_IND17",  L"TXT_KEY_DN_IND18",  L"TXT_KEY_DN_IND19",  L"TXT_KEY_DN_IND20",  L"TXT_KEY_DN_IND21" },
//China
	{	 L"TXT_KEY_DN_CHI00", L"TXT_KEY_DN_CHI01", L"TXT_KEY_DN_CHI02", L"TXT_KEY_DN_CHI03",  L"TXT_KEY_DN_CHI04",  L"TXT_KEY_DN_CHI05",  L"TXT_KEY_DN_CHI06",  L"TXT_KEY_DN_CHI07",  L"TXT_KEY_DN_CHI08",  L"TXT_KEY_DN_CHI09",  L"TXT_KEY_DN_CHI10",  L"TXT_KEY_DN_CHI11",  L"TXT_KEY_DN_CHI12",  L"TXT_KEY_DN_CHI13",  L"TXT_KEY_DN_CHI14",  L"TXT_KEY_DN_CHI15",  L"TXT_KEY_DN_CHI16",  L"TXT_KEY_DN_CHI17",  L"TXT_KEY_DN_CHI18",  L"TXT_KEY_DN_CHI19",  L"TXT_KEY_DN_CHI20",  L"TXT_KEY_DN_CHI21" },
//Elam
	{	 L"TXT_KEY_DN_ELA00", L"TXT_KEY_DN_ELA01", L"TXT_KEY_DN_ELA02", L"TXT_KEY_DN_ELA03",  L"TXT_KEY_DN_ELA04",  L"TXT_KEY_DN_ELA05",  L"TXT_KEY_DN_ELA06",  L"TXT_KEY_DN_ELA07",  L"TXT_KEY_DN_ELA08",  L"TXT_KEY_DN_ELA09",  L"TXT_KEY_DN_ELA10",  L"TXT_KEY_DN_ELA11",  L"TXT_KEY_DN_ELA12",  L"TXT_KEY_DN_ELA13",  L"TXT_KEY_DN_ELA14",  L"TXT_KEY_DN_ELA15",  L"TXT_KEY_DN_ELA16",  L"TXT_KEY_DN_ELA17",  L"TXT_KEY_DN_ELA18",  L"TXT_KEY_DN_ELA19",  L"TXT_KEY_DN_ELA20",  L"TXT_KEY_DN_ELA21" },
//Babylonia
	{	 L"TXT_KEY_DN_BAB00", L"TXT_KEY_DN_BAB01", L"TXT_KEY_DN_BAB02", L"TXT_KEY_DN_BAB03",  L"TXT_KEY_DN_BAB04",  L"TXT_KEY_DN_BAB05",  L"TXT_KEY_DN_BAB06",  L"TXT_KEY_DN_BAB07",  L"TXT_KEY_DN_BAB08",  L"TXT_KEY_DN_BAB09",  L"TXT_KEY_DN_BAB10",  L"TXT_KEY_DN_BAB11",  L"TXT_KEY_DN_BAB12",  L"TXT_KEY_DN_BAB13",  L"TXT_KEY_DN_BAB14",  L"TXT_KEY_DN_BAB15",  L"TXT_KEY_DN_BAB16",  L"TXT_KEY_DN_BAB17",  L"TXT_KEY_DN_BAB18",  L"TXT_KEY_DN_BAB19",  L"TXT_KEY_DN_BAB20",  L"TXT_KEY_DN_BAB21" },
//Greece
	{	 L"TXT_KEY_DN_GRE00", L"TXT_KEY_DN_GRE01", L"TXT_KEY_DN_GRE02", L"TXT_KEY_DN_GRE03",  L"TXT_KEY_DN_GRE04",  L"TXT_KEY_DN_GRE05",  L"TXT_KEY_DN_GRE06",  L"TXT_KEY_DN_GRE07",  L"TXT_KEY_DN_GRE08",  L"TXT_KEY_DN_GRE09",  L"TXT_KEY_DN_GRE10",  L"TXT_KEY_DN_GRE11",  L"TXT_KEY_DN_GRE12",  L"TXT_KEY_DN_GRE13",  L"TXT_KEY_DN_GRE14",  L"TXT_KEY_DN_GRE15",  L"TXT_KEY_DN_GRE16",  L"TXT_KEY_DN_GRE17",  L"TXT_KEY_DN_GRE18",  L"TXT_KEY_DN_GRE19",  L"TXT_KEY_DN_GRE20",  L"TXT_KEY_DN_GRE21" },
//Persia
	{	 L"TXT_KEY_DN_PER00", L"TXT_KEY_DN_PER01", L"TXT_KEY_DN_PER02", L"TXT_KEY_DN_PER03",  L"TXT_KEY_DN_PER04",  L"TXT_KEY_DN_PER05",  L"TXT_KEY_DN_PER06",  L"TXT_KEY_DN_PER07",  L"TXT_KEY_DN_PER08",  L"TXT_KEY_DN_PER09",  L"TXT_KEY_DN_PER10",  L"TXT_KEY_DN_PER11",  L"TXT_KEY_DN_PER12",  L"TXT_KEY_DN_PER13",  L"TXT_KEY_DN_PER14",  L"TXT_KEY_DN_PER15",  L"TXT_KEY_DN_PER16",  L"TXT_KEY_DN_PER17",  L"TXT_KEY_DN_PER18",  L"TXT_KEY_DN_PER19",  L"TXT_KEY_DN_PER20",  L"TXT_KEY_DN_PER21" },
//Carthage
	{	 L"TXT_KEY_DN_CAR00", L"TXT_KEY_DN_CAR01", L"TXT_KEY_DN_CAR02", L"TXT_KEY_DN_CAR03",  L"TXT_KEY_DN_CAR04",  L"TXT_KEY_DN_CAR05",  L"TXT_KEY_DN_CAR06",  L"TXT_KEY_DN_CAR07",  L"TXT_KEY_DN_CAR08",  L"TXT_KEY_DN_CAR09",  L"TXT_KEY_DN_CAR10",  L"TXT_KEY_DN_CAR11",  L"TXT_KEY_DN_CAR12",  L"TXT_KEY_DN_CAR13",  L"TXT_KEY_DN_CAR14",  L"TXT_KEY_DN_CAR15",  L"TXT_KEY_DN_CAR16",  L"TXT_KEY_DN_CAR17",  L"TXT_KEY_DN_CAR18",  L"TXT_KEY_DN_CAR19",  L"TXT_KEY_DN_CAR20",  L"TXT_KEY_DN_CAR21" },
//Rome
	{	 L"TXT_KEY_DN_ROM00", L"TXT_KEY_DN_ROM01", L"TXT_KEY_DN_ROM02", L"TXT_KEY_DN_ROM03",  L"TXT_KEY_DN_ROM04",  L"TXT_KEY_DN_ROM05",  L"TXT_KEY_DN_ROM06",  L"TXT_KEY_DN_ROM07",  L"TXT_KEY_DN_ROM08",  L"TXT_KEY_DN_ROM09",  L"TXT_KEY_DN_ROM10",  L"TXT_KEY_DN_ROM11",  L"TXT_KEY_DN_ROM12",  L"TXT_KEY_DN_ROM13",  L"TXT_KEY_DN_ROM14",  L"TXT_KEY_DN_ROM15",  L"TXT_KEY_DN_ROM16",  L"TXT_KEY_DN_ROM17",  L"TXT_KEY_DN_ROM18",  L"TXT_KEY_DN_ROM19",  L"TXT_KEY_DN_ROM20",  L"TXT_KEY_DN_ROM21" },
//Japan
	{	 L"TXT_KEY_DN_JAP00", L"TXT_KEY_DN_JAP01", L"TXT_KEY_DN_JAP02", L"TXT_KEY_DN_JAP03",  L"TXT_KEY_DN_JAP04",  L"TXT_KEY_DN_JAP05",  L"TXT_KEY_DN_JAP06",  L"TXT_KEY_DN_JAP07",  L"TXT_KEY_DN_JAP08",  L"TXT_KEY_DN_JAP09",  L"TXT_KEY_DN_JAP10",  L"TXT_KEY_DN_JAP11",  L"TXT_KEY_DN_JAP12",  L"TXT_KEY_DN_JAP13",  L"TXT_KEY_DN_JAP14",  L"TXT_KEY_DN_JAP15",  L"TXT_KEY_DN_JAP16",  L"TXT_KEY_DN_JAP17",  L"TXT_KEY_DN_JAP18",  L"TXT_KEY_DN_JAP19",  L"TXT_KEY_DN_JAP20",  L"TXT_KEY_DN_JAP21" },
//Ethiopia
	{	 L"TXT_KEY_DN_ETH00", L"TXT_KEY_DN_ETH01", L"TXT_KEY_DN_ETH02", L"TXT_KEY_DN_ETH03",  L"TXT_KEY_DN_ETH04",  L"TXT_KEY_DN_ETH05",  L"TXT_KEY_DN_ETH06",  L"TXT_KEY_DN_ETH07",  L"TXT_KEY_DN_ETH08",  L"TXT_KEY_DN_ETH09",  L"TXT_KEY_DN_ETH10",  L"TXT_KEY_DN_ETH11",  L"TXT_KEY_DN_ETH12",  L"TXT_KEY_DN_ETH13",  L"TXT_KEY_DN_ETH14",  L"TXT_KEY_DN_ETH15",  L"TXT_KEY_DN_ETH16",  L"TXT_KEY_DN_ETH17",  L"TXT_KEY_DN_ETH18",  L"TXT_KEY_DN_ETH19",  L"TXT_KEY_DN_ETH20",  L"TXT_KEY_DN_ETH21" },
//Maya
	{	 L"TXT_KEY_DN_MAY00", L"TXT_KEY_DN_MAY01", L"TXT_KEY_DN_MAY02", L"TXT_KEY_DN_MAY03",  L"TXT_KEY_DN_MAY04",  L"TXT_KEY_DN_MAY05",  L"TXT_KEY_DN_MAY06",  L"TXT_KEY_DN_MAY07",  L"TXT_KEY_DN_MAY08",  L"TXT_KEY_DN_MAY09",  L"TXT_KEY_DN_MAY10",  L"TXT_KEY_DN_MAY11",  L"TXT_KEY_DN_MAY12",  L"TXT_KEY_DN_MAY13",  L"TXT_KEY_DN_MAY14",  L"TXT_KEY_DN_MAY15",  L"TXT_KEY_DN_MAY16",  L"TXT_KEY_DN_MAY17",  L"TXT_KEY_DN_MAY18",  L"TXT_KEY_DN_MAY19",  L"TXT_KEY_DN_MAY20",  L"TXT_KEY_DN_MAY21" },
//Viking
	{	 L"TXT_KEY_DN_VIK00", L"TXT_KEY_DN_VIK01", L"TXT_KEY_DN_VIK02", L"TXT_KEY_DN_VIK03",  L"TXT_KEY_DN_VIK04",  L"TXT_KEY_DN_VIK05",  L"TXT_KEY_DN_VIK06",  L"TXT_KEY_DN_VIK07",  L"TXT_KEY_DN_VIK08",  L"TXT_KEY_DN_VIK09",  L"TXT_KEY_DN_VIK10",  L"TXT_KEY_DN_VIK11",  L"TXT_KEY_DN_VIK12",  L"TXT_KEY_DN_VIK13",  L"TXT_KEY_DN_VIK14",  L"TXT_KEY_DN_VIK15",  L"TXT_KEY_DN_VIK16",  L"TXT_KEY_DN_VIK17",  L"TXT_KEY_DN_VIK18",  L"TXT_KEY_DN_VIK19",  L"TXT_KEY_DN_VIK20",  L"TXT_KEY_DN_VIK21" },
//Arabia
	{	 L"TXT_KEY_DN_ARA00", L"TXT_KEY_DN_ARA01", L"TXT_KEY_DN_ARA02", L"TXT_KEY_DN_ARA03",  L"TXT_KEY_DN_ARA04",  L"TXT_KEY_DN_ARA05",  L"TXT_KEY_DN_ARA06",  L"TXT_KEY_DN_ARA07",  L"TXT_KEY_DN_ARA08",  L"TXT_KEY_DN_ARA09",  L"TXT_KEY_DN_ARA10",  L"TXT_KEY_DN_ARA11",  L"TXT_KEY_DN_ARA12",  L"TXT_KEY_DN_ARA13",  L"TXT_KEY_DN_ARA14",  L"TXT_KEY_DN_ARA15",  L"TXT_KEY_DN_ARA16",  L"TXT_KEY_DN_ARA17",  L"TXT_KEY_DN_ARA18",  L"TXT_KEY_DN_ARA19",  L"TXT_KEY_DN_ARA20",  L"TXT_KEY_DN_ARA21" },
//Khmer
	{	 L"TXT_KEY_DN_KHM00", L"TXT_KEY_DN_KHM01", L"TXT_KEY_DN_KHM02", L"TXT_KEY_DN_KHM03",  L"TXT_KEY_DN_KHM04",  L"TXT_KEY_DN_KHM05",  L"TXT_KEY_DN_KHM06",  L"TXT_KEY_DN_KHM07",  L"TXT_KEY_DN_KHM08",  L"TXT_KEY_DN_KHM09",  L"TXT_KEY_DN_KHM10",  L"TXT_KEY_DN_KHM11",  L"TXT_KEY_DN_KHM12",  L"TXT_KEY_DN_KHM13",  L"TXT_KEY_DN_KHM14",  L"TXT_KEY_DN_KHM15",  L"TXT_KEY_DN_KHM16",  L"TXT_KEY_DN_KHM17",  L"TXT_KEY_DN_KHM18",  L"TXT_KEY_DN_KHM19",  L"TXT_KEY_DN_KHM20",  L"TXT_KEY_DN_KHM21" },
//Spain
	{	 L"TXT_KEY_DN_SPA00", L"TXT_KEY_DN_SPA01", L"TXT_KEY_DN_SPA02", L"TXT_KEY_DN_SPA03",  L"TXT_KEY_DN_SPA04",  L"TXT_KEY_DN_SPA05",  L"TXT_KEY_DN_SPA06",  L"TXT_KEY_DN_SPA07",  L"TXT_KEY_DN_SPA08",  L"TXT_KEY_DN_SPA09",  L"TXT_KEY_DN_SPA10",  L"TXT_KEY_DN_SPA11",  L"TXT_KEY_DN_SPA12",  L"TXT_KEY_DN_SPA13",  L"TXT_KEY_DN_SPA14",  L"TXT_KEY_DN_SPA15",  L"TXT_KEY_DN_SPA16",  L"TXT_KEY_DN_SPA17",  L"TXT_KEY_DN_SPA18",  L"TXT_KEY_DN_SPA19",  L"TXT_KEY_DN_SPA20",  L"TXT_KEY_DN_SPA21" },
//France
	{	 L"TXT_KEY_DN_FRA00", L"TXT_KEY_DN_FRA01", L"TXT_KEY_DN_FRA02", L"TXT_KEY_DN_FRA03",  L"TXT_KEY_DN_FRA04",  L"TXT_KEY_DN_FRA05",  L"TXT_KEY_DN_FRA06",  L"TXT_KEY_DN_FRA07",  L"TXT_KEY_DN_FRA08",  L"TXT_KEY_DN_FRA09",  L"TXT_KEY_DN_FRA10",  L"TXT_KEY_DN_FRA11",  L"TXT_KEY_DN_FRA12",  L"TXT_KEY_DN_FRA13",  L"TXT_KEY_DN_FRA14",  L"TXT_KEY_DN_FRA15",  L"TXT_KEY_DN_FRA16",  L"TXT_KEY_DN_FRA17",  L"TXT_KEY_DN_FRA18",  L"TXT_KEY_DN_FRA19",  L"TXT_KEY_DN_FRA20",  L"TXT_KEY_DN_FRA21" },
//England
	{	 L"TXT_KEY_DN_ENG00", L"TXT_KEY_DN_ENG01", L"TXT_KEY_DN_ENG02", L"TXT_KEY_DN_ENG03",  L"TXT_KEY_DN_ENG04",  L"TXT_KEY_DN_ENG05",  L"TXT_KEY_DN_ENG06",  L"TXT_KEY_DN_ENG07",  L"TXT_KEY_DN_ENG08",  L"TXT_KEY_DN_ENG09",  L"TXT_KEY_DN_ENG10",  L"TXT_KEY_DN_ENG11",  L"TXT_KEY_DN_ENG12",  L"TXT_KEY_DN_ENG13",  L"TXT_KEY_DN_ENG14",  L"TXT_KEY_DN_ENG15",  L"TXT_KEY_DN_ENG16",  L"TXT_KEY_DN_ENG17",  L"TXT_KEY_DN_ENG18",  L"TXT_KEY_DN_ENG19",  L"TXT_KEY_DN_ENG20",  L"TXT_KEY_DN_ENG21" },
//Germany
	{	 L"TXT_KEY_DN_GER00", L"TXT_KEY_DN_GER01", L"TXT_KEY_DN_GER02", L"TXT_KEY_DN_GER03",  L"TXT_KEY_DN_GER04",  L"TXT_KEY_DN_GER05",  L"TXT_KEY_DN_GER06",  L"TXT_KEY_DN_GER07",  L"TXT_KEY_DN_GER08",  L"TXT_KEY_DN_GER09",  L"TXT_KEY_DN_GER10",  L"TXT_KEY_DN_GER11",  L"TXT_KEY_DN_GER12",  L"TXT_KEY_DN_GER13",  L"TXT_KEY_DN_GER14",  L"TXT_KEY_DN_GER15",  L"TXT_KEY_DN_GER16",  L"TXT_KEY_DN_GER17",  L"TXT_KEY_DN_GER18",  L"TXT_KEY_DN_GER19",  L"TXT_KEY_DN_GER20",  L"TXT_KEY_DN_GER21" },
//Russia
	{	 L"TXT_KEY_DN_RUS00", L"TXT_KEY_DN_RUS01", L"TXT_KEY_DN_RUS02", L"TXT_KEY_DN_RUS03",  L"TXT_KEY_DN_RUS04",  L"TXT_KEY_DN_RUS05",  L"TXT_KEY_DN_RUS06",  L"TXT_KEY_DN_RUS07",  L"TXT_KEY_DN_RUS08",  L"TXT_KEY_DN_RUS09",  L"TXT_KEY_DN_RUS10",  L"TXT_KEY_DN_RUS11",  L"TXT_KEY_DN_RUS12",  L"TXT_KEY_DN_RUS13",  L"TXT_KEY_DN_RUS14",  L"TXT_KEY_DN_RUS15",  L"TXT_KEY_DN_RUS16",  L"TXT_KEY_DN_RUS17",  L"TXT_KEY_DN_RUS18",  L"TXT_KEY_DN_RUS19",  L"TXT_KEY_DN_RUS20",  L"TXT_KEY_DN_RUS21" },
//Holland
	{	 L"TXT_KEY_DN_NED00", L"TXT_KEY_DN_NED01", L"TXT_KEY_DN_NED02", L"TXT_KEY_DN_NED03",  L"TXT_KEY_DN_NED04",  L"TXT_KEY_DN_NED05",  L"TXT_KEY_DN_NED06",  L"TXT_KEY_DN_NED07",  L"TXT_KEY_DN_NED08",  L"TXT_KEY_DN_NED09",  L"TXT_KEY_DN_NED10",  L"TXT_KEY_DN_NED11",  L"TXT_KEY_DN_NED12",  L"TXT_KEY_DN_NED13",  L"TXT_KEY_DN_NED14",  L"TXT_KEY_DN_NED15",  L"TXT_KEY_DN_NED16",  L"TXT_KEY_DN_NED17",  L"TXT_KEY_DN_NED18",  L"TXT_KEY_DN_NED19",  L"TXT_KEY_DN_NED20",  L"TXT_KEY_DN_NED21" },
//Mali
	{	 L"TXT_KEY_DN_MAL00", L"TXT_KEY_DN_MAL01", L"TXT_KEY_DN_MAL02", L"TXT_KEY_DN_MAL03",  L"TXT_KEY_DN_MAL04",  L"TXT_KEY_DN_MAL05",  L"TXT_KEY_DN_MAL06",  L"TXT_KEY_DN_MAL07",  L"TXT_KEY_DN_MAL08",  L"TXT_KEY_DN_MAL09",  L"TXT_KEY_DN_MAL10",  L"TXT_KEY_DN_MAL11",  L"TXT_KEY_DN_MAL12",  L"TXT_KEY_DN_MAL13",  L"TXT_KEY_DN_MAL14",  L"TXT_KEY_DN_MAL15",  L"TXT_KEY_DN_MAL16",  L"TXT_KEY_DN_MAL17",  L"TXT_KEY_DN_MAL18",  L"TXT_KEY_DN_MAL19",  L"TXT_KEY_DN_MAL20",  L"TXT_KEY_DN_MAL21" },
//Portugal
	{	 L"TXT_KEY_DN_POR00", L"TXT_KEY_DN_POR01", L"TXT_KEY_DN_POR02", L"TXT_KEY_DN_POR03",  L"TXT_KEY_DN_POR04",  L"TXT_KEY_DN_POR05",  L"TXT_KEY_DN_POR06",  L"TXT_KEY_DN_POR07",  L"TXT_KEY_DN_POR08",  L"TXT_KEY_DN_POR09",  L"TXT_KEY_DN_POR10",  L"TXT_KEY_DN_POR11",  L"TXT_KEY_DN_POR12",  L"TXT_KEY_DN_POR13",  L"TXT_KEY_DN_POR14",  L"TXT_KEY_DN_POR15",  L"TXT_KEY_DN_POR16",  L"TXT_KEY_DN_POR17",  L"TXT_KEY_DN_POR18",  L"TXT_KEY_DN_POR19",  L"TXT_KEY_DN_POR20",  L"TXT_KEY_DN_POR21" },
//Inca
	{	 L"TXT_KEY_DN_INC00", L"TXT_KEY_DN_INC01", L"TXT_KEY_DN_INC02", L"TXT_KEY_DN_INC03",  L"TXT_KEY_DN_INC04",  L"TXT_KEY_DN_INC05",  L"TXT_KEY_DN_INC06",  L"TXT_KEY_DN_INC07",  L"TXT_KEY_DN_INC08",  L"TXT_KEY_DN_INC09",  L"TXT_KEY_DN_INC10",  L"TXT_KEY_DN_INC11",  L"TXT_KEY_DN_INC12",  L"TXT_KEY_DN_INC13",  L"TXT_KEY_DN_INC14",  L"TXT_KEY_DN_INC15",  L"TXT_KEY_DN_INC16",  L"TXT_KEY_DN_INC17",  L"TXT_KEY_DN_INC18",  L"TXT_KEY_DN_INC19",  L"TXT_KEY_DN_INC20",  L"TXT_KEY_DN_INC21" },
//Mongolia
	{	 L"TXT_KEY_DN_MON00", L"TXT_KEY_DN_MON01", L"TXT_KEY_DN_MON02", L"TXT_KEY_DN_MON03",  L"TXT_KEY_DN_MON04",  L"TXT_KEY_DN_MON05",  L"TXT_KEY_DN_MON06",  L"TXT_KEY_DN_MON07",  L"TXT_KEY_DN_MON08",  L"TXT_KEY_DN_MON09",  L"TXT_KEY_DN_MON10",  L"TXT_KEY_DN_MON11",  L"TXT_KEY_DN_MON12",  L"TXT_KEY_DN_MON13",  L"TXT_KEY_DN_MON14",  L"TXT_KEY_DN_MON15",  L"TXT_KEY_DN_MON16",  L"TXT_KEY_DN_MON17",  L"TXT_KEY_DN_MON18",  L"TXT_KEY_DN_MON19",  L"TXT_KEY_DN_MON20",  L"TXT_KEY_DN_MON21" },
//Aztec
	{	 L"TXT_KEY_DN_AZT00", L"TXT_KEY_DN_AZT01", L"TXT_KEY_DN_AZT02", L"TXT_KEY_DN_AZT03",  L"TXT_KEY_DN_AZT04",  L"TXT_KEY_DN_AZT05",  L"TXT_KEY_DN_AZT06",  L"TXT_KEY_DN_AZT07",  L"TXT_KEY_DN_AZT08",  L"TXT_KEY_DN_AZT09",  L"TXT_KEY_DN_AZT10",  L"TXT_KEY_DN_AZT11",  L"TXT_KEY_DN_AZT12",  L"TXT_KEY_DN_AZT13",  L"TXT_KEY_DN_AZT14",  L"TXT_KEY_DN_AZT15",  L"TXT_KEY_DN_AZT16",  L"TXT_KEY_DN_AZT17",  L"TXT_KEY_DN_AZT18",  L"TXT_KEY_DN_AZT19",  L"TXT_KEY_DN_AZT20",  L"TXT_KEY_DN_AZT21" },
//Turkey
	{	 L"TXT_KEY_DN_TUR00", L"TXT_KEY_DN_TUR01", L"TXT_KEY_DN_TUR02", L"TXT_KEY_DN_TUR03",  L"TXT_KEY_DN_TUR04",  L"TXT_KEY_DN_TUR05",  L"TXT_KEY_DN_TUR06",  L"TXT_KEY_DN_TUR07",  L"TXT_KEY_DN_TUR08",  L"TXT_KEY_DN_TUR09",  L"TXT_KEY_DN_TUR10",  L"TXT_KEY_DN_TUR11",  L"TXT_KEY_DN_TUR12",  L"TXT_KEY_DN_TUR13",  L"TXT_KEY_DN_TUR14",  L"TXT_KEY_DN_TUR15",  L"TXT_KEY_DN_TUR16",  L"TXT_KEY_DN_TUR17",  L"TXT_KEY_DN_TUR18",  L"TXT_KEY_DN_TUR19",  L"TXT_KEY_DN_TUR20",  L"TXT_KEY_DN_TUR21" },
//America
	{	 L"TXT_KEY_DN_AME00", L"TXT_KEY_DN_AME01", L"TXT_KEY_DN_AME02", L"TXT_KEY_DN_AME03",  L"TXT_KEY_DN_AME04",  L"TXT_KEY_DN_AME05",  L"TXT_KEY_DN_AME06",  L"TXT_KEY_DN_AME07",  L"TXT_KEY_DN_AME08",  L"TXT_KEY_DN_AME09",  L"TXT_KEY_DN_AME10",  L"TXT_KEY_DN_AME11",  L"TXT_KEY_DN_AME12",  L"TXT_KEY_DN_AME13",  L"TXT_KEY_DN_AME14",  L"TXT_KEY_DN_AME15",  L"TXT_KEY_DN_AME16",  L"TXT_KEY_DN_AME17",  L"TXT_KEY_DN_AME18",  L"TXT_KEY_DN_AME19",  L"TXT_KEY_DN_AME20",  L"TXT_KEY_DN_AME21" }};


int civDynamicNamesFlag[28] = 	{	 1,  1,  0,  0,  1,  0,  1,  1,  0,  0,  1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  1,  0 };
//									EGY	IND CHI ELA BAB GRE PER CAR ROM JAP ETH MAY VIK ARA KHM SPA FRA ENG GER RUS HOL MAL POR INC MON AZT TUR AME
// 1 = REL, 0 = GOV

int civDynamicNamesEraThreshold[28] = { 2,  3,  4,  4,  2,  2,  3,  2,  3,  4,  3,  3,  3,  4,  4,  4,  4,  4,  4,  4,  4,  3,  4,  3,  3,  3,  3,  4};
