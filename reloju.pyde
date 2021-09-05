m = 0
n = 0
o = 0
def setup ():
    size (300, 300)
def draw():
    background(255)
    background(110)
    global m
    global n
    global o
    fill(18, 250, 124)
    circle(27, m, 50)
    if m > height:
       m = 0
    else:
       m = map(second(), 0, 59, 0, height)
    fill(106, 18, 250)
    circle(145, n, 70)
    if n > height:
       n = 0
    else:
       n = map(minute(), 0, 59, 0, height)
    fill(218, 250, 18)
    circle(257, n, 80)
    if o > height:
       o = 0
    else:
       o = map(hour(), 0, 59, 0, height)
