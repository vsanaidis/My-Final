from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import friend_requests
from django.contrib.auth.models import User
from .models import friend_requests as FriendRequest
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
# Create your views here.


@login_required
@require_POST
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)

    if request.user == to_user:
        messages.error(request, "You cannot send a friend request to yourself.")
        return redirect('user_profile', username=to_user.username)

    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=request.user,
        to_user=to_user,
        defaults={'status': 'pending'}
    )
    if created:
        messages.success(request, f"Friend request sent to {to_user.username}.")
    else:
        messages.info(request, f"You have already sent a friend request to {to_user.username}.")
    
    return redirect('user_profile', username=to_user.username)  # Redirect back to the user's profile
@login_required
@require_POST
def cancel_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    FriendRequest.objects.filter(
        from_user=request.user,
        to_user=to_user,
        status='pending'
    ).delete()
    return redirect('friend_notifications:friend_requests')
@login_required
def get_friend_requests(request):
    friend_requests = FriendRequest.objects.filter(to_user=request.user, status='pending')
    data = [{
        'id': req.id,
        'from_user': req.from_user.username,
        'created_at': req.created_at.isoformat()
    } for req in friend_requests]
    return JsonResponse(data, safe=False)

@login_required
@require_POST
def handle_friend_request(request, request_id):
    action = request.POST.get('action')
    friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user)

    if action == 'accept':
        friend_request.status = 'accepted'
        friend_request.save()
        messages.success(request, f"You have successfully accepted {friend_request.from_user.username}'s friend request.")
    elif action == 'reject':
        friend_request.status = 'rejected'
        friend_request.save()
        messages.info(request, f"You have rejected {friend_request.from_user.username}'s friend request.")
    return redirect('friend_notifications:friend_requests')

@login_required
def view_friend_requests(request):
    incoming_requests = FriendRequest.objects.filter(to_user=request.user, status='pending')
    sent_requests = FriendRequest.objects.filter(from_user=request.user, status='pending')
    
    context = {
        'incoming_requests': incoming_requests,
        'sent_requests': sent_requests,
    }
    return render(request, 'friend_notifications.html', context)

@login_required
def my_friends(request):
    print("My friends")
    # Get all accepted friend requests where the current user is either the sender or receiver
    accepted_requests = FriendRequest.objects.filter(
        (Q(from_user=request.user) | Q(to_user=request.user)) & Q(status='accepted')
    )

    # Create a list of friends
    friends = []
    for fr in accepted_requests:
        if fr.from_user == request.user:
            friends.append(fr.to_user)
        else:
            friends.append(fr.from_user)

    context = {
        'friends': friends
    }

    return render(request, 'my_friends.html', context)

