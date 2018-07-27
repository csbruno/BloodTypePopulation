from random import randint
from random import choice
from time import time

# A and B, R = dominants;
# i and r = recessive
bloodAlleles = [
"A",
"B"
]
bloodTypes = [
"Ai", #Blood type A
"AA", #Blood type A
"BB", #Blood type B
"Bi", #Blood type B
"AB", #Blood type AB
"ii"  #Blood type O
]
ant = [
"HH",
"Hh",
"hh"
]
rhFactors = [
"RR", #Positive +
"Rr", #Positive +
"rr"  #Negative -
]
MALE = 0
FEMALE = 1
class Person:
        deathAge = 80
        reproduceAge = 18
        maxReproduceAge = 50
        reproducePause = 5
        oldGenReproduce = False
        maxChild = 10
        def __init__(self, bloodType, rhType, gender,gen):
                self.bloodType = bloodType
                self.rhType = rhType
                self.gender = gender
                self.age = 0
                self.isAlive = True
                self.canReproduce = False
                self.maxChildren= 1000
                self.yearsSinceLastChild = 0
                self.hadChild = False
                self.gen = gen
                self.gen +=1
                self.childCount = 0
                self.eriFetal = False
                self.haveCouple = False
                self.patner = None
             
        def grow(self):
                if(self.age >= self.deathAge):
                        self.isAlive = False
                        return
                self.age += 1

                if(self.hadChild): self.yearsSinceLastChild +=1
                
                if(self.age > self.reproduceAge and self.age < self.maxReproduceAge and self.childCount <= self.maxChild):
                        self.canReproduce = True
                      #  print(self.childCount)
                else:
                        self.canReproduce = False


        def reproduce(self,p):
                if(self.gender == p.gender or
                        self.canReproduce == False or
                         (not self.isAlive) or p.gen != self.gen):
                        return
                else:
                        self.hadChild = True
                        self.haveCouple = True
                        self.patner = p
                        p.patner = self
                        self.yearsSinceLastChild = 0
                        self.childCount +=1
                        nChild = Person(doCombination(self.bloodType,p.bloodType),
                                doCombination(self.rhType,p.rhType),randomGenre(),self.gen)

                        if(self.rhType == "rr" and (not nChild.rhType == "rr")):
                                self.eriFetal = True
                                if(self.childCount>1):
                                        nChild.isAlive = False
                        return nChild
        





#Return all possible combinations.
#Example: inputs("Ai","AB") return ["AA","AB","Ai","Bi"]
def doCombination(type1,type2):
        types =[]
        for a in (type1):
                for b in type2:
                        types.append(b + a)
        r = types[randint(0,len(types)-1)]
        if((r[0]=="i" and (r[1] == "A" or r[1] =="B"))or(r[0]=="B" and r[1]=="A")):
           return r[1] + r[0]
        return r

#Randomthings
def randomBType():
        return(bloodTypes[randint(0,len(bloodTypes)-1)])
def randomRHType():
        return(rhFactors[randint(0,len(rhFactors)-1)])
def randomGenre():
        return(randint(0,1))
def randomPerson(gen,genre):
        return Person(randomBType(),randomRHType(),genre,gen)
def parseResult(results):
        r = {}
        r["A"] = results["Ai"] + results["AA"]
        r["B"] = results["Bi"] + results["BB"]
        r["AB"] = results["AB"]
        r["O"] = results["ii"]
        return(r)
        

start_time = time()
initialPop = 300
initialGen = 0
population = []
for p in range(0,initialPop):
        population.append(randomPerson(initialGen,MALE))
        population.append(randomPerson(initialGen,FEMALE))
years = 2000
curYear= 0
while (curYear < years):
        curYear +=1
        print("Current y: {0}".format(curYear))
        nList = []
        for p  in range(0,len(population)):
                population[p].grow()
        #       print(population[p].canReproduce)
                if(population[p].canReproduce and population[p].isAlive):
                        nList.append(population[p])
        pos = 0
        wait= 0
        for e in nList:
                if(e.haveCouple):
                       if(e in nList): nList.remove(e)
                       if(e.patner in nList): nList.remove(e.patner)
        while(len(nList)> pos):
                p1 = choice(nList)
                p2 = choice(nList)
                if(wait>10):
                        break
                if(p1 == p2  or p1.gen != p2.gen):
                        wait+=1
                        continue
                c =p1.reproduce(p2)
                if(type(c) != type(p1)):
                        continue
                pos +=2
                population.append(c)
                nList.remove(p1)
                nList.remove(p2)

results = {}
alive = 0
for i in population:
        if(results.get(i.bloodType)):
                results[i.bloodType] +=1
        else:
                results[i.bloodType] =1
        if(i.isAlive): alive +=1



print(" Alive pop:{0}\n Total Pop:{1}\n Years:{2} ".format(alive,len(population),years))      
print(parseResults(results))
print("Runtime: %ss " % (time() - start_time))






