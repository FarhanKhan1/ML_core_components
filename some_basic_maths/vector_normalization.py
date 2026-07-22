
def magnitude_(v):
    result = sum([i*i for i in v])**0.5
    return result


def normalize_vector(v):
    magnitude = magnitude_(v)
    return ([dim/magnitude for dim in v])


test_cases = [[3,4],
 [5,3,4],
 [1,2,3,4,5,6,7]]

for v in test_cases:
    print(normalize_vector(v))
