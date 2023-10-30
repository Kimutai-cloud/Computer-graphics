import cairo # originally it was pycairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400) # originaly it was cairo.Format instead of cairo.FORMAT
ctx =cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.rectangle(150, 100, 100, 240)# originally it was cairo.square 
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

surface.write_to_png("q2.png")