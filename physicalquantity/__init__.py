#!/usr/bin/python3
import json

ISO_UNITS = {
  "one":       {},
  "metre":     {"dimensions": {"length": 1}},
  "kg":        {"dimensions": {"mass": 1}},
  "second":    {"dimensions": {"time": 1}},
  "ampere":    {"dimensions": {"current": 1}},
  "kelvin":    {"dimensions": {"temperature": 1}},
  "mole":      {"dimensions": {"substance": 1}},
  "candela":   {"dimensions": {"intensity": 1}},
  "hertz":     {"dimensions": {"time": -1}},
  "newton":    {"dimensions": {"length": 1, "mass": 1, "time": -2}},
  "pascal":    {"dimensions": {"length": -1, "mass": 1, "time": -2}},
  "joule":     {"dimensions": {"length": 2, "mass": 1, "time": -2}},
  "watt":      {"dimensions": {"length": 2, "mass": 1, "time": -3}},
  "coulomb":   {"dimensions": {"current": 1, "time": 1}},
  "volt":      {"dimensions": {"length": 2, "mass": 1, "time": -3, "current": -1}},
  "ohm":       {"dimensions": {"length": 2, "mass": 1, "time": -3, "current": -2}},
  "siemens":   {"dimensions": {"length": -2, "mass": -1, "time": 3, "current": 2}},
  "farad":     {"dimensions": {"length": -2, "mass": -1, "time": 4, "current": 2}},
  "tesla":     {"dimensions": {"mass": 1, "time": -2, "current": -1}},
  "weber":     {"dimensions": {"length": 2, "mass": 1, "time": -2, "current": -1}},
  "henry":     {"dimensions": {"length": 2, "mass": 1, "time": -2, "current": -2}},
  "lux":       {"dimensions": {"intensity": 1, "length": -2}},
  "grey":      {"dimensions": {"length": 2, "time": -2}},
  "m2":        {"dimensions": {"length": 2}},
  "m3":        {"dimensions": {"length": 3}},
}

NONAME_UNITS = {
  "velocity":       {"dimensions": {"length": 1, "time": -1}},
  "acceleration":   {"dimensions": {"length": 1, "time": -2}},
  "wavenumber":     {"dimensions": {"length": -1}},
  "density":        {"dimensions": {"mass": 1, "length": -3}},
  "surfacedensity": {"dimensions": {"mass": 1, "length": -2}},
  "specificvolume": {"dimensions": {"mass": -1, "length": 3}},
  "currentdensity": {"dimensions": {"current": 1, "length": -2}},
  "magneticfieldstrength": {"dimensions": {"current": 1, "length": -1}},
  "concentration":  {"dimensions": {"substance": 1, "length": -3}},
  "massconcentration": {"dimensions": {"mass": 1, "length": -3}},
  "luminance": {"dimensions": {"intensity": 1, "length": -2}},
}

TRANSPOSED_UNITS = {
  "degrees":   {"scale": 0.017453292},
  "foot":      {"dimensions": {"length": 1}, "scale": 0.3048},
  "inch":      {"dimensions": {"length": 1}, "scale": 0.0254},
  "mile":      {"dimensions": {"length": 1}, "scale": 1609.344},
  "yard":      {"dimensions": {"length": 1}, "scale": 0.9144},
  "au":        {"dimensions": {"length": 1}, "scale": 149597870700},
  "lightyear": {"dimensions": {"length": 1}, "scale": 9460730472580000},
  "parsec":    {"dimensions": {"length": 1}, "scale": 30856775812799588},
  "gram":      {"dimensions": {"mass": 1}, "scale": 0.001},
  "pound":     {"dimensions": {"mass": 1}, "scale": 0.45359},
  "ounce":     {"dimensions": {"mass": 1}, "scale": 0.02835},
  "minute":    {"dimensions": {"time": 1}, "scale": 60},
  "hour":      {"dimensions": {"time": 1}, "scale": 3600},
  "day":       {"dimensions": {"time": 1}, "scale": 86400},
  "year":      {"dimensions": {"time": 1}, "scale": 31557600},
  "celcius":   {"dimensions": {"temperature": 1}, "offset": 273.15},
  "fahrenheid":{"dimensions": {"temperature": 1}, "offset": 255.3722, "scale": 0.5555555556},
  "are":       {"dimensions": {"length": 2}, "scale": 100},
  "hectare":   {"dimensions": {"length": 2}, "scale": 10000},
  "acre":      {"dimensions": {"length": 2}, "scale": 4046.86},
  "barn":      {"dimensions": {"length": 2}, "scale": 0.0000000000000000000000000001},
  "litre":     {"dimensions": {"length": 3}, "scale": 0.001},
  "barrel":    {"dimensions": {"length": 3}, "scale": 0.158987294928},
  "gallon":    {"dimensions": {"length": 3}, "scale": 0.003785411784},
  "pint":      {"dimensions": {"length": 3}, "scale": 0.000473176473}
}

