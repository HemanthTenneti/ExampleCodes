# Value of series object attributes
from pandas import Series
from numpy import NaN

section = ["XIIA", "XIIB", "XIIC", "XIID"]
strength = [25, NaN, 27, 28]
StrengthSer = Series(strength, section)
print(StrengthSer)
print("-" * 75)
print(f"{'Attribute name':<20} {'Object':^20}")
print("-" * 75)
print(f"{'Index:':<20}", StrengthSer.index)
print(f"{'Values:':<20}", StrengthSer.values)
print(f"{'Datatype:':<20}", StrengthSer.dtype)
print(f"{'Object Shape:':<20}", StrengthSer.shape[0])
print(f"{'Number of bytes:':<20}", StrengthSer.nbytes)
print(f"{'n-Dimensions:':<20}", StrengthSer.ndim)
print(f"{'Size:':<20}", StrengthSer.size)
print(f"{'Has NaNs:':<20}", StrengthSer.hasnans)
print(f"{'IsEmpty:':<20}", StrengthSer.empty)
print("-" * 75)
