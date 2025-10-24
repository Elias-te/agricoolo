from django.db import models
from django.contrib.auth.models import User
class AnalysisRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    query = models.TextField()  # The farmer’s question or data
    response = models.TextField(blank=True, null=True)  # Gemini output
    status = models.CharField(max_length=20, default="Pending")  # Pending/Completed
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Analysis by {self.user.username} ({self.status})"