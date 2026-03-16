 
names= ["Amit","Riya"]
ages= [25,30] 

l = [ (names,ages) for names,ages in zip(names,ages) ]
print(l)




d= {"a":10,"b":20}
key="b"
print(d[key])



d= {"x":1,"y":2}
key="x"
if key in d:
    print(True)



d= {"a":10,"b":20,"c":30}
key=d.keys()
print(sum(d.values()) )
print(len(key))


d= {"a":10,"b":20,"c":30}
key = d.keys()
print(len(key))


d= {"a":10}
key="a"
new_value=50
d[key]=new_value
print(d)


d= {"a":1,"b":2}
key=d.keys()
print(key) 



d= {"a":1,"b":2}
key = d.values()
print(key)



d1= {"a":1}
d2= {"b":2}
key = d1 | d2 
print(key)


"""s="banana"
d1 = s.count("a")
d2 = s.count("b")
d3 = s.count("n")
d = {"a":d1,"b":d2,"n":d3}
print(d)"""
s="I love Python I love coding"
word = s.split()
d = {word: word.count(word) for word in set(word)}
print(d)

words= ["apple","ant","bat","ball"]



from collections import defaultdict
from itertools import count

words = ["apple", "ant", "bat", "ball" , "cat", "car", "dog", "doll"]
d = defaultdict(list)
for w in words:
    d[w[0]].append(w)
print(dict(d))

d= {"a":10,"b":20,"c":10}
value = 10
result = {k: v for k, v in d.items() if v != value}   
print(result)

d = {"a": 10, "b": 20, "c": 10}
value = 10

result = {k: v for k, v in d.items() if v != value}
print(result)

 

words= ["eat","tea","tan","ate","nat","bat" , "tab", "cat", "act", "tac", "dog", "god", "odg", "dgo", "hello", "world", "python", "java", "ruby", "perl", "swift", "kotlin", "scala", "groovy", "haskell", "elixir", "clojure", "erlang", "rust", "go", "dart", "typescript", "javascript", "csharp", "fsharp", "objectivec", "visualbasic", "sql", "nosql", "mongodb", "redis", "cassandra", "hadoop", "spark", "flink", "kafka", "rabbitmq", "activemq"]
d = defaultdict(list)
for w in words:
    key = ''.join(sorted(w))
    d[key].append(w)
    result = list(d.values())  
print(result)



s = "leetcode"
from collections import Counter


def mana(s):
    count = Counter(s)

    for i,ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1

print(mana(s))  



  
