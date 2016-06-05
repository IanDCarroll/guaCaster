import wtnDice

def castYao():
	#todo adjust tp call a wtnDice.di['totl'] getter method 
	cast = 	wtnDice.rollTotl(3,2,{})
	return cast

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
	idGua(guaCode)

def idGua(guaCode):
	#Gua[0] is the upper trigram; Gua[1] is the lower trigram
	jiuGua = [[],[]] #Old situation
	yiGua = [[],[]] #The situation which affects the change
	xinGua =[[],[]] #New situation
	#Lower Trigram

	for i in range(0,3): #Upper Trigram
	    if guaCode[i] == 3:    #Yang changes to Yin
		jiuGua[0].append(9)	#Yang
		yiGua[0].append(9)	#Active
		xinGua[0].append(6)	#Yin
	    elif guaCode[i] == 4:  #Yin stays yin
		jiuGua[0].append(6)	#Yin
		yiGua[0].append(6)	#Passive
		xinGua[0].append(6)	#Yin
	    elif guaCode[i] == 5:  #Yang stays Yang
		jiuGua[0].append(9)	#Yang
		yiGua[0].append(6)	#Passive
		xinGua[0].append(9)	#Yang
	    else: #guaCode[i] ==6: #Yin changes to Yang
		jiuGua[0].append(6)	#Yin
		yiGua[0].append(9)	#Active
		xinGua[0].append(9)	#Yang

	for i in range(3,6): #Lower Trigram
	    if guaCode[i] == 3:    #Yang changes to Yin
		jiuGua[1].append(9)	#Yang
		yiGua[1].append(9)	#Active
		xinGua[1].append(6)	#Yin
	    elif guaCode[i] == 4:  #Yin stays yin
		jiuGua[1].append(6)	#Yin
		yiGua[1].append(6)	#Passive
		xinGua[1].append(6)	#Yin
	    elif guaCode[i] == 5:  #Yang stays Yang
		jiuGua[1].append(9)	#Yang
		yiGua[1].append(6)	#Passive
		xinGua[1].append(9)	#Yang
	    else: #guaCode[i] ==6: #Yin changes to Yang
		jiuGua[1].append(6)	#Yin
		yiGua[1].append(9)	#Active
		xinGua[1].append(9)	#Yang

	print jiuGua
	print yiGua
	print xinGua
	



def main():
     print castGua()

if __name__=='__main__':
    main()
