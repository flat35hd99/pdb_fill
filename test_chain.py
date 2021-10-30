# def hoge (self, other):
#     # other is int, float, numpy
#     if (type(other) == "int" || type(other) == "float64"):
#         coord = self.get_coord
#         new_coord = coord * other
#         new_chain = copy(self)
#         new_chain.set_coord(new_coord)
#         return new_chain
#     if (type(other) == "numpy.ndarray"):
#         # process
#         return new_chain

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../biopython'))
from Bio.PDB import PDBParser, PDBList
import numpy as np
import math

pdb_code="5V8K"
pdb = PDBList()
pdb_filename = pdb.retrieve_pdb_file(pdb_code, file_format="pdb")

parser = PDBParser(QUIET=True)
structure = parser.get_structure(pdb_code, pdb_filename)

chains = np.array(list(structure.get_chains()))
chain = chains[0]

operator_unit = np.array([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
])

theta = math.pi/3
operator_rotate_x = np.array([
  [1, 0, 0],
  [0, math.cos(theta), - math.sin(theta)],
  [0, math.sin(theta), math.cos(theta)]
])

operator_rotate_z = np.array([
  [math.cos(theta), - math.sin(theta), 0],
  [math.sin(theta), math.cos(theta), 0],
  [0, 0, 1]
])

new_chain = chain * operator_rotate_z
print(new_chain)
structure.add(new_chain)