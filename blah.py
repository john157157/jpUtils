import sys
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / "jpSource"))



import jp_core

print(jp_core.is_windows())