UNIT_ALIAS = {
    "one": ["number", "radians", "dimentionless", "steradian"],
    "metre": ["meter", "meters","metres", "length", "m"],
    "foot": ["feet","ft"],
    "candela": ["intencity", "lumen", "illuminance"],
    "au": ["astronomicalunit"],
    "gram": ["g"],
    "kg": ["weight"],
    "pound": ["lbs", "lb", "pounds"],
    "ounce": ["oz"],
    "second": ["time", "seconds", "sec"],
    "minute": ["minutes","min"],
    "hour": ["hr"],
    "day": ["dy"],
    "year": ["yr"],
    "ampere": ["current", "amp"],
    "kelvin": ["temperature"],
    "hertz": ["frequency","becquerel", "hz"],
    "newton": ["force"],
    "pascal": ["stress", "pressure", "pa"],
    "joule": ["energy", "work", "heat"],
    "watt": ["power"],
    "coulomb": ["charge"],
    "volt": ["potential"],
    "ohm": ["resistance"],
    "farad": ["capacitance"],
    "tesla": ["fluxdensity"],
    "weber": ["flux"],
    "henry": ["inductance"],
    "lux": ["illuminance"],
    "grey": ["absorbedradiation", "sievert"],
    "m2": ["squaremetre"],
    "m3": ["cubicmetre"],
    "litre": ["liter"]
}

ISO_PREFIX = {
  "yotta": 1000000000000000000000000,
  "zetta": 1000000000000000000000,
  "exa":   1000000000000000000,
  "peta":  1000000000000000,
  "tera":  1000000000000,
  "giga":  1000000000,
  "mega":  1000000,
  "kilo":  1000,
  "hecto": 100,
  "deca":  10,
  "deci":  0.1,
  "centi": 0.01,
  "mili":  0.001,
  "micro": 0.000001,
  "nano":  0.000000001,
  "pico":  0.000000000001,
  "femto": 0.000000000000001,
  "atto":  0.000000000000000001,
  "zepto": 0.000000000000000000001,
  "yocto": 0.000000000000000000000001
}

def _name_to_unit(name):
    offset = 0.0
    scale = 1.0
    rescale = 1.0
    unit_name = name
    uses_prefix = False
    full_prefix = ""
    fullname = name
    for prefix,scale in ISO_PREFIX.items():
        if name.startswith(prefix):
            name = name[len(prefix):]
            rescale *= scale
            full_prefix += prefix
    if name in ISO_UNITS:
        unit = ISO_UNITS[name]
        unit_name = fullname
    elif name in TRANSPOSED_UNITS:
        unit = TRANSPOSED_UNITS[name]
        unit_name = fullname
    else:
        unit = None
        for key, value in UNIT_ALIAS.items():
            if name in value:
                if key in ISO_UNITS:
                    unit = ISO_UNITS[key]
                    unit_name = full_prefix + key
                elif key in TRANSPOSED_UNITS:
                    unit = TRANSPOSED_UNITS[name]
                    unit_name = full_prefix + key
                else:
                    raise RuntimeError("Invalid unit name for physical quantity")
    if unit is None:
        if fullname in NONAME_UNITS:
            unit = NONAME_UNITS[fullname]
            unit_name = None
        else:
            raise RuntimeError("Invalid unit name for physical quantity")
    if "scale" in unit:
        scale = unit["scale"] * rescale
    else:
        scale = rescale
    if "offset" in unit:
        offset = unit["offset"]
    dimensions = []
    dims = {}
    if "dimensions" in unit:
        dims = unit["dimensions"]
    for dimension in ["length",
                      "mass",
                      "time",
                      "current",
                      "temperature",
                      "substance",
                      "intensity"]:
        if dimension in dims:
            dimensions.append(dims[dimension])
        else:
            dimensions.append(0)
    unit["dim_array"] = dimensions
    unit["unit_name"] = unit_name
    unit["offset"] = offset
    unit["scale"] = scale
    return unit

