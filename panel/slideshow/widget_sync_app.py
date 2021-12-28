import panel as pn
pn.extension(sizing_mode="stretch_width")

widget = pn.widgets.FloatSlider(name='FloatSlider')

pn.state.location.sync(widget, {'value': 'slider_value'})

widget.servable()
