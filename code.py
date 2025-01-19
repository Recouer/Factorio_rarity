import numpy as np

recycler_mat = np.array([
    [1 - 0.248, 0.248 * 0.9, 0.248 * 0.09, 0.248 * 0.009, 0.248 * 0.001],
    [0, 1 - 0.248, 0.248 * 0.9, 0.248 * 0.09, 0.248 * 0.01],
    [0, 0, 1 - 0.248, 0.248 * 0.9, 0.248 * 0.1],
    [0, 0, 0, 1 - 0.248, 0.248],
    [0, 0, 0, 0, 0]
]) * 0.25

def assembler_mat(rarity_m, prod_m):
    if rarity_m + prod_m != 4:
        print(f"wrong values for the modules, sum should be at 4, but found: {rarity_m + prod_m}")
    rarity = 0.062 * rarity_m
    production = 1 + 0.25 * prod_m
    return np.array([
        [1 - rarity, rarity * 0.9, rarity * 0.09, rarity * 0.009, rarity * 0.001],
        [0, 1 - rarity, rarity * 0.9, rarity * 0.09, rarity * 0.01],
        [0, 0, 1 - rarity, rarity * 0.9, rarity * 0.1],
        [0, 0, 0, 1 - rarity, rarity],
        [0, 0, 0, 0, 1]
    ]) * production

def cryogenic_mat(rarity_m, prod_m):
    if rarity_m + prod_m != 8:
        print(f"wrong values for the modules, sum should be at 8, but found: {rarity_m + prod_m}")
    rarity = 0.062 * rarity_m
    production = 1 + 0.25 * prod_m
    return np.array([
        [1 - rarity, rarity * 0.9, rarity * 0.09, rarity * 0.009, rarity * 0.001],
        [0, 1 - rarity, rarity * 0.9, rarity * 0.09, rarity * 0.01],
        [0, 0, 1 - rarity, rarity * 0.9, rarity * 0.1],
        [0, 0, 0, 1 - rarity, rarity],
        [0, 0, 0, 0, 1]
    ]) * production

def fundry_mat(rarity_m, prod_m):
    if rarity_m + prod_m != 4:
        print(f"wrong values for the modules, sum should be at 4, but found: {rarity_m + prod_m}")
    rarity = 0.062 * rarity_m
    production = 1.5 + 0.25 * prod_m
    return np.array([
        [1 - rarity, rarity * 0.9, rarity * 0.09, rarity * 0.009, rarity * 0.001],
        [0, 1 - rarity, rarity * 0.9, rarity * 0.09, rarity * 0.01],
        [0, 0, 1 - rarity, rarity * 0.9, rarity * 0.1],
        [0, 0, 0, 1 - rarity, rarity],
        [0, 0, 0, 0, 1]
    ]) * production

def EM_Plant_mat(rarity_m, prod_m):
    if rarity_m + prod_m != 5:
        print(f"wrong values for the modules, sum should be at 5, but found: {rarity_m + prod_m}")
    rarity = 0.062 * rarity_m
    production = 1.5 + 0.25 * prod_m
    return np.array([
        [1 - rarity, rarity * 0.9, rarity * 0.09, rarity * 0.009, rarity * 0.001],
        [0, 1 - rarity, rarity * 0.9, rarity * 0.09, rarity * 0.01],
        [0, 0, 1 - rarity, rarity * 0.9, rarity * 0.1],
        [0, 0, 0, 1 - rarity, rarity],
        [0, 0, 0, 0, 1]
    ]) * production

class Resource:
    def __init__(self):
        self.resources = [1, 0, 0, 0, 0]
        self.products = [0, 0, 0, 0, 0]
        self.total = [1, 0, 0, 0, 0]
    
    def __repr__(self):
        stringy = ""
        stringy += self.resources.__repr__() + "\n"
        stringy += self.products.__repr__() + "\n"
        stringy += self.total.__repr__() + "\n"
        return stringy

    def get_ratios(self):
        total = sum(self.total)
        stringy = ""
        stringy += f"normal = {self.total[0] / total}\n"
        stringy += f"uncommon = {self.total[1] / total}\n"
        stringy += f"rare = {self.total[2] / total}\n"
        stringy += f"epic = {self.total[3] / total}\n"
        stringy += f"legendary = {self.total[4] / total}\n"
        return stringy

    def get_numbers(self, rarity):
        total = sum(self.total)
        total_list = self.total.copy()

        mult = total / total_list[rarity]
        return [(i * mult) for i in total_list] 

    
    def recycler(self):
        self.resources += sum(np.atleast_2d(self.products).T * recycler_mat)
        self.total += sum(np.atleast_2d(self.products).T * recycler_mat)
        for i in range(4):
            self.products[i] = 0
        return self

    def EM_plant(self, rarity_m, prod_m):
        self.products += sum(np.atleast_2d(self.resources).T * EM_Plant_mat(rarity_m, prod_m))
        for i in range(5):
            self.resources[i] = 0
        return self

    def fundry(self, rarity_m, prod_m):
        self.products += sum(np.atleast_2d(self.resources).T * fundry_mat(rarity_m, prod_m))
        for i in range(5):
            self.resources[i] = 0
        return self

    def cryogenic_plant(self, rarity_m, prod_m):
        self.products += sum(np.atleast_2d(self.resources).T * cryogenic_mat(rarity_m, prod_m))
        for i in range(5):
            self.resources[i] = 0
        return self

    def assembler(self, rarity_m, prod_m):
        self.products += sum(np.atleast_2d(self.resources).T * assembler_mat(rarity_m, prod_m))
        for i in range(5):
            self.resources[i] = 0
        return self


def pow(func, power, values):
    values
    for _ in range(power):
        values = func(values)
    return values

def proportion(modules):
    return 1.5 * 0.062 * modules * (1 / (1 - (1.5/4*(1 - 0.062*4)*(1-0.062*modules))))

values = Resource()
values.assembler(4, 0).fundry(4, 0)
pow(lambda x: x.fundry(4, 0).recycler(), 10, values)
print(values.__repr__())
## your method

values = Resource()
values.assembler(0, 0).fundry(0, 4)
pow(lambda x: x.fundry(4, 0).recycler(), 10, values)
print(values.__repr__())
# my method
