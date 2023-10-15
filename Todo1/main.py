import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 500, 500)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0, 0.8, 0.8)
ctx.paint()

ctx.rectangle(150, 100, 100, 240)
ctx.fill()

surface.write_to_png("example1.png")