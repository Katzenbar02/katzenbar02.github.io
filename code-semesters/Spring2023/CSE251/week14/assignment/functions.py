"""
Course: CSE 251, week 14
File: functions.py
Author: <Joshua Ludwig>

Instructions:

Depth First Search
https://www.youtube.com/watch?v=9RHO6jU--GU

Breadth First Search
https://www.youtube.com/watch?v=86g8jAQug04


Requesting a family from the server:
request = Request_thread(f'{TOP_API_URL}/family/{id}')
request.start()
request.join()

Example JSON returned from the server
{
    'id': 6128784944, 
    'husband_id': 2367673859,        # use with the Person API
    'wife_id': 2373686152,           # use with the Person API
    'children': [2380738417, 2185423094, 2192483455]    # use with the Person API
}

Requesting an individual from the server:
request = Request_thread(f'{TOP_API_URL}/person/{id}')
request.start()
request.join()

Example JSON returned from the server
{
    'id': 2373686152, 
    'name': 'Stella', 
    'birth': '9-3-1846', 
    'parent_id': 5428641880,   # use with the Family API
    'family_id': 6128784944    # use with the Family API
}

You will lose 10% if you don't detail your part 1 and part 2 code below

Describe how to speed up part 1

<By using multiple threads to fetch data concurrently, 
the function can overlap network requests and potentially 
reduce the overall waiting time. This parallelization can 
lead to a faster retrieval of data from the server compared 
to fetching data sequentially.>


Describe how to speed up part 2

<By using multithreading with a thread pool, 
the breadth_fs_pedigree function can fetch family 
and person data concurrently, reducing the overall 
time required to retrieve the complete pedigree.>


Extra (Optional) 10% Bonus to speed up part 3

<By utilizing multithreading and performing the requests 
concurrently, this function  makes the data fetching process 
faster compared to a sequential approach. The use of a thread pool 
helps manage the threads efficiently and allows for parallel execution 
of tasks, resulting in improved performance when fetching data from the server.>

"""
from common import *
from multiprocessing.pool import ThreadPool

# -----------------------------------------------------------------------------
def depth_fs_pedigree(family_id, tree):
    if family_id is None:
        return

    print(f'Retrieving Family: {family_id}')

    req_family = Request_thread(f'{TOP_API_URL}/family/{family_id}')
    req_family.start()
    req_family.join()

    new_family = Family(req_family.get_response())
    tree.add_family(new_family)

    husband_id, wife_id, children_ids = new_family.get_husband(), new_family.get_wife(), [c for c in new_family.get_children() if not tree.does_person_exist(c)]
    print(f'   Retrieving Husband : {husband_id}')
    print(f'   Retrieving Wife    : {wife_id}')
    print(f'   Retrieving children: {", ".join(str(child_id) for child_id in children_ids)}')

    req_parents = [Request_thread(f'{TOP_API_URL}/person/{id}') for id in [husband_id, wife_id]]
    for t in req_parents:
        t.start()
    for t in req_parents:
        t.join()
    parents = [Person(r.get_response()) for r in req_parents if r.get_response() is not None]
    family_threads = [threading.Thread(target=depth_fs_pedigree, args=(p.get_parentid(), tree)) for p in parents]

    req_children = [Request_thread(f'{TOP_API_URL}/person/{id}') for id in children_ids]
    for t in req_children:
        t.start()

    for person in parents:
        tree.add_person(person)
    for thread in family_threads:
        thread.start()

    for t in req_children:
        t.join()
        if t.get_response() is not None:
            tree.add_person(Person(t.get_response()))

    for thread in family_threads:
        thread.join()


# -----------------------------------------------------------------------------
def breadth_fs_pedigree(family_id, tree):
    def get_family(family_id):
        req_family = Request_thread(f'{TOP_API_URL}/family/{family_id}')
        req_family.start()
        req_family.join()
        new_family = Family(req_family.get_response())
        tree.add_family(new_family)
        parents_ids = [new_family.get_husband(), new_family.get_wife()]
        current_parent_id_list.extend(parents_ids)
        children_ids = [child_id for child_id in new_family.get_children() if not tree.does_person_exist(child_id)]
        current_child_id_list.extend(children_ids)

    def get_parent(id):
        req_person = Request_thread(f'{TOP_API_URL}/person/{id}')
        req_person.start()
        req_person.join()
        new_person = Person(req_person.get_response())
        if new_person is not None:
            tree.add_person(new_person)
            return new_person.get_parentid()

    def get_child(id):
        get_parent(id)

    current_family_id_list = [family_id]
    next_family_id_list = []
    with ThreadPool(50) as pool:
        while len(current_family_id_list) != 0:
            current_parent_id_list = []
            current_child_id_list = []

            pool.map(get_family, current_family_id_list)
            next_family_id_list = pool.map(get_parent, current_parent_id_list)
            pool.map(get_child, current_child_id_list)

            current_family_id_list = [id for id in next_family_id_list if id is not None]
            next_family_id_list = []

# -----------------------------------------------------------------------------
def breadth_fs_pedigree_limit5(family_id, tree):
    def get_family(family_id):
        req_family = Request_thread(f'{TOP_API_URL}/family/{family_id}')
        req_family.start()
        req_family.join()
        new_family = Family(req_family.get_response())
        tree.add_family(new_family)
        parents_ids = [new_family.get_husband(), new_family.get_wife()]
        current_parent_id_list.extend(parents_ids)
        children_ids = [child_id for child_id in new_family.get_children() if not tree.does_person_exist(child_id)]
        current_child_id_list.extend(children_ids)

    def get_parent(id):
        req_person = Request_thread(f'{TOP_API_URL}/person/{id}')
        req_person.start()
        req_person.join()
        new_person = Person(req_person.get_response())
        if new_person is not None:
            tree.add_person(new_person)
            return new_person.get_parentid()

    def get_child(id):
        get_parent(id)

    current_family_id_list = [family_id]
    next_family_id_list = []
    with ThreadPool(5) as pool:
        while len(current_family_id_list) != 0:
            current_parent_id_list = []
            current_child_id_list = []

            pool.map(get_family, current_family_id_list)
            next_family_id_list = pool.map(get_parent, current_parent_id_list)
            pool.map(get_child, current_child_id_list)

            current_family_id_list = [id for id in next_family_id_list if id is not None]
            next_family_id_list = []
