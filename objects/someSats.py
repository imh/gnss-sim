import swiftnav.almanac as sa
import swiftnav.coord_system as cs
import numpy as n

def load_yuma(yuma):
    yuma = yuma.readlines()
    almanacs = {}
    for n, line in enumerate(yuma):
        if line[:3] == "ID:":
            block = yuma[n:n+13]
            fields = map(lambda x: x[25:], block)

            prn     = int(fields[0])
            healthy = (int(fields[1]) == 0)
            ecc     = float(fields[2])
            toa     = float(fields[3])
            inc     = float(fields[4])
            rora    = float(fields[5])
            a       = float(fields[6])**2
            raaw    = float(fields[7])
            argp    = float(fields[8])
            ma      = float(fields[9])
            af0     = float(fields[10])
            af1     = float(fields[11])
            week    = int(fields[12])

            almanac = sa.Almanac(ecc, toa, inc, rora, a, raaw, argp, ma, af0, af1, week, prn, healthy)
            almanacs[prn] = almanac
    return almanacs

with open("/Users/imh/software/swift/projects/integer-ambiguity/301.ALM") as f:
    alm = load_yuma(f)

llh = n.array([n.deg2rad(37.8400), n.deg2rad(-122.2816), 40])
ecef = cs.wgsllh2ecef(*llh)

def normalized(x):
    return x / n.sqrt(x.dot(x))

es = {prn:
          normalized(
               a.calc_state(0)[0]-ecef
          ) for prn, a in alm.iteritems()}



H = n.array([es[1], es[14], es[22], es[31], es[32]])
print H