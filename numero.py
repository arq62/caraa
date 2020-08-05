def namer(inp):
	
		numstr = str(inp)
		numstr.lstrip('0')

		suffix = ['' , 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion','Undecillion','Duodecillion','Tredecillion','Quattuordecillion','Quindecillion','Hexdecillion','Septendecillion','Octodecillion','Novemdecillion','Vigintillion','Unvigintillion','Duovigintillion','Trevigintillion','Quattourvigintillion','Quinvigintillion','Hexvigintillion','Septenvigintillion','Octovigintillion','Novemvigintillion','Trigintillion','Untrigintillion','Duotrigintillion']
	
		singledigits = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]

		teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

		ty = ['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

		m = len(numstr) % 3
		if m == 1:
			numstr = '00' + numstr
		elif m == 2:
			numstr = '0' + numstr

		newle = len(numstr)/3
		newlen = int(newle)
		tripletlist =[]

		for i in range(newlen):
			k = numstr[3*i:3*i +3]
			tripletlist.append(k)


		def digitname(n):
			return singledigits[n]
	
		def hundreds(a):
			if a == 0:
				return ""
			else:
				return digitname(a)+' '+ 'hundred '

		def doublet(b,c):
			if b == 0:
				return digitname(c)
			elif b == 1:
				return teen[c]
			else:
				op_b = ty[b]		
				op_c = digitname(c)
				return op_b + ' ' + op_c
		

		def trp(trip):
			a = trip[0]
			b = trip[1]
			c = trip[2]
			op_a = hundreds(int(a))
			op_bc = doublet(int(b),int(c))
			return op_a +op_bc
	
		nom =''
		for i in range(newlen):
			k = tripletlist[i]
			if tripletlist[i] != '000':
				nom += (trp(k)+' ' + suffix[newlen - i -1] + ' ')

		return nom

def namelength(s):
	k = namer(s)
	nomlen = len(k) - k.count(' ')
	return nomlen



import matplotlib.pyplot as plt


#x = range(0,99,3)
#y = []
#for i in x:
#	y.append(namelength(10**i))

z=input('exp')
x=range(0,10**z)

for i in x:
	y.append(namelength(i))


plt.scatter(x,y)
plt.xlabel("logx/log10")
plt.ylabel("length")
plt.show()


#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
