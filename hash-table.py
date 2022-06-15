import random as rand
import time
import numpy as np
#sunarthsh pou gia ena alphartithmitiko bgazei enan arithmo ton opoio epeita
#tha kanw modN (opou N to megethos tou pinaka) gia na brw th thesh tou ston pinaka
#einai hash code function 
def poly_accum_hash_code(word):
    z = 33
    code = 0
    for c in word:#gia kathe xarakthra tou string word
        code = z * code + ord(c)#o kwdikos ths lekshs diamorfwnetai (ord(c) einai o kwdikos tou c sto ASCII table)
    return code

#sunarthsh pou briskei ton amesws megalutero prwto arithmo apo ton num
def primeGreaterThan2(num):
    while True:
        if num % 2 == 1:#an o arithmos einai perittos tote exei nohma na psaksoume an einai prwtos
            isPrime = True#ta dedomena pou exoume ews twra de mas apokleioun na einai prwtos arithmos
            for x in range(3, int(num**0.5), 2):#blepoume an uparxei kapoios arithmos apo to 3 ews to (num)^0.5 pou na ton diairei akribws
                if num % x == 0:#an uparxei arithmos pou diairei ton num tote den einai prwtos
                    isPrime = False
                    break
            if isPrime:#ean den brhkame arithmo pou na diairei ton num tote einai prwtos kai epistrefoume thn timh tou
                return num
        num += 1 #ean brhkame arithmo pou na diairei ton num tote den einai prwtos kai sunexizoume thn anazhthsh prwtou arithmou eksetazontas ton epomeno tou
        
#sunarthsh pou ftiaxnei to ID mia kartas
def makeACard(sd):
    positions=[]#mia lista sthn opoia bazw tis theseis pou exoun katalavei ta A,B,C,D gia na mhn katalaboun duo h parapanw thn idia thesh
    for c in "ABCD": #to c pairnei tis times A , B , C , D
        flag=1 #ena flag to opoio otan ginei 0 shmainei oti topothetisame to c epituxws sto string sd
        while (flag!=0):
            position=rand.randint(0,15) #h thesh tou string sthn opoia tha topothethsw to c
            if position not in positions: #ean den exei katalavei thn thesh auth kapoio allo xarakthra tote to c thn katalambanei
                sd = sd[:position] + c + sd[position+1:] #antikathistw ton xarakthra sth thesh auth me ton c
                positions.append(position) #prosthetw ston pinaka pou periexei tis theseis pou topothetisa ta A,B,C,D th thesh tou c
                flag=0
    return sd

#mia klash pou periexei ta stoixeia kathe kartas
class Card:
    def __init__(self,key,poso_plhrwmwn,hmera,lista): 
        self.lista=lista #diathrei poies meres episkefthikame to katasthma
        self.key=key #deixnei to id ths kartas
        self.poso_plhrwmwn=poso_plhrwmwn #deixnei to poso plhrwmwn
        self.hmera=hmera#mera episkepshs
        lista.append(hmera) #prosthetw sth lista hmera poia mera episkepthkame to katasthma
    def add_hmera_poso(self,poso_plhrwmwn,hmera,lista): #an brethei kai deuterh pistwtikh me to idio id tote prosthetw to neo poso plhrwmwn kai thnn hmera episkepshs
        self.lista.append(hmera)
        self.poso_plhrwmwn+=poso_plhrwmwn

