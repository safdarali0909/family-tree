from django.shortcuts import render, get_object_or_404, redirect
from .models import FamilyMember


def home(request):
    roots = FamilyMember.objects.filter(parent__isnull=True)
    members = FamilyMember.objects.all()
    return render(request, 'family_home.html', {
        'roots':   roots,
        'members': members,
    })


def add_member(request):
    if request.method == 'POST':
        name       = request.POST.get('name', '').strip()
        parent_id  = request.POST.get('parent')
        birth_date = request.POST.get('birth_date') or None
        death_date = request.POST.get('death_date') or None

        if name:
            parent = None
            if parent_id:
                try:
                    parent = FamilyMember.objects.get(pk=parent_id)
                except FamilyMember.DoesNotExist:
                    pass
            FamilyMember.objects.create(
                name=name,
                parent=parent,
                birth_date=birth_date,
                death_date=death_date,
            )
    return redirect('home')


def edit_member(request, pk):
    member = get_object_or_404(FamilyMember, pk=pk)
    members = FamilyMember.objects.exclude(pk=pk)

    if request.method == 'POST':
        name       = request.POST.get('name', '').strip()
        parent_id  = request.POST.get('parent')
        birth_date = request.POST.get('birth_date') or None
        death_date = request.POST.get('death_date') or None

        if name:
            member.name       = name
            member.birth_date = birth_date
            member.death_date = death_date
            member.parent     = None
            if parent_id:
                try:
                    member.parent = FamilyMember.objects.get(pk=parent_id)
                except FamilyMember.DoesNotExist:
                    pass
            member.save()
            return redirect('home')

    return render(request, 'edit_member.html', {
        'member':  member,
        'members': members,
    })


def delete_member(request, pk):
    member = get_object_or_404(FamilyMember, pk=pk)
    if request.method == 'POST':
        member.delete()
    return redirect('home')