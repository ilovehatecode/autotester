import random
import string

class Concept:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
        
class Relationship:

    def __init__(self, u, v, relationshipType):
        self.source = u
        self.destination = v
        self.relationshipType = relationshipType

    def getSource(self):
        return self.source

    def getDestination(self):
        return self.destination

    def getRelationshipType(self):
        return self.relationshipType
    
    def getArticle(self, negate):
        vowels = ['a', 'e', 'i', 'o', 'u']
        first_letter = string.lower(self.getDestination().getName()[0])
        is_vowel = False
        for v in vowels:
            if(v == first_letter):
                is_vowel = True
                
        if(is_vowel):
            if(negate == 0):
                return ' an '
            else:
                return ' not an '
        else:
            if(negate == 0):
                return ' a '
            else:
                return ' not a '

class Test:

    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.test_ans = []
        self.user_ans = []
        self.test_ques = []
    def createQuestion(self):
        size = len(self.E)
        r = random.randrange(size)
        e = self.E[r]
        negate = random.randint(0,1)
        ans = True
        q = e.getRelationshipType() + " " + e.getSource().getName() + e.getArticle(negate)  + e.getDestination().getName() + "?"
        if(negate == 1):
            ans = False
        self.test_ans.append(ans)
        return q, ans

    def make_test(self, num=1):
        i = 0
        while(i<num):
            q, ans = self.createQuestion()
            self.test_ques.append(q)
            self.test_ans.append(ans)
            i = i + 1
        i = 0
        while(i<num):
            user_input = input(self.test_ques[i])
            if(user_input == self.test_ans[i]):
                print("correct")
            else:
                print("incorrect")
            i = i + 1
        
##Runs test
def main():
    ##Create Concepts
    u = Concept("Alpha Hydroxl Acid")
    v = Concept("Acid")
    ##Connect concepts with relationships
    e = Relationship(u, v,"is")
    ##Place concepts and relationships in separate list
    V = [v]
    E = [e]
    ##Create Test
    t = Test(V,E)
    t.make_test()
    


main()
        
    
        
        







