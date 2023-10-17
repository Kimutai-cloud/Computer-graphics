import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 500, 500)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(50, 200)
ctx.line_to(100, 200)
ctx.line_to(150, 250)
ctx.line_to(250, 150)
ctx.line_to(350, 250)
ctx.line_to(450, 150)
ctx.line_to(500, 200)
ctx.line_to(550, 200)
ctx.close_path()
ctx.set_source_rgb(0, 1, 0)
ctx.set_line_width(10)
ctx.stroke()



surface.write_to_png("openpolygon.png")