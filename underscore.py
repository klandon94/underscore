## Refer back to Python library --> functools for useful information

class Underscore:
    # Produces a new array of values by mapping each value in list through a transformation function
    def map(self, list, function):
        for i in range(len(list)):
            list[i] = function(list[i])
        return list
    
    # Looks through each value in the list and returns an array of all the values that pass a truth test (predicate)
    def filter(self, list, predicate):
        newlist = []
        for i in range(len(list)):
            if predicate(list[i]):
                newlist.append(list[i])
        if len(newlist) == 0:
            return None
        return newlist

    # Boils down a list of values into a single value
    def reduce(self, list, function):
        value = 0
        for i in list:
            value = function(value,i)
        return value
    
    # Looks through each value in the list and returns the first one that passes a predicate
    def find(self, list, predicate):
        for i in range(len(list)):
            if predicate(list[i]):
                return list[i]
        return None
    
    # Returns the values in list without the elements that the predicate passes -- basically opposite of filter
    def reject(self, list, predicate):
        newlist = []
        for i in range(len(list)):
            if not predicate(list[i]):
                newlist.append(list[i])
        if len(newlist) == 0:
            return None
        return newlist

_ = Underscore()
triples = _.map([1,2,3,4,5,6], lambda x:x*3)
evens = _.filter([1,2,3,4,5,6], lambda x:(x%2==0))
sums = _.reduce([1,2,3,4,5,6], lambda x,y:x+y) # calculates ((((1+2)+3)+4)+5) --> left argument x is the accumulated value and the right argument y is the update value from the sequence
odd = _.find([2,4,1,7,3,10], lambda x:(x%2==1))
opposites = _.reject([1,2,3,4,5,6], lambda x:(x%2==0))

print(evens)



# def multiply(x):
#     return x*x
# def add(x):
#     return x+x

# funcs = [multiply,add]
# for i in range(5):
#     value = list(map(lambda x:x(i),funcs))
#     print(value)