import wtnDice

def castYao():
	#todo adjust tp call a wtnDice.di['totl'] getter method 
	cast = 	wtnDice.rollTotl(3,2,{})
	if cast == 3:
	    return '_________  > Jiu >  ___   ___'
	elif cast == 4:
	    return '___   ___ |  Xin  | ___   ___'
	elif cast == 5:
	    return '_________ |  Xin  | _________'
	else: #cast == 6:
	    return '___   ___  > Jiu >  _________'

def castGua():
	gua = []
	for i in range(1,7):
	    gua.append(str(i) + " " + castYao())
	gua.reverse()
	for j in range(0,6):
	    print gua[j]
	

def main():
     print castGua()

if __name__=='__main__':
    main()