def _find_si_name(dimarr):
    for key, val in ISO_UNITS.items():
        dimensions = {}
        dimension_array = []
        if "dimensions" in val:
            dimensions = val["dimensions"]
        for dimension in ["length",
                          "mass",
                          "time",
                          "current",
                          "temperature",
                          "substance",
                          "intensity"]:
            if dimension in dimensions:
                dimension_array.append(dimensions[dimension])
            else:
                dimension_array.append(0)
        if dimarr == dimension_array:
            return key
    return None

class PhysicalQuantity:
    def __init__(
            self,
            value,
            name="one",
            dimensions=None):
        self.value = value
        self.offset = 0.0
        self.scale = 1.0
        if name is None and dimensions is not None:
            self.dimensions = dimensions
            self.unit_name = None
            return
        unit = _name_to_unit(name)
        self.unit_name = unit["unit_name"] 
        self.scale = unit["scale"]
        self.offset = unit["offset"]
        self.dimensions = unit["dim_array"]

    def normalized(self):
        si_name = _find_si_name(self.dimensions)
        if si_name is None:
            return PhysicalQuantity(self.value * self.scale + self.offset, None, self.dimensions)
        return PhysicalQuantity(self.value * self.scale + self.offset, si_name)

    def __mul__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        result_dimensions = [x + y for (x, y) in zip(selfn.dimensions, othern.dimensions)]
        result_value = selfn.value * othern.value
        si_name = _find_si_name(result_dimensions)
        if si_name is None:
            return PhysicalQuantity(result_value, None, result_dimensions)
        return PhysicalQuantity(result_value, si_name)

    def __truediv__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        result_dimensions = [x - y for (x, y) in zip(selfn.dimensions, othern.dimensions)]
        result_value = selfn.value / othern.value
        si_name = _find_si_name(result_dimensions)
        if si_name is None:
            return PhysicalQuantity(result_value, None, result_dimensions)
        return PhysicalQuantity(result_value, si_name)

    def __add__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        if selfn.dimensions != othern.dimensions:
            raise RuntimeError("Can't add up physical quantities with non-matching units")
        if selfn.unit_name is None:
            return PhysicalQuantity(selfn.value + othern.value, None, selfn.dimensions)
        else:
            return PhysicalQuantity(selfn.value + othern.value, selfn.unit_name)

    def __sub__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        if selfn.dimensions != othern.dimensions:
            raise RuntimeError("Can't add up physical quantities with non-matching units")
        if selfn.unit_name is None:
            return PhysicalQuantity(selfn.value - othern.value, None, selfn.dimensions)
        else:
            return PhysicalQuantity(selfn.value - othern.value, selfn.unit_name)

    def __pow__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        if othern.dimensions != [0,0,0,0,0,0,0]:
            raise RuntimeError("Can only raise to a dimensionless power")

    def __eq__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        return selfn.value == othern.value and selfn.dimensions == othern.dimensions 

    def __ne__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        return selfn.value != othern.value or selfn.dimensions != othern.dimensions

    def __lt__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        return selfn.value < othern.value and selfn.dimensions == othern.dimensions

    def __gt__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        return selfn.value > othern.value and selfn.dimensions == othern.dimensions

    def __le__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        return selfn.value <= othern.value and selfn.dimensions == othern.dimensions

    def __ge__(self, other):
        selfn = self.normalized()
        othern = other.normalized()
        return selfn.value >= othern.value and selfn.dimensions == othern.dimensions

    def as_absolute(self, name):
        unit = _name_to_unit(name)
        if self.dimensions != unit["dim_array"]:
            raise RuntimeError("Unit mismatch for absolute cast")
        nself = self.normalized()
        return PhysicalQuantity((nself.value - unit["offset"]) / unit["scale"], name)

    def as_relative(self, name):
        unit = _name_to_unit(name)
        if self.dimensions != unit["dim_array"]:
            raise RuntimeError("Unit mismatch for absolute cast")
        nself = self.normalized()
        return PhysicalQuantity(nself.value / unit["scale"], name)
       
    def same_dimensions(self, name):
        unit = _name_to_unit(name)
        return self.dimensions == unit["dim_array"]

    def json(self):
        result = {}
        result["value"] = self.value
        if self.unit_name is None:
            result["unit"] = {}
            result["unit"]["dimensions"] = self.dimensions
            if self.scale != 1.0:
                result["unit"]["scale"] = self.scale
            if self.offset != 0.0:
                result["unit"]["offset"] = self.offset
        else:
            result["unit"] = self.unit_name
        return json.dumps(result, indent=4, sort_keys=True)


