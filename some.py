import rename
import vals

re = rename.Rename()


re.set_path('./classes')
#re.set_extension(['.mp4', '.docs'])
re.ignore_extension()
#re.set_pattern(vals.FORMAT_PATTERN)
re.ignore_pattern()

re.numerical_acs(suffix='class', seperator='_', prefix='some')
