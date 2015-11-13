import operator

from django.contrib.auth.decorators import login_required

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.db.models import Q

from django.shortcuts import get_object_or_404, render

from userprofile.models import UserProfile


@login_required
def index(request):
    user_list = UserProfile.objects.all()
    users = get_paginated_list(request, user_list)
    return render(request, 'users/user_list.html', {'objects': users})


def get_paginated_list(request, user_list):
    paginator = Paginator(user_list, 3)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return users


@login_required
def search(request):
    search = request.GET.get('s')
    fieldnames = {'user__username__icontains',
                  'region__icontains', 'specialism__icontains',
                  'interests__icontains'}
    qgroup = reduce(operator.or_, (Q(**{fieldname: search}) for fieldname in fieldnames))
    if search:
        user_list = UserProfile.objects.filter(qgroup)
    else:
        user_list = UserProfile.objects.all()
    users = get_paginated_list(request, user_list)
    return render(request, 'users/user_list.html', {'objects': users, 'search': search})


@login_required
def detail(request, user_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    return render(request, 'users/user_detail.html', {'user': user})
