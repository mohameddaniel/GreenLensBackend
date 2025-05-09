from django.shortcuts import render # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view, parser_classes # type: ignore
from .models import Login,Conseil,Historique
from rest_framework.parsers import MultiPartParser, FormParser #type: ignore
from .const.predict import predict_image_class
import jwt ,datetime
from decimal import Decimal
from .utils.jwt_required import jwt_required
from .utils.ACCESS import secret_key


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    pwd = request.data.get('password')
  
    if not email or not pwd:
        return Response({
            "error":"Email et le mot de passe sont requis "
        },status=400)
    
    try:
        person = Login.objects.get(email=email)
        if pwd != person.password or not person:
            return Response({
                'error':'le mot passe ou email est incrorrect'
            })
        
        payload = {
            'id':person.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(days=2),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,secret_key,algorithm='HS256')
        
        return Response({
            "access_token": token,
        })

    except Login.DoesNotExist:
        return Response({
            "error":"Email ou mot de passe incorrect"
        })
    




# Api for register App
@api_view(['POST'])
def Register(request):
    fullname = request.data.get('fullname')
    email = request.data.get('email')
    pwd = request.data.get('password')

    if not fullname or not email or not pwd:
        return Response({
            'error': 'Tous les champs sont requis.'
        })

    try:
        user = Login(fullName=fullname, email=email, password=pwd)
        user.save()

        return Response({
            'message': 'Utilisateur sauvegardé avec succès.',
        }, status=201)

    except Exception as e:
        return Response({
            'error': f'Erreur serveur : {str(e)}'
        })



@api_view(['GET'])
@jwt_required
def getProfile(request):
    try:
        user = request.user
        return Response({
                "fullname":user.fullName,
                "email":user.email
        })
    except Exception as e:
        return Response({
            'error':f'error {str(e)}'
        })

#get a Consiel 
@api_view(['POST'])
@jwt_required
@parser_classes([MultiPartParser, FormParser])
def get_consiel(request):
    image = request.FILES.get('image')

    if not image:
        return Response({"error": "Aucune image reçue."}, status=400) 
    
    try:
        class_name ,result = predict_image_class(image)
        login = request.user
        consiel = Conseil.objects.get(class_name=class_name)
        his = Historique(prediction_resultat=Decimal(float(result)),Conseil=consiel,Login=login,image=image)
        his.save()
        return Response({
            'class_name': consiel.class_name,
            'description': consiel.description.split(','),
            'symptoms': consiel.symptoms.split(','),
            'prevention': consiel.prevention.split(','),
            'note': consiel.note,
            'date': consiel.date_creation
        })
    
    except Conseil.DoesNotExist:
        return Response({
            'error': "Conseil matching query does not exist."
        }, status=404)
    
    except Exception as e:
        return Response({
            'error': f"Erreur: {str(e)}"
        }, status=500)                    




@api_view(['GET'])
@jwt_required
def get_history(request):
    try:
        user = request.user
        his = Historique.objects.filter(Login=user).order_by('-id')

        historique_list = []

        for h in his:
            historique_list.append({
                'class_name': h.Conseil.class_name,
                'image':h.image.url if h.image and hasattr(h.image, 'url') else None,
                'result': float(h.prediction_resultat),
                'date': h.date_prediction.strftime("%Y-%m-%d %H:%M:%S") if h.date_prediction else None,
                'note': h.Conseil.note,
                'Description':h.Conseil.description,
                "treatment":h.Conseil.treatment.rstrip('.').split('.'),
                "prevention":h.Conseil.prevention.rstrip('.').split('.'),
                "symptoms":h.Conseil.symptoms.split(',')
            })
        return Response({
            "data":historique_list
        })
    except Exception as e:
        return Response({
            'error':f'Error {str(e)}'
        })