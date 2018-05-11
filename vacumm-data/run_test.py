import sys
import os

print(os.path.join(sys.prefix, 'share', 'vacumm'))

assert os.path.isdir(os.path.join(sys.prefix, 'share', 'vacumm'))
