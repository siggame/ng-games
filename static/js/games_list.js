(function(){
    var app = angular.module('ng-games', ['ngResource', 'ui.router']);

    app.config(function($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise("/");

        $stateProvider
            .state('gameList', {
                url: "/",
                templateUrl: '/static/html/game_list.html',
                controller: 'GamesController',
                controllerAs: 'game_list'
            });
    });

    app.filter('escape', function() {
        return window.encodeURIComponent;
    });

    app.factory("CompetitionName", function() {
        // Get the competition name from the URL
        parts = window.location.pathname.split("/");
        return parts[2];
    });

    app.factory("Game", function(CompetitionName, $resource) {
        url = "/api/competition/" + CompetitionName + "/games/";
        return $resource(url);
    });

    app.factory("MyTeam", function(CompetitionName, $resource) {
        url = "/api/competition/" + CompetitionName + "/team/";
        return $resource(url);
    });

    app.factory("Team", function(CompetitionName, $resource) {
        url = "/api/competition/" + CompetitionName + "/teams/";
        return $resource(url);
    });

    app.controller('GamesController', function(CompetitionName, Team, MyTeam, Game){
        var controller = this;
        controller.competition_name = CompetitionName;

        controller.latestStatus = function(game) {
            return _.last(game.updates).status;
        }

        controller.isComplete = function(game) {
            return _.last(game.updates).status == "complete";
        }

        controller.timeStamp = function(game) {
            return _.last(game.updates).time;
        }

        Game.query(function(data) {
            controller.games = data;
        });

        Team.query(function(data) {
            controller.teams = _.object(_.pluck(data, 'id'), _.pluck(data, 'name'));

            controller.getTeamName = function(teamID) {
                return controller.teams[teamID];
            }
        });

        MyTeam.get(function(data) {
            controller.my_team = data;

            controller.getOpponent = function(game) {
                var team = _.first(_.filter(game.players, function(x) {
                    return x.id != controller.my_team.id;
                }));
                return controller.getTeamName(team.id);
            }

            controller.isWinner = function(game) {
                return controller.isComplete(game)
                    && game.winner == controller.my_team.id;
            }

            controller.isLoser = function(game) {
                return controller.isComplete(game)
                    && game.winner != controller.my_team.id;
            }
        });
    });
})();
