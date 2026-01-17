# filters.py
import django_filters
from .models import PastPaper, EducationType, Level, Subject


class PastPaperFilter(django_filters.FilterSet):
    education_type = django_filters.ModelChoiceFilter(
        queryset=EducationType.objects.all(),
        empty_label="Select Education Type",
        field_name='subject__level__education_type',
        label='Education Type'
    )
    
    level = django_filters.ModelChoiceFilter(
        queryset=Level.objects.all(),
        empty_label="Select Level",
        field_name='subject__level',
        label='Level'
    )
    
    subject = django_filters.ModelChoiceFilter(
        queryset=Subject.objects.all(),
        empty_label="Select Subject",
        field_name='subject',
        label='Subject'
    )
    
    year = django_filters.NumberFilter(
        field_name='year',
        lookup_expr='exact',
        label='Year'
    )
    
    paper_number = django_filters.ChoiceFilter(
        choices=PastPaper.PAPER_CHOICES,
        empty_label="Select Paper Type",
        field_name='paper_number'
    )

    class Meta:
        model = PastPaper
        fields = ['education_type', 'level', 'subject', 'year', 'paper_number']