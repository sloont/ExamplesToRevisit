destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = destinations.index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)

attractions = [[] for i in destinations]


# function for adding new attractions to list

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
    except ValueError:
        print('destination not registered')
        return
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return


# adding attractions to list

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# function to find attractions based on interests and destination

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for i in range(len(attractions_in_city)):
        possible_attraction = attractions_in_city[i]
        attraction_tags = possible_attraction[1]
        for j in range(len(interests)):
            for k in range(len(attraction_tags)):
                if interests[j] == attraction_tags[k]:
                    attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest


la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)


#

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    for i in range(len(traveler_attractions)):
        interests_string += "the " + traveler_attractions[i]
    interests_string += "."

    return interests_string


dereck = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(dereck)
