var app = angular.module('home.app.basic', []);

app.controller('AppController', ['$scope', '$http', function($scope, $http) {
        $scope.satellites = [];
        return $http.get('/api/satellites').then(function(result) {
            return angular.forEach(result.data, function(item) {
                return $scope.satellites.push(item);
            });
        });
    }
]);


