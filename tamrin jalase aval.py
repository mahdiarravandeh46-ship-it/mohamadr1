# import turtle as t
# t.speed(0)
# t.reset()
# for x in range(1, 100):
#     t.fd(100)
#     t.lt(95)

# t.reset()
# for x in range (1, 19):
#     t.fd(100)
#     if x % 2 == 0:
#         t.lt(175)
#     else:
#         t.lt(225)

import turtle as t


#  بدنه ماشین
t.reset()
t.color(1,0.6,0.1)
t.begin_fill()
t.fd(200)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(50)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(50)
t.end_fill()
# چرخ اول ماشین
t.color(1,0.4,0.1)
t.up()
t.fd(14)
t.down()
t.begin_fill()
t.circle(15)
t.end_fill()
# چرخ دوم ماشین
t.setheading(0)
t.up()
t.fd(180)
t.rt(90)
t.fd(14.5)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(15)
t.end_fill()
