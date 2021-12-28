import panel as pn
import pandas as pd

import hvplot.pandas

pn.extension('ace', sizing_mode="stretch_width")


data = pd.read_csv("panel\slideshow\index.csv", index_col="name")
gifs = [row.gif for _,row in data.iterrows()]
descriptions = [row.description for _,row in data.iterrows()]

slider = pn.widgets.DiscreteSlider(value=list(data.index)[0], options=list(data.index), max_width=800)

img = pn.pane.GIF(str(data.iloc[0]["gif"]), embed=False, height=400, sizing_mode="scale_height")
description = pn.pane.Markdown(data.iloc[0]["description"])

slider._slider.jscallback(args={'img': img, "description": description}, value=f"""
var gifs={gifs}
var descriptions={descriptions}
img.text = '<img src="' + gifs[cb_obj.value] + '" style="height:100%;object-fit: cover"></img>'
description.text = descriptions[cb_obj.value]
""")

app = pn.Column(slider, img, description, name="Output", height=550, max_width=800)

ace = pn.widgets.Ace(readonly=True, height=500, language='python', value=\
"""\
import panel as pn
import pandas as pd

pn.extension(sizing_mode="stretch_width")

data = pd.read_csv("panel\slideshow\index.csv", index_col="name")

def slideshow(index):
    return pn.Column(
        pn.pane.GIF(data.loc[index]["gif"], embed=False, sizing_mode="scale_height", height=400),
        pn.pane.Markdown(data.loc[index]["description"]),
    )

slider = pn.widgets.DiscreteSlider(options=list(data.index))
output = pn.bind(slideshow, slider)

app = pn.Column(slider, output, max_width=800)
app.servable()""", name="Code")

app1 = pn.Tabs(app, ace)
app1.servable()