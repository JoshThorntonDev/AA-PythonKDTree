from typing import Sequence
from nearestNeigh.nearest_neigh import NearestNeigh
from nearestNeigh.point import Point
import heapq
import time

# ------------------------------------------------------------------------
# This class is required to be implemented. Naive approach implementation.
#
# __author__ = 'Prodip Guha Roy'
# __copyright__ = 'Copyright 2021, RMIT University'
#
# ------------------------------------------------------------------------
class NaiveNN(NearestNeigh):

    points = []

    def build_index(self, points: [Point]):
        self.points = points


    def search(self, search_term: Point, k: int) -> [Point]:
        start = time.time()
        closestPoints = []
        distances = []
        smallestDistances = []

        # calculate the distances of all points that have the same cat as search_term
        for i in range (0,len(self.points)):
            if self.points[i].cat == search_term.cat:
                distances.append(search_term.dist_to(self.points[i]))

        # sort distances smallest to largest
        smallestDistances=heapq.nsmallest(k, distances)

        # find the points that belong to the distances
        for j in range(0,len(smallestDistances)):
            for i in range (0,len(self.points)):

                if smallestDistances[j] == search_term.dist_to(self.points[i]):
                    closestPoints.append(self.points[i])
        end = time.time()
        print(end-start)
        return closestPoints





    def add_point(self, point: Point) -> bool:
        if self.is_point_in(point):
            return False
        else:
            self.points.append(point)
            return True


    def delete_point(self, point: Point) -> bool:
        if point in self.points:
            self.points.remove(point)
            return True
        else:
            return False




    def is_point_in(self, point: Point) -> bool:
        if point in self.points:
            return True
        else:
            return False

