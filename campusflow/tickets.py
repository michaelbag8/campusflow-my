import copy

from campusflow.errors import ValidationError
from campusflow.storage import load_tickets, save_tickets
from campusflow.validation import (
    calculate_priority as compute_priority,
    ticket_id_number,
    validate_affected_users as validate_affected_users_value,
    validate_category as validate_category_value,
    validate_staff_label as validate_staff_label_value,
    validate_ticket,
    validate_title as validate_title_value,
    validate_urgency as validate_urgency_value,
)

FILENAME = "tickets.json"
allowed_categories = ("Network", "Hardware", "Software", "Other")
allowed_urgencies = ("low", "medium", "high")


def validate_title(value=None, input_func=None, output_func=None) -> str:
    if value is not None:
        return validate_title_value(value)
    input_func = input if input_func is None else input_func
    output_func = print if output_func is None else output_func
    while True:
        title = input_func("Ticket title: ").strip()
        try:
            return validate_title_value(title)
        except ValidationError:
            output_func("Title field must not be empty")


def validate_category(value=None, input_func=None, output_func=None) -> str:
    if value is not None:
        return validate_category_value(value)
    input_func = input if input_func is None else input_func
    output_func = print if output_func is None else output_func
    while True:
        category = input_func(
            "Select category (Network, Software, Hardware, Other): "
        ).strip()
        try:
            return validate_category_value(category)
        except ValidationError:
            output_func("Unsupported category. Please try again.")


def validate_urgency(value=None, input_func=None, output_func=None) -> str:
    if value is not None:
        return validate_urgency_value(value)
    input_func = input if input_func is None else input_func
    output_func = print if output_func is None else output_func
    while True:
        urgency = input_func("Urgency level (high, medium or low): ").strip()
        try:
            return validate_urgency_value(urgency)
        except ValidationError:
            output_func("Invalid urgency. Enter low, medium, or high.")


def validate_affected_users(value=None, input_func=None, output_func=None) -> int:
    if value is not None:
        return validate_affected_users_value(value)
    input_func = input if input_func is None else input_func
    output_func = print if output_func is None else output_func
    while True:
        affected_users = input_func("Number of affected users: ").strip()
        try:
            parsed = int(affected_users)
        except ValueError:
            output_func("Entry must be a positive integer greater than 0")
            continue
        try:
            return validate_affected_users_value(parsed)
        except ValidationError:
            output_func("Entry must be a positive integer greater than 0")


def calculate_priority(urgency: str, affected_users: int) -> str:
    return compute_priority(urgency, affected_users)


def save_ticket(ticket: dict):
    current = load_tickets(FILENAME)
    current.append(ticket)
    save_tickets(FILENAME, current)


def create_ticket(tickets: list[dict], title=None, category=None, urgency=None, affected_users=None) -> dict:
    if tickets is None:
        tickets = []

    if title is None:
        title = validate_title()
    if category is None:
        category = validate_category()
    if urgency is None:
        urgency = validate_urgency()
    if affected_users is None:
        affected_users = validate_affected_users()

    max_id = max(
        (
            ticket_id_number(ticket["id"])
            for ticket in tickets
            if isinstance(ticket, dict) and isinstance(ticket.get("id"), str)
        ),
        default=0,
    )
    ticket_id = f"T{max_id + 1:03d}"
    ticket = {
        "id": ticket_id,
        "title": validate_title_value(title),
        "category": validate_category_value(category),
        "urgency": validate_urgency_value(urgency),
        "affected_users": validate_affected_users_value(affected_users),
        "priority": compute_priority(
            validate_urgency_value(urgency),
            validate_affected_users_value(affected_users),
        ),
        "status": "open",
        "assigned_to": None,
        "notes": [],
    }
    validate_ticket(ticket)
    tickets.append(ticket)
    return ticket


def list_tickets(tickets: list[dict], output_func=print) -> None:
    if not tickets:
        output_func("No tickets found.")
        return

    for ticket in tickets:
        for key, value in ticket.items():
            output_func(f"{key}: {value}")
        output_func("")


def view_ticket(tickets: list[dict], input_func=input, output_func=print) -> None:
    ticket_id = input_func("Input ticket ID: ").strip().upper()

    for ticket in tickets:
        if ticket.get("id", "").upper() == ticket_id:
            for key, value in ticket.items():
                output_func(f"{key}: {value}")
            return

    output_func("Ticket not found.")


def validate_staff_label(value):
    return validate_staff_label_value(value)