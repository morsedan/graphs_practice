
class FamilyNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parents = []


def earliest_ancestor(ancestors, starting_node):
    relationships = {}
    for relationship in ancestors:
        parent, child = relationship[0], relationship[1]

        if parent not in relationships:
            parent = FamilyNode(parent)
        else:
            parent = relationships[parent]
        parent.children.append(child)
        relationships[parent.value] = parent

        if child not in relationships:
            child = FamilyNode(child)
        else:
            child = relationships[child]
        child.parents.append(parent.value)
        relationships[child.value] = child

    ancestor = relationships[starting_node]
    # print(ancestor.value, ancestor.parents, ancestor.children)
    earliest_ancestors = []
    # while ancestor.parents != []:
    #     earliest_ancestors = ancestor.parents
    #
    #     for value in earliest_ancestors:
    #         if relationships[value].parents != []:
    person = get_oldest_ancestor(relationships, starting_node)
    if person == starting_node:
        return -1
    print("Here", person)
    return person

    # return greatest_ancestor
    # for individual in relationships:
    #     print(relationships[individual].parents, relationships[individual].value, relationships[individual].children)
    # print(starting_node)

def get_oldest_ancestor(relationships, individual):
    print(relationships[individual].parents)
    if relationships[individual].parents == []:
        print(individual, "has no parents", relationships[individual].parents)
        return individual
    else:
        print("Parents here")
        for parent in relationships[individual].parents:
            return get_oldest_ancestor(relationships, parent)
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 7)
