import cairo
import math 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)

# Create a context object
ctx = cairo.Context(surface)

# Set the background color to gray
ctx.set_source_rgb(0, 0, 0)
ctx.paint()

ctx.arc(300, 200, 150, 0, 2*math.pi)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.fill()

ctx.arc(300, 200, 125, 0, 2*math.pi)
ctx.set_source_rgb(192/255, 192/255, 192/255)
ctx.set_line_width(10)
ctx.fill()

ctx.arc(300, 200, 100, 0, 2*math.pi)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.fill()

ctx.arc(300, 200, 75, 0, 2*math.pi)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.fill()

ctx.arc(300, 200, 75, 0, 2*math.pi)
ctx.set_source_rgb(0, 0, 1)
ctx.set_line_width(10)
ctx.fill()

ctx.move_to(300, 125)
ctx.line_to(350, 255)
ctx.line_to(230, 180)
ctx.line_to(370, 180)
ctx.line_to(250, 255)
ctx.close_path()
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.set_line_width(5)
ctx.set_line_cap (cairo.LINE_CAP_ROUND)
ctx.fill()
surface.write_to_png("CP.png")




