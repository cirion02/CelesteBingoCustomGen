import json

import generators.generatorJsons.newLockout as newLockout

import generators.sortBaseGen as sortBaseGen
import generators.invasionGen as invasionGen

def generate(genType:str, seed:str) -> dict:
	return gameModeDict[genType](seed)

gameModeDict = {
	"Sorted New Lockout" :
		lambda seed : sortBaseGen.genSortedBoard(newLockout.newLockoutJson, seed),
	"Invasion New Lockout" :
		lambda seed : invasionGen.genInvasionBoard(newLockout.newLockoutJson, seed),
}

gameModeSet = tuple(list(gameModeDict.keys()))