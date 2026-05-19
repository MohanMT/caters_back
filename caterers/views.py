from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bson import ObjectId

from .db import collection


@api_view(['GET', 'POST'])
def caterers(request):

    if request.method == 'GET':

        data = list(collection.find())

        for item in data:
            item['_id'] = str(item['_id'])

        return Response(data)

    if request.method == 'POST':

        body = request.data

        required_fields = ['name', 'location', 'pricePerPlate', 'cuisines', 'rating']

        # Support both single object and array of caterers
        items = body if isinstance(body, list) else [body]

        for item in items:
            for field in required_fields:
                if field not in item:
                    return Response(
                        {'error': f'{field} is required'},
                        status=400
                    )

        if isinstance(body, list):
            result = collection.insert_many(items)
            return Response({
                'message': f'{len(result.inserted_ids)} Caterers Added',
                'ids': [str(i) for i in result.inserted_ids]
            })

        inserted = collection.insert_one(items[0])
        return Response({
            'message': 'Caterer Added',
            'id': str(inserted.inserted_id)
        })
        

@api_view(['GET'])
def caterer_detail(request, id):

    try:

        caterer = collection.find_one({
            '_id': ObjectId(id)
        })

        if not caterer:
            return Response({
                'error': 'Not Found'
            }, status=404)

        caterer['_id'] = str(caterer['_id'])

        return Response(caterer)

    except:
        return Response({
            'error': 'Invalid ID'
        }, status=400)