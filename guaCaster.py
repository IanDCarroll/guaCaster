import wtnDice
import guaNames

def castYao():
	#todo adjust tp call a wtnDice.di['totl'] getter method 
	cast = wtnDice.roll(3,2,{},[])
	return cast

def idGua(guaCode):

	jiuGua = 0 #Old situation
	yiGua = 0 #The situation which affects the change
	xinGua = 0 #New situation

	for i in range(0,6): #Upper Trigram
	    if guaCode[i] == 3:    #Yang changes to Yin
		jiuGua += 9 * (10 ** i)	#Yang
		yiGua += 9 * (10 ** i)	#Active
		xinGua += 6 * (10 ** i)	#Yin
	    elif guaCode[i] == 4:  #Yin stays yin
		jiuGua += 6 * (10 ** i)	#Yin
		yiGua += 6 * (10 ** i)	#Passive
		xinGua += 6 * (10 ** i)	#Yin
	    elif guaCode[i] == 5:  #Yang stays Yang
		jiuGua += 9 * (10 ** i)	#Yang
		yiGua += 6 * (10 ** i)	#Passive
		xinGua += 9 * (10 ** i)	#Yang
	    else: #guaCode[i] ==6: #Yin changes to Yang
		jiuGua += 6 * (10 ** i)	#Yin
		yiGua += 9 * (10 ** i)	#Active
		xinGua += 9 * (10 ** i)	#Yang

	a = guaNames.nameGua(jiuGua)
	b = guaNames.nameGua(yiGua)
	c = guaNames.nameGua(xinGua)

	return 'Jiu Gua: %s\nYi  Gua: %s\nXin Gua: %s' % (a,b,c)
	


def castGua():
	guaImag = []
	guaCode = []
	for i in range(0,6):
	    guaCode.append(castYao())
	guaCode.reverse() #gua are built from the bottom up
	for j in range(0,6):
	    if guaCode[j] == 3: #coins tossed are 1,1,1
		guaImag.append('_________  > Jiu >  ___   ___')
	    elif guaCode[j] == 4: #coins tossed are 1,2,1
		guaImag.append('___   ___ |  Xin  | ___   ___')
	    elif guaCode[j] == 5: #coins tossed are 2,1,2
		guaImag.append('_________ |  Xin  | _________')
	    else: #if guaCode[j] == 6: #coins tossed are 2,2,2
		guaImag.append('___   ___  > Jiu >  _________')
	    print guaImag[j]
	return idGua(guaCode)


def main():
     print castGua()

if __name__=='__main__':
    main()
