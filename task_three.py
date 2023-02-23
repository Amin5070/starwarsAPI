"""
1. TODO - import all resource classes here -> Done
2. TODO - get count of each resource       -> Done
3. TODO - get singular resource URL from each resource
    - for example,
    - hit plural URL of starships and that will list all starships data
    - iterate on each starship data and capture singular URLs
    - all_starship_data = data.get("results")
    - you will iterate on `all_starship_data`,
4. TODO - pull data from random 3 "singular" resource URLs
    - utilize`utils` package to produce random 3 numbers from resource ids
    - and pull data for them
5. TODO - convert the script into CLI application
6. TODO - pretty print output (from pprint import pprint)
"""

from pprint import pprint

from resources.s_characters import Character
from resources.s_films import Film
from resources.s_planets import Planet
from resources.s_species import Specie
from resources.s_starships import Starship
from resources.s_vehicles import Vehicle

# pydentic classes

from models.datamodels.characters import Characters
from models.datamodels.films import Films
from models.datamodels.planets import Planets
from models.datamodels.species import Species
from models.datamodels.starships import Starships
from models.datamodels.vehicles import Vehicles

if __name__ == "__main__":
    people_object = Character()
    total_people = people_object.get_count()
    print(f"Total people: {total_people}")
    pe_urls = people_object.get_resource_urls()
    pprint(f"people url = {pe_urls}")
    people_data = people_object.get_sample_data()
    people_data = Characters(**people_data)
    pprint(people_object.pull_random_data())
    print("*" * 50, "\n")

    film_object = Film()
    total_films = film_object.get_count()
    print(f"Total films: {total_films}")
    urls = film_object.get_resource_urls()
    pprint(f"film url = {urls}")
    film_data = film_object.get_sample_data()
    film_data = Films(**film_data)
    pprint(film_object.pull_random_data())
    print("*"*50,"\n")

    planet_object = Planet()
    total_planets = planet_object.get_count()
    print(f"Total planets: {total_planets}")
    pl_urls = planet_object.get_resource_urls()
    pprint(f"planet url = {pl_urls}")
    planet_data = planet_object.get_sample_data()
    planet_data = Planets(**planet_data)
    pprint(planet_object.pull_random_data())
    print("*" * 50, "\n")

    species_object = Specie()
    total_species = species_object.get_count()
    print(f"Total species: {total_species}")
    sp_urls = species_object.get_resource_urls()
    pprint(f"species url = {sp_urls}")
    species_data = species_object.get_sample_data()
    species_data = Species(**species_data)
    pprint(species_object.pull_random_data())
    print("*" * 50, "\n")

    starships_object = Starship()
    total_starships = starships_object.get_count()
    print(f"Total starships: {total_starships}")
    st_urls = starships_object.get_resource_urls()
    pprint(f"starships url = {st_urls}")
    starships_data = starships_object.get_sample_data(id_ = 9)
    starships_data = Starships(**starships_data)
    pprint(starships_object.pull_random_data())

    vehicle_object = Vehicle()
    total_vehicle = vehicle_object.get_count()
    print(f"Total vehicle: {total_vehicle}")
    vehicle_data = vehicle_object.get_sample_data(id_=4)
    vehicle_data = Vehicles(**vehicle_data)
    pprint(vehicle_object.pull_random_data())
    print("*" * 50, "\n")

breakpoint()