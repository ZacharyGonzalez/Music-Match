# Music-Match

## SPOTIFY WORK
Alright, Spotify Charts is a website where we can download the data we want as a CSV, but we would have to scrape the site to get the data efficiently.
They do not want people scraping their site and it seems as though we'd have to rate limit ourselves to avoid IP ban from their site.

That will require a lengthy scripts to be written. But we can use that data to form the heat map of where things are listened, and when. We can also use spotify's
actually API to cross reference the CSV's to collect the tracks metadata and do interesting things with that.

## Addition Mapping API's or Data
Gov site provides insane levels of metrics, overwhelmingly so: https://www.bls.gov/data/ 
## Future Heatmap front end 

We want the heatmap to take abstract entries and plot them accordingly, because we want many different kinds of mappings to be provided to it.
and for each complete mapping sent to the it, it should create a layer so that that specific mapping set can be toggled on or off.

query of abstract parameter CSV+Metadata -> General Map Plotting function ->  Generate generic heatmap layer


## Concepts

a heatmap can be generate by plotting songs on x, states on y. for a song, we can find out how much it was listened to for every state. That on its own will provide us states for producing a generic heatmap for EACH song.

For the states we can find out their unemployment rate and produce a heatmap form that and overlay it with the other mapping or just compute the similarities.