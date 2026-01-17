from django.shortcuts import render, redirect, get_object_or_404
from .models import PastPaper, DownloadLog,Subject
from django.http import FileResponse, Http404
from django.utils.encoding import smart_str
import os
from django.conf import settings


def home(request):

    return render(request, 'index.html')


def contact(request):

    return render(request, 'contact.html')


def about(request):

    return render(request, 'about.html')


def faq(request):

    return render(request, 'faq.html')


def papers(requset):
    return render(requset, 'papers.html')



     # views.py
# views.py
from django.views.generic import ListView
import django_filters
from django.db.models import Q
from .models import PastPaper, EducationType, Level, Subject
from .filters import PastPaperFilter


class PastPaperListView(ListView):
    model = PastPaper
    template_name = 'papers.html'
    context_object_name = 'papers'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get filter values from GET parameters
        education_type = self.request.GET.get('education_type')
        level = self.request.GET.get('level')
        subject = self.request.GET.get('subject')
        year = self.request.GET.get('year')
        paper_number = self.request.GET.get('paper_number')
        
        # Apply filters
        if education_type:
            queryset = queryset.filter(subject__level__education_type_id=education_type)
        
        if level:
            queryset = queryset.filter(subject__level_id=level)
            
        if subject:
            queryset = queryset.filter(subject_id=subject)
            
        if year:
            queryset = queryset.filter(year=year)
            
        if paper_number:
            queryset = queryset.filter(paper_number=paper_number)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get filter values
        education_type = self.request.GET.get('education_type')
        level = self.request.GET.get('level')
        
        # Prepare context for template
        context['education_types'] = EducationType.objects.all()
        
        # Filter levels based on education type
        if education_type:
            context['levels'] = Level.objects.filter(education_type_id=education_type)
        else:
            context['levels'] = Level.objects.none()
        
        # Filter subjects based on level
        if level:
            context['subjects'] = Subject.objects.filter(level_id=level)
        else:
            context['subjects'] = Subject.objects.none()
        
        # Pass current filter values
        context['current_education_type'] = education_type
        context['current_level'] = level
        context['current_subject'] = self.request.GET.get('subject')
        context['current_year'] = self.request.GET.get('year')
        context['current_paper_number'] = self.request.GET.get('paper_number')
        
        return context


def get_client_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE ADDR')
    
    return ip or '0.0.0.0'


def download_paper(request, pk):
    """Stream the paper file as an attachment.

    Falls back to raising Http404 if no file is present.
    """
    paper = get_object_or_404(PastPaper, pk=pk)

    ip = get_client_ip(request)
    DownloadLog.objects.create(
        paper = paper,
        ip_address = ip
    )

    file_field = paper.file
    if not file_field or not getattr(file_field, 'name', None):
        raise Http404("No file attached to this paper.")

    candidates = []

    # 1) try storage-provided path
    try:
        candidates.append(getattr(file_field, 'path'))
    except Exception:
        pass

    # 2) try join MEDIA_ROOT with file_field.name
    name = getattr(file_field, 'name', '')
    if name:
        candidates.append(os.path.join(settings.MEDIA_ROOT, name))

        # 3) handle legacy entries that include a leading 'media/' segment
        if name.startswith('media/'):
            candidates.append(os.path.join(settings.MEDIA_ROOT, name[len('media/'):]))

    # iterate candidates and pick the first existing file
    file_path = None
    for c in candidates:
        if c and os.path.exists(c):
            file_path = c
            break

    if not file_path:
        # last resort: try the file_field.url (redirect) if available
        url = getattr(file_field, 'url', None)
        if url:
            # Redirect to the file URL which the storage backend may serve
            from django.shortcuts import redirect

            return redirect(url)

        raise Http404("File not found on disk")

    filename = os.path.basename(file_path)
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=smart_str(filename))
    return response


# Create your views here.
