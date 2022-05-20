from django.contrib import admin


class Link:

    def __init__(self, name, url, description=None):
        self._name = name
        self._url = url
        self._description = description

    def url(self):
        return self._url

    def name(self):
        return self._name

    def description(self):
        return self._description

    def __str__(self):
        return self._name


class PAWSAdminSite( admin.AdminSite ):
    """
    Custom admin site with other variables to provide more
    information in the admin GUI
    """

    links = []

    def each_context(self, request):
        context = super(PAWSAdminSite, self).each_context(request)
        context['links'] = self.links
        return context

    def add_link(self, link=None):
        if link is not None and isinstance(link, Link):
            self.links.append(link)


admin_site = PAWSAdminSite(name='paws-admin')
admin_site.site_title = 'PAWS Application'
admin_site.site_header = 'PAWS Application'
admin_site.site_url = 'https://www.unillanos.edu.co'
