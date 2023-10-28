# test function to figure out package paths for imports

# link to solutions: https://stackoverflow.com/questions/62924551/python-import-module-from-within-module-in-another-subpackage

import sys
sys.path.append('/Users/tas/Documents/Python/dark_castle3')

# from dc3.class_std.invisible_class_def import Invisible
from dc3.class_std.invisible_class_def import Invisible

print("It worked!")