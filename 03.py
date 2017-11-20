'''
made by malcolm
in november 2017
for isc3u
finds the lowest number in an array
'''

def array_function(array = []):
    for i in array:
        Min = min(array)
        return Min
a = [1, 2, 3, 4, 12]
min_value = array_function(a)
print'the lowest number in the array is: ' 
print(min_value)

