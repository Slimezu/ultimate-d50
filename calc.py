```python
import numpy as np

print("=== Chalk Dust Graininess (D50) Calculator ===\n")

print("Remember:")
print("- Upper = Bigger size where % passing is ABOVE 50")
print("- Lower = Smaller size where % passing is BELOW 50\n")

# Input for testing
size_upper = float(input("Enter size_upper (bigger size in µm, % > 50): "))
pass_upper = float(input("Enter pass_upper (% passing > 50): "))

size_lower = float(input("\nEnter size_lower (smaller size in µm, % < 50): "))
pass_lower = float(input("Enter pass_lower (% passing < 50): "))

# The calculation (original formula)
log_d50 = np.log10(size_lower) + (50 - pass_lower) * (np.log10(size_upper) - np.log10(size_lower)) / (pass_upper - pass_lower)
d50 = 10 ** log_d50

print(f"\n✅ D50 = {d50:.2f} µm")

# Easy interpretation for chalk compression
if d50 < 8:
    print("→ Very fine dust (common in used chalk). Needs higher pressure to compress.")
elif d50 < 15:
    print("→ Fine dust. Moderate pressure should work, but may need a binder if it crumbles.")
else:
    print("→ Coarser dust. Easier to compress into solid form.")
```

