import cairo

# Set up pycairo
surface = cairo. ImageSurface (cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Bezier curve
ctx.move_to(50, 200)
ctx.curve_to(200, 350, 200, 100, 350, 250) 
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png("bezier.png")