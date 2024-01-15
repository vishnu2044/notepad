from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notes 
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create_note(request):
    if request.method == "POST":
        try:
            title = request.data.get('title', None)
            body = request.data.get('body', None)
            if title is None or body is None:
                return Response({"error": "Title and body are required"}, status=status.HTTP_400_BAD_REQUEST)
            
            Notes.objects.create(
                title=title,
                body=body
            )
            return Response({"message": "Note created successfully"}, status=status.HTTP_201_CREATED)
        
        except:
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_notes(request):
    try:
        notes = Notes.objects.all()
        serializer = NoteSerializer(notes, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Notes.DoesNotExist:
        return Response({"error" : "notes is empty"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_single_note(request, id):
    try:
        note = Notes.objects.get(id = id)
        noteserializer = NoteSerializer(note)   
        return Response(noteserializer.data, status=status.HTTP_200_OK)


    except Notes.DoesNotExist:
        return Response({"error" : "notes is empty"}, status=status.HTTP_404_NOT_FOUND) 

  
@api_view(['PUT'])
def update_note(request, id):
    try:
        title = request.data.get("title")
        body = request.data.get("body")
        Notes.objects.filter(id=id).update(
            body = body,
            title = title
            )
        if Notes.objects.filter(id = id).exists():
            return Response({'success' : "updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    except :
        return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['DELETE'])
def delete_note(request, id):
    try:
        note = get_object_or_404(Notes, id=id)
        note.delete()
        return Response({"success": "Note deleted successfully"}, status=status.HTTP_200_OK)
    except Notes.DoesNotExist:
        return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

