
from flask import Blueprint, render_template, redirect, url_for, request, flash
from forms import WorkshopForm
from models.workshop import Workshop   # lowercase models
from extensions import db

workshop_bp = Blueprint("workshops", __name__)


# VIEW ALL WORKSHOPS
@workshop_bp.route("/workshops")
def view_workshops():

    workshops = Workshop.query.all()

    return render_template(
        "workshops.html",
        workshops=workshops
    )


# CREATE WORKSHOP
#@workshop_bp.route("/workshops/create", methods=["GET", "POST"])
#def create_workshop():

    #if request.method == "POST":

       #_for("workshops.view_workshops"))

    #

@workshop_bp.route("/workshops/create", methods=["GET", "POST"])
def create_workshop():
    form = WorkshopForm()
    if form.validate_on_submit():
        workshop = Workshop(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            location=form.location.data,
            capacity=form.capacity.data
        )
        db.session.add(workshop)
        db.session.commit()
        flash("Workshop created successfully!", "success")
        return redirect(url_for("workshops.view_workshops"))
    return render_template("create_workshop.html", form=form)

# VIEW SINGLE WORKSHOP
@workshop_bp.route("/workshops/<int:id>")
def workshop_details(id):

    workshop = Workshop.query.get_or_404(id)

    return render_template(
        "workshop_details.html",
        workshop=workshop
    )


# EDIT WORKSHOP
#@workshop_bp.route("/workshops/<int:id>/edit", methods=["GET", "POST"])
#


@workshop_bp.route("/workshops/<int:id>/edit", methods=["GET", "POST"])
def edit_workshop(id):
    workshop = Workshop.query.get_or_404(id)
    form = WorkshopForm(obj=workshop)  # pre-fill form
    if form.validate_on_submit():
        form.populate_obj(workshop)  # updates the object
        db.session.commit()
        flash("Workshop updated successfully!", "success")
        return redirect(url_for("workshops.view_workshops"))
    return render_template("edit_workshop.html", form=form, workshop=workshop)

    
# DELETE WORKSHOP
@workshop_bp.route("/workshops/<int:id>/delete")
def delete_workshop(id):

    workshop = Workshop.query.get_or_404(id)

    db.session.delete(workshop)
    db.session.commit()

    return redirect(url_for("workshops.view_workshops"))