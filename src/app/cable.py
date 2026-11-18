import ezdxf as ez
from ezdxf.addons import odafc


from pathlib import Path


class Cableplan:
    def __init__(self, lineplan: Path):
        self.lineplan = odafc.readfile(lineplan)


if __name__ == "__main__":
    cable = Cableplan(
        Path("../../tests/20250609-PRASA-KZN-PTCS D&C-RSS-ROSSBURGH-SLP-REV-A7.dwg")
    )
