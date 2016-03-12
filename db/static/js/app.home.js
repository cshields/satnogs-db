(function(){
    var app = angular.module('db', []);

    app.controller('DbController', ['$scope', '$http', function($scope, $http){
        $scope.satellites = [];
        $scope.transmitters = [];
        $http.get('./api/satellites/?format=json').success(function(data){
            $scope.satellites = data;
        });
        $http.get('./api/transmitters/?format=json').success(function(data){
            $scope.transmitters = data;
        });
    }]);
})();


/*app.filter("lookupTransmitters", function() {
    function lookup(noradID, transmitterList) {
        var userName;
        angular.forEach(transmitterList, function(transmitter) {
            if ( transmitter.norad_cat_id == noradID ) {
                 userName = user.user_full_name;
            };
        });
        return userName;
    };
    return lookup;
});*/