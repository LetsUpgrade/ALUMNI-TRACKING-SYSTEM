from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from .models import User
from .forms import CollegeSignupForm, RegistrationForm, CollegeDetailsForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse
from .decorators import college_required, admin_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator([admin_required], name='dispatch')
class SignupView(CreateView):
    model = User
    form_class = CollegeSignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'college'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('college-profile', self.request.user.id)


@login_required
@college_required
def profile(request, pk):
    if request.method == 'POST':
        u_form = CollegeDetailsForm(
            request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('college-profile', pk)

    else:
        u_form = CollegeDetailsForm(instance=request.user)

    context = {
        'form': u_form
    }
    return render(request, 'collegeprofile.html', context)


@method_decorator([college_required], name='dispatch')
class PendingQueryView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return User.objects.filter(
            Verified=False,
            is_college=False,
            College=self.request.user.College)
    template_name = "pendingalumni.html"
    context_object_name = 'alumnis'
    ordering = ['Year_Joined']
    paginate_by = 12


class AlumniAuthenticationView(LoginRequiredMixin, UpdateView):
    model = User
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "College",
        "About",
        "Work",
        "Year_Joined",
        "Branch",
        "Image",
        "Verified"
    ]
    template_name = 'verify.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pending-query')
