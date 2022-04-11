from numpy import pi, isclose

from pyroll.core.grooves import FalseRoundGroove


def test_false_round():
    g = FalseRoundGroove(depth=31.8646, r1=5, r2=38, flank_angle=65 / 180 * pi)

    assert isclose(g.usable_width, 78.13476937)
    assert isclose(g.alpha1, 65 / 180 * pi)
    assert isclose(g.alpha2, 65 / 180 * pi)
    assert isclose(g.z1, 42.2527)