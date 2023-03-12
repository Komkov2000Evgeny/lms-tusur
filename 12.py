#1
class Friends():
    def __init__(self, connections):
        from collections import defaultdict
        counter = defaultdict(int)

        for element in connections:
            bundle = ""
            for symbol in element:
                bundle += symbol    
            counter[bundle] += 1

        for key in counter.keys():
            if counter[key]>1:
                connexion = set()
                for collectionin in key:
                    connexion.add(collectionin)
                for _ in range(counter[key]-1):
                    connections.remove(connexion)

        self.connections = connections

    def add(self, connection):        
        if connection not in self.connections:
            self.connections.append(connection) 
            return print(False)
        else:
            return print(True)

    def remove(self, connection):        
        if connection in self.connections:
            self.connections.remove(connection) 
            return print(True)
        else:
            return print(False)

    def names(self):
        return print({name for element in self.connections for name in element})

    def connected(self,name_key):
        result = set()
        for element in self.connections:
            if name_key in element:
                for name in element:
                    if name != name_key:
                        result.add(name)
        return print(result)

f = Friends([{"1", "2"}, {"3", "1"}])
print(f.connections)
f.add({"1", "3"})
print(f.connections)
f.remove({"1", "2"})
print(f.connections)
f.names()
f.remove({"1", "2"})
f.names()
f.connected("3")

#2

class Students():
    groups = {}
    def __init__(self, name, group, evaluations):
        if group in Students.groups.keys():
            Students.groups[group].update({name:evaluations})
        else:
            Students.groups[group] = ({name:evaluations})
    
    def information():
        print(Students.groups)

    def average_score_students_group(group_search):      
        for group in Students.groups:
            if group == group_search:                
                for name in Students.groups[group]:                 
                    average_score = 0
                    for science in Students.groups[group][name]:                        
                        average_score += Students.groups[group][name][science]
                    average_score /= len(Students.groups[group][name])
                    print("%s -> %s"%(name,average_score))

    def average_score_group(group_search):      
        for group in Students.groups:
            if group == group_search:
                average_score = 0
                for name in Students.groups[group]:                 
                    average_score_student = 0
                    for science in Students.groups[group][name]:                        
                        average_score_student += Students.groups[group][name][science]
                    average_score_student /= len(Students.groups[group][name])
                    average_score += average_score_student
                average_score /= len(Students.groups[group])
                print("%s -> %s"%(group_search,average_score))

    def average_score_group_science(group_search, science_search):      
        for group in Students.groups:
            if group == group_search:
                average_score_science = 0
                for name in Students.groups[group]:
                    for science in Students.groups[group][name]:
                        if science == science_search:
                            average_score_science += Students.groups[group][name][science]                    
                average_score_science /= len(Students.groups[group])
                print("%s -> %s"%(group_search,average_score_science))

s1 = Students("Ivan", 209, {"Physics":3, "Mathematics":3, "Chemistry":3})
s2 = Students("Ruslan", 209, {"Physics":5, "Mathematics":5, "Chemistry":5})
s3 = Students("Misha", 200, {"Physics":4, "Mathematics":3, "Chemistry":4})
s4 = Students("Lesha", 200, {"Physics":4, "Mathematics":5, "Chemistry":4})
#Students.information()
Students.average_score_group_science(209, "Mathematics")




