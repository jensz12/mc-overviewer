# -*- coding: utf-8 -*-


end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]

# Define the path to your world here. 'Zagi Single Player' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['Community Server'] = "C:/Users/jens/Downloads/map/map"

# Define where to put the output.
outputdir = "C:/Users/jens/Downloads/map/completed"

# Dag med Smooth Lightning
renders["singleoverworld"] = {
    "world": "Community Server",
    "title": "Dag",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}
# Overworld caves
renders["singlecave"] = {
    "world": "Community Server",
    "title": "Cave",
    "rendermode": cave,
    "dimension": "overworld",
}
# Overworld nat
renders["singlenight"] = {
    "world": "Community Server",
    "title": "Nat",
    "rendermode": smooth_night,
    "dimension": "overworld",
}

# Nether med Smooth Lightning
renders["singlenether"] = {
    "world": "Community Server",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}

# End
renders["singleend"] = {
    "world": "Community Server",
    "title": "End",
    "rendermode": end_smooth_lighting,
    "dimension": "end",
}
