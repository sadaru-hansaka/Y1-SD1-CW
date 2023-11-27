from graphics import *

#histogram
def graph(progress,trailer,retriever,exclude,outcome_count):
    win = GraphWin("Histogram", 500, 450)

    straight_Line = Line(Point(20,350), Point(480,350)) #base line of chart
    straight_Line.draw(win)

    # progress, trailer , exclude , retriever  bars
    progress_bar = Rectangle(Point(60, 350), Point(150, (350-progress*20)))
    progress_bar.setFill(color_rgb(203, 255, 169))
    progress_bar.draw(win)

    trailer_bar = Rectangle(Point(160, 350), Point(250, (350-trailer*20)))
    trailer_bar.setFill(color_rgb(97, 130, 100))
    trailer_bar.draw(win)

    retriever_bar = Rectangle(Point(260, 350), Point(350, (350-retriever*20)))
    retriever_bar.setFill(color_rgb(137, 185, 173))
    retriever_bar.draw(win)

    exclude_bar = Rectangle(Point(360, 350), Point(450, (350-exclude*20)))
    exclude_bar.setFill(color_rgb(255, 197, 197))
    exclude_bar.draw(win)


    #bar names
    progress_label = Text(Point(105, 370), "Progress")
    progress_label.draw(win)

    trailer_label = Text(Point(210, 370), "Trailer")
    trailer_label.draw(win)

    retriever_label = Text(Point(305, 370), "Retriever")
    retriever_label.draw(win)

    exclude_label = Text(Point(405, 370), "Excluded")####
    exclude_label.draw(win)

    #topic 
    topic=Text(Point(250,40),"Histogram Result")
    topic.draw(win)
    topic.setFace("times roman")
    topic.setSize(18)
    topic.setStyle("bold")

    #number of outcome text
    num_outcomes = Text(Point(145,410),"X outcomes in total") # assign count to X
    num_outcomes.draw(win)
    num_outcomes.setStyle("bold")
    num_outcomes.setSize(18)
    num_outcomes.setText(f"{outcome_count} outcomes in total")

    #counts of progress,trailer,retriever and exclude
    progress_count=Text(Point(108,(340-(progress*20))),"progress")
    progress_count.draw(win)
    progress_count.setText(f"{progress}")

    trailer_count=Text(Point(213,(340-(trailer*20))),"progress")
    trailer_count.draw(win)
    trailer_count.setText(f"{trailer}")

    retriever_count=Text(Point(308,(340-(retriever*20))),"progress")
    retriever_count.draw(win)
    retriever_count.setText(f"{retriever}")

    exclude_count=Text(Point(408,(340-(exclude*20))),"progress")
    exclude_count.draw(win)
    exclude_count.setText(f"{exclude}")

    win.getMouse()
    win.close()