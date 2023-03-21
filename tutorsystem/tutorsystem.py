from flask import Flask, render_template

app = Flask(__name__)


# Users

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/bulletin")
def bulletin():
    return render_template("bulletin.html")

@app.route("/comment")
def comment():
    return render_template("comment.html")


# FUNDAY Teachers

@app.route("/sub")
def sub():
    return render_template("sub.html")

@app.route("/reply")
def reply():
    return render_template("reply.html")


@app.route("/training")
def training():
    return render_template("training.html")

@app.route("/classlist")
def classlist():
    return render_template("classlist.html")

@app.route("/schedulechange")
def schedulechange():
    return render_template("schedulechange.html")

@app.route("/evaluation")
def evaluation():
    return render_template("evaluation.html")

@app.route("/salary")
def salary():
    return render_template("salary.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


# Admins
    # System Settings
@app.route("/directory")
def directory():
    return render_template("directory.html")

@app.route("/announcement")
def announcement():
    return render_template("announcement.html")

@app.route("/teacherprofile")
def teacherprofile():
    return render_template("teacherprofile.html")

@app.route("/messageboard")
def messageboard():
    return render_template("messageboard.html")

    # Scheduling
@app.route("/studentcount")
def studentcount():
    return render_template("studentcount.html")

@app.route("/classdistribution")
def classdistribution():
    return render_template("classdistribution.html")

@app.route("/viewschedule")
def viewschedule():
    return render_template("viewschedule.html")

@app.route("/searchclass")
def searchclass():
    return render_template("searchclass.html")

    # Administrative Records

@app.route("/administrativerecords")
def administrativerecords():
    return render_template("administrativerecords.html")

@app.route("/classlog")
def classlog():
    return render_template("classlog.html")

    # Teaching Performance

@app.route("/studentrating")
def studentrating():
    return render_template("studentrating.html")

@app.route("/teacherevaluation")
def teacherevaluation():
    return render_template("teacherevaluation.html")

@app.route("/classperformance")
def classperformance():
    return render_template("classperformance.html")

    # Salary Management

@app.route("/salarydetails")
def salarydetails():
    return render_template("salarydetails.html")

@app.route("/editsalary")
def editsalary():
    return render_template("editsalary.html")

    # Workshop

@app.route("/workshop")
def workshop():
    return render_template("workshop.html")

    # Lead & Senior Teachers

@app.route("/sharedmaterials")
def sharedmaterials():
    return render_template("sharedmaterials.html")

@app.route("/scheduling")
def scheduling():
    return render_template("scheduling.html")

@app.route("/teammanagement")
def teammanagement():
    return render_template("teammanagement.html")

@app.route("/classroommanagement")
def classroommanagement():
    return render_template("classroommanagement.html")


if __name__ == '__main__':
    app.run(debug=True)