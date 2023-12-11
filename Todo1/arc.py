import cairo
import math

# Set up pycairo
surface =cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint

ctx.arc(250,120,30,100,math.pi)
ctx.set_source_rgb(0,1,0)
ctx.fill()

# Draw an arc
ctx.arc(200,200,150,180,math.pi)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)






ctx.move_to(200,200)
ctx.line_to(50,200)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.move_to(200,200)
ctx.line_to(110,80)
ctx.stroke()
surface.write_to_png("arc.png")