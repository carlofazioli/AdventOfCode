import glob
import pytest


from fuel import FuelCalculator


# Find examples and results:
examples1 = sorted(glob.glob('tests/example1.*'))
results1 = sorted(glob.glob('tests/result1.*'))

examples2 = sorted(glob.glob('tests/example2.*'))
results2 = sorted(glob.glob('tests/result2.*'))

print(examples1)
print(results1)

# Run tests
@pytest.mark.parametrize('input_f, output_f', list(zip(examples1, results1)))
def test_day1(input_f, output_f):
    fcalc = FuelCalculator(source=input_f)
    output = fcalc.req()
    with open(output_f) as f:
        target = int(f.read().strip('\n'))
    assert output == target

@pytest.mark.parametrize('input_f, output_f', list(zip(examples2, results2)))
def test_day2(input_f, output_f):
    fcalc = FuelCalculator(source=input_f)
    output = fcalc.full_req()
    with open(output_f) as f:
        target = int(f.read().strip('\n'))
    assert output == target
