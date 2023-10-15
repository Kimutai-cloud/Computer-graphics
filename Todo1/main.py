import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.rectangle(150, 100, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

ctx.rectangle(250, 200, 100, 240)
ctx.set_source_rgb(0, 1, 0)
ctx.stroke()

ctx.rectangle(350, 300, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

surface.write_to_png("example1.png")