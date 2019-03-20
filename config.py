from typing import List, Tuple

time_unit_cuts = [60, 3600, 3600 * 24]  # type: List[int]
time_units = [
    (1, 'second'),
    (60, 'minute'),
    (3600, 'hour'),
    (24 * 3600, 'day'),
]  # type: List[Tuple[int, str]]

pepper = b'Prince Oberyn Martell, commonly referred to as the Red Viper of Dorne'
secret = 'my secret key'
cookie_max_age = 600
