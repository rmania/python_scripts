# example to show performance boost of generators
import memory_profiler as mem_profile
import random
import time

names = ['Diederik', 'Rick', 'Rik', 'Steve', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Languages']

print(f"Memory (Before'): {mem_profile.memory_usage()}MB")


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
    yield person

t1 = time.clock()
people = people_list(100000)
t2 = time.clock()

print(f"Memory (After : {mem_profile.memory_usage()}")
print(f"took {t2-t1} seconds")

