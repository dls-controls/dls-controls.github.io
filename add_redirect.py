import sys
import os
from pathlib import Path

REDIRECT = """\
<!DOCTYPE html>
<html>
  <head>
    <title>Redirecting to pythonSoftIOC</title>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=%(path)s">
    <link rel="canonical" href="%(path)s">
  </head>
</html>
"""

# python3 add_redirect.py pythonIoc pythonSoftIOC
old_repo = sys.argv[1]
new_repo = sys.argv[2]

os.chdir(Path(__file__).parent / old_repo)
for root, dirs, files in os.walk("."):
  for fname in files:
    if fname.endswith(".html"):
      path = Path("..", *[".." for _ in Path(root).parts]) / new_repo / root / fname
      with open(Path(root) / fname, "w") as f:
        f.write(REDIRECT % locals())
