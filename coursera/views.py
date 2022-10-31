from django.shortcuts import render
from django.views import View
from django.http import FileResponse

from .helper import get_categories, get_courses, write_csv
from coursera.models import CourseraModel

# Create your views here.

class CourseraView(View):
    template_name = "index.html"
    categories = get_categories() # get the list of all available categories in real time

    def get(self, request):
        return render(request, self.template_name, {"categories":self.categories, "courses": CourseraModel.objects.all().order_by('-created_at')})

    def post(self, request):
        category = request.POST["category"]
        search = CourseraModel.objects.create(category=category)
        filename = f"media/{category}-{search.created_at}.csv"
        search.filename=filename
        search.save()
        courses = get_courses(category=category)

        # Creating file for the courses associated to caategory
        write_csv(filename, courses)
        return render(request, self.template_name, {"categories":self.categories, "courses": CourseraModel.objects.all().order_by('-created_at')})


def download_file(request, id: int) -> FileResponse:
    obj = CourseraModel.objects.get(id=id)
    filename = obj.filename
    response = FileResponse(open(filename, 'rb'))
    return response
