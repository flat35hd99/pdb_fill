# def hoge (self, other):
#     # other is int, float, numpy
#     if (type(other) == "int" || type(other) == "float64"):
#         coord = self.get_coord
#         new_coord = coord * other
#         new_atom = copy(self)
#         new_atom.set_coord(new_coord)
#         return new_atom
#     if (type(other) == "numpy.ndarray"):
#         # process
#         return new_atom

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

atoms = np.array(list(structure.get_atoms()))
atom = atoms[0]
atom.set_coord(np.array([1,1,1]))

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

new_atom_operated_by_unit = atom * operator_unit
new_atom_operated_by_rotate_x = atom * operator_rotate_x
new_atom_operated_by_rotate_z = atom * operator_rotate_z

print(new_atom_operated_by_unit.get_coord())
print(new_atom_operated_by_rotate_x.get_coord())
print(new_atom_operated_by_rotate_z.get_coord())