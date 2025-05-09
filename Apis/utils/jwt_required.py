import jwt
from rest_framework.response import Response
from rest_framework import status
from functools import wraps
from ..models import Login 
from .ACCESS import  secret_key

def jwt_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'Token manquant'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, 'daniel', algorithms=['HS256'])
            user = Login.objects.get(id=payload['id'])
            request.user = user 
            return view_func(request, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token expiré'}, status=401)
        except jwt.InvalidTokenError:
            return Response({'error': 'Token invalide'}, status=401)
        except Login.DoesNotExist:
            return Response({'error': 'Utilisateur non trouvé'}, status=404)

    return wrapper
