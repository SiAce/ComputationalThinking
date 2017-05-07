from Tkinter import *

def draw(c, position, high, low):
    y1 = (high + low) / 10
    y2 = low / 10
    c.create_rectangle(position, 400 - y1, position + 50, 400 - y2, fill = "lightblue" )
    c.create_rectangle(position, 400 - y2, position + 50, 400, fill = "lightgreen" )


def main():

    degree_high, degree_low, no_degree_high, no_degree_low = 0, 0, 0, 0
    white_high, white_low, not_white_high, not_white_low = 0, 0, 0, 0
    male_high, male_low, female_high, female_low = 0, 0, 0, 0

    f = open("data.txt", "r")
    data = []
    line = f.readline()
    while line != "":
        data.append(line.split(", "))
        line = f.readline()
    f.close()

    for person in data:

        if person[3] == "Bachelors" or person[3] == "Masters" or person[3] == "Doctorate":
            if person[14] == ">50K.\n":
                degree_high += 1
            else:
                degree_low += 1
        else:
            if person[14] == ">50K.\n":
                no_degree_high += 1
            else:
                no_degree_low += 1

        if person[8] == "White":
            if person[14] == ">50K.\n":
                white_high += 1
            else:
                white_low += 1
        else:
            if person[14] == ">50K.\n":
                not_white_high += 1
            else:
                not_white_low += 1

        if person[9] == "Male":
            if person[14] == ">50K.\n":
                male_high += 1
            else:
                male_low += 1
        else:
            if person[14] == ">50K.\n":
                female_high += 1
            else:
                female_low += 1

    r = Tk()
    c = Canvas(r, width = 600, height = 500, bg = "white")
    c.pack()

    draw(c, 100, degree_high, degree_low)
    draw(c, 150, no_degree_high, no_degree_low)
    draw(c, 250, white_high, white_low)
    draw(c, 300, not_white_high, not_white_low)
    draw(c, 400, male_high, male_low)
    draw(c, 450, female_high, female_low)

    r.mainloop()

main()