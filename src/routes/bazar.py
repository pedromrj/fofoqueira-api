from flask import jsonify, Blueprint
from src.services.bazar import BazarService

service = BazarService()
router_bazar = Blueprint("router_bazar", __name__)

@router_bazar.route('/bazar', methods=['GET'])
def get_usuarios():
    return jsonify(service.getBazar())
    
        