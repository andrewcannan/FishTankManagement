import pytest
from fish_tank.fish import Goldfish, Angelfish, Babelfish
from fish_tank.tank import FishTank


def test_initial_tank():
    tank = FishTank()
    assert len(tank.fish_list) == 0
    assert tank.days_until_cleaning == 30
    assert tank.fish_types == {
            'Goldfish': Goldfish,
            'Angelfish': Angelfish,
            'Babelfish': Babelfish
        }
    assert tank.food_required() == 0.0
    
def test_add_fish():
    tank = FishTank()
    goldie = Goldfish('Goldie')
    tank.add_fish(goldie)
    assert len(tank.fish_list) == 1
    assert tank.days_until_cleaning == 29
    assert tank.fish_list[0].name == 'Goldie'
    assert tank.fish_list[0].food_required() == 0.1
    
def test_add_multiple_fish():
    tank = FishTank()
    goldie = Goldfish('Goldie')
    angel = Angelfish('Angel')
    tank.add_fish(goldie)
    tank.add_fish(angel)
    assert len(tank.fish_list) == 2
    assert tank.food_required() == goldie.food_required() + angel.food_required()
    
def test_add_fish_type():
    tank = FishTank()
    tank.add_fish_type('Clownfish', 0.4)
    assert 'Clownfish' in tank.fish_types
    
def test_add_duplicate_fish_type():
    tank = FishTank()
    tank.add_fish_type('Clownfish', 0.4)
    with pytest.raises(ValueError) as excinfo:
        tank.add_fish_type('Clownfish', 0.5)
    assert str(excinfo.value) == 'Fish type Clownfish already exists.'
    
def test_add_fish_of_new_type():
    tank = FishTank()
    tank.add_fish_type('Clownfish', 0.4)
    Clownfish = tank.fish_types['Clownfish']
    nemo = Clownfish('Nemo')
    tank.add_fish(nemo)
    assert len(tank.fish_list) == 1
    assert tank.fish_list[0].name == 'Nemo'
    assert tank.fish_list[0].food_required() == 0.4
    
def test_sum_of_food_required():
    tank = FishTank()
    goldie = Goldfish('Goldie')
    angel = Angelfish("Angel")
    tank.add_fish(goldie)
    tank.add_fish(angel)
    assert tank.food_required() == goldie.food_required() + angel.food_required()
    
def test_days_until_cleaning():
    tank = FishTank()
    assert tank.days_until_cleaning == 30
    goldie = Goldfish('Goldie')
    tank.add_fish(goldie)
    assert tank.days_until_cleaning == 29
    tank.fish_list.pop(0)
    tank.reset_days_until_cleaning()
    assert tank.days_until_cleaning == 30
    goldie = Goldfish('Goldie')
    angel = Angelfish('Angel')
    tank.add_fish(goldie)
    tank.add_fish(angel)
    assert tank.days_until_cleaning == 28
    tank.fish_list.pop(1)
    tank.reset_days_until_cleaning()
    assert tank.days_until_cleaning == 29

if __name__ == '__main__':
    pytest.main()