from nearestNeigh.nearest_neigh import NearestNeigh
from nearestNeigh.point import Point
from operator import itemgetter

# -----------------------------------------------------------------
# This class is required to be implemented. Kd-tree implementation.
#
# __author__ = 'Prodip Guha Roy'
# __copyright__ = 'Copyright 2021, RMIT University'
#
# -----------------------------------------------------------------

class Node:  # a node inside the kdtree, stores a Point object, as well as a left and right child.
    def __init__(self, point):
        self.storedpoint = point
        self.leftchild = None
        self.rightchild = None

    def insert(self, newnode, x_or_y=0):
        if self.storedpoint.__eq__(newnode.storedpoint):
            return False  # cant insert a node that is already in the tree
        x_or_y = (x_or_y + 1) % 2

        if x_or_y == 1:  # determine child position based on x or y
            if newnode.storedpoint.lat < self.storedpoint.lat:  # compare x
                if self.leftchild:
                    return self.leftchild.insert(newnode,
                                                 x_or_y)  # if the current node being looked at has a child, go deeper down the tree
                else:
                    self.leftchild = newnode  # assign the new node
                    return True

            if newnode.storedpoint.lat >= self.storedpoint.lat:  # compare x
                if self.rightchild:
                    return self.rightchild.insert(newnode,
                                                  x_or_y)  # if the current node being looked at has a child, go deeper down the tree
                else:
                    self.rightchild = newnode  # assign the new node
                    return True

        else:
            if newnode.storedpoint.lon < self.storedpoint.lon:  # compare y
                if self.leftchild:
                    return self.leftchild.insert(newnode,
                                                 x_or_y)  # if the current node being looked at has a child, go deeper down the tree
                else:
                    self.leftchild = newnode  # assign the new node

                    return True

            if newnode.storedpoint.lon >= self.storedpoint.lon:  # compare x
                if self.rightchild:
                    return self.rightchild.insert(newnode,
                                                  x_or_y)  # if the current node being looked at has a child, go deeper down the tree
                else:
                    self.rightchild = newnode  # assign the new node

                    return True

    def get_fake_parent(self, newnode, x_or_y=0):  # return what would be the parent of a node if it was added
        x_or_y = (x_or_y + 1) % 2

        if x_or_y == 1:  # determine child position based on x or y
            if newnode.storedpoint.lat < self.storedpoint.lat:  # compare x
                if self.leftchild:
                    return self.leftchild.get_fake_parent(newnode,
                                                          x_or_y)  # if the current node being looked at has a child, go deeper down the tree
                else:
                    return self

            if newnode.storedpoint.lat >= self.storedpoint.lat:  # compare x
                if self.rightchild:
                    return self.rightchild.get_fake_parent(newnode,
                                                           x_or_y)  # if the current node being looked at has a child, go deeper down the tree
                else:
                    return self

        else:
            if newnode.storedpoint.lon < self.storedpoint.lon:  # compare y
                if self.leftchild:
                    return self.leftchild.get_fake_parent(newnode,
                                                          x_or_y)  # if the current node being looked at has a child, go deeper down the tree
                else:
                    return self

            if newnode.storedpoint.lon >= self.storedpoint.lon:  # compare x
                if self.rightchild:
                    return self.rightchild.get_fake_parent(newnode,
                                                           x_or_y)  # if the current node being looked at has a child, go deeper down the tree
                else:
                    return self

    def get_point(self, target, x_or_y=0):  # for a given point (target), find an identical copy in the tree
        if self.storedpoint.__eq__(target.storedpoint):
            return self  # point is in tree, so return it

        x_or_y = (x_or_y + 1) % 2

        if x_or_y == 1:
            if target.storedpoint.lat < self.storedpoint.lat:
                if self.leftchild:
                    return self.leftchild.get_point(target, x_or_y)
                else:
                    return None

            if target.storedpoint.lat >= self.storedpoint.lat:
                if self.rightchild:
                    return self.rightchild.get_point(target, x_or_y)
                else:
                    return None

        else:
            if target.storedpoint.lon < self.storedpoint.lon:
                if self.leftchild:
                    return self.leftchild.get_point(target, x_or_y)
                else:
                    return None

            if target.storedpoint.lon >= self.storedpoint.lon:
                if self.rightchild:
                    return self.rightchild.get_point(target, x_or_y)
                else:
                    return None
        return None

    def get_parent(self, target, x_or_y=0):  # returns none when the point doesnt exist
        # if the current node has a child node that is identical to the node being tested for, return current node as the parent
        if self.leftchild != None:
            if self.leftchild.storedpoint.__eq__(target.storedpoint):
                return self
        if self.rightchild != None:
            if self.rightchild.storedpoint.__eq__(target.storedpoint):
                return self

        x_or_y = (x_or_y + 1) % 2

        if x_or_y == 1:
            if target.storedpoint.lat < self.storedpoint.lat:
                if self.leftchild:
                    return self.leftchild.get_parent(target, x_or_y)
                else:
                    return None

            if target.storedpoint.lat >= self.storedpoint.lat:
                if self.rightchild:
                    return self.rightchild.get_parent(target, x_or_y)
                else:
                    return None

        else:
            if target.storedpoint.lon < self.storedpoint.lon:
                if self.leftchild:
                    return self.leftchild.get_parent(target, x_or_y)
                else:
                    return None

            if target.storedpoint.lon >= self.storedpoint.lon:
                if self.rightchild:
                    return self.rightchild.get_parent(target, x_or_y)
                else:
                    return None
        return None

    def is_leaf(self) -> bool:  # quick way to know if a node is a leaf, allows for deletion
        if self.leftchild == None and self.rightchild == None:
            return True
        else:
            return False

    def has_two_children(self) -> bool:  # quick way to know if a node is a leaf, allows for deletion
        if self.leftchild != None and self.rightchild != None:
            return True
        else:
            return False

    values = []

    def traversal(self):
        if self.leftchild:
            self.leftchild.traversal()
        Node.values.append(self)
        if self.rightchild:
            self.rightchild.traversal()

    def get_depth(self, target, current_depth=0,
                  x_or_y=0):  # for a given point (target), find an identical copy in the tree
        if self.storedpoint == target.storedpoint:
            return current_depth  # point is in tree, so return it

        x_or_y = (x_or_y + 1) % 2

        if x_or_y == 1:
            if target.storedpoint.lat < self.storedpoint.lat:
                if self.leftchild:
                    current_depth += 1
                    return self.leftchild.get_depth(target, current_depth, x_or_y)
                else:
                    return None

            if target.storedpoint.lat >= self.storedpoint.lat:
                if self.rightchild:
                    current_depth += 1
                    return self.rightchild.get_depth(target, current_depth, x_or_y)
                else:
                    return None

        else:
            if target.storedpoint.lon < self.storedpoint.lon:
                if self.leftchild:
                    current_depth += 1
                    return self.leftchild.get_depth(target, current_depth, x_or_y)
                else:
                    return None

            if target.storedpoint.lon >= self.storedpoint.lon:
                if self.rightchild:
                    current_depth += 1
                    return self.rightchild.get_depth(target, current_depth, x_or_y)
                else:
                    return None
        return None


