import math
from decimal import Decimal, InvalidOperation

# Test Cases
test_values = [
    0.0,
    -0.0,
    float('nan'),
    float('inf'),
    float('-inf'),
    0.1,
    0.2,
    0.1 + 0.2,  # Floating point drift (0.30000000000000004)
    0.3,        # Exact decimal
    0.5,        # Exact binary fraction
    0.875,      # Exact binary fraction
    1e-300,     # Subnormal/very small
    1.00005,    # Rounding boundary for 10000
    1.00004,    # Rounding boundary for 10000
]

def check_basis_points(v):
    if math.isnan(v) or math.isinf(v): return "REJECT"
    return int(round(v * 10000))

def check_millionths(v):
    if math.isnan(v) or math.isinf(v): return "REJECT"
    return int(round(v * 1000000))

def check_decimal_serialization(v):
    if math.isnan(v) or math.isinf(v): return "REJECT"
    try:
        # repr(float) to str to Decimal
        return str(Decimal(str(v)))
    except InvalidOperation:
        return "ERROR"

def check_fixed_point_string(v, places=4):
    if math.isnan(v) or math.isinf(v): return "REJECT"
    # Note: string formatting uses bankers rounding or standard?
    return f"{v:.{places}f}"

def check_rational(v):
    if math.isnan(v) or math.isinf(v): return "REJECT"
    # Using as_integer_ratio() gives exact representation
    return v.as_integer_ratio()

print(f"{'Float':<25} | {'Basis Pts':<10} | {'Millionths':<12} | {'Decimal Str':<22} | {'Fixed Str':<10} | {'Rational'}")
print("-" * 110)
for v in test_values:
    bp = check_basis_points(v)
    mp = check_millionths(v)
    ds = check_decimal_serialization(v)
    fs = check_fixed_point_string(v, 4)
    rt = check_rational(v)
    
    # Handle -0.0 explicitly for display
    v_repr = repr(v)
    if v == 0.0 and math.copysign(1, v) == -1:
        v_repr = "-0.0"
        
    print(f"{v_repr:<25} | {str(bp):<10} | {str(mp):<12} | {str(ds):<22} | {str(fs):<10} | {str(rt)}")

