# Advent of Code
# Day 1
# Carlo Fazioli
# Dec 2019

class FuelCalculator:
    def __init__(self, source=None):
        # If instantiated with a set of module weights ('source'), store them.
        self.module_weights = None
        self.parse_source(source)

    def parse_source(self, source):
        if isinstance(source, str):
            # Parse a file for module weights, one per row:
            with open(source) as f:
                self.module_weights = [l.strip('\n') for l in f]
                self.module_weights = list(map(int, self.module_weights))
        if isinstance(source, list):
            self.module_weights = source
        return self.module_weights

    def req(self, source=None):
        # Compute the fuel requirements, for just the modules.
        # And also, for the modules plus the fuel requirements of the modules' fuel requirements.
        self.parse_source(source)
        req = 0
        for mod in self.module_weights:
            req += self.module_req(mod)
        return req

    def full_req(self, source=None):
        self.parse_source(source)
        full_req = 0
        for mod in self.module_weights:
            full_req += self.module_and_fuel_req(mod)
        return full_req
        

    def module_req(self, module_mass):
        # The formula for a module's fuel requirment.
        return module_mass//3 - 2

    def module_and_fuel_req(self, module_mass):
        # Recursively computing the req for the module and its fuel, and its fuel, and its...
        fuel_req = self.module_req(module_mass)
        if fuel_req < 0:
            return 0
        else:
            return fuel_req + self.module_and_fuel_req(fuel_req)
