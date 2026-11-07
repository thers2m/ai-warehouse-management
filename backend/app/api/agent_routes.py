from flask import Blueprint, jsonify

bp = Blueprint("agent", __name__, url_prefix="/api/agent")


@bp.post("/chat")
def chat():
    return jsonify(error="AI Agent chưa được cấu hình. Sẽ tích hợp LLM tool calling ở giai đoạn sau."), 501
