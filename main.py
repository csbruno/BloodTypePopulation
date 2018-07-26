from random import randint
from random import choice

# A and B, R = dominants;
# i and r = recessive
bloodTypes = [
"Ai", #Blood type A
"AA", #Blood type A
"BB", #Blood type B
"Bi", #Blood type B
"AB", #Blood type AB
"ii"  #Blood type O
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
        maxChild = 1
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
                        return Person(doCombination(self.bloodType,p.bloodType),
                                doCombination(self.rhType,p.rhType),randomGenre(),self.gen)





#Return all possible combinations.
#Example: inputs("Ai","AB") return ["AA","AB","Ai","Bi"]
def doCombination(type1,type2):
        types =[]
        for a in (type1):
                for b in type2:
                        if(a[0] == "i"): #Fix inverse outputs E.: "iA"
                                types.append(b + a)
                        else:
                                types.append(a + b)
        
        return types[randint(0,len(types)-1)]

#Randomthings
def randomBType():
        return(bloodTypes[randint(0,len(bloodTypes)-1)])
def randomRHType():
        return(rhFactors[randint(0,len(rhFactors)-1)])
def randomGenre():
        return(randint(0,1))
def randomPerson(gen,genre):
        return Person(randomBType(),randomRHType(),genre,gen)


initialGen = 0
population = []
for p in range(0,100):
        population.append(randomPerson(initialGen,MALE))
        population.append(randomPerson(initialGen,FEMALE))
years = 100
curYear= 0
while (curYear < years):
        curYear +=1
        
        nList = []
        for p  in range(0,len(population)):
                population[p].grow()
        #       print(population[p].canReproduce)
                if(population[p].canReproduce):
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
                p1.gen != p2.gen
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

parsedR = {}
parsedR["A"] = results["Ai"] + results["AA"]
parsedR["B"] = results["Bi"] + results["BB"]
parsedR["AB"] = results["AB"] + results["BA"]
parsedR["O"] = results["ii"]
print("Year:1000, Pop:{1} ".format(curYear,alive))
        

print(parsedR)

print(len(population))
#print(population)






