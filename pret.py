'''antoine grouazel 2014'''
import numpy
import matplotlib.pyplot as plt
import matplotlib
import logging
class comparatif():
	def showBars(self,coutA,coutB):
		f=plt.figure()
		f.hold()
		for oo in range(4):
			plt.subplot(3,1,oo)
			print coutA.shape
			
			plt.bar(range(len(coutA)),coutA[oo],1,0,'r')
			plt.bar(range(len(coutA)),coutB[oo],1,0,'b')
		plt.show()
#		f.subplot(3,1,2)
#		plt.bar(range(self.nb_mensualite[0]),coutA[0],'r')
#		plt.bar(range(self.nb_mensualite[0]),coutB[0],'r')
#		f.subplot(3,1,3)
#		plt.bar(range(self.nb_mensualite[0]),coutA[0],'r')
#		plt.bar(range(self.nb_mensualite[0]),coutB[0],'r')
		
		
class pret():
	def __init__(self,teg,montant=100000,frais_dossier=900):
		
		self.TEG=teg
		self.frais_dossier=frais_dossier
		self.montant=montant
#		self.nb_mensualite=[120, 160, 180]
		self.nb_mensualite=[120]
		self.assurance=self.nb_mensualite*14
		self.mensualite=650
#		cout=0.0
		return

	def displayInfos(self):
		cout=numpy.zeros((len(self.nb_mensualite),180))
		rembourse=numpy.zeros((len(self.nb_mensualite),180))
		for men in range(len(self.nb_mensualite)):
			for ii in range(self.nb_mensualite[men]):
				rembourse[men,ii]=rembourse[men,ii] + self.mensualite
				restant=self.montant - rembourse[men,ii]
#				print restant
				cout[men,ii]=cout[men,ii]+self.TEG*restant
				print 'restant %s remoubse %s cout %s',restant,rembourse[men],cout[men]
#		total_cout = cout[-1]
		return cout,rembourse,restant
		
if __name__ == '__main__':
	
	test1 = pret(teg=4.23)
	coutA,r,res = test1.displayInfos()
	testB1 = pret(teg=4.21,montant=50000)
	testB2 = pret(teg=4.21,montant=50000)
	coutB2,r,res = testB2.displayInfos()
	coutB1,r,res = testB1.displayInfos()
	coutB = coutB2 + coutB1
	essai = comparatif()
	essai.showBars(coutA,coutB)