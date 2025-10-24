from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from .models import AnalysisRequest
from .serializers import AnalysisRequestSerializer
import google.generativeai as genai
from rest_framework import status



@api_view(["POST"])
def analyze_query(request):
    query = request.data.get("query", "")

    if not query:
        return Response({"error": "Query is required"}, status=status.HTTP_400_BAD_REQUEST)

    user = request.user if request.user.is_authenticated else None

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        gemini_response = model.generate_content(query)
        response_text = gemini_response.text
    except Exception as e:
        response_text = f"Error with Gemini API: {e}"

    # Create record — now user can be None safely
    AnalysisRequest.objects.create(
        user=user,
        query=query,
        response=response_text
    )

    return Response({"response": response_text}, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([])
def get_user_analyses(request):
    """
    Get all previous Gemini analyses for a farmer.
    """
    analyses = AnalysisRequest.objects.filter(user=request.user).order_by("-created_at")
    serializer = AnalysisRequestSerializer(analyses, many=True)
    return Response(serializer.data)


