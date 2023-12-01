# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: ……………………..…
# Date: ……………………..…


#import graphics.py library
from graphics import *

#histogram
def graph(progress,trailer,retriever,exclude,outcome_count):
    win = GraphWin("Histogram", 500, 450) #500*450px

    X_axiss = Line(Point(20,350), Point(480,350)) #base line of chart
    X_axiss.draw(win)

    # progress column
    progress_bar = Rectangle(Point(60,350), Point(150,(350-progress*10)))#create a rectangle
    progress_bar.setFill(color_rgb(99,126,118))  #fill with a colur
    progress_bar.draw(win)

    progress_tag = Text(Point(105,370), "Progress") #create "progress" text
    progress_tag.draw(win)

    progress_count=Text(Point(108,(340-(progress*10))),"progress") #diaplay the number of count above the column
    progress_count.draw(win)
    progress_count.setText(f"{progress}")#set the count
#---------------------------------------------------------------------------------------
    #trailer column
    trailer_bar = Rectangle(Point(160,350), Point(250,(350-trailer*10)))
    trailer_bar.setFill(color_rgb(198,151,116))
    trailer_bar.draw(win)

    trailer_tag = Text(Point(210,370), "Trailer")
    trailer_tag.draw(win)

    trailer_count=Text(Point(213,(340-(trailer*10))),"progress")
    trailer_count.draw(win)
    trailer_count.setText(f"{trailer}")
#------------------------------------------------------------------------------
    #retriever column
    retriever_bar = Rectangle(Point(260,350), Point(350,(350-retriever*10)))
    retriever_bar.setFill(color_rgb(121,172,120))
    retriever_bar.draw(win)

    retriever_tag = Text(Point(305,370), "Retriever")
    retriever_tag.draw(win)

    retriever_count=Text(Point(308,(340-(retriever*10))),"progress")
    retriever_count.draw(win)
    retriever_count.setText(f"{retriever}")
#-------------------------------------------------------------------------
    #exclude column
    exclude_bar = Rectangle(Point(360,350), Point(450, (350-exclude*10)))
    exclude_bar.setFill(color_rgb(192,238,204))
    exclude_bar.draw(win)

    exclude_tag = Text(Point(405,370), "Excluded")
    exclude_tag.draw(win)

    exclude_count=Text(Point(408,(340-(exclude*10))),"progress")
    exclude_count.draw(win)
    exclude_count.setText(f"{exclude}")
#---------------------------------------------------------------------------------------
    #topic "Histogram result"
    topic=Text(Point(250,40),"Histogram Result")
    topic.draw(win)
    topic.setFace("times roman") #font
    topic.setSize(18) #text size
    topic.setStyle("bold") #text bold

    #number of outcome text
    number_of_outcomes = Text(Point(145,410),"X outcomes in total") # assign count to X
    number_of_outcomes.draw(win)
    number_of_outcomes.setStyle("bold")
    number_of_outcomes.setSize(18)
    number_of_outcomes.setText(f"{outcome_count} outcomes in total")

    win.getMouse()
    win.close()