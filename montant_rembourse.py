from dateutil import rrule
import numpy
import datetime
import logging
just = 20
def nb_mensualite_debut_capital(somme_bien,somme_reel,mensualite):
    rembours = 0
    nb_mens = 0
    diff = somme_reel - somme_bien
    while rembours<diff:
        rembours = rembours + mensualite
        nb_mens +=1
    annui = '%1.1f'%(nb_mens/12.)
    print 'il faut ',nb_mens,' mois pour commencer a capitalise soit(',annui,'anuites)' 
    

def calcul_remboursement(somme_totale=150000,taux=3.8,nb_mensualite=20*12):
    nb_mensualite = int(nb_mensualite)
#    print type(nb_mensualite)
    val_mensualite = mensualite(somme_totale,taux,nb_mensualite)
    rembours = val_mensualite*nb_mensualite
    rembours_str = '%1.2f'%(rembours)
    nb_mensualite_debut_capital(somme_bien=somme_totale,somme_reel=rembours,mensualite=val_mensualite)
    pourcent_plus = '%1.2f'%(100.*(1-somme_totale/rembours))
    print 'montant total rembourse='.ljust(just),rembours_str,' soit ',pourcent_plus,'% plus que le montant emprunte'
    return val_mensualite

def mensualite(somme,taux,nb_mensualite):
    nb_mensualite = int(nb_mensualite)
    
    print 'nb_mensualite'.ljust(just),nb_mensualite
    print 'taux'.ljust(just),taux,'%'
    print 'somme'.ljust(just),somme
    taux = taux/100.
    #calcul montant reel
    if taux>0:
        val_mensualite = (somme*taux/12)/(1-numpy.power((1+taux/12),-nb_mensualite))
    else:
        val_mensualite = somme/nb_mensualite
    
#    deb = datetime.datetime(2015,1,1)
#    for dd in rrule.rrule(rrule.MONTHLY,dtstart=deb,count=nb_mensualite):
#        somme = 
#    #calcul
#    restant = somme
#    while restant>0:
#        restant = restant - 
    print 'montant mensualite ='.ljust(just),'%2.2feuros'%val_mensualite
    return val_mensualite

def montant_notaire(somme_bien):
    return 0.075*somme_bien

def multi_emprunt(somme_totale=150000,taux=3.8,nb_mensualite=20*12,ptz=False,un_pourcent_logement=False):
    print 'un_pourcent_logement',un_pourcent_logement
    print 'ptz',ptz
    montant_ptz = 30000
    montant_upl = 30000
    if ptz and un_pourcent_logement==False:
        mens_normal = calcul_remboursement(somme_totale-montant_ptz,taux,nb_mensualite)
        mens_ptz = calcul_remboursement(montant_ptz,0,nb_mensualite)
        print 'total mensualite'.ljust(just),mens_normal,'+',mens_ptz,'=',mens_normal+mens_ptz
    elif ptz==True and un_pourcent_logement==True:
        mens_normal = calcul_remboursement(somme_totale-montant_ptz-montant_upl,taux,nb_mensualite)
        mens_ptz = calcul_remboursement(montant_ptz,0,nb_mensualite)
        mens_upl = calcul_remboursement(montant_upl,1,nb_mensualite)
        print 'total mensualite'.ljust(just),mens_normal,'+',mens_ptz,'+',mens_upl,'=%2.2f'%(mens_normal+mens_ptz+mens_upl),'euros'
    elif ptz==False and un_pourcent_logement==True:
        mens_normal = calcul_remboursement(somme_totale-montant_upl,taux,nb_mensualite)
        mens_upl = calcul_remboursement(montant_upl,1,nb_mensualite)
        print 'total mensualite'.ljust(just),mens_normal,'+',mens_upl,'=%2.2f'%(mens_normal+mens_upl),'euros'
    else:
        mens_normal = calcul_remboursement(somme_totale,taux,nb_mensualite)
    val_notaire = montant_notaire(somme_bien=somme_totale)
    print 'cout notariaux'.ljust(just),val_notaire,'euros'

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-m','--montant',action='store',dest='montant',help='montant du bien acheter',type='float')
    parser.add_option('-n','--nb_annees',action='store',dest='nbann',help='nombre d annuite',type='int')
    parser.add_option('-t','--taux',action='store',dest='tau',help='usure (taux du pret)',type='float')
    parser.add_option('-p','--ptz',action='store_true',dest='ptz',help='pret a taux zero accorde [defaut: pas de PTZ]',default=False)
    parser.add_option('-u','--upl',action='store_true',dest='upl',help='pret 1% logement accorde [defaut: pas de pret accession]',default=False)
    
    (options, args) = parser.parse_args()
#    print options.nbann*12.
#    calcul_remboursement(somme_totale=options.montant,taux=options.tau,nb_mensualite=options.nbann*12.)
    multi_emprunt(somme_totale=options.montant,taux=options.tau,nb_mensualite=options.nbann*12.,ptz=options.ptz,un_pourcent_logement=options.upl)
#    print ',mensualite(somme=100000.,taux=3.5,nb_mensualite=20*12)
#    print 'notaire=',montant_notaire(somme_bien=100000)