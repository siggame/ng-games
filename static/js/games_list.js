(function(){
  var app = angular.module('ng-games', ['ngResource']);

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
