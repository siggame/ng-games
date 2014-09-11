(function(){
  var app = angular.module('ng-games', []);

  app.controller('GamesController', function(){
    this.games_list = games;
  });

  var games = [];
})();
