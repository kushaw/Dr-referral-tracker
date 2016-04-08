'use strict';

MetronicApp.controller('OrganizationsController', function($rootScope, $scope, $http, $timeout) {
    $scope.$on('$viewContentLoaded', function() {   
        // initialize core components
        Metronic.initAjax();
			Layout.init(); // init current layout
Demo.init(); // init demo features
TableEditable.init();
    });
	
	
	$scope.orgData = {
    "results": [
        {
            "id": 5,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Chary Primary Care",
            "org_type": "",
            "org_contact_name": "Dr. Monia Chary",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 6,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Dr. Peter Urda",
            "org_type": "",
            "org_contact_name": "Dr. Peter Urda",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 16,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Tracey Barnes",
            "org_type": "",
            "org_contact_name": "",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 21,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Louisville Hand and Wrist",
            "org_type": "",
            "org_contact_name": "",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 26,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Dr. Anthony Remson",
            "org_type": "",
            "org_contact_name": "",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 29,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Story and Williams ",
            "org_type": "",
            "org_contact_name": "",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 30,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Dr. Robert Nolan , Jr.",
            "org_type": "",
            "org_contact_name": "",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 33,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Kaplan Barron Pediatric",
            "org_type": "",
            "org_contact_name": "",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 34,
            "creation_time": null,
            "modification_time": null,
            "org_name": "Baptist Health ",
            "org_type": "",
            "org_contact_name": "",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        },
        {
            "id": 18,
            "creation_time": null,
            "modification_time": null,
            "org_name": "US Healthworks ",
            "org_type": "",
            "org_contact_name": "",
            "org_phone": "",
            "org_email": "",
            "org_special": false,
            "clinic": 1
        }
    ],
    "pagination": {
        "page_size": 10,
        "next_url": "http://162.243.91.30/api/v1/organization/?page=2",
        "previous_page": null,
        "current_page": 1,
        "next_page": 2,
        "count": 45,
        "first_page": 1,
        "last_page": 5,
        "previous_url": null
    }
}
		

    // set sidebar closed and body solid layout mode
    $rootScope.settings.layout.pageSidebarClosed = false;
});