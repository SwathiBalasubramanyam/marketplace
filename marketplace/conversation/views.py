from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from item.models import Item

from .forms import ConversationMessageForm
from  .models import Conversation

# Create your views here.

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass # redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_msg = form.save(commit=False)
            conversation_msg.conversation = conversation
            conversation_msg.created_by = request.user
            conversation_msg.save()

            return redirect('item:detail', pk=item_pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    conversation = Conversation.objects.filter()
    return render(request, 'converation.html')