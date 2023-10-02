import os
from django.http import JsonResponse
from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import VideoChunk, Video
from .serializes import VideoSerializer

@transaction.atomic
@api_view(['POST'])
def combine_and_save_video(request):
    try:
        session_id = request.data.get('session_id')
        if not session_id:
            return JsonResponse({'message': 'Session ID is required'}, status=400)

        # Get all video chunks for the given session ID
        chunks = VideoChunk.objects.filter(session_id=session_id).order_by('chunk_number')

        # Ensure all chunks are present
        total_chunks = chunks[0].total_chunks
        if len(chunks) != total_chunks:
            return JsonResponse({'message': 'Not all chunks have been uploaded'}, status=400)

        # Combine video chunks into a complete video
        combined_video = b''
        for chunk in chunks:
            with open(chunk.video_chunk.path, 'rb') as file:
                combined_video += file.read()

        # Delete individual chunk files
        for chunk in chunks:
            os.remove(chunk.video_chunk.path)
            chunk.delete()

        # Save the complete video to the database
        video = Video(session_id=session_id, video_file=combined_video)
        video.save()

        return JsonResponse({'message': 'Video saved successfully'})

    except Exception as e:
        return JsonResponse({'message': 'Error: ' + str(e)}, status=500)
    
    
@api_view(['GET'])
def get_all_videos(request):
    try:
        # Query the database to get all videos
        videos = Video.objects.all()

        # Serialize the video data if needed (using Django REST framework serializers)
        video_data = VideoSerializer(videos, many=True).data

        return JsonResponse({'videos': video_data})

    except Exception as e:
        return JsonResponse({'message': 'Error: ' + str(e)}, status=500)


@api_view(['GET'])
def get_complete_video(request, session_id):
    try:
        # Query the database for the complete video based on the session_id
        video = Video.objects.get(session_id=session_id)

        # Set the content type for the response to indicate it's a video file
        response = HttpResponse(video.video_file, content_type='video/mp4')

        # Optionally, you can specify the file name
        response['Content-Disposition'] = f'attachment; filename="{session_id}.mp4"'

        return response

    except Video.DoesNotExist:
        return HttpResponse('Video not found', status=404)

    except Exception as e:
        return HttpResponse('Error: ' + str(e), status=500)
    
