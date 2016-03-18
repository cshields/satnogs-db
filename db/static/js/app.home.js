(function(){
    var app = angular.module('db', []);

    app.controller('DbController', ['$scope',  '$http', '$log', function($scope, $http, $log){
        $scope.satellites = [];
        $scope.satellites.transmitters = [];
        $http.get('./api/satellites/?format=json').success(function(data){
            $scope.satellites = data;
        });
        $http.get('./api/transmitters/?format=json').success(function(data){
            $scope.transmitters = data;

        });
    }]);

    /*app.directive('satelliteTitle', function() {
        return {
            restrict: 'E', // For element
            templateUrl: 'satellite-title.html'.
            controller: function(){

            }
            controllerAs: satellites
        }
    });*/


})();