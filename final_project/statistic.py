from Tkinter import *


def GenerateOne():
    if option.get() == 1:
        if one_variable.get() == "Education":

            bachelors, masters, doctorate, others = 0, 0, 0, 0

            for person in data:
                if person[3] == "Bachelors":
                    bachelors += 1
                elif person[3] == "Masters":
                    masters += 1
                elif person[3] == "Doctorate":
                    doctorate += 1
                else:
                    others += 1

            all = bachelors + masters + doctorate + others
            pb = 1.0 * bachelors / all
            pm = 1.0 * masters / all
            pd = 1.0 * doctorate / all
            po = 1.0 * others / all
            eb, sb = 360 * pb, 0
            em, sm = 360 * pm, eb
            ed, sd = 360 * pd, eb + em
            eo, so = 360 * po, eb + em + ed

            one_variable_canvas.delete("all")

            one_variable_canvas.create_arc(one_box, start=sb, extent=eb, fill="yellow")
            one_variable_canvas.create_arc(one_box, start=sm, extent=em, fill="green")
            one_variable_canvas.create_arc(one_box, start=sd, extent=ed, fill="blue")
            one_variable_canvas.create_arc(one_box, start=so, extent=eo, fill="gray")

            one_variable_canvas.create_rectangle((210, 50, 230, 60), fill="yellow")
            one_variable_canvas.create_text(240, 50, text="Bachelors\n%.1f%%" % (pb * 100), anchor=NW)
            one_variable_canvas.create_rectangle((210, 90, 230, 100), fill="green")
            one_variable_canvas.create_text(240, 90, text="Masters\n%.1f%%" % (pm * 100), anchor=NW)
            one_variable_canvas.create_rectangle((210, 130, 230, 140), fill="blue")
            one_variable_canvas.create_text(240, 130, text="Doctorate\n%.1f%%" % (pd * 100), anchor=NW)
            one_variable_canvas.create_rectangle((210, 170, 230, 180), fill="gray")
            one_variable_canvas.create_text(240, 170, text="Others\n%.1f%%" % (po * 100), anchor=NW)

        elif one_variable.get() == "Race":

            white, others = 0, 0

            for person in data:
                if person[8] == "White":
                    white += 1
                else:
                    others += 1

            all = white + others
            pw = 1.0 * white / all
            po = 1.0 * others / all

            ew, sw = 360 * pw, 0
            eo, so = 360 * po, ew

            one_variable_canvas.delete("all")

            one_variable_canvas.create_arc(one_box, start=sw, extent=ew, fill="yellow")
            one_variable_canvas.create_arc(one_box, start=so, extent=eo, fill="green")

            one_variable_canvas.create_rectangle((210, 50, 230, 60), fill="yellow")
            one_variable_canvas.create_text(240, 50, text="White\n%.1f%%" % (pw * 100), anchor=NW)
            one_variable_canvas.create_rectangle((210, 90, 230, 100), fill="green")
            one_variable_canvas.create_text(240, 90, text="Others\n%.1f%%" % (po * 100), anchor=NW)

        elif one_variable.get() == "Gender":

            male, female = 0, 0

            for person in data:
                if person[9] == "Male":
                    male += 1
                else:
                    female += 1

            all = male + female
            pm = 1.0 * male / all
            pf = 1.0 * female / all

            em, sm = 360 * pm, 0
            ef, sf = 360 * pf, em

            one_variable_canvas.delete("all")

            one_variable_canvas.create_arc(one_box, start=sm, extent=em, fill="yellow")
            one_variable_canvas.create_arc(one_box, start=sf, extent=ef, fill="green")

            one_variable_canvas.create_rectangle((210, 50, 230, 60), fill="yellow")
            one_variable_canvas.create_text(240, 50, text="Male\n%.1f%%" % (pm * 100), anchor=NW)
            one_variable_canvas.create_rectangle((210, 90, 230, 100), fill="green")
            one_variable_canvas.create_text(240, 90, text="Female\n%.1f%%" % (pf * 100), anchor=NW)

        elif one_variable.get() == "Income":

            high, low = 0, 0

            for person in data:
                if person[14] == ">50K.\n":
                    high += 1
                else:
                    low += 1

            all = high + low
            ph = 1.0 * high / all
            pl = 1.0 * low / all

            eh, sh = 360 * ph, 0
            el, sl = 360 * pl, eh

            one_variable_canvas.delete("all")

            one_variable_canvas.create_arc(one_box, start=sh, extent=eh, fill="yellow")
            one_variable_canvas.create_arc(one_box, start=sl, extent=el, fill="green")

            one_variable_canvas.create_rectangle((210, 50, 230, 60), fill="yellow")
            one_variable_canvas.create_text(240, 50, text=">50K\n%.1f%%" % (ph * 100), anchor=NW)
            one_variable_canvas.create_rectangle((210, 90, 230, 100), fill="green")
            one_variable_canvas.create_text(240, 90, text="<=50K\n%.1f%%" % (pl * 100), anchor=NW)


