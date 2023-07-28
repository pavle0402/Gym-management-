from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Trainer, Member
from .forms import RegisterMemberForm, RegisterTrainerForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout


def home_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome back {username}, have a nice day at work!")
            return redirect('members_list')
        else:
            messages.warning(request, "Incorrect login information. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html',{})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out. See you soon.")
    return redirect('home')

class MembersListView(ListView):
    template_name = 'members/member_list.html'
    model = Member 
    context_object_name = "members"
    ordering = "registered_on"

class RegisterMemberView(CreateView):
    template_name = 'members/register_member.html'
    model = Member
    form_class = RegisterMemberForm
    success_url = reverse_lazy('members_list')

class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('members_list')


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, "Member deleted successfully.")
        return JsonResponse({"message": "Member deleted successfully."})

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    

class MemberUpdateView(UpdateView):
    model = Member 
    form_class = RegisterMemberForm
    template_name = 'members/edit_member.html'
    success_url = reverse_lazy('members_list')


#trainer views

class RegisterTrainerView(CreateView):
    model = Trainer
    form_class = RegisterTrainerForm
    template_name = 'trainers/register_trainer.html'
    success_url = reverse_lazy('trainers_list')


class TrainerListView(ListView):
    model = Trainer
    template_name = 'trainers/trainer_list.html'
    context_object_name = 'trainers'


class TrainerDeleteView(DeleteView):
    model = Trainer
    success_url = reverse_lazy('trainers_list')

    
    def delete(self,request, *args, **kwargs):
        self.object = self.get_object() 
        self.object.delete()
        messages.success(request, "Member deleted successfully.")
        return JsonResponse({"message": "Member deleted successfully."})


    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    


class TrainerEditView(UpdateView):
    model = Trainer
    form_class = RegisterTrainerForm
    template_name = 'trainers/edit_trainer.html'
    success_url = reverse_lazy('trainers_list')


def subtract_sessions(request, member_id):
    if request.method == "POST":
        member = get_object_or_404(Member, pk=member_id)
        if member:
            if member.training > 0:
                member.training -= 1
                member.save()
                return JsonResponse({'status':'success', 'sessions_left': member.training})
            else:
                return JsonResponse({'status':'error', 'message':'No sessions left.'})



def trainer_details(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    trainer_data = {
        'skills': [skill.name for skill in trainer.skills.all()],
        'clients': [client.name for client in trainer.clients.all()]
    }
    return JsonResponse(trainer_data)
    


#staff authentication

