(function(){
    var app = angular.module('ng-games', ['ngResource']);
    
    app.factory("Game", function($resource) {
        return $resource("/api/games/:id");
    });
    
    app.controller('GamesController', function(Game){
        controller = this;
        
        this.all_games = [];
        this.page_size = 10;
        this.last_index = 0;
        this.games_shown = [];
        
        this.nextPage = function() {
            // Don't try to load more games if we already have them loaded
            if(this.last_index > this.all_games.length - 10) {return;}
       
            // Add x new games to the shown_games, x = page_size
            for(var i = this.last_index; i < this.last_index + this.page_size; i++) {
                this.games_shown.push(this.all_games[i]);
            }
            
            // update index
            this.last_index += this.page_size;
        };
        
        Game.query(function(data) {
            // load all games
            controller.all_games = data;
            // add first x games, x = page_size
            controller.games_shown = data.slice(0, controller.page_size)
            // update index 
            controller.last_index += controller.page_size
        });
    });
})();