def GenerateTwo():
    if option.get() == 2:

        two_variable_canvas.delete("all")

        variables = {"Education": ["Bachelors", "Masters", "Doctorate", "Others"], "Race": ["White", "Others"],
                     "Gender": ["Male", "Female"], "Income": [">50K.\n", "<=50K.\n"]}
        variable_column = {"Education": 3, "Race": 8, "Gender": 9, "Income": 14}
        variable_num = {"Education": 4, "Race": 2, "Gender": 2, "Income": 2}
        variable_list = {"Bachelors": 0, "Masters": 1, "Doctorate": 2, "White": 0, "Male": 0, "Female": 1, ">50K.\n": 0,
                         "<=50K.\n": 1}

        value_list = []
        for i in range(variable_num[x_variable.get()]):
            y_list = []
            for j in range(variable_num[y_variable.get()]):
                y_list.append(0)
            value_list.append(y_list)

        for person in data:

            for variable_x in variables[x_variable.get()]:
                if person[variable_column[x_variable.get()]] == variable_x:
                    for variable_y in variables[y_variable.get()]:
                        if person[variable_column[y_variable.get()]] == variable_y:
                            value_list[variable_list[variable_x]][variable_list[variable_y]] += 1
                        else:
                            value_list[variable_list[variable_x]][variable_num[y_variable.get()] - 1] += 1
                else:
                    for variable_y in variables[y_variable.get()]:
                        if person[variable_column[y_variable.get()]] == variable_y:
                            value_list[variable_num[x_variable.get()] - 1][variable_list[variable_y]] += 1
                        else:
                            value_list[variable_num[x_variable.get()] - 1][variable_num[y_variable.get()] - 1] += 1

        for i in range(variable_num[x_variable.get()]):
            x_width = 300.0 / variable_num[x_variable.get()]
            all = 0
            two_variable_canvas.create_text(i * x_width + 10, 260, text="%s" % (variables[x_variable.get()][i]),
                                            fill="lightblue", anchor=NW)
            for j in range(variable_num[y_variable.get()]):
                all += value_list[i][j]
            for j in range(variable_num[y_variable.get()]):
                before = 0
                for k in range(j):
                    before += value_list[i][k]
                two_variable_canvas.create_rectangle((i * x_width + 10, 250.0 * before / all + 10,
                                                      (i + 0.5) * x_width + 10,
                                                      250.0 * (before + value_list[i][j]) / all + 10),
                                                     fill="gray%s" % (99 - int(100.0 * before / all)))
                two_variable_canvas.create_text(i * x_width + 10, 250.0 * before / all + 10, text="%s\n%.1f%%" % (
                variables[y_variable.get()][j], 100.0 * value_list[i][j] / all), fill="coral", anchor=NW)


f = open("data.txt", "r")
data = []
line = f.readline()
while line != "":
    data.append(line.split(", "))
    line = f.readline()
f.close()

r = Tk()
r.title("Statistic")
option = IntVar()

one_frame = Frame(r, width=500, height=300, bd=4, relief="groove")
one_frame.grid(row=1, column=1, sticky=N + S + W + E)
one_variable_button = Radiobutton(one_frame, text="One Variable", variable=option, value=1)
one_variable_button.grid(row=1, column=1, sticky=N + S + W + E)
one_variable_generate = Button(one_frame, text="Generate", command=GenerateOne)
one_variable_generate.grid(row=1, column=2)
one_variable_lable = Label(one_frame, text="Variable")
one_variable_lable.grid(row=2, column=1, sticky=N + S + W + E)
one_variable = StringVar()
one_variable_option = OptionMenu(one_frame, one_variable, "Education", "Race", "Gender", "Income")
one_variable_option.grid(row=2, column=2, sticky=N + S + W + E)
one_variable_canvas = Canvas(one_frame, width=300, height=300, bg="white")
one_variable_canvas.grid(row=1, column=3, rowspan=2, sticky=N + S + W + E)
one_box = (50, 50, 200, 200)

two_frame = Frame(r, width=500, height=300, bd=4, relief="groove")
two_frame.grid(row=2, column=1, sticky=N + S + W + E)
two_variable_button = Radiobutton(two_frame, text="Two Variables", variable=option, value=2)
two_variable_button.grid(row=1, column=1, sticky=N + S + W + E)
one_variable_generate = Button(two_frame, text="Generate", command=GenerateTwo)
one_variable_generate.grid(row=1, column=2)
x_variable_lable = Label(two_frame, text="X Variable")
x_variable_lable.grid(row=2, column=1, sticky=N + S + W + E)
y_variable_lable = Label(two_frame, text="Y Variable")
y_variable_lable.grid(row=3, column=1, sticky=N + S + W + E)
x_variable = StringVar()
x_variable_option = OptionMenu(two_frame, x_variable, "Education", "Race", "Gender", "Income")
x_variable_option.grid(row=2, column=2, sticky=N + S + W + E)
y_variable = StringVar()
y_variable_option = OptionMenu(two_frame, y_variable, "Education", "Race", "Gender", "Income")
y_variable_option.grid(row=3, column=2, sticky=N + S + W + E)
two_variable_canvas = Canvas(two_frame, width=300, height=300, bg="white")
two_variable_canvas.grid(row=1, column=3, rowspan=3, sticky=N + S + W + E)

r.mainloop()