#sunarthsh pou otan xreiastei diplasiasmos twn stoixeiwn tou hashtable metaferw ta stoixeia pou exoun apothkeutei sto arxiko hashtable
#kai ta taksinomw basei tou megethous tou neou pinaka
def rehash(arr,N,ful):
    full2=[]#lista pou apothkeuw tis kateilhmmenes theseis tou neou pinaka
    u=primeGreaterThan2(2*N) #to megethos tou pinaka pou einai o megaluteros prwtos arithmos apo ton diplasio tou arxikou megethous tou hashtable
    arr2=[None for i in range(u)]#arxikopoiw to neo hashtable me None
    for i in ful: #gia kathe thesh pou einai kateilhmmenh
        posit=poly_accum_hash_code(arr[i].key)%(u)#briskw to index ston neo hashtable sto opoio tha epanatopothethsw (an einai adeio) to stoixeio tou paliou hashtable
        if(arr2[posit]==None):#ean h thesh einai kenh
            arr2[posit]=arr[i]#topothetw to stoixeio ston neo hashtable
        else:
            flag=0#flag pou mas deixnei an h karta uphrxe hdh sto neo hashtable (flag=1 an uparxei)
            while(arr2[posit]!=None):#oso h thesh den einai kenh sunexizoume na psaxnoume an yparxei hdh auth h karta sto hashtable
                if(arr2[posit].key==arr[i].key): #elegxoume an to id ths trexousas kartas tautizetai me to id kapoias kartas tou pinaka
                    arr2[posit].add_hmera_poso(arr[i].poso_plhrwmwn,arr[i].hmera,arr2[posit].lista)#an einai idio to id prosthetoume th mera episkepshs kai to poso plhrwmhs sthn karta
                    flag=1#h karta uphrxe hdh sto hashtable
                    break
                posit+=1#pername sthn epomenh thesh afou de brethike karta me to idio id
                if (posit>=N):#an h thesh kseperasei to telos tou pinaka tote ksekiname pali apo thn arxh tou hashtable
                    posit=0
            if(flag==0):#ean de brethike karta me to idio id kai ftasame se kenh thesh sto hashtable
                arr2[posit]=arr[i]#prosthetoume to stoixeio sthn kenh thesh tou hashtable
        full2.append(posit)#prosthetw sth lista full2 th thesh tou pinaka pou katalhfthike
    return arr2,u,full2

#sunarthsh pou briskei thn karta me th megaluterh episkepsimothta kai ton arithmo twn episkepsewn sthn karta auth
#epipleon briskei th mera me th mikroterh episkepsimoththa kai
#briskei thn karta me to mikrotero poso plhrwmwn kathws kai poio htan auto
def statistics(arr,ful):
    maximum=len(arr[ful[0]].lista) #orizw san karta me ths perissoteres episkepseis ayth pou brisketai sthn thesh pou deixnei to prwto stoixeio ths listas ful
    keep_maximum=arr[ful[0]].key
    minimum_pay=arr[ful[0]].poso_plhrwmwn #orizw san karta me to mikrotero poso plhrwmwn ayth pou brisketai sthn thesh pou deixnei to prwto stoixeio ths listas ful
    keep_minimum_pay=arr[ful[0]].key
    days=[0 for i in range(6)] #orizw th lista days sthn opoia tha shmeiwnw poses fores episkefthkame to katasthma gia kathe mera gia na brw auth me tis elaxistes episkepseis
    for i in ful:#gia kathe kateillhmeno stoixeio tou hashtable
        if(len(arr[i].lista)>maximum):#elegxw an uparxei karta me perissoteres episkepseis sto katasthma
            maximum=len(arr[i].lista)#an uparxei allazw to maximum
            keep_maximum=arr[i].key # kai apothkeuw to id ths kartas auths
        if(arr[i].poso_plhrwmwn <minimum_pay):#elegxw an uparxei karta me mikrotero poso plhrwmwn sto katasthma
            minimum_pay=arr[i].poso_plhrwmwn#an uparxei allazw to minimum pay
            keep_minimum_pay=arr[i].key# kai apothkeuw to id ths kartas auths
        for j in range(6):#blepw gia kathe karta poies meres episkeptike to katasthma
            days[j]+=(arr[i].lista).count(j)
    return maximum,keep_maximum,minimum_pay, keep_minimum_pay, days.index(min(days))

