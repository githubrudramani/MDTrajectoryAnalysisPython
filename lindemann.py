import numpy as np  # you probably don't need this line
from glob import glob
print("Lets together calculate the Lindemann Index")
fnames = glob('/Users/rudramani/work/Python-Programing-Udemy/test*.dat')
z = [np.loadtxt(g) for g in fnames]
#print(z)
#print(len(z))
print("loading every files completed, now slice the file for every 50 frames")
out_file = open("lindemann7.7.dat", "a")
s = 0
for t in range(100): # for 3 delta values , for every total-data/3 group
	f = []
	for p in range(s, s + 40): # for every two files
		f.append(z[p])
	print("Files has been sliced!")
	#print(f)
	#print(f[0])
	#print(len(f[0]))
	#print(len(f[0][0]))
	N = len(f[0]) # no of atoms
	#print(N)  # no of atoms
	N_corretion =  N *(N-1)/2
	#print(N_corretion)


	i = 0
	j = 0
	rij = 0
	a = []
	for k in range(0,len(f)):
		for i  in range(0, len(f[0])):
			for j in range(i+1,len(f[0])):
				rij = (np.subtract(f[k][i],f[k][j]))
				#kij = (np.subtract(f[1][i],f[1][j]))
				#mij = (np.subtract(f[2][i],f[2][j]))

				#print(rij)

			#print(mij)
				a.append(np.linalg.norm(rij))
				#b.append(np.linalg.norm(kij))
				#c.append(np.linalg.norm(mij))
			
	#print(a)
	B = np.reshape(a, (-1, int(N_corretion)))  # # ie r0,1 ; r0,2 ;...r0,1999 ;r1,2 ;r1,3...............; r1998,1999 
	#print(B)                                      # for each frame or data, each row of this matix is intedistance  
	#print(len(B))								# of  each frame and number of column goes to each frame/ each data set							

	

	#print(len(B[0]))
	#print(len(B[0])
		
	#print(len(B[0]))
	#print(b)
	#print(c)
	#r = np.matrix([a, b, c])
	#print(r)
	#print(B[0][0])
	#print(B[1][0])
	#print(B[2][0])
	#def mean(numbers):
	   # return float(sum(numbers)) / max(len(numbers), 1)
	# mean([numbers])
	#print(B[:,0:1]) # every row and first column
	#print(np.sum(B,axis=0))
	sum_rij = np.sum(B,axis=0)   # sum of each column of matrix B
	#print(sum_rij)
	avg_rij = sum_rij/float(len(B)) # average of each column of matrix B, len(B) is no of files or frame, or no of rows of B
	#print(avg_rij)
	Rij_avg = avg_rij

	#print("just chill")
	rij_square = np.square(B)
	#print(rij_square)
	sum_rij_square = np.sum(rij_square, axis=0)
	#print(sum_rij_square)
	avg_sum_rij_square = sum_rij_square/float(len(B))
	#print(avg_sum_rij_square)
	Rij2_avg = avg_sum_rij_square
	print("Just have calculated the distance mean and distance square mean! ")

	#print(Rij_avg)
	#print(Rij2_avg)
	madhu = 0

	for q in range(0, len(B[0])):  # len(B[0] is no of columns
		delta_i = np.sqrt(Rij2_avg[q] - Rij_avg[q] * Rij_avg[q])/float(Rij_avg[q])
		#print(delta_i)
		madhu = madhu + delta_i
	#print(madhu)
	final_delta = madhu/N_corretion
	print("lindemann for this round is :")
	print(final_delta)
	#print(final_delta, file = out_file ) # this is for python 3
	print >>out_file, final_delta # this is for python2
	print("  NEXT ROUND, KEEP PATIENT!")
	
	s = s + 40
print("At last you are done!")
print("Your final file is lindemann*.dat.")
out_file.close()
	
