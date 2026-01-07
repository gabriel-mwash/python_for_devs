from molecule_class import Molecule, Atom
from typing import TextIO

def read_molecule(r: TextIO) -> Molecule:
    """ Read a single molecule from r and return it,
    or return None to signal EOF
    """

    # if there isn't another line, we're at EOF
    line = r.readline()
    if not line:
        return None

    # name of the molecule: " COMPND    name"
    key, name = line.split()

    # other lines are either "END" or "ATOM num kind x y z"
    molecule = Molecule(name)
    reading = True

    while reading:
        line = r.readline()
        if line.startswith("END"):
            reading = False
        else:
            key, num, kind, x, y, z = line.split()
            molecule.add(Atom(int(num), kind, float(x), float(y), float(z)))
    return molecule
