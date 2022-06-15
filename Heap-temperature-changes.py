import time
import random

class MinHeap():
    def __init__(self, arr):
        self.array=[] #to array tha periexei tuples ths morfhs ('x,y' , thermokrasia)
        self.pos={} #leksiko pou deixnei th thesh tou kleidiou sto array (p.x. '2,199':50 opou to '2,199' einai to kleidi kai 50 h thesh tou)
        self.size=len(arr) #size einai o arithmos twn stoixeiwn pou periexei o minimum Heap
        for i, item in enumerate(arr): #to i deixnei to index tou stoixeiou ston arr kai to item einai to periexomeno tou arr sto antistoixo index
            self.array.append((item[0], item[1])) #prosthetw sto array tuple ths morfhs ('x,y' , thermokrasia)
            self.pos[item[0]]=i #prosthetoume sto leksiko to kleidi 'x,y' me timh i pou deixnei th thesh tou ston min Heap
        for i in range(self.size//2,-1,-1): #apo th mesh peripou tou min Heap kai pros ta panw kalw thn heapify gia na dw an isxuei h idiothta tou heap
            #kai an den isxuei na anadiataksw kapoia stoixeia tou
            self.heapify(i)
            
    #sunarthsh pou deixnei ta stoixeia tou heap se morfh (x,y) : thermokrasia
    def display(self):
        print('MinHeap=')
        for i in range(self.size): #gia kathe stoixeio tou heap 
            print(f'({self.array[i][0]} : {self.array[i][1]})', end=' ')
        print()
            
    #sunarthsh pou epistrefei True an to heap einai adeio, alliws False
    def isEmpty(self):
        return self.size == 0 #an to megethos tou heap einai mhden den periexei stoixeia
    
    #heapify einai mia sunarthsh h opoia pairnei san orisma to index tou node pou thelw na kanw heapify
    #wste telika na isxuei h idiothta tou heap meta to heapify
    def heapify(self, i):
        smallest = i #to index tou patera
        le = 2 * i + 1 #to index tou aristerou paidiou
        ri = 2 * i + 2 #to index tou deksiou paidiou
        if le < self.size and self.array[le][1] < self.array[smallest][1]:
            #an to index tou aristerou paidiou uparxei ston heap kai h thermokrasia tou aristerou paidiou
            #einai mikroterh apo th thermokrasia tou patera prepei na ginei pateras to aristero paidi  
            smallest = le
        if ri < self.size and self.array[ri][1] < self.array[smallest][1]:
            #an to index tou deksiou paidiou uparxei ston heap kai h thermokrasia tou deksiou paidiou
            #einai mikroterh apo th thermokrasia tou patera prepei na ginei pateras to deksi paidi 
            smallest = ri
        if smallest != i: #an o pateras antalakse thesh me kapoio apo ta paidia tou pou eixe mikroterh thermokrasia
            self.pos[self.array[smallest][0]],self.pos[self.array[i][0]] = i,smallest #kanw swap tis suntetagmenes tou patera me tou paidiou sto leksiko pos pou
            #diathrei tis theseis ston min Heap twn 'x,y'
            self.array[smallest],self.array[i]=self.array[i],self.array[smallest]#kanw swap ta tuples ston pinaka array
            self.heapify(smallest)#kalw thn heapify gia na dw an diathreitai h idiothta tou heap sto paidi pou phre th thesh tou patera kai na ginoun
            #oi aparaithtes allages gia na diathreitai
            
    #h synarthsh getMin epistrefei th riza tou heap pou exei th mikroterh thermokrasia h None an einai adeios
    def getMin(self):
        if self.size == 0:
            return None
        return self.array[0]
    
    #h sunarthsh extractMin epistrefei to tuple ('x,y' , thermokrasia) tou shmeiou me th mikroterh thermokrasia pou brisketai sth riza tou heap kai to afairei apo ton heap
    def extractMin(self):
        if self.size == 0: #an o heap einai adeios epistrefei None
            return None
        root = self.array[0] #root einai to tuple ('x,y' , thermokrasia) pou brisketai sth riza tou heap
        lastNode = self.array[self.size - 1] #lastNode einai to tuple('x,y' , thermokrasia) pou brisketai sto telos tou heap
        self.array[0] = lastNode #bazoume to tuple ('x,y' , thermokrasia) tou teleutaiou stoixeiou tou heap sto tuple ('x,y' , thermokrasia) pou brisketai sth riza tou
        self.pos[lastNode[0]] = 0 #allazoume to index tou teleutaiou stoixeiou tou heap sto leksiko pos se 0 dioti to phgame sth riza tou heap
        del self.pos[root[0]] #diagrafoume apo to leksiko to stoixeio pou briskotan prin sth riza 
        self.size -= 1 #meiwnw kata 1 to megethos tou heap afou to afairesa apo ekei
        self.heapify(0)#kalw thn heapify gia na dw an diathreitai h idiothta tou heap sth riza kai na ginoun oi aparaithtes allages gia na diathreitai
        return root
    
    #h sunarthsh insert prosthetei ena neo stoixeio ston heap
    def insert(self, item):
        if self.size < len(self.array): #an to array exei kapoies theseis eleftheres
            self.array[self.size] = (item[0], 10**80) #prosthetw sto array tis suntetagmenes tou stoixeiou kai tou dinw kleidi me polu megalh timh gia na einai sto telos tou heap
        else: #an den uparxei xwros sto array
            self.array.append((item[0], 10**80))#prosthetw sto telos tou array tis suntetagmenes tou stoixeiou kai tou dinw kleidi me polu megalh timh gia na einai sto telos tou heap
        self.pos[item[0]] = self.size #prosthetw sto leksiko pos tis suntetagmenes tou item
        self.size += 1 #auksanw kata 1 to megethos tou heap
        self.decreaseKey(item) #orizw thn katallhlh thermokrasia gia tis suntetagmenes tou item kai to bazw sthn katallhlh thesh ston heap
            
    #me th sunarthsh decreaseKey allazw thn thermokrasia enos item se mikroterh kai prosarmozw th thesh tou ston heap
    def decreaseKey(self, item):
        i=self.pos[item[0]] #i einai h thesh ston heap tou item
        val=item[1] #val einai h timh ths thermokrasias tou item
        if self.array[i][1] <= val:#h nea timh ths thermokrasias tou stoixeiou prepei na einai mikroterh apo thn prohgoumenh
            return
        self.array[i] = item #allazw th thermokrasia tou stoixeiou se mikroterh ston pinaka arr (oi suntetagmenes einai idies)
        p=(i - 1)//2 #p einai h thesh tou parent tou stoixeiou sth thesh i
        while i > 0 and self.array[i][1] < self.array[p][1]: #oso den eimai sth riza elegxw kai h timh ths thermokrasias ston parent einai
            #megaluterh apo auth sth thesh i
            self.pos[self.array[i][0]],self.pos[self.array[p][0]] = p,i #kanw swap ta index tou patera me tou paidiou sto leksiko pos
            self.array[p], self.array[i] = self.array[i], self.array[p] #kanw swap ta stoixeia tou patera me tou giou sto array
            i=p #to i pairnei thn timh tou index tou patera
            p=(i-1)//2 #to p pairnei thn timh tou index tou patera tou prwhn patera
            
    #me th sunarthsh increaseKey allazw thn thermokrasia enos item se megaluterh kai prosarmozw th thesh tou ston heap
    def increaseKey(self, item):
        i=self.pos[item[0]] #i einai h thesh ston heap tou item
        val=item[1] #val einai h timh ths thermokrasias tou item
        if self.array[i][1] >= val: #h nea timh ths thermokrasias tou stoixeiou prepei na einai megaluterh apo thn prohgoumenh
            return
        self.array[i] = item #allazw th thermokrasia tou stoixeiou se megaluterh ston pinaka arr (oi suntetagmenes einai idies)
        self.heapify(i) #kalw thn heapify gia na dw an diathreitai h idiothta tou heap sta paidia kai na ginoun oi aparaithtes allages gia na diathreitai
        
    #h sunarthsh isInMinHeap epistrefei duo times, sthn prwth periptwsh pou briskw to stoixeio ston heap h prwth timh poy epistrefetai deixnei thn timh ths thermokrasias
    #pou eixe to stoixeio kai h deuterh timh pou epistrefetai einai 1 (True) enw an den to brw epistrefw -100 sth thermokrasia dioti den uphrxe kai 0 (False) 
    def isInMinHeap(self, v):
        if(v in self.pos): #ean uparxei stoixeio sto leksiko pos me autes tis suntetagmenes
            u=self.array[self.pos.get(v)] #to u einai ena tuple pou periexei tis suntetagmenes pou epsaxna sto leksiko kai thn thermokrasia sthn opoia antistoixousan
            return u[1],1
        return -100,0
    
    #h sunarthsh deleteKey diagrafei ena stoixeio tou heap
    def deleteKey(self, item):
        self.decreaseKey((item[0], -1e100)) #dinw sto stoixeio pou thelw na afairesw polu mikrh thermokrasia gia na paei sth riza tou heap kai na to afairesw eukola meta
        self.extractMin() #afairw to stoixeio me th mikroterh thermokrasia


class MaxHeap():
    def __init__(self, arr):
        self.array = [] #to array tha periexei tuples ths morfhs ('x,y' , thermokrasia)
        self.pos = {} #leksiko pou deixnei th thesh tou kleidiou sto array (p.x. ('2,199',50) opou to '2,199' einai to kleidi kai 50 h thesh tou)
        self.size = len(arr) #size einai o arithmos twn stoixeiwn pou periexei o maximum Heap
        for i, item in enumerate(arr): #to i deixnei to index tou stoixeiou ston arr kai to item einai to periexomeno tou arr sto antistoixo index
            self.array.append((item[0], item[1])) #prosthetw sto array tuple ths morfhs ('x,y' , thermokrasia)
            self.pos[item[0]]=i #prosthetoume sto leksiko to kleidi 'x,y' me timh i pou deixnei th thesh tou ston max Heap
        for i in range(self.size//2,-1,-1): #apo th mesh peripou tou max Heap kai pros ta panw kalw thn heapify gia na dw an isxuei h idiothta tou heap
            #kai an den isxuei na anadiataksw kapoia stoixeia tou
            self.heapify(i)
            
    #sunarthsh pou deixnei ta stoixeia tou heap se morfh (x,y) : thermokrasia
    def display(self):
        print('MaxHeap =')
        for i in range(self.size): #gia kathe stoixeio tou heap 
            print(f'({self.array[i][0]} : {self.array[i][1]})', end=' ')
        print()
            
    #sunarthsh pou epistrefei True an to heap einai adeio, alliws False
    def isEmpty(self):
        return self.size == 0 #an to megethos tou heap einai mhden den periexei stoixeia
    
    #heapify einai mia sunarthsh h opoia pairnei san orisma to index tou node pou thelw na kanw heapify
    #wste telika na isxuei h idiothta tou heap meta to heapify
    def heapify(self, i):
        largest = i #to index tou patera
        le = 2 * i + 1 #to index tou aristerou paidiou
        ri = 2 * i + 2 #to index tou deksiou paidiou
        if le < self.size and self.array[le][1] > self.array[largest][1]:
            #an to index tou aristerou paidiou uparxei ston heap kai h thermokrasia tou aristerou paidiou
            #einai megaluterh apo th thermokrasia tou patera prepei na ginei pateras to aristero paidi  
            largest = le
        if ri < self.size and self.array[ri][1] > self.array[largest][1]:
            #an to index tou deksiou paidiou uparxei ston heap kai h thermokrasia tou deksiou paidiou
            #einai megaluterh apo th thermokrasia tou patera prepei na ginei pateras to deksi paidi 
            largest = ri
        if largest != i: #an o pateras antalakse thesh me kapoio apo ta paidia tou pou eixe megaluterh thermokrasia
            self.pos[self.array[largest][0]],self.pos[self.array[i][0]] = i,largest #kanw swap tis suntetagmenes tou patera me tou paidiou sto leksiko pos pou
            #diathrei tis theseis ston max Heap twn 'x,y'
            self.array[largest],self.array[i]=self.array[i],self.array[largest]#kanw swap ta tuples ston pinaka array
            self.heapify(largest)#kalw thn heapify gia na dw an diathreitai h idiothta tou heap sto paidi pou phre th thesh tou patera kai na ginoun
            #oi aparaithtes allages gia na diathreitai
            
    #h synarthsh getMax epistrefei th riza tou heap pou exei th megaluterh thermokrasia h None an einai adeios
    def getMax(self):
        if self.size == 0:
            return None
        return self.array[0]
    
    #h sunarthsh extractMax epistrefei to tuple ('x,y' , thermokrasia) tou shmeiou me th megaluterh thermokrasia pou brisketai sth riza tou heap kai to afairei apo ton heap
    def extractMax(self):
        if self.size == 0: #an o heap einai adeios epistrefei None
            return None
        root = self.array[0] #root einai to tuple ('x,y' , thermokrasia) pou brisketai sth riza tou heap
        lastNode = self.array[self.size - 1] #lastNode einai to tuple('x,y' , thermokrasia) pou brisketai sto telos tou heap
        self.array[0] = lastNode #bazoume to tuple ('x,y' , thermokrasia) tou teleutaiou stoixeiou tou heap sto tuple ('x,y' , thermokrasia) pou brisketai sth riza tou
        self.pos[lastNode[0]] = 0 #allazoume to index tou teleutaiou stoixeiou tou heap sto leksiko pos se 0 dioti to phgame sth riza tou heap
        del self.pos[root[0]] #diagrafoume apo to leksiko to stoixeio pou briskotan prin sth riza 
        self.size -= 1 #meiwnw kata 1 to megethos tou heap afou to afairesa apo ekei
        self.heapify(0)#kalw thn heapify gia na dw an diathreitai h idiothta tou heap sth riza kai na ginoun oi aparaithtes allages gia na diathreitai
        return root
    
    #h sunarthsh insert prosthetei ena neo stoixeio ston heap
    def insert(self, item):
        if self.size < len(self.array): #an to array exei kapoies theseis eleftheres
            self.array[self.size] = (item[0], -1e100) #prosthetw sto array tis suntetagmenes tou stoixeiou kai tou dinw kleidi me polu mikrh timh gia na einai sto telos tou heap
        else: #an den uparxei xwros sto array
            self.array.append((item[0], -1e100))#prosthetw sto telos tou array tis suntetagmenes tou stoixeiou kai tou dinw kleidi me polu mikrh timh gia na einai sto telos tou heap
        self.pos[item[0]] = self.size #prosthetw sto leksiko pos tis suntetagmenes tou item
        self.size += 1 #auksanw kata 1 to megethos tou heap
        self.increaseKey(item) #orizw thn katallhlh thermokrasia gia tis suntetagmenes tou item kai to bazw sthn katallhlh thesh ston heap
            
    #me th sunarthsh increaseKey allazw thn thermokrasia enos item se megaluterh kai prosarmozw th thesh tou ston heap
    def increaseKey(self, item):
        i=self.pos[item[0]] #i einai h thesh ston heap tou item
        val=item[1] #val einai h timh ths thermokrasias tou item
        if self.array[i][1] >= val:#h nea timh ths thermokrasias tou stoixeiou prepei na einai megaluterh apo thn prohgoumenh
            return
        self.array[i] = item #allazw th thermokrasia tou stoixeiou se megaluterh ston pinaka arr (oi suntetagmenes einai idies)
        p=(i - 1)//2 #p einai h thesh tou parent tou stoixeiou sth thesh i
        while i > 0 and self.array[i][1] > self.array[p][1]: #oso den eimai sth riza elegxw an h timh ths thermokrasias ston parent einai
            #mikroterh apo auth sth thesh i
            self.pos[self.array[i][0]],self.pos[self.array[p][0]] = p,i #kanw swap ta index tou patera me tou paidiou sto leksiko pos
            self.array[p], self.array[i] = self.array[i], self.array[p] #kanw swap ta stoixeia tou patera me tou giou sto array
            i=p #to i pairnei thn timh tou index tou patera
            p=(i-1)//2 #to p pairnei thn timh tou index tou patera tou prwhn patera
            
    #me th sunarthsh decreaseKey allazw thn thermokrasia enos item se mikroterh kai prosarmozw th thesh tou ston heap
    def decreaseKey(self, item):
        i=self.pos[item[0]] #i einai h thesh ston heap tou item
        val=item[1] #val einai h timh ths thermokrasias tou item
        if self.array[i][1] <= val: #h nea timh ths thermokrasias tou stoixeiou prepei na einai mikroterh apo thn prohgoumenh
            return
        self.array[i] = item #allazw th thermokrasia tou stoixeiou se mikroterh ston pinaka arr (oi suntetagmenes einai idies)
        self.heapify(i) #kalw thn heapify gia na dw an diathreitai h idiothta tou heap sta paidia kai na ginoun oi aparaithtes allages gia na diathreitai
        
    #h sunarthsh isInMaxHeap epistrefei duo times, sthn prwth periptwsh pou briskw to stoixeio ston heap h prwth timh poy epistrefetai deixnei thn timh ths thermokrasias
    #pou eixe to stoixeio kai h deuterh timh pou epistrefetai einai 1 (True) enw an den to brw epistrefw -100 sth thermokrasia dioti den uphrxe kai 0 (False) 
    def isInMaxHeap(self, v):
        if(v in self.pos): #ean uparxei stoixeio sto leksiko pos me autes tis suntetagmenes
            u=self.array[self.pos.get(v)] #to u einai ena tuple pou periexei tis suntetagmenes pou epsaxna sto leksiko kai thn thermokrasia sthn opoia antistoixousan
            return u[1],1
        return -100,0
    
    #h sunarthsh deleteKey diagrafei ena stoixeio tou heao
    def deleteKey(self, item):
        self.increaseKey((item[0], 10**80)) #dinw sto stoixeio pou thelw na afairesw polu megalh thermokrasia gia na paei sth riza tou heap kai na to afairesw eukola meta
        self.extractMax() #afairw to stoixeio me th megaluterh thermokrasia        

#h sunarthsh seeIfItExists epistrefei, an uparxei to stoixeio hdh, thn palia thermokrasia tou kai 1(brethike) alliws -100 kai 0 (de brethike) epipleon an to brhkame ston minHeap
#epistrefei 1 enw an to brhkame ston maxHeap epistrefei 2 kai an  den to brhkame pouthena epistrefei 3
def seeIfItExists(temp,coord,median,h1,h2,flag):
    u1=h1.isInMinHeap(coord)
    u2=h2.isInMaxHeap(coord)
    if(u1[1]==1):
        return u1,1
    elif(u2[1]==1):
        return u2,2
    else:
        return (0,0),3

#h sunarthsh actions diakrinei 2 periptwseis stis opoies elegxoume an prepei na aykhsoume h na meiwsoume thn timh tou stoixeiou
def actions(temp,h,coord,old_temp):
    if(old_temp>temp):
        h.decreaseKey((coord,temp))
    elif(old_temp<temp):
        h.increaseKey((coord,temp))
        
#h sunarthsh decisions topothetei to neo tuple ('x,y', thermokrasia) son katallhlo heap ektos an uparxei hdh to shmeio 'x,y' se kapoio heap
#pou se auth thn periptwsh tropopoiei th thermokrasia tou, epipleon upologizei thn timh tou median
def decisions(h1,h2,coord,temp,median):
    len1=h1.size #len1 einai to megethos tou minHeap h1
    len2=h2.size #len2 einai to megethos tou maxHeap h2
    if(len1>len2):#ean o minHeap h1 exei perissotera stoixeia apo ton maxHeap h2
        if(temp>=h1.getMin()[1]): #elegxw an to stoixeio pou irthe molis exei thermokrasia h opoia tha to topothetouse ston minHeap h1
            [(old_temp,isIt),flag]=seeIfItExists(temp,coord,median,h1,h2,(1,1)) #elegxw an uparxei hdh stoixeio me tis idies suntetagmes ston minHeap h1
            if(flag==1): #an uparxei hdh stoixeio me idies suntetagmenes tote tha kalesw th sunarthsh actions gia na tou tropopoihsw th thermokrasia tou
                actions(temp,h1,coord,old_temp)
            if(flag==3): #an den uparxei hdh stoixeio me idies suntetagmenes tote tha metaferw to mikrotero stoixeio tou minHeap h1 ston maxHeap h2 (afou irthe neo
                         #stoixeio megalutero h iso apo auto)
                h2.insert(h1.extractMin())
                h1.insert((coord,temp))
        else:#to stoixeio pou irthe molis exei thermokrasia h opoia einai mikroterh tou min stoixeiou tou minHeap h1
            [(old_temp,isIt),flag]=seeIfItExists(temp,coord,median,h1,h2,(2,2)) #elegxw an uparxei hdh stoixeio me tis idies suntetagmes ston maxHeap h2
            if(flag==2): #an uparxei hdh stoixeio me idies suntetagmenes tote tha kalesw th sunarthsh actions gia na tou tropopoihsw th thermokrasia
                actions(temp,h2,coord,old_temp)
            if(flag==3): #an den uparxei hdh stoixeio me idies suntetagmenes tote tha to prosthesw ston maxHeap h2
                h2.insert((coord,temp))
    elif(len1<len2): #ean o minHeap h1 exei ligotera stoixeia apo ton maxHeap h2
        if(temp<=h2.getMax()[1]): #elegxw an to stoixeio pou irthe molis exei thermokrasia h opoia tha to topothetouse ston maxHeap h2
            [(old_temp,isIt),flag]=seeIfItExists(temp,coord,median,h1,h2,(2,2)) #elegxw an uparxei hdh stoixeio me tis idies suntetagmes ston maxHeap h2
            if(flag==2): #an uparxei hdh stoixeio me idies suntetagmenes tote tha kalesw th sunarthsh actions gia na tou tropopoihsw th thermokrasia tou
                actions(temp,h2,coord,old_temp)
            if(flag==3): #an den uparxei hdh stoixeio me idies suntetagmenes tote tha metaferw to megalutero stoixeio tou maxHeap h2 ston minHeap h1 (afou irthe neo
                         #stoixeio mikrotero h iso apo auto)
                h1.insert(h2.extractMax())
                h2.insert((coord,temp))
        else:#to stoixeio pou irthe molis exei thermokrasia h opoia einai megaluterh tou max stoixeiou tou maxHeap h2
            [(old_temp,isIt),flag]=seeIfItExists(temp,coord,median,h1,h2,(1,1)) #elegxw an uparxei hdh stoixeio me tis idies suntetagmes ston minHeap h1
            if(flag==1):#an uparxei hdh stoixeio me idies suntetagmenes tote tha kalesw th sunarthsh actions gia na tou tropopoihsw th thermokrasia tou
                actions(temp,h1,coord,old_temp)
            if(flag==3):#an den uparxei hdh stoixeio me idies suntetagmenes tote tha to prosthesw ston minHeap h1
                h1.insert((coord,temp))
    else:#ean o minHeap h1 exei iso arithmo stoixeiwn me ton maxHeap h2
        [(old_temp,isIt),flag]=seeIfItExists(temp,coord,median,h1,h2,(1,2)) #elegxw an uparxei hdh stoixeio me tis idies suntetagmes ston minHeap h1 h ston maxHeap h2
        if (flag==1): #an uparxei hdh stoixeio me idies suntetagmenes ston minHeap h1 tote tha kalesw th sunarthsh actions gia na tou tropopoihsw th thermokrasia tou
            actions(temp,h1,coord,old_temp)
        elif(flag==2): #an uparxei hdh stoixeio me idies suntetagmenes ston maxHeap h2 tote tha kalesw th sunarthsh actions gia na tou tropopoihsw th thermokrasia tou
            actions(temp,h2,coord,old_temp)
        elif(flag==3):#an den uparxei hdh stoixeio me idies suntetagmenes tote tha to prosthesw ston minHeap h1 an h thermokrasia tou einai megaluterh tou median alliws ston maxHeap h2
            if(temp>=median[1]):
                h1.insert((coord,temp))
            elif(temp<median[1]):
                h2.insert((coord,temp))
    if(flag==1 or flag==2): #an egine allagh thermokrasias se kapoio stoixeio eite tou minHeap eite tou maxHeap
        if(h1.getMin()[1]<h2.getMax()[1]): #elegxw an prepei na ginei antallagh stoixeiwn metaksu tou minHeap kai tou maxHeap se periptwsh pou h allagh ths thermokrasias odhghse ena stoixeio
            #tou minHeap gia paradeigma na ginei mikrotero apo to megisto tou maxHeap eite to antitheto
            h2.insert(h1.extractMin())
            h1.insert(h2.extractMax())
    u=h1.size+h2.size #me to u tha ksexwrisw tis periptwseis tou an exw artio h peritto arithmo stoixeiwn sunolika gia na upologisw swsta ton median
    if(u%2==0): #an to u einai artio
        median=(h1.getMin()[0] +'\' and \'' + h2.getMax()[0],round((h1.getMin()[1]+h2.getMax()[1])/2,2)) #o median upologizetai san o mesos oros tou minimum stoixeiou tou minHeap h1
        #kai tou maximum stoixeiou tou maxHeap h2
    else: #an to u einai peritto tha dw poios apo tous duo heaps exei ena stoixeio parapanw dioti auto to parapanw stoixeio pou einai h to minimum tou minHeap h1 eite to
          #maximum tou maxHeap h2 tha nai to median
        if(h1.size>h2.size):
            median=h1.getMin()
        elif(h1.size<h2.size):
            median=h2.getMax()
    return median

#h sunarthsh starting ousiastika ksexwrizei ta duo prwta tuples poy irthan se katallhlo pinaka   
def starting(first_two,coord,temp,arr1,arr2,median,count):
    first_two.append((coord,temp)) #bohthitikos pinakas mesw tou opoiou tha sugkrinw ta duo prwta stoixeia gia na ta topothethsw se katallhlo pinaka
    if (count==1):#count einai ousiastika to i sth main kai to count ginetai 1 sth 2h epanalhpsh opou tha exoume ta 2 prwta stoixeia kai tha mporoume na ta sugkrinoume
        if(first_two[0][1]>first_two[1][1]):
            arr1.append(first_two[0])
            arr2.append(first_two[1])
        else:
            arr1.append(first_two[1])
            arr2.append(first_two[0])
        median=('{h1.getMin()[0]} and {h2.getMax()[0]}',(arr1[0][1]+arr2[0][1])/2) #efoson exw 2 stoixeia (artios arithmos) o median tha nai o mesos oros tous
        return median
    return median #o median sthn 1h epanalhpsh paramenei 0 dioti exoume mono ena stoixeio
         
random.seed(1066581)#thetw san seed to AM mou
num_of_elements=14#arithmos shmeiwn sth gh
arr1=[]#pinakas pou periexei tuples ths morfhs ('x,y' , thermokrasia)
arr2=[]#pinakas pou periexei tuples ths morfhs ('x,y' , thermokrasia)
first_2=[] #krataei ta duo prwta tuples 
median=('x,y',0) #o median
T=[] #bohthhtikos pinakas 100 stoixeiwn
t0=time.time()
for i in range(num_of_elements): #gia osa shmeia ths ghs epithimoume 
    x,y=random.randint(0,1000),random.randint(0,1000) #tuxaies suntetagmenes x,y sto diasthma [0,1000]
    coord=str(x)+','+str(y) #coord einai oi suntetagmenes tou shmeiou se morfh 'x,y'
    temp=round(random.randint(0,99) + random.randint(0,99)/100 -50 , 2) #temp einai tuxaia thermokrasia sto diasthma [-50,50)
    if(i>1):#gia tis epanalhpseis apo thn 3h kai panw
        median=decisions(h1,h2,coord,temp,median)
    else: #afora tis duo prwtes epanalhpseis
        median=starting(first_2,coord,temp,arr1,arr2,median,i)#euresh tou median gia ta duo prwta stoixeia
        if(i==1):
            #arxikopoihsh twn 2 heaps
            h1=MinHeap(arr1) #o heap h1 einai min heap kai tha periexei ta shmeia pou einai megalutera tou median
            h2=MaxHeap(arr2) #o heap h2 einai max heap kai tha periexei ta shmeia pou einai mikrotera tou median
    if(i<5):#dhmiourgw ena pinaka T o opoios tha periexei tis suntetagmenes twn 100 prwtwn stoixeiwn me diaforetikh thermokrasia se sxesh me prin
        temp2=round(random.randint(0,99) + random.randint(0,99)/100 -50 , 2)
        T.append((coord,temp2))
        
print(f'The time it took for the algorithm to put all the coordinates in the heap and find the median is:{time.time()-t0:.2f}sec')  
print(f'Median is: {median}')
print()
t1=time.time()
print(T)
print()
print()
h1.display()
h2.display()
print()
print()
for j in range(5):
    median=decisions(h1,h2,T[j][0],T[j][1],median) #kalw thn decisions gia na allaksw tis thermokrasies twn 100 shmeiwn
    print(f'Median is: {median} in change number {j+1}')#tupwnw ton median se kathe epanalhpsh
    h1.display()
    h2.display()
    print()
    print()   
print(f'The time it took to change the 5 temperatures is:{time.time()-t1:.2f}sec')        
print(f'The new median is: {median}')

