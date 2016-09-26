import csv
import random
from flask import Flask, render_template, Markup

occy = Flask(__name__)
occupations = {}

with open('occupations.csv','r') as csvfile:
    words = csv.reader(csvfile)
    for row in words:
        occupations[row[0]] = float(row[1])

def randomOccupation():
    counter = 0.0
    randy = random.random() * 99.8
    for occ in occupations:
        counter += occupations[occ]
        if counter >= randy:
            return occ
    return "Legal"


@occy.route("/occupations")
def occysite():
    randocc = randomOccupation()
    return render_template("occupations.html", occ=Markup(
    "<a href=\""
    +"http://lmgtfy.com/?q=" + "+".join(randocc.split(" "))
    +"\">"
    +randocc
    +"</a>")
    ,occupations=occupations)

if __name__ == "__main__":
    occy.run()
