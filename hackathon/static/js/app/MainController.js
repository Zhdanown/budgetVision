var app = angular.module("main-ctrl", []);

app.controller("MainController", function($scope, GetUser, Processes, Tasks) {
  $scope.data = [
    {
      id: 1,
      title: "node1",
      nodes: [
        {
          id: 11,
          title: "node1.1",
          nodes: [
            {
              id: 111,
              title: "node1.1.1",
              nodes: []
            }
          ]
        },
        {
          id: 12,
          title: "node1.2",
          nodes: []
        }
      ]
    },
    {
      id: 2,
      title: "node2",
      nodrop: true,
      nodes: [
        {
          id: 21,
          title: "node2.1",
          nodes: []
        },
        {
          id: 22,
          title: "node2.2",
          nodes: []
        }
      ]
    },
    {
      id: 3,
      title: "node3",
      nodes: [
        {
          id: 31,
          title: "node3.1",
          nodes: []
        }
      ]
    }
  ];

  $scope.openCard = function (card) {
      $scope.selectedCard = card;
  }

  /* Get User Organizations */
  GetUser.get({ pk: 1 }, res => {
    console.log(res);
  })

  Processes.query({}, res => {
    console.log(res);
  })

  console.log("main controller");
});