class KDTreeNN(NearestNeigh):
    def make_kd_tree(self, points, x_or_y=0):

        # x_or_y is used to tell the function whether to sort the list based on x or y


        if len(points) > 1:  # if multiple things are in the list, there will be at least one parent and one leaf remaining to be created
            x_or_y = (x_or_y + 1) % 2

            if x_or_y == 1:  # sort list based on x or y
                points.sort(key=lambda point: point.lat)
            else:
                points.sort(key=lambda point: point.lon)

            half = len(points) >> 1  # find middle position

            found_leftmost = False
            leftmost_offset = 0
            while not found_leftmost:
                i = 1
                if x_or_y == 1:
                    if points[half - i].lat != points[half - leftmost_offset].lat:  # (1,2),(2,3),(5,6),(7,8),(10,12)
                        found_leftmost = True
                    else:
                        leftmost_offset += 1
                        i += 1
                if x_or_y == 0:
                    if points[half - i].lon != points[half - leftmost_offset].lon:
                        found_leftmost = True
                    else:
                        leftmost_offset += 1
                        i += 1

            current = Node(points[half - leftmost_offset])  # create a node out of the Point in the middle of the list, code needs to be changed

            current.leftchild = self.make_kd_tree(points[:half - leftmost_offset],
                                                  x_or_y)  # left child of the current node, returns None if there isnt a point to make a node from
            current.rightchild = self.make_kd_tree(points[half - leftmost_offset + 1:],
                                                   x_or_y)  # right child of the current node, returns None if there isnt a point to make a node from

            return current


        elif len(points) == 1:  # if only one thing is in the list, it must be a leaf, so make the lone point into a node and return
            return Node(points[0])

    kd_tree = Node

    def build_index(self, points: [Point]):
        self.kd_tree = self.make_kd_tree(points)  # make a kdtree using the list of Points.




    def recursive_search(self, current_node, current_min, search_term, k, dp=0):
        depth = self.kd_tree.get_depth(current_node)
        if current_node.storedpoint.cat != search_term.cat: # if the point has a different category, skip it
            if current_node.leftchild != None:
                self.recursive_search(current_node.leftchild, current_min, search_term, k, dp)
            if current_node.rightchild != None:
                self.recursive_search(current_node.rightchild, current_min, search_term, k, dp)

        else:
            d = search_term.dist_to(current_node.storedpoint)

            if d < current_min:
                current_min = d

            KDTreeNN.dictionary[d] = current_node.storedpoint



            if depth % 2 == 0:
                dummy_point = Point('dummy', search_term.cat, current_node.storedpoint.lat, search_term.lon)

            else:
                dummy_point = Point('dummy', search_term.cat, search_term.lat, current_node.storedpoint.lon)

            dp = search_term.dist_to(dummy_point)

            if dp < current_min:  # need to do both subtrees
                # current_min = dp
                if current_node.leftchild != None:
                    self.recursive_search(current_node.leftchild, current_min, search_term, k,dp)
                if current_node.rightchild != None:
                    self.recursive_search(current_node.rightchild, current_min, search_term, k,dp)

            else:  # only need to do one subtree

                if depth % 2 == 0:
                    # x split
                    if current_node.storedpoint.lat >= search_term.lat:
                        if current_node.leftchild != None:
                            self.recursive_search(current_node.leftchild, current_min, search_term, k,dp)
                    else:
                        if current_node.rightchild != None:
                            self.recursive_search(current_node.rightchild, current_min, search_term, k,dp)

                else:
                    # y split
                    if current_node.storedpoint.lon >= search_term.lon:
                        if current_node.rightchild != None:
                            self.recursive_search(current_node.rightchild, current_min, search_term, k,dp)
                    else:
                        if current_node.leftchild != None:
                            self.recursive_search(current_node.leftchild, current_min, search_term, k,dp)



    dictionary = {} # a dictionary used to store the distance of a given point from search_term, as well as the point itself.
    def search(self, search_term: Point, k: int) -> [Point]:

        fake_parent = self.kd_tree.get_fake_parent(Node(search_term))

        min = search_term.dist_to(fake_parent.storedpoint)

        self.recursive_search(self.kd_tree, min, search_term, k)


        sorted_points = dict(sorted(KDTreeNN.dictionary.items(), key=itemgetter(0))[:k])


        KDTreeNN.dictionary = {} # need to clear the dictionary each time or subsequent searches will break


        return sorted_points.values()

    def add_point(self, point: Point) -> bool:
        return self.kd_tree.insert(Node(point))  # run insert method on the root node

    def delete_point(self, point: Point) -> bool:
        target_node = self.kd_tree.get_point(Node(point))  # create a Node using point, and find it in the tree
        if target_node == None:  # "case 0": node doesnt exist in tree, so cant delete.
            return False

        else:  # case 1, node to be deleted is a leaf
            if target_node.is_leaf():  # check if leaf, if not, try case 2

                target_parent = self.kd_tree.get_parent(target_node)  # get the parent of the node to be deleted
                if target_parent != None:  # this is an extreme edge case where the only point in the tree is the root

                    # figure out which of the parent's two children is the node that is to be deleted
                    if target_parent.leftchild != None:
                        if target_parent.leftchild.storedpoint == target_node.storedpoint:
                            target_parent.leftchild = None  # destroy reference to child
                    if target_parent.rightchild != None:
                        if target_parent.rightchild.storedpoint == target_node.storedpoint:
                            target_parent.rightchild = None  # destroy reference to child*

            else:  # case 2 and 3

                def case2(target_node):
                    if target_node.rightchild != None:

                        target_node.rightchild.traversal()

                        smallest_index = 0
                        if target_node_depth % 2 == 0:
                            minimum = self.kd_tree.values[0].storedpoint.lat
                            for i in range(1, len(Node.values)):
                                if minimum > Node.values[i].storedpoint.lat:
                                    minimum = Node.values[i].storedpoint.lat
                                    smallest_index = i

                        if target_node_depth % 2 == 1:
                            minimum = self.kd_tree.values[0].storedpoint.lon
                            for i in range(1, len(Node.values)):
                                if minimum > Node.values[i].storedpoint.lon:
                                    minimum = Node.values[i].storedpoint.lon
                                    smallest_index = i

                        smallest_node = Node.values[smallest_index]
                        smallest_node_parent = self.kd_tree.get_parent(smallest_node)

                        if Node.values[smallest_index].is_leaf():
                            if smallest_node_parent.rightchild != None:
                                if smallest_node_parent.rightchild.storedpoint.__eq__(smallest_node.storedpoint):
                                    smallest_node_parent.rightchild = None
                                    target_node.storedpoint = smallest_node.storedpoint
                            else:
                                smallest_node_parent.leftchild = None
                                target_node.storedpoint = smallest_node.storedpoint
                        else:
                            case2(
                                smallest_node)  # node chosen to replace deleted node, has child. so need to replace the replacement :/
                    else: # case 3, essentially just changes the tree in a way that lets us reuse case2
                        target_node.rightchild = target_node.leftchild
                        target_node.leftchild = None

                        case2(target_node)

                target_node_depth = self.kd_tree.get_depth(target_node)

                case2(target_node)
                Node.values = []
            return True

    def is_point_in(self, point: Point) -> bool:
        if self.kd_tree.get_point(Node(point)) != None:
            return True
        else:
            return False

