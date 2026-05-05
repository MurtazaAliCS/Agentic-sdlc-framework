from flask import Blueprint, request, jsonify
from models.models import Ticket, db

ticket_routes = Blueprint("ticket_routes", __name__)

@ticket_routes.route("/")
def home():
    return jsonify({"message": "Student Helpdesk System is running"})

@ticket_routes.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    category = data.get("category")

    if not title or not description:
        return jsonify({"error": "Title and description are required."}), 400

    ticket = Ticket(title=title, description=description, category=category)
    db.session.add(ticket)
    db.session.commit()

    return jsonify({"message": "Ticket created successfully."}), 201

@ticket_routes.route("/tickets", methods=["GET"])
def list_tickets():
    tickets = Ticket.query.all()
    return jsonify([
        {"id": t.id, "title": t.title, "status": t.status}
        for t in tickets
    ])