


"""...............................dictionary..................................."""


"""https://github.com/vidyagowda159/Alpha-4/blob/master/Datatypes/collection_datatypes/dictionary.py"""


# creating a dictionary

# d = {"a": 1, "b": 2}
# d = dict({"a": 1, "b": 2})
# d = dict([("a", 1), ("b", 2)])
# d = dict(a=1, x=10)

# default value
# d = {}
# d = dict()


# composite keys

# d1 = {("march", 4): "Friday",
#       ("march", 5): "Saturday"
#       }

# accessing the values
d = {'Bangalore': 25, "Chennai": 35, "Delhi": 30}

# print(d["Bangalore"])     #25
# print(d["Kolkata"])     # KeyError

# print(d.get("Bangalore", "Key is not present"))   #25
# print(d.get("Kolkata", "Key is not present"))     #Key is not present

# inserting values to a dictionary
d = {'Bangalore': 25, "Chennai": 35, "Delhi": 30}

d["Kolkata"] = 40
# print(d)                               #{'Bangalore': 25, 'Chennai': 35, 'Delhi': 30, 'Kolkata': 40}

d["Bangalore"] = 27
# print(d)                               #{'Bangalore': 27, 'Chennai': 35, 'Delhi': 30, 'Kolkata': 40}
#
d.update(Mysore=26)
# print(d)                                 #{'Bangalore': 27, 'Chennai': 35, 'Delhi': 30, 'Kolkata': 40, 'Mysore': 26}
#
d.update({"a": 1, "b": 1, "c": 2})
# print(d)                                 #{'Bangalore': 27, 'Chennai': 35, 'Delhi': 30, 'Kolkata': 40, 'Mysore': 26, 'a': 1, 'b': 1, 'c': 2}

# print(d.setdefault("Rajasthan"))           #None
# print(d)                                   #{'Bangalore': 27, 'Chennai': 35, 'Delhi': 30, 'Kolkata': 40, 'Mysore': 26, 'a': 1, 'b': 1, 'c': 2, 'Rajasthan': None}

# print(d.setdefault("Rajasthan", 50))      #50      (if we give value then value will replace None)
# print(d)                                  #{'Bangalore': 27, 'Chennai': 35, 'Delhi': 30, 'Kolkata': 40, 'Mysore': 26, 'a': 1, 'b': 1, 'c': 2, 'Rajasthan': 50}



# delete values from a dictionary
# d = {'Bangalore': 25, "Chennai": 35, "Delhi": 30}
#
# print(d.pop("Chennai"))         #35
# print(d)                        #{'Bangalore': 25, 'Delhi': 30}
#
# print(d.popitem())              #('Delhi', 30)
# print(d)                        #{'Bangalore': 25}



# s = "hello"
# l = [1, 2, 3, 4]
# d = {}
# print(d.fromkeys(s))              #{'h': None, 'e': None, 'l': None, 'o': None}
# print(dict.fromkeys(l))              #{1: None, 2: None, 3: None, 4: None}
# print(d)                           #{}


# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# print({**d1, **d2})                 #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(d1 | d2)                      #TypeError: unsupported operand type(s) for |: 'dict' and 'dict'

l1 = [[1, 2], [3, 4], [5, 6]]
# print(dict(l1))
#output - {1: 2, 3: 4, 5: 6}

l1 = [(1, 2), (3, 4), [5, 6]]
# print(dict(l1))
#output - {1: 2, 3: 4, 5: 6}

# l1 = ["ab", "12", "cd"]
# print(dict(l1))
#output = {'a': 'b', '1': '2', 'c': 'd'}


# s = {1, 2, 3}

# print(str(s))                   #{1, 2, 3}
# print(list(s))                  #[1, 2, 3]
# print(tuple(s))                 #(1, 2, 3)



