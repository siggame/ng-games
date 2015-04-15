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

    app.factory("Game", function($resource) {
        return $resource("/api/games/:id");
    });

    app.controller('GamesController', function(Game){
        controller = this;

        Game.query(function(data) {
            controller.games = data;
        });
    });
})();