standard_digits="1358264718362718" #ta arxika stathera pshfia
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"] #oi meres pou ginontai episkepseis sta katasthmata
rand.seed(1066581)#thetw san seed ton AM mou
episkepseis=10 #o arithmos twn episkepsewn
N=primeGreaterThan2(2) #orizw san arxiko megethos tou hashtable ton amesws megalutero prwto arithmo apo to 1000
load_factor=0.6 #orizw ton load factor
sugkrouseis=0 #se auth th metablhth apothkeuw poses sugkrouseis exoun ginei
num_of_cards=0 #metraei ton arithmo twn kartwn pou exoun topothetithei sto hashtable
full=[]#apothkeuw sth lista full ths kateilhmenes theseis tou hashtable
arr = [None for i in range(N)] #arxikopoiw to hashtable me None
t0=time.time() #metraw to xrono dhmiourgias tou hashtable
for i in range(episkepseis):#to i deixnei ton arithmo ths episkepshs pou pragmatopoieitai
    if((num_of_cards/N)<load_factor): #elegxo an exoume kseperasei to load factor
        poso=rand.randint(20,100)#to poso plhrwmwn einai enas tuxaios arithmos apo to 20 ews to 100
        mera=rand.randint(0,5)#h mera episkepshs einai mia tyxaia apo to 0-deutera ews 5-sabbato
        k=Card(makeACard(standard_digits),poso,mera,[])#dhmiourgw mia karta k
        posit=poly_accum_hash_code(k.key)%N#briskw to index sto hashtable sto opoio tha topothethsw (an einai adeio) thn karta
        if(arr[posit]==None):#ean h thesh einai kenh
            arr[posit]=k#topothetw to stoixeio ston hashtable
            num_of_cards+=1#auksanw ton arithmo twn kartwn pou exoun apothikeusei ta stoixeia tous sto hashtable
        else:
            flag=0 #flag pou mas deixnei an h karta uphrxe hdh sto neo hashtable (flag=1 an uparxei)
            help1=0 #deixnei an xreiasthke na gurisoume sthn arxh tou pinaka gia na apothkeusoyme h na broume mia karta otan ginetai 1
            helping=posit #bohthikh metavlhth gia na upologizw tis sugkrouseis
            while(arr[posit]!=None):#oso h thesh den einai kenh sunexizoume na psaxnoume an yparxei hdh auth h karta sto hashtable
                if(arr[posit].key==k.key):#elegxoume an to id ths trexousas kartas tautizetai me to id kapoias kartas tou pinaka
                    arr[posit].add_hmera_poso(poso,mera,arr[posit].lista)#an einai idio to id prosthetoume th mera episkepshs kai to poso plhrwmhs sthn karta
                    flag=1#h karta uphrxe hdh sto hashtable
                    break
                print("collision!")
                posit+=1#pername sthn epomenh thesh afou de brethike karta me to idio id
                if (posit>=N):#an h thesh kseperasei to telos tou pinaka tote ksekiname pali apo thn arxh tou hashtable
                    posit=0
                    help1=1
            if(flag==0):#ean de brethike karta me to idio id kai ftasame se kenh thesh sto hashtable
                if (help1==0):
                    sugkrouseis+=(posit-helping)#upologizw tis sugkrouseis pou eginan an de gurisame sthn arxh tou hashtable
                else:
                    sugkrouseis+=(N-helping+posit)#upologizw tis sugkrouseis pou eginan an gurisame sthn arxh tou hashtable
                num_of_cards+=1#auksanw ton arithmo twn kartwn pou exoun apothikeusei ta stoixeia tous sto hashtable
                arr[posit]=k#prosthetoume to stoixeio sthn kenh thesh tou hashtable
        print(f'Hash Table:')
        for j in range(len(arr)):
            if(arr[j]!=None):
                print(f'ID: {arr[j].key}, payment= {arr[j].poso_plhrwmwn}, days of visit {days[arr[j].hmera]}')
            else:
                print(None)
        print()
        full.append(posit)#prosthetw sth lista full th thesh tou pinaka pou katalhfthike
    else:
        [arr,N,full]=rehash(arr,N,full)#an kseperasthke o load factor prepei na diplasiasw to hashtable
        i-=1#meiwnw to i gia na mhn paralhfthei mia episkepsh
        print(f'Hash Table after rehashing:')
        for j in range(len(arr)):
            if(arr[j]!=None):
                print(arr[j].key)
            else:
                print(None)
        print()

#tupwnw osa zhthmata eixame gia thn ergasia parakatw
print(f'The time it takes for the hash table to be made with {episkepseis} visits is:{time.time()-t0:.2f}sec')
[number_of_max_visits,max_visits_card,number_of_minimum_pay,card_minimum_pay, day] =statistics(arr,full)
print(f'The card with the most visits has an ID: {max_visits_card} and the number of maximum visits is: {number_of_max_visits}')
print(f'The card with the least payments has an ID: {card_minimum_pay} and the amount of payments is: {number_of_minimum_pay}')
print(f'The day with the least visits is {days[day]}')
print(f'The number of total collisions is {sugkrouseis} with a load factor: {load_factor}')
