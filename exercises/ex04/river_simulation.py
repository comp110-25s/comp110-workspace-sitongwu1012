"""River simulation"""

__author__: str = "730826007"

from river import River

my_river = River(num_fish=10, num_bears=2)

my_river.view_river()
my_river.one_river_week()
