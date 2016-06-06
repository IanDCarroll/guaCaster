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
	jGua = [[],[]] #Old situation
	yGua = [[],[]] #The situation which affects the change
	xGua =[[],[]] #New situation
	#Lower Trigram
	jiuGua = ''
	yiGua = ''
	xinGua = ''

	for i in range(0,3): #Upper Trigram
	    if guaCode[i] == 3:    #Yang changes to Yin
		jGua[0].append(9)	#Yang
		yGua[0].append(9)	#Active
		xGua[0].append(6)	#Yin
	    elif guaCode[i] == 4:  #Yin stays yin
		jGua[0].append(6)	#Yin
		yGua[0].append(6)	#Passive
		xGua[0].append(6)	#Yin
	    elif guaCode[i] == 5:  #Yang stays Yang
		jGua[0].append(9)	#Yang
		yGua[0].append(6)	#Passive
		xGua[0].append(9)	#Yang
	    else: #guaCode[i] ==6: #Yin changes to Yang
		jGua[0].append(6)	#Yin
		yGua[0].append(9)	#Active
		xGua[0].append(9)	#Yang

	for i in range(3,6): #Lower Trigram
	    if guaCode[i] == 3:    #Yang changes to Yin
		jGua[1].append(9)	#Yang
		yGua[1].append(9)	#Active
		xGua[1].append(6)	#Yin
	    elif guaCode[i] == 4:  #Yin stays yin
		jGua[1].append(6)	#Yin
		yGua[1].append(6)	#Passive
		xGua[1].append(6)	#Yin
	    elif guaCode[i] == 5:  #Yang stays Yang
		jGua[1].append(9)	#Yang
		yGua[1].append(6)	#Passive
		xGua[1].append(9)	#Yang
	    else: #guaCode[i] ==6: #Yin changes to Yang
		jGua[1].append(6)	#Yin
		yGua[1].append(9)	#Active
		xGua[1].append(9)	#Yang

	#commands like x += 2 or x = "poop" 
	#don't point back to the public variable x
	#when it's passed as an arg.
	def nameGua(gua,guaName):
		if gua[1] == [6,6,9]: #Lower Zhen
		    if gua[0] == [6,6,9]:
			guaName = '51'
		    elif gua[0] == [9,6,9]:
			guaName = '21'
		    elif gua[0] == [6,9,9]:
			guaName = '17'
		    elif gua[0] == [9,9,9]:
			guaName = '25'
		    elif gua[0] == [9,9,6]:
			guaName = '42'
		    elif gua[0] == [6,9,6]:
			guaName = '3'
		    elif gua[0] == [9,6,6]:
			guaName = '27'
		    else: #gua[0] == [6,6,6]:
			guaName = '24'

		elif gua[1] == [9,6,9]: #Lower Li
		    if gua[0] == [6,6,9]:
			guaName = '55'
		    elif gua[0] == [9,6,9]:
			guaName = '30'
		    elif gua[0] == [6,9,9]:
			guaName = '49'
		    elif gua[0] == [9,9,9]:
			guaName = '13'
		    elif gua[0] == [9,9,6]:
			guaName = '37'
		    elif gua[0] == [6,9,6]:
			guaName = '63'
		    elif gua[0] == [9,6,6]:
			guaName = '22'
		    else: #gua[0] == [6,6,6]:
			guaName = '36'

		elif gua[1] == [6,9,9]: #Lower Dui
		    if gua[0] == [6,6,9]:
			guaName = '54'
		    elif gua[0] == [9,6,9]:
			guaName = '38'
		    elif gua[0] == [6,9,9]:
			guaName = '58'
		    elif gua[0] == [9,9,9]:
			guaName = '10'
		    elif gua[0] == [9,9,6]:
			guaName = '61'
		    elif gua[0] == [6,9,6]:
			guaName = '60'
		    elif gua[0] == [9,6,6]:
			guaName = '41'
		    else: #gua[0] == [6,6,6]:
			guaName = '19'

		elif gua[1] == [9,9,9]: #Lower Qian
		    if gua[0] == [6,6,9]:
			guaName = '34'
		    elif gua[0] == [9,6,9]:
			guaName = '14'
		    elif gua[0] == [6,9,9]:
			guaName = '43'
		    elif gua[0] == [9,9,9]:
			guaName = '1'
		    elif gua[0] == [9,9,6]:
			guaName = '9'
		    elif gua[0] == [6,9,6]:
			guaName = '5'
		    elif gua[0] == [9,6,6]:
			guaName = '26'
		    else: #gua[0] == [6,6,6]:
			guaName = '11'

		elif gua[1] == [9,9,6]: #Lower Xun
		    if gua[0] == [6,6,9]:
			guaName = '32'
		    elif gua[0] == [9,6,9]:
			guaName = '50'
		    elif gua[0] == [6,9,9]:
			guaName = '28'
		    elif gua[0] == [9,9,9]:
			guaName = '44'
		    elif gua[0] == [9,9,6]:
			guaName = '57'
		    elif gua[0] == [6,9,6]:
			guaName = '48'
		    elif gua[0] == [9,6,6]:
			guaName = '18'
		    else: #gua[0] == [6,6,6]:
			guaName = '46'

		elif gua[1] == [6,9,6]: #Lower Kan
		    if gua[0] == [6,6,9]:
			guaName = '40'
		    elif gua[0] == [9,6,9]:
			guaName = '64'
		    elif gua[0] == [6,9,9]:
			guaName = '47'
		    elif gua[0] == [9,9,9]:
			guaName = '6'
		    elif gua[0] == [9,9,6]:
			guaName = '59'
		    elif gua[0] == [6,9,6]:
			guaName = '29'
		    elif gua[0] == [9,6,6]:
			guaName = '4'
		    else: #gua[0] == [6,6,6]:
			guaName = '7'

		elif gua[1] == [9,6,6]: #Lower Gen
		    if gua[0] == [6,6,9]:
			guaName = '62'
		    elif gua[0] == [9,6,9]:
			guaName = '56'
		    elif gua[0] == [6,9,9]:
			guaName = '31'
		    elif gua[0] == [9,9,9]:
			guaName = '33'
		    elif gua[0] == [9,9,6]:
			guaName = '53'
		    elif gua[0] == [6,9,6]:
			guaName = '39'
		    elif gua[0] == [9,6,6]:
			guaName = '52'
		    else: #gua[0] == [6,6,6]:
			guaName = '15'

		else: #gua[1] == [6,6,6]: #Lower Kun
		    if gua[0] == [6,6,9]:
			guaName = '16'
		    elif gua[0] == [9,6,9]:
			guaName = '35'
		    elif gua[0] == [6,9,9]:
			guaName = '45'
		    elif gua[0] == [9,9,9]:
			guaName = '12'
		    elif gua[0] == [9,9,6]:
			guaName = '20'
		    elif gua[0] == [6,9,6]:
			guaName = '8'
		    elif gua[0] == [6,6,9]:
			guaName = '23'
		    else: #gua[0] == [6,6,6]:
			guaName = '2'

	nameGua(jGua,jiuGua)
	nameGua(yGua,yiGua)
	nameGua(xGua,xinGua)

	print jiuGua
	print yiGua
	print xinGua
	



def main():
     print castGua()

if __name__=='__main__':
    main()
