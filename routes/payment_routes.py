from flask import Blueprint, jsonify, request
from app import db
from models import Payment, PaymentStatusEnum

payment_bp = Blueprint('payment', __name__, url_prefix='/payments')

# CREATE
@payment_bp.route("/", methods=["POST"])
def create_payment():
    data = request.get_json()
    new_payment = Payment(
        contract_id=data["contractId"],
        amount=data["amount"],
        method=data.get("method"),
        status=PaymentStatusEnum[data.get("status", "pending")]
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message": "Payment created", "payment": new_payment.to_json()}), 201

# READ ALL
@payment_bp.route("/", methods=["GET"])
def get_payments():
    payments = Payment.query.all()
    return jsonify({"payments": [p.to_json() for p in payments]})

# READ SINGLE
@payment_bp.route("/<int:id>", methods=["GET"])
def get_payment(id):
    payment = Payment.query.get_or_404(id)
    return jsonify(payment.to_json())

# UPDATE
@payment_bp.route("/<int:id>", methods=["PUT"])
def update_payment(id):
    payment = Payment.query.get_or_404(id)
    data = request.get_json()
    payment.amount = data.get("amount", payment.amount)
    payment.method = data.get("method", payment.method)
    payment.status = PaymentStatusEnum[data.get("status", payment.status.name)]
    payment.paid_at = data.get("paidAt", payment.paid_at)
    db.session.commit()
    return jsonify({"message": "Payment updated", "payment": payment.to_json()})

# DELETE
@payment_bp.route("/<int:id>", methods=["DELETE"])
def delete_payment(id):
    payment = Payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({"message": "Payment deleted"})