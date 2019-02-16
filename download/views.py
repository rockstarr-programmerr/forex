from django.shortcuts import render, get_object_or_404

from .models import DownloadItem


def download_list(request):
	downloads = DownloadItem.objects.filter(available=True)

	context = {
		'downloads': downloads
	}

	return render(request, 'download/download_list.html', context)

def download_detail(request, pk):
	download = get_object_or_404(DownloadItem, pk=pk)

	context = {
		'download': download
	}

	return render(request, 'download/download_detail.html', context)
