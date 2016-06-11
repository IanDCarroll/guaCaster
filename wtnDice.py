#python port of whtnDice:

#import neccesary libraries
from datetime import datetime
#placeholder for physics module
import numpy as np
import os

def physics(di):
    rolls = []
    counter = 0
    while counter < di['nmbr']:
	#Sam @ https://github.com/swacad really helped on this
	#and on ironing out the code so it actually runs.
	#this is a cryptogrphically secure seed, 
	#so it's not predictible even by a really awesome computer!
	np.random.seed(int(os.urandom(4).encode('hex'),16))
	rolls.append((int((np.random.random()) * (di['sids'])))+1)
	counter += 1

    di['rols'] = rolls
    di['totl'] = sum(rolls)
    di['time'] = datetime.now().isoformat(' ')

def rolDBize(di, rolDB):
    rolNtry = [di['time'],di['nmbr'],di['sids'],di['rols'],di['totl']]
    rolDB.append(rolNtry)

def whtnize(di):
    if di['totl'] == di['nmbr']:
	di['whtn'] = ' Wheaton!'
    elif di['totl'] == di['nmbr'] * di['sids']:
	di['whtn'] = ' Percy!'
    elif di['totl'] < (di['nmbr'] * di['sids'])/3:
	di['whtn'] = ' lesser wheaton.'
    elif di['totl'] > ((di['nmbr'] * di['sids'])/3)*2:
	di['whtn'] = ' lesser Percy.'
    else: 
	di['whtn'] = ''

#Print function not used when wtnDice not used as main. 
def rollOut(di):
    return "%s d%s: %s Total: %s%s" % (di['nmbr'], di['sids'],
	di['rols'], di['totl'], di['whtn'])

#calling functions
def roll(dNum,dSid,di,rolDB): 
    di['nmbr'] = dNum
    di['sids'] = dSid

    physics(di)
    rolDBize(di, rolDB)
    whtnize(di)
    return di['totl']


#def rollMix():

def rollHigher(dNum,dSid,di,rolDB):
    di['nmbr'] = dNum
    di['sids'] = dSid
    physics(di)

    di['nmbr'] = 1
    sort = sorted(di['rols'], key=None, reverse=True)
    di['totl'] = sort[0]
    whtnize(di)

    di['nmbr'] = 'H'
    rolDBize(di, rolDB)

    return di['totl']

def rollLower(dNum,dSid,di,rolDB):
    di['nmbr'] = dNum
    di['sids'] = dSid
    physics(di)

    di['nmbr'] = 1
    sort = sorted(di['rols'])
    di['totl'] = sort[0]
    whtnize(di)

    di['nmbr'] = 'L'
    rolDBize(di, rolDB)

    return di['totl']

def rollDigit(dNum,dSid,di,rolDB):
    di['nmbr'] = dNum
    di['sids'] = dSid
    physics(di)

    di['rols'].reverse()
    di['totl'] = 0
    count = 0
    for roll in di['rols']:
	if count == 0:
	    di['totl'] += (roll % di['sids'])
	    count += 1 
	else:
	    di['totl'] += (roll % di['sids']) * (di['sids'] ** count)
	    count += 1
    di['sids'] = di['sids'] ** di['nmbr']
    if di['totl'] == 0: di['totl'] = di['sids']

    di['nmbr'] = 1
    di['rols'].reverse()
    whtnize(di)
    di['nmbr'] = 'D'

    return di['totl']

#def rollExtra():

#def rollManual():

def main():
    di = {'time':'','nmbr':0,'sids':0,'rols':[],'totl':0,'whtn':''}
    rolDB = []

if __name__ == '__main__':
    main()
