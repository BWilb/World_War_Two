import random
import allied_classes
import comintern_ww2_text_adventure

def roosevelt_intial_tank(fdr):
    """Initial tank production of USA, from 1,200 to 4,500"""
    production = random.randrange(1200, 4500)
    for i in range(production):
        tank = comintern_ww2_text_adventure.tanks.PattonTank()
        fdr.tank_list.append(tank)

def roosevelt_initial_soldier(fdr):
    """Initial recruitment of soldiers, from 30,000 to 55,000"""
    recruits = random.randrange(30000, 55000)
    for i in range(recruits):
        soldier = allied_classes.AmericanSoldier()
        fdr.troop_list.append(soldier)

def fdr_ww2(fdr):

def main():
    roosevelt = allied_classes.FDR()
    roosevelt_intial_tank(roosevelt)
    roosevelt_initial_soldier(roosevelt)
    fdr_ww2(roosevelt)