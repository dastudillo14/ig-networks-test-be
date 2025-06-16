from django.db import models

# Create your models here.
class Application(models.Model):
    resume_link = models.TextField()
    experience_years = models.CharField(null=True, max_length=20)
    experience_detail = models.TextField(null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    jobpost = models.ForeignKey('jobpost.JobPost', on_delete=models.CASCADE)
    status = models.ForeignKey('status.Status', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"applicant {self.applicant.id} - {self.jobpost.id} - {self.submission_date}"