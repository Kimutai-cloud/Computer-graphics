import cairo

# Set up surface
surface = cairo. ImageSurface (cairo. FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()
# Set line color and width
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(20)
# Butt Cap
ctx.move_to(100, 80)
ctx.line_to(500, 80) 
ctx.set_line_cap (cairo.LINE_CAP_BUTT)
ctx.stroke()
# Square Cap
ctx.move_to(100, 200)
ctx.line_to(500, 200)
ctx.set_line_cap (cairo.LINE_CAP_SQUARE)
ctx.stroke()
# Round Cap
ctx.move_to(100, 320)
ctx.line_to(500, 320)
ctx.set_line_cap (cairo.LINE_CAP_ROUND)
ctx.stroke()

surface.write_to_png("line.png")