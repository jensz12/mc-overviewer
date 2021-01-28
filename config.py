# -*- coding: utf-8 -*-

end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]

# Define the path to your world here. 'Lobby' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['Lobby'] = "C:/Users/jens/Downloads/map/map/lobby"

# Define where to put the output.
outputdir = "C:/Users/jens/Downloads/map/completed"

# Dag med Smooth Lightning
renders["overworld"] = {
    "world": "Lobby",
    "title": "Dag",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}
# Overworld caves
renders["cave"] = {
    "world": "Lobby",
    "title": "Cave",
    "rendermode": cave,
    "dimension": "overworld",
}
# Overworld nat
renders["night"] = {
    "world": "Lobby",
    "title": "Nat",
    "rendermode": smooth_night,
    "dimension": "overworld",
}
