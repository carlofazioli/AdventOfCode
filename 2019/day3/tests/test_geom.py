import glob
import pytest


from geom import *


# Basic tests:
def test_points_eq():
    A = Point(1,3)
    B = Point(1,3)
    C = Point(4,0)
    assert A == B
    assert A != C

def test_segment_slope():
    s = Segment

# Find examples and results


