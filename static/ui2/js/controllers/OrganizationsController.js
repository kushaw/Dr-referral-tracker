'use strict';

/*MetronicApp.controller('WithAjaxCtrl',  WithAjaxCtrl);



function WithAjaxCtrl(DTOptionsBuilder, DTColumnBuilder) {
    var vm = this;
	
    vm.dtOptions = DTOptionsBuilder.fromSource('json/org_data.json')
        .withPaginationType('full_numbers');
    vm.dtColumns = [
        DTColumnBuilder.newColumn('id').withTitle('ID'),
		DTColumnBuilder.newColumn('org_name').withTitle('Name'),
        DTColumnBuilder.newColumn('org_contact_name').withTitle('Contact Name'),
        
		DTColumnBuilder.newColumn('org_phone').withTitle('User Name'),
		DTColumnBuilder.newColumn('org_email').withTitle('User Name'),
		DTColumnBuilder.newColumn('org_special').withTitle('User Name')
    ];
}
*/



MetronicApp.controller('OrganizationsController', function($rootScope, $scope, $http, $timeout) {
    $scope.$on('$viewContentLoaded', function() {   
        // initialize core components
        Metronic.initAjax();
			//$(document).ready(function(e) {
		
        	//; // init demo features
			 
			
    //});
    });
	
	$scope.orgData 
	
	$http.get('http://localhost:8000/api/v1/organization/')
       .then(function(res){
          $scope.orgData = res.data;
		  console.log($scope.orgData) 
		  $timeout(function() {
			   console.log("TableEditable.init - initiated _1")
			   Layout.init(); // init current layout
				Demo.init()
				TableEditable.init(); 
			},0);
        });
	
	
	


    // set sidebar closed and body solid layout mode
    $rootScope.settings.layout.pageSidebarClosed = false;
});