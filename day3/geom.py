from math import sqrt, isclose
from importlib import reload


def parse_wiring(filename):
    paths = list()
    with open(filename) as f:
        for line in f:
            wiring_steps = line[:-1].split(',')
            points = [Point(0, 0)]
            for step in wiring_steps:
                curr = points[-1]
                move = step[0]
                dist = float(step[1:])
                if move in ['L', 'D']:
                    dist *= -1
                if move in ['L', 'R']:
                    next = Point(curr.x + dist, curr.y)
                else:
                    next = Point(curr.x, curr.y + dist)
                points.append(next)
            paths.append(Path(points))
    return paths
                    
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return isclose(self.x, other.x) and isclose(self.y, other.y)
        return NotImplemented

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


class Segment:
    def __init__(self, a, b):
        assert isinstance(a, Point)
        assert isinstance(b, Point)
        self.a = a
        self.b = b
        self.dx = self.b.x - self.a.x
        self.dy = self.b.y - self.a.y

    def __repr__(self):
        return '(' + str(self.a) + ', ' + str(self.b) + ')'

    def contains(self, c):
        assert isinstance(c, Point)
        tmp = Segment(self.a, c)
        if isclose(tmp.dx*self.dy, tmp.dy*self.dx):
            in_x = min(self.a.x, self.b.x) <= c.x <= max(self.a.x, self.b.x)
            in_y = min(self.a.y, self.b.y) <= c.y <= max(self.a.y, self.b.y)
            return in_x and in_y
        return False

    def len(self):
        dx = abs(self.a.x - self.b.x)
        dy = abs(self.a.y - self.b.y)
        return sqrt(dx*dx + dy*dy)

    def y(self, x):
        if isclose(self.dx, 0):
            return None
        else:
            return self.a.y + self.dy * (x - self.a.x) / self.dx

    def intersects(self, seg):
        assert isinstance(seg, Segment)
        if isclose(seg.dx*self.dy, seg.dy*self.dx):
            # Segments are parallel.  
            # Return do-not-intersect for this use case.
            return None
        else:
            if isclose(self.dx, 0):
                p = Point(self.a.x, seg.y(self.a.x))
            elif isclose(seg.dx, 0):
                p = Point(seg.a.x, self.y(seg.a.x))
            else:
                # Solve the linear system:
                r1 = self.dy * self.a.x - self.dx * self.a.y
                r2 = seg.dy * seg.a.x - seg.dx * seg.a.y
                det = self.dx*seg.dy - self.dy*seg.dx
                x = (self.dx*r2 - seg.dx*r1) / det
                y = (self.dy*r2 - seg.dy*r1) / det
                p = Point(x, y)
        if self.contains(p):
            return p


class Path:
    def __init__(self, 
                 points_list,
                 include_origin=False):
        self.points = list()
        if include_origin:
            self.points.append(Point(0, 0))
        self.points += points_list
        for p in self.points:
            assert isinstance(p, Point)
        self.segments = list()
        for a, b in zip(self.points[:-1], self.points[1:]):
            self.segments.append(Segment(a,b))
        
    def path_intersect(self, path):
        intersections = list()
        for self_seg in self.segments:
            for path_seg in path.segments:
                p = self_seg.intersects(path_seg)
                if p:
                    intersections.append(p)
        return intersections
