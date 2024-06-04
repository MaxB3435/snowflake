def setup():
    size(600,600)
    
def draw():
    background(255)
    translate(100,100)
    snowflake(400,1)
    
def snowflake(sz,level):
    for i in range(3):
        segment(sz,level)
        rotate(radians(120))

def segment(sz,level):
    if level == 0:
        line(0,0,sz,0)
        translate(sz,0)
    else:
        line(o,o,sz/3.0,0)
        translate(sz/3.0,0)
        rotate(radians(-60))
        line(0,0,sz/3.0,0)
        translate(sz/3.0,0)
        rotate(radians(120))
        line(0,0,sz/3.0,0)
        translate(sz/3.0,0)
        rotate(radians(-60))
        line(0,0,3.0,0)
        translate(sz/3.0,0)
                       
                       
