from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductSearchHistory
from activity.models import Activity, User


@api_view(['POST'])
def save_search(request):
    query         = request.data.get('query')
    results_count = request.data.get('results_count', 0)
    user_id       = request.data.get('user_id')

    obj = ProductSearchHistory.objects.create(
        query=query,
        results_count=results_count,
        user_id=user_id,
    )

    if user_id:
        Activity.objects.create(
            user_id=str(user_id),
            type='search',
            data={
                'query':         query,
                'results_count': results_count,
            }
        )

    return Response({'success': True, 'id': obj.id}, status=201)


@api_view(['POST'])
def google_auth(request):
    email     = request.data.get('email')
    username  = request.data.get('username', '')
    photo_url = request.data.get('photo_url', '')

    if not email:
        return Response({'success': False, 'message': 'Email missing'})

    user = User.objects.filter(email=email).first()

    if not user:
        base_username  = username or email.split('@')[0]
        final_username = base_username
        counter        = 1
        while User.objects.filter(username=final_username).exists():
            final_username = f"{base_username}{counter}"
            counter += 1

        user = User.objects.create(
            username=final_username,
            email=email,
            password='google_oauth',
        )

    return Response({
        'success':   True,
        'message':   'Google login successful',
        'user_id':   user.id,
        'username':  user.username,
        'email':     user.email,
        'photo_url': photo_url,
    })