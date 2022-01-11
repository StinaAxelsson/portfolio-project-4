from django.shortcuts import render
from django.db.models import Q
from django.views import View
from socialnetwork.models import Users


class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        search_result = Users.objects.filter(
            Q(user__username__icontains=query)
        )
        if not query:
            search_result = ""

        context = {
            'search_result': search_result,
        }

        return render(request, 'search_users.html', context)
