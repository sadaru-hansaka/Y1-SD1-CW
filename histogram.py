from graphics import *

def graph():
    win = GraphWin("Histogram", 500, 450)
    win.setBackground("white")

    aLine = Line(Point(20,350), Point(480,350))
    aLine.draw(win)

    # 4 bars
    bar1 = Rectangle(Point(60, 350), Point(150, 200))
    bar1.setFill(color_rgb(203, 255, 169))
    bar1.draw(win)

    bar2 = Rectangle(Point(160, 350), Point(250, 320))
    bar2.setFill(color_rgb(97, 130, 100))
    bar2.draw(win)

    bar3 = Rectangle(Point(260, 350), Point(350, 320))
    bar3.setFill(color_rgb(137, 185, 173))
    bar3.draw(win)

    bar4 = Rectangle(Point(360, 350), Point(450, 320))
    bar4.setFill(color_rgb(255, 197, 197))
    bar4.draw(win)


    #bar names
    label1 = Text(Point(105, 370), "Progress")
    label1.draw(win)

    label2 = Text(Point(210, 370), "Trailer")
    label2.draw(win)

    label3 = Text(Point(305, 370), "Retriever")
    label3.draw(win)

    label4 = Text(Point(405, 370), "Excluded")####
    label4.draw(win)

    #topic
    topic=Text(Point(250,40),"Histogram Result")
    topic.draw(win)
    topic.setFace("times roman")
    topic.setSize(18)
    topic.setStyle("bold")

    win.getMouse()
    win.close()
