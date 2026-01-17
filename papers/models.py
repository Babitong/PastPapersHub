
from django.db import models

# EDUCATION TYPE
class EducationType(models.Model):
    name = models.CharField(max_length=50, unique=True,help_text='General Education or Technical Education')

    def __str__(self):
        return self.name

# 1. CATEGORY: GCE Level (Ordinary or Advanced)
class Level(models.Model):
    education_type = models.ForeignKey(EducationType, on_delete=models.CASCADE, related_name='levels')
    """GCE O/L or A/L."""
    name = models.CharField(max_length=50, unique=True, help_text="e.g., Ordinary Level (O/L) , Advanced Level (A/L) , ITVEE , ATVEE")

    class meta:
        unique_together = ('education_type','name')
    
    def __str__(self):
        return f'{self.name}({self.education_type.name})'
    

# DEPARTMENT CLASS
class Department(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='department')
    name = models.CharField(max_length=100)

    class meta:
        unique_together = ('level','name')

    def __str__(self):
        return f'{self.name} ({self.level.name})'


# 2. CATEGORY: Subject (Mathematics, History, etc.)
class Subject(models.Model):
    """The academic subject."""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True, help_text="e.g., 0570 for Mathematics")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='subjects')
    department = models.ManyToManyField(Department, blank=True)

    class Meta:
        # Prevents adding 'Mathematics' for O/L again if it already exists
        unique_together = ('name', 'level')

    def __str__(self):
        return f"{self.code} - {self.name} ({self.level.name})"

# 3. CORE MODEL: The Past Question Paper File
class PastPaper(models.Model):
    """The downloadable PDF file for a specific paper."""
    
    PAPER_CHOICES = [
        ('1', 'Paper 1 (MCQ)'),
        ('2', 'Paper 2 (Essay/Problem Solving)'),
        ('3', 'Paper 3 (Practical)'),
        
    ]

    # Foreign Key relationships (One Subject has Many Papers)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='papers')

    # Essential metadata fields
    year = models.IntegerField(help_text="The year the exam was written (e.g., 2024)")
    paper_number = models.CharField(max_length=1, choices=PAPER_CHOICES, help_text="The specific paper number (1, 2, or 3)")
    
    # The crucial file field for students to download
    # store under MEDIA_ROOT/past_papers/
    file = models.FileField(upload_to='media/past_papers/')

    # Optional but helpful field (e.g., marking scheme)
    # store marking schemes under MEDIA_ROOT/marking_schemes/
    marking_scheme_file = models.FileField(upload_to='media/marking_schemes/', null=True, blank=True)
    
    class Meta:
        # Ensures no duplicate entries for the exact same paper
        unique_together = ('subject', 'year', 'paper_number')
        ordering = ['-year', 'subject__name', 'paper_number'] # Sorts newest first

    def __str__(self):
        return f"{self.subject.name} {self.year} - Paper {self.paper_number} "
    

class DownloadLog(models.Model):
    paper = models.ForeignKey(PastPaper, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=False) 
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.paper} Downloaded'



