from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
# def detail(request, question_id):
#   return HttpResponse("You're looking at question %s."%question_id)


# def results(request, question_id):
#   response="You're looking at the results of question %s."
#   return HttpResponse("response %s."%question_id)

# def vote(request, question_id):
#   return HttpResponse("You're votiong on question %s."%question_id)
