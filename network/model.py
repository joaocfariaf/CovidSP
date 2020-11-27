import math
import numpy as np
import igraph as ig
import itertools
from typing import List, Tuple

from params import BASELINE_EMPLOYEES_PER_COMPANY, BASELINE_JOBS_PER_PERSON, FAMILY_ZONE_PROBABILITY, JOB_ZONE_PROBABILITY, MAX_FAMILY_SIZE

UNDEFINED = -1

class Entity:
    def __init__(self, _id: int) -> None:
        self.id = _id

class Person(Entity):
    def __init__(self, _id: int) -> None:
        super().__init__(_id)
        self.family = UNDEFINED
        self.company = UNDEFINED
        self.friendship = UNDEFINED

class LocatedEntity(Entity):
    def __init__(self, _id: int) -> None:
        super().__init__(_id)
        self.zone = UNDEFINED
        self.position = (-1,-1)

class Family(LocatedEntity):
    def __init__(self, _id: int, _size: int) -> None:
        super().__init__(_id)
        self.size = _size
        self.member_ids = []

class Company(LocatedEntity):
    def __init__(self, _id: int) -> None:
        super().__init__(_id)
        self.zone = UNDEFINED


def __init_graph_from_families(num_families: int, max_family_size: int, distr='binomial') -> Tuple[ig.Graph, List[Person], List[Family]]:
    if distr != 'binomial': raise NotImplementedError
    network = ig.Graph()
    families = [ None ] * num_families
    num_persons = 0
    ##
    ## Sample the families with a binomial
    ##
    for i in range(num_families):
        family_size = np.random.binomial(max_family_size,0.5)
        families[i] = Family(i,family_size)
        num_persons += family_size
    ##
    ## Create people from family
    ##
    persons = [ None ] * num_persons
    person_id = 0
    for family in families:
        for i in range(family.size):
            new_person = Person(person_id)
            new_person.family = family.id
            persons[person_id] = new_person
            family.member_ids.append(person_id)
            person_id += 1
    ##
    ## Create graph
    ##
    for family in families:
        network.add_vertices(family.member_ids)
        network.add_edges(itertools.combinations(family.member_ids, 2))
    return network, persons, families

def __init_companies(num_companies: int) -> List[Company]:
    return [Company(i) for i in range(num_companies)]

def __zone(entities: List[LocatedEntity], zone_distr: List[float]) -> List[int]:
    num_entities = len(entities)
    num_zones = len(zone_distr)
    if num_entities <= 0:
        raise ValueError(f'Invalid number of entities:{num_entities}')
    if num_zones <= 0:
        raise ValueError(f'Invalid number of zones:{num_zones}')
    sample = list(np.random.multinomial(num_entities, zone_distr))
    entity_count = 0
    zone = 0
    for entity in entities:
        if entity_count == sample[zone]:
            ## Reached zone maximum
            entity_count = 0
            zone += 1
            while zone < len(sample) and entity_count == sample[zone]:
                zone += 1
            if zone == len(sample):
                raise RuntimeError('Number of entities sampled not equal to total number of entities (????)')
        # Position entity at its zone
        entity.zone = zone
        entity_count += 1
    return sample

def generate(args: dict) -> ig.Graph:
    num_families = args['num_families']
    network, persons, families = __init_graph_from_families(num_families, MAX_FAMILY_SIZE)
    num_people = network.vcount()
    print(f"num_people={num_people}")
    families_per_zone = __zone(families, FAMILY_ZONE_PROBABILITY)
    print(f"families_per_zone={families_per_zone}")
    num_companies = math.ceil(num_people*BASELINE_JOBS_PER_PERSON/BASELINE_EMPLOYEES_PER_COMPANY)
    print(f"num_companies={num_companies}")
    companies = __init_companies(num_companies)
    companies_per_zone = __zone(companies, JOB_ZONE_PROBABILITY)
    print(f"companies_per_zone={companies_per_zone}")
    # __employ_people(network, )
    # print(network)
    return network