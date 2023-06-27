from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from games.models import Game, Team


def match(request):
    # Retrieve current and upcoming games
    current_games = Game.objects.filter(datetime__lte=timezone.now(), datetime_end__gt=timezone.now())
    upcoming_games = Game.objects.filter(datetime__gt=timezone.now())

    context = {
        'current_games': current_games,
        'upcoming_games': upcoming_games
    }

    return render(request, 'bureau/match.html', context)


def detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    context = {
        'game': game
    }
    return render(request, 'bureau/detail.html', context)


def roster(request):
    home_team_name = request.GET.get('home_team')
    away_team_name = request.GET.get('away_team')

    home_team = Team.objects.filter(name=home_team_name).first()
    away_team = Team.objects.filter(name=away_team_name).first()

    context = {
        'home_team': home_team,
        'away_team': away_team
    }

    return render(request, 'bureau/roster.html', context)
