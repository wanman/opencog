from opencog.atomspace import AtomSpace
from opencog.type_constructors import types
from opencog.utilities import initialize_opencog
from opencog.logger import log

from blending.blend import RandomBlender

__author__ = 'DongMin Kim'

log.use_stdout()
log.set_level("WARN")

a = AtomSpace()
initialize_opencog(a)

a.add_node(types.ConceptNode, "car")
a.add_node(types.ConceptNode, "man")

random_blending_inst = RandomBlender(a)
random_blending_inst.blend()
