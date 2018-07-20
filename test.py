# -*- coding: utf-8 -*-

import facades

from oemof.solph import EnergySystem, Bus, Model

typemap = {
    'bus': Bus,
    'demand': facades.Demand,
    'generator': facades.Generator}

es = EnergySystem.from_datapackage(
    'datapackage.json',
    attributemap={},
    typemap=typemap)

es._typemap = typemap
es.timeindex = es.timeindex[0:4]

m = Model(es)

f = [f for (s, t), f in es.flows().items() if s.label == 'biomass-Bordelum'][0]
print(f.max)

m.receive_duals()
m.solve(solver='gurobi', solve_kwargs={'tee': True})
