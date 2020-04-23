#D&D Attack Roller
#12-04-2020
#A script to perform attack rolls of D&D weapons 
import random


attackModifier = ('')
weaponChoice = ('g')
        # Find out the attack modifier from the user
while attackModifier not in range(0, 6):
    print ('what is your attack modifier?')
    if attackModifier in range(0, 6):
        print ('your attack modifier is ' + str(attackModifier))
        break
    attackModifier = int(input())

        #find out which weapon the user is using and return the value of max damage for the weapon
def getWeapon(weaponChoice):
    print ('Will you be using a dagger, sword, or battleaxe?')
    weaponChoice = input()
    weaponChoice = weaponChoice.lower()
    if 's' in weaponChoice:
        print ('the sword is a fine selection')
        weaponChoice = ('6')
        playerAttack = False
        return weaponChoice
    elif 'd' in weaponChoice:
        print ('what a useless weapon')
        weaponChoice = ('4')
        playerAttack = False
        return weaponChoice
    elif 'b' in weaponChoice:
        print ('A slow but powerful weapon')
        weaponChoice = ('12')
        playerAttack = False
        return weaponChoice

def weaponDamage():
    if weaponChoice == 6:
        maxDamage = 6
        print ('sword 6')
    elif weaponChoice == 4:
        maxDamage = 4
        print ('dagger 4')
    elif weaponChoice == 12:
        maxDamage = 12
        print ('battleaxe 12')

playerAttack = True
getWeapon('')
weaponDamage()
print (str(weaponChoice))
