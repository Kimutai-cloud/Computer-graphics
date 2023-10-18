import cairo
import math 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)

# Create a context object
ctx = cairo.Context(surface)

# Set the background color to gray
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(100, 200)
ctx.curve_to(150, 300, 250, 100, 300, 200)
ctx.move_to(100, 300)
ctx.curve_to(150, 400, 250, 200, 300, 300)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png("task.png")




