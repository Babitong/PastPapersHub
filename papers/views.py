from django.shortcuts import render, redirect, get_object_or_404
from .models import Level, Subject, PastPaper, DownloadLog
from datetime import date
from django.db.models import Q
from django.http import FileResponse, Http404
from django.utils.encoding import smart_str
import os
from django.conf import settings


def home(request):

    return render(request, 'index.html')

def papers(request):
    levels = Level.objects.all().order_by('name')
    subjects = Subject.objects.all().order_by('name')
    current_year = date.today().year
    available_years = range(current_year, 2016, -1)

    # Use select_related to avoid extra queries for subject and level
    past_papers_qs = PastPaper.objects.all().select_related('subject', 'subject__level')

    level_id = request.GET.get('level')
    subject_id = request.GET.get('subject')
    year = request.GET.get('year')

    filter_conditions = Q()

    if level_id:
        filter_conditions &= Q(subject__level__pk=level_id)

    if subject_id:
        filter_conditions &= Q(subject__pk=subject_id)

    if year:
        filter_conditions &= Q(year=year)

    papers = past_papers_qs.filter(filter_conditions).order_by('-year', 'subject__name', 'paper_number')

    return render(request, 'papers.html', {
        'levels': levels,
        'subjects': subjects,
        'available_years': available_years,
        'papers': papers,
    })


    



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
